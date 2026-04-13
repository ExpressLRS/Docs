"""Hook to generate the product catalog at build time.

Downloads hardware artifacts from the ExpressLRS artifactory, processes
targets.json and layout files, and writes a flat products.json used by
the Product Finder page.

Skips the build if products.json already exists. Delete the file to
force a refresh.
"""

import json
import os
import re
import tempfile
import urllib.request
import zipfile

HARDWARE_URL = "https://artifactory.expresslrs.org/ExpressLRS/hardware.zip"
POWER_LEVELS_MW = [10, 25, 50, 100, 250, 500, 1000, 2000]
ALLOWED_ENRICHMENT_FIELDS = {"notes", "product_url", "image_url", "form_factor"}
COMPACT_FIELDS = [
    "id", "vendor", "vendor_name", "product_name", "category", "device_class",
    "radio_band", "firmware_target", "platform", "tx_type", "screen_type",
    "min_power_value", "max_power_value", "max_output_power_mw", "pwm_outputs",
    "diversity_type", "notes", "product_url", "image_url", "form_factor",
]


def on_pre_build(config, **kwargs):
    docs_dir = config["docs_dir"]
    output_path = os.path.join(docs_dir, "assets", "data", "products.json")
    if os.path.exists(output_path):
        return

    hook_dir = os.path.dirname(__file__)
    enrichment_path = os.path.join(hook_dir, "enrichment.json")

    with tempfile.TemporaryDirectory() as tmp:
        zip_path = os.path.join(tmp, "hardware.zip")
        hardware_dir = os.path.join(tmp, "hardware")

        print("product_catalog: downloading hardware artifacts...")
        req = urllib.request.Request(HARDWARE_URL, headers={"User-Agent": "ExpressLRS-Docs/1.0"})
        with urllib.request.urlopen(req) as resp, open(zip_path, "wb") as out:
            out.write(resp.read())

        with zipfile.ZipFile(zip_path) as zf:
            zf.extractall(hardware_dir)

        targets_path = os.path.join(hardware_dir, "targets.json")
        if not os.path.exists(targets_path):
            print("product_catalog: targets.json not found in archive, skipping")
            return

        with open(targets_path, encoding="utf-8") as f:
            targets = json.load(f)

        enrichment = _read_json(enrichment_path, {"defaults": {}, "products": {}})
        defaults = _sanitize_enrichment(enrichment.get("defaults", {}))
        enriched_products = {
            pid: _sanitize_enrichment(entry)
            for pid, entry in enrichment.get("products", {}).items()
        }

        products = []
        for vendor, vendor_entry in targets.items():
            if vendor in ("diy", "generic"):
                continue
            vendor_name = vendor_entry.get("name", vendor)
            for radio_key, target_map in vendor_entry.items():
                if radio_key == "name":
                    continue
                for target, config in target_map.items():
                    product_name = config.get("product_name", "")
                    if re.match(r"^(generic|diy)\b", product_name, re.IGNORECASE):
                        continue

                    pid = f"{vendor}:{radio_key}:{target}"
                    category = _category_from_radio_key(radio_key)
                    band = _radio_band(radio_key)
                    layout = _read_layout(
                        hardware_dir, config.get("layout_file"), category,
                    )
                    merged_hw = {**layout, **(config.get("overlay") or {})}
                    power_range = _numeric_power_range(merged_hw)
                    tx_type = _detect_tx_type(category, merged_hw)
                    classification = _device_class(category, tx_type)
                    hw_screen = _screen_type_label(merged_hw.get("screen_type"))
                    inferred_screen = _infer_screen_type(config, product_name)
                    screen = _normalized_screen_type(
                        category, tx_type, hw_screen, inferred_screen,
                    )

                    record = {
                        "id": pid,
                        "vendor": vendor,
                        "vendor_name": vendor_name,
                        "product_name": product_name,
                        "category": category,
                        "device_class": classification,
                        "radio_band": band,
                        "firmware_target": config.get("firmware"),
                        "platform": config.get("platform"),
                        "tx_type": tx_type,
                        "screen_type": screen,
                        "min_power_value": power_range[0],
                        "max_power_value": power_range[1],
                        "max_output_power_mw": _output_power_from_name(product_name),
                        "pwm_outputs": _pwm_count(merged_hw, product_name),
                        "diversity_type": _infer_diversity(merged_hw),
                        "notes": "",
                    }
                    merged = {**record, **defaults, **enriched_products.get(pid, {})}
                    products.append(_compact(merged))

        products.sort(key=lambda p: (p.get("vendor_name", ""), p.get("product_name", "")))

        os.makedirs(os.path.dirname(output_path), exist_ok=True)
        with open(output_path, "w", encoding="utf-8") as f:
            json.dump(products, f, indent=2)
            f.write("\n")

        print(f"product_catalog: wrote {len(products)} products to {output_path}")


# ---------------------------------------------------------------------------
# Helpers
# ---------------------------------------------------------------------------

def _read_json(path, fallback=None):
    if not os.path.exists(path):
        return fallback if fallback is not None else {}
    with open(path, encoding="utf-8") as f:
        return json.load(f)


def _sanitize_enrichment(entry):
    return {k: v for k, v in (entry or {}).items() if k in ALLOWED_ENRICHMENT_FIELDS}


def _radio_band(radio_key):
    if radio_key.endswith("_2400"):
        return "2400"
    if radio_key.endswith("_900"):
        return "900"
    if radio_key.endswith("_dual"):
        return "dual"
    return "unknown"


def _category_from_radio_key(radio_key):
    return "tx" if radio_key.startswith("tx") else "rx"


def _detect_tx_type(category, hardware):
    if category != "tx":
        return None
    serial_rx = hardware.get("serial_rx")
    serial_tx = hardware.get("serial_tx")
    if not isinstance(serial_rx, int) or not isinstance(serial_tx, int):
        return None
    return "external" if serial_rx == serial_tx else "internal"


def _device_class(category, tx_type):
    if category == "rx":
        return "receiver"
    if tx_type == "internal":
        return "radio_handset"
    return "transmitter_module"


def _screen_type_label(value):
    if value == 1:
        return "oled"
    if value == 4:
        return "tft"
    return None


def _infer_screen_type(config, product_name):
    if re.search(r"oled", product_name, re.IGNORECASE):
        return "oled"
    logo = config.get("logo_file") or ""
    if re.search(r"tft", product_name, re.IGNORECASE) or re.search(r"_tft\.", logo, re.IGNORECASE):
        return "tft"
    return None


def _normalized_screen_type(category, tx_type, hw_screen, inferred_screen):
    detected = hw_screen or inferred_screen
    if detected:
        return detected
    if category == "tx" and tx_type == "external":
        return "none"
    return None


def _numeric_power_range(hardware):
    power_min = hardware.get("power_min")
    power_max = hardware.get("power_max")
    if not isinstance(power_min, int) and not isinstance(power_max, int):
        return (None, None)
    min_idx = power_min if isinstance(power_min, int) else 0
    max_idx = power_max if isinstance(power_max, int) else len(POWER_LEVELS_MW) - 1
    min_idx = max(0, min(min_idx, len(POWER_LEVELS_MW) - 1))
    max_idx = max(0, min(max_idx, len(POWER_LEVELS_MW) - 1))
    return (POWER_LEVELS_MW[min_idx], POWER_LEVELS_MW[max_idx])


def _output_power_from_name(product_name):
    watts = re.search(r"(\d+(?:\.\d+)?)\s*w", product_name, re.IGNORECASE)
    if watts:
        return round(float(watts.group(1)) * 1000)
    milliwatts = re.search(r"(\d+)\s*mw", product_name, re.IGNORECASE)
    if milliwatts:
        return int(milliwatts.group(1))
    return None


def _pwm_count(hardware, product_name):
    pwm = hardware.get("pwm_outputs")
    if isinstance(pwm, list):
        return len(pwm)
    channels = re.search(r"(\d+)\s*ch", product_name, re.IGNORECASE)
    if channels:
        return int(channels.group(1))
    return None


def _infer_diversity(hardware):
    if "radio_nss_2" in hardware:
        return "gemini"
    if "ant_ctrl" in hardware:
        return "antenna"
    return "single"


def _read_layout(hardware_dir, layout_file, category):
    if not layout_file:
        return {}
    folder = "TX" if category == "tx" else "RX"
    path = os.path.join(hardware_dir, folder, layout_file)
    if not os.path.exists(path):
        return {}
    return _read_json(path, {})


def _compact(record):
    return {k: record[k] for k in COMPACT_FIELDS if record.get(k) is not None and record.get(k) != ""}
