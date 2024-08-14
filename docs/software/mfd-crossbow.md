---
template: main.html
description: ExpressLRS Backpack integration with the MFD Crossbow AAT.
---

![Software Banner](https://raw.githubusercontent.com/ExpressLRS/ExpressLRS-Hardware/master/img/software.png)

## Introduction
Version 3.4+ of ELRS introduces a new option in the Backpack section of the ELRS LUA script called "Telemetry." This feature allows a Backpack equipped ELRS Transmitter to forward CRSF telemetry frames to any peer that is capable of receiving ESPNOW messages. These frames can be consumed by any Backpack receivers that are bound with your bind phrase.

## Prerequisites
- ELRS transmitter module with internal TX-Backpack.
- Backpack-capable receiver
- ELRS LUA script on your handset.

## Enabling the Backpack Telemetry

### Step 1: Update Firmware
Ensure both your transmitter module, and the embedded Backpack are up to date with the latest release versions:

- For the main ELRS firmware, follow the [Firmware Update Guide](https://www.expresslrs.org/quick-start/getting-started/) for detailed instructions.
- For the TX-Backpack, follow the [Transmitter Backpack Firmware Guide](https://www.expresslrs.org/hardware/backpack/backpack-tx-setup/) for detailed instructions.

### Step 2: Enable Backpack Telemetry in ELRS LUA Script
1. **Access the LUA Script:**
      - Power on your transmitter and navigate to the System menu.
      - Execute the ELRS LUA script.

2. **Navigate to the Backpack Section:**
      - Scroll to find the "Backpack" section within the LUA script.
      - Select the "Telemetry" option.

3. **Enable Backpack Telemetry:**
      - Set the "Telemetry" option to `On`.
      - Exit the script.
      - Your TX module is now configured to broadcast telemetry to a Backpack receiver.

4. **Disabling Backpack Telemetry:**

      Backpack telemetry is transmitted on the 2.4G WiFi band, via ESPNOW (this should have a very limited impact on any LoRa signals, as it is modulated via OFDM like a normal WiFi hotspot). Every telemetry message that your transmitter receives from the craft will be re-transmitted via ESPNOW. You may want to disable Backpack Telemetry to reduce your footprint on the RF noise floor when you aren't using it, especially if you are at something like a race day, where there is often contention on the RF spectrum. To disable Backpack Telemetry:

      - Execute the ELRS LUA script.
      - Scroll to find the "Backpack" section within the LUA script.
      - Select the "Telemetry" option.
      - Set the "Telemetry" option to `Off`.
      - Exit the script.

### Step 3: Flash the Backpack firmware to a Backpack Receiver


### Crossbow Configuration


### Viewing Telemetry Data
Once configured, power up your GPS-equipped craft and establish the link between your ELRS Transmitter and Receiver. Ensure that GPS telemetry is being received on your Handset (go to the Model menu in EdgeTX, and inspect the Telemetry page to make sure you are getting GPS coordinates). The Sentinel Antenna Tracker will be able to read GPS data and other telemetry information from the telemetry feed provided by the ELRS transmitter.

## Troubleshooting
If you encounter issues:

- **No Telemetry Data:** Ensure the "Telemetry" option is enabled in the Backpack section of the LUA script and that the firmware is up to date. Also check that your Telemetry Ratio is set to a value that is able to provide frequent telemetry packets. As a rule of thumb, a ratio somewhere between 1:2 to about 1:16 (depending on your packet rate) will suffice. See [Packet Rate and Telemetry Ratio](https://www.expresslrs.org/quick-start/transmitters/lua-howto/#packet-rate-and-telemetry-ratio) and [Telemetry](https://www.expresslrs.org/quick-start/pre-1stflight/#telemetry)

- **Binding Issues:** Verify that the bind phrase is correctly set and matches between the Backpack on your transmitter and the Backpack receiver.

- **Interference:** The Backpack Telemetry feature uses a point to point WiFi-based link to forward telemetry. The Backpack receiver should be within 10m of the ELRS transmitter (ideally 5m or less) for good WiFi signal. Some ELRS transmitters and receivers have better Backpack WiFi antennas than others, so your mileage may vary depending on your hardware. If you are experiencing drops in the link between ELRS and the tracker, try moving the two closer, or move to an area with less WiFi noise.
