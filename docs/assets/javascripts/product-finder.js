/**
 * ExpressLRS Product Finder
 * Vanilla JS — loads products.json, renders grouped results, filters via URL state.
 */

(function () {
  "use strict";

  // -----------------------------------------------------------------------
  // State
  // -----------------------------------------------------------------------

  var catalog = [];
  var filters = {
    search: "",
    classification: "",
    band: "",
    vendor: "",
    screen: "",
    diversity: "",
    minPower: "",
    minPwm: "",
  };

  var DEFAULTS = Object.assign({}, filters);

  // -----------------------------------------------------------------------
  // DOM refs
  // -----------------------------------------------------------------------

  var els = {};

  function cacheDom() {
    els.search = document.getElementById("pf-search");
    els.vendor = document.getElementById("pf-vendor");
    els.classification = document.getElementById("pf-classification");
    els.band = document.getElementById("pf-band");
    els.minPower = document.getElementById("pf-min-power");
    els.diversity = document.getElementById("pf-diversity");
    els.minPwm = document.getElementById("pf-min-pwm");
    els.screen = document.getElementById("pf-screen");
    els.reset = document.getElementById("pf-reset");
    els.summary = document.getElementById("pf-summary");
    els.activeFilters = document.getElementById("pf-active-filters");
    els.container = document.getElementById("pf-results-container");
    els.stats = document.getElementById("pf-stats");
    els.statsPopover = document.getElementById("pf-stats-popover");
  }

  // -----------------------------------------------------------------------
  // URL query state
  // -----------------------------------------------------------------------

  var PARAM_MAP = {
    search: "search",
    classification: "classification",
    band: "band",
    vendor: "vendor",
    screen: "screen",
    diversity: "diversity",
    minPower: "min-power",
    minPwm: "min-pwm",
  };

  function readQuery() {
    var params = new URLSearchParams(window.location.search);
    for (var key in PARAM_MAP) {
      filters[key] = params.get(PARAM_MAP[key]) || "";
    }
  }

  function writeQuery() {
    var params = new URLSearchParams();
    for (var key in PARAM_MAP) {
      if (filters[key]) params.set(PARAM_MAP[key], filters[key]);
    }
    var query = params.toString();
    var next = window.location.pathname + (query ? "?" + query : "");
    window.history.replaceState({}, "", next);
  }

  // -----------------------------------------------------------------------
  // Label formatters
  // -----------------------------------------------------------------------

  function titleCase(value) {
    return String(value)
      .split(/[_-]/g)
      .map(function (p) { return p.charAt(0).toUpperCase() + p.slice(1); })
      .join(" ");
  }

  function bandLabel(value) {
    return { "2400": "2.4GHz", "900": "900MHz", dual: "Dual-band" }[value] || value;
  }

  function categoryLabel(value) {
    return {
      receiver: "Receiver",
      transmitter_module: "Transmitter Module",
      radio_handset: "Radio Handset",
    }[value] || titleCase(value);
  }

  function badgeLabel(value) {
    return { receiver: "Receiver", transmitter_module: "Module", radio_handset: "Radio" }[value] || titleCase(value);
  }

  function diversityLabel(value) {
    return value === "gemini" ? "Gemini (True Diversity)" : titleCase(value);
  }

  function screenLabel(value) {
    return { none: "None", oled: "OLED", tft: "TFT" }[value] || titleCase(value);
  }

  function powerDisplay(product) {
    if (product.min_power_value != null && product.max_power_value != null) {
      return product.min_power_value === product.max_power_value
        ? product.max_power_value + " mW"
        : product.min_power_value + "-" + product.max_power_value + " mW";
    }
    if (product.max_output_power_mw != null) return product.max_output_power_mw + " mW";
    return null;
  }

  function cardSpecs(product) {
    var specs = [];
    var power = powerDisplay(product);
    if (power) specs.push(["Power", power]);
    if (product.diversity_type) specs.push(["Diversity", diversityLabel(product.diversity_type)]);

    if (product.category === "tx") {
      specs.unshift(["Band", bandLabel(product.radio_band)]);
      if (product.screen_type && product.screen_type !== "none") {
        specs.push(["Screen", screenLabel(product.screen_type)]);
      }
      return specs;
    }

    // rx
    specs.unshift(["Band", bandLabel(product.radio_band)]);
    if (product.pwm_outputs != null) specs.push(["PWM", String(product.pwm_outputs)]);
    return specs;
  }

  // -----------------------------------------------------------------------
  // Stats
  // -----------------------------------------------------------------------

  function countBy(items, valueFn) {
    var counts = {};
    items.forEach(function (item) {
      var val = valueFn(item);
      if (!val) return;
      counts[val] = (counts[val] || 0) + 1;
    });
    return Object.keys(counts)
      .map(function (k) { return { label: k, count: counts[k] }; })
      .sort(function (a, b) { return b.count - a.count || a.label.localeCompare(b.label); });
  }

  function radioChipLabel(product) {
    if (product.firmware_target && product.firmware_target.indexOf("LR1121") !== -1) return "LR1121";
    if (product.radio_band === "2400") return "SX1280";
    if (product.radio_band === "900") return "SX127x";
    return null;
  }

  function renderStatsPopover(products) {
    var deviceTypes = countBy(products, function (p) { return p.device_class; });
    var mcus = countBy(products, function (p) { return p.platform ? p.platform.toUpperCase() : null; });
    var chips = countBy(products, radioChipLabel);
    var diversity = countBy(products, function (p) { return p.diversity_type ? diversityLabel(p.diversity_type) : null; });

    var sections = [
      { title: "Device Types", items: deviceTypes, labelFn: function (l) { return categoryLabel(l) || l; } },
      { title: "MCUs", items: mcus },
      { title: "Radio Chips", items: chips },
      { title: "Diversity", items: diversity },
    ];

    var html = sections.map(function (section) {
      if (!section.items.length) return "";
      var chips = section.items.map(function (item) {
        var label = section.labelFn ? section.labelFn(item.label) : item.label;
        return '<span class="pf-stat-chip">' + escapeHtml(label) +
          ' <span class="pf-stat-chip__count">' + item.count + '</span></span>';
      }).join("");
      return '<div class="pf-stats-section"><p class="pf-stats-title">' +
        escapeHtml(section.title) + '</p><div class="pf-stats-chips">' + chips + '</div></div>';
    }).join("");

    els.statsPopover.innerHTML = '<p class="pf-stats-popover__title">Interesting Stats<button class="pf-stats-popover__close" id="pf-stats-close">&times;</button></p>' + html;
  }

  // -----------------------------------------------------------------------
  // Filtering
  // -----------------------------------------------------------------------

  function matchesThreshold(actual, threshold) {
    if (!threshold) return true;
    if (actual == null) return false;
    return Number(actual) >= Number(threshold);
  }

  function matchesProduct(product) {
    if (filters.search) {
      var text = [product.vendor_name, product.product_name, product.notes]
        .concat(product.tags || [])
        .filter(Boolean)
        .join(" ")
        .toLowerCase();
      if (text.indexOf(filters.search.toLowerCase()) === -1) return false;
    }
    if (filters.classification && product.device_class !== filters.classification) return false;
    if (filters.band && product.radio_band !== filters.band) return false;
    if (filters.vendor && product.vendor !== filters.vendor) return false;
    if (filters.screen) {
      if (product.device_class !== "transmitter_module") return false;
      if (filters.screen === "none") {
        if (product.screen_type && product.screen_type !== "none") return false;
      } else if (product.screen_type !== filters.screen) {
        return false;
      }
    }
    if (filters.diversity && product.diversity_type !== filters.diversity) return false;
    if (!matchesThreshold(product.max_power_value || product.max_output_power_mw, filters.minPower)) return false;
    if (!matchesThreshold(product.pwm_outputs, filters.minPwm)) return false;
    return true;
  }

  // -----------------------------------------------------------------------
  // Grouping
  // -----------------------------------------------------------------------

  function groupByVendor(products) {
    var groups = {};
    products.forEach(function (p) {
      var key = p.vendor_name || p.vendor;
      if (!groups[key]) groups[key] = [];
      groups[key].push(p);
    });
    return Object.keys(groups)
      .sort(function (a, b) { return a.localeCompare(b); })
      .map(function (name) { return { name: name, products: groups[name] }; });
  }

  // -----------------------------------------------------------------------
  // Rendering
  // -----------------------------------------------------------------------

  function escapeHtml(str) {
    var div = document.createElement("div");
    div.textContent = str;
    return div.innerHTML;
  }

  function renderCard(product) {
    var isRx = product.device_class === "receiver";
    var typeClass = isRx ? "pf-card--rx" : "pf-card--tx";
    var specs = cardSpecs(product);
    var pillsHtml = specs
      .map(function (s) {
        return '<div class="pf-pill"><span class="pf-pill__label">' +
          escapeHtml(s[0]) +
          '</span><span class="pf-pill__value">' +
          escapeHtml(s[1]) +
          "</span></div>";
      })
      .join("");

    return (
      '<div class="pf-card ' + typeClass + '">' +
      '<div class="pf-card__header"><div>' +
      '<p class="pf-card__vendor">' + escapeHtml(product.vendor_name) + "</p>" +
      '<h3 class="pf-card__name">' + escapeHtml(product.product_name) + "</h3>" +
      '</div><span class="pf-card__badge">' + escapeHtml(badgeLabel(product.device_class)) + "</span></div>" +
      '<div class="pf-card__specs">' + pillsHtml + "</div>" +
      "</div>"
    );
  }

  function renderResults() {
    var filtered = catalog.filter(matchesProduct);
    var groups = groupByVendor(filtered);

    // Summary
    var hasFilters = Object.keys(filters).some(function (k) { return filters[k] !== ""; });
    if (hasFilters) {
      els.summary.textContent =
        filtered.length + " of " + catalog.length + " products match the current filters.";
      els.summary.style.display = "";
    } else {
      els.summary.textContent = "";
      els.summary.style.display = "none";
    }

    // Active filter chips
    renderActiveFilters();

    // Smart disable
    var disablePwm = filters.classification === "transmitter_module" || filters.classification === "radio_handset";
    var disableScreen = filters.classification === "receiver" || filters.classification === "radio_handset";
    els.minPwm.disabled = disablePwm;
    els.screen.disabled = disableScreen;
    if (disablePwm && filters.minPwm) { filters.minPwm = ""; els.minPwm.value = ""; }
    if (disableScreen && filters.screen) { filters.screen = ""; els.screen.value = ""; }

    // Cards
    if (groups.length === 0) {
      els.container.innerHTML =
        '<div class="pf-empty">' +
        (hasFilters ? "No products matched the current filter set." : "No products available.") +
        "</div>";
      return;
    }

    var html = groups
      .map(function (group) {
        var cards = group.products.map(renderCard).join("");
        return (
          '<div class="pf-vendor-group">' +
          '<h3 class="pf-vendor-heading">' +
          escapeHtml(group.name) +
          ' <span class="pf-vendor-count">' + group.products.length + "</span>" +
          "</h3>" +
          '<div class="pf-card-grid">' + cards + "</div>" +
          "</div>"
        );
      })
      .join("");

    els.container.innerHTML = html;
  }

  function renderActiveFilters() {
    var labelMap = {
      search: "Search",
      classification: "Product Type",
      band: "Frequency",
      vendor: "Manufacturer",
      screen: "Display",
      diversity: "Antenna",
      minPower: "Min TX Power",
      minPwm: "Min PWM Outputs",
    };

    function displayValue(key) {
      switch (key) {
        case "classification": return categoryLabel(filters[key]);
        case "band": return bandLabel(filters[key]);
        case "vendor":
          var match = catalog.find(function (p) { return p.vendor === filters[key]; });
          return match ? match.vendor_name : titleCase(filters[key]);
        case "screen": return screenLabel(filters[key]);
        case "diversity": return diversityLabel(filters[key]);
        case "minPower": return filters[key] + " mW";
        default: return filters[key];
      }
    }

    var chips = [];
    for (var key in labelMap) {
      if (filters[key]) {
        chips.push(
          '<span class="pf-chip">' +
          escapeHtml(labelMap[key]) + ": " + escapeHtml(displayValue(key)) +
          ' <button class="pf-chip__close" data-filter="' + key + '" title="Remove">&times;</button>' +
          "</span>"
        );
      }
    }
    els.activeFilters.innerHTML = chips.join("");
  }

  // -----------------------------------------------------------------------
  // Dynamic filter options
  // -----------------------------------------------------------------------

  function populateSelect(selectEl, values, formatter) {
    var first = selectEl.querySelector("option");
    var current = selectEl.value;
    selectEl.innerHTML = "";
    selectEl.appendChild(first);
    values.forEach(function (v) {
      var opt = document.createElement("option");
      opt.value = v;
      opt.textContent = formatter ? formatter(v) : v;
      selectEl.appendChild(opt);
    });
    selectEl.value = current;
  }

  function populateDynamicFilters() {
    // Vendor
    var vendors = [];
    var vendorNames = {};
    catalog.forEach(function (p) {
      if (p.vendor && !vendorNames[p.vendor]) {
        vendorNames[p.vendor] = p.vendor_name || p.vendor;
        vendors.push(p.vendor);
      }
    });
    vendors.sort(function (a, b) { return vendorNames[a].localeCompare(vendorNames[b]); });
    populateSelect(els.vendor, vendors, function (v) { return vendorNames[v]; });

    // Min power
    var powers = [];
    var seen = {};
    catalog.forEach(function (p) {
      var v = p.max_power_value || p.max_output_power_mw;
      if (v && !seen[v]) { seen[v] = true; powers.push(v); }
    });
    powers.sort(function (a, b) { return a - b; });
    populateSelect(els.minPower, powers, function (v) { return v + " mW"; });

    // Min PWM
    var pwms = [];
    var seenPwm = {};
    catalog.forEach(function (p) {
      if (p.pwm_outputs && !seenPwm[p.pwm_outputs]) {
        seenPwm[p.pwm_outputs] = true;
        pwms.push(p.pwm_outputs);
      }
    });
    pwms.sort(function (a, b) { return a - b; });
    populateSelect(els.minPwm, pwms, String);
  }

  // -----------------------------------------------------------------------
  // Event wiring
  // -----------------------------------------------------------------------

  function syncFiltersFromDom() {
    filters.search = els.search.value;
    filters.vendor = els.vendor.value;
    filters.classification = els.classification.value;
    filters.band = els.band.value;
    filters.minPower = els.minPower.value;
    filters.diversity = els.diversity.value;
    filters.minPwm = els.minPwm.value;
    filters.screen = els.screen.value;
  }

  function syncDomFromFilters() {
    els.search.value = filters.search;
    els.vendor.value = filters.vendor;
    els.classification.value = filters.classification;
    els.band.value = filters.band;
    els.minPower.value = filters.minPower;
    els.diversity.value = filters.diversity;
    els.minPwm.value = filters.minPwm;
    els.screen.value = filters.screen;
  }

  function onFilterChange() {
    syncFiltersFromDom();
    writeQuery();
    renderResults();
  }

  var searchTimer = null;
  function onSearchInput() {
    clearTimeout(searchTimer);
    searchTimer = setTimeout(onFilterChange, 200);
  }

  function onReset() {
    Object.assign(filters, DEFAULTS);
    syncDomFromFilters();
    writeQuery();
    renderResults();
  }

  function onChipClose(e) {
    var btn = e.target.closest("[data-filter]");
    if (!btn) return;
    var key = btn.getAttribute("data-filter");
    filters[key] = "";
    syncDomFromFilters();
    writeQuery();
    renderResults();
  }

  function bindEvents() {
    els.search.addEventListener("input", onSearchInput);
    els.vendor.addEventListener("change", onFilterChange);
    els.classification.addEventListener("change", onFilterChange);
    els.band.addEventListener("change", onFilterChange);
    els.minPower.addEventListener("change", onFilterChange);
    els.diversity.addEventListener("change", onFilterChange);
    els.minPwm.addEventListener("change", onFilterChange);
    els.screen.addEventListener("change", onFilterChange);
    els.reset.addEventListener("click", onReset);
    els.activeFilters.addEventListener("click", onChipClose);

    // Stats popover: tap to toggle on touch devices
    var statsWrap = els.stats.parentElement;
    els.stats.addEventListener("click", function (e) {
      e.stopPropagation();
      statsWrap.classList.toggle("pf-stats-open");
    });
    document.addEventListener("click", function (e) {
      if (!statsWrap.contains(e.target)) {
        statsWrap.classList.remove("pf-stats-open");
      }
    });
    els.statsPopover.addEventListener("click", function (e) {
      if (e.target.closest(".pf-stats-popover__close")) {
        statsWrap.classList.remove("pf-stats-open");
      }
    });
  }

  // -----------------------------------------------------------------------
  // Init
  // -----------------------------------------------------------------------

  function init() {
    cacheDom();
    if (!els.container) return; // not on product finder page

    readQuery();
    bindEvents();

    fetch(document.querySelector('script[src*="product-finder"]').src.replace("javascripts/product-finder.js", "data/products.json"))
      .then(function (res) {
        if (!res.ok) throw new Error("Failed to load catalog");
        return res.json();
      })
      .then(function (items) {
        catalog = items;

        // Stats
        var vendorSet = {};
        catalog.forEach(function (p) { vendorSet[p.vendor] = true; });
        els.stats.textContent = catalog.length + " products from " + Object.keys(vendorSet).length + " manufacturers.";

        populateDynamicFilters();
        renderStatsPopover(catalog);
        syncDomFromFilters();
        renderResults();
      })
      .catch(function () {
        els.summary.textContent = "Unable to load product catalog.";
        els.container.innerHTML = '<div class="pf-empty">Catalog failed to load. Try refreshing the page.</div>';
      });
  }

  if (document.readyState === "loading") {
    document.addEventListener("DOMContentLoaded", init);
  } else {
    init();
  }
})();
