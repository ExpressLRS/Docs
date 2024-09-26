---
template: main.html
description: ExpressLRS Backpack can forward telemetry data to third party systems via ESPNOW.
---

![Software Banner](https://raw.githubusercontent.com/ExpressLRS/ExpressLRS-Hardware/master/img/software.png)

## Introduction
Version 3.4+ of ELRS introduces a new option in the Backpack section of the ELRS LUA script called "Telemetry." This feature allows a Backpack equipped ELRS Transmitter to forward CRSF telemetry frames to any peer that is capable of receiving ESPNOW messages. These frames can be consumed by any Backpack receivers that are bound with your bind phrase.

<figure markdown>
![Sentinel Integration](../assets/images/backpack-telemetry.png)
<figcaption>Sentinel Integration</figcaption>
</figure>

This capability is particularly useful for devices like the Sentinel Antenna Tracker, which can subscribe to ESPNOW telemetry packets and read GPS data from the telemetry feed. See [the Sentinel product page](https://www.virtualpilot.co.uk/index.php?route=product/product&product_id=59)

## Prerequisites
- ELRS transmitter and receiver with the latest firmware.
- Backpack-capable receiver (e.g., in the Sentinel Antenna Tracker).
- Configured ELRS LUA script on your transmitter.

## Setting Up the Backpack Telemetry Feature

### Step 1: Update Firmware
Ensure both your transmitter and receiver are running the latest firmware. Follow the [firmware update guide](https://www.expresslrs.org/quick-start/getting-started/) for detailed instructions. This feature is available in v3.4.0 onwards.

### Step 2: Enable Backpack Telemetry in ELRS LUA Script
1. **Access the LUA Script:**
      - Power on your transmitter and navigate to the System menu.
      - Execute the ELRS LUA script.

2. **Navigate to the Backpack Section:**
      - Scroll to find the "Backpack" section within the LUA script.
      - Select the "Telemetry" option.

3. **Enable Backpack Telemetry:**
      - Set the "Telemetry" option to `ESPNOW`.
      - Exit the script.

      **NOTE:** Backpack telemetry is transmitted on the 2.4G WiFi band, via ESPNOW (this should have a very limited impact on any LoRa signals, as it is modulated via OFDM like a normal WiFi hotspot). Every telemetry message that your transmitter receives from the craft will be re-transmitted via ESPNOW. You may want to disable Backpack Telemetry to reduce your footprint on the RF noise floor when you aren't using it, especially if you are at something like a race day, where there is often contention on the RF spectrum. To disable Backpack Telemetry:

      - Execute the ELRS LUA script.
      - Scroll to find the "Backpack" section within the LUA script.
      - Select the "Telemetry" option.
      - Set the "Telemetry" option to `Off`.
      - Exit the script.

### Step 3: Bind Backpack Receivers
Ensure your Backpack receivers (e.g., the one in the Sentinel Antenna Tracker) are bound using your bind phrase. This allows them to receive telemetry data sent via ESPNOW. See [the Sentinel ELRS setup guide](https://github.com/aat-sentinel/Documentation/blob/main/Sentinel%20AAT%20lite%20User%20Guide%20-%20ELRS%20setup.pdf)

## Using the Telemetry Feature with Sentinel Antenna Tracker

### Sentinel Configuration
The Sentinel Antenna Tracker includes an ESP12 Backpack-capable receiver that can consume ESPNOW telemetry frames. Ensure the tracker is properly configured to subscribe to ESPNOW telemetry packets. See [the Sentinel ELRS setup guide](https://github.com/aat-sentinel/Documentation/blob/main/Sentinel%20AAT%20lite%20User%20Guide%20-%20ELRS%20setup.pdf)

### Viewing Telemetry Data
Once configured, power up your GPS-equipped craft and establish the link between your ELRS Transmitter and Receiver. Ensure that GPS telemetry is being received on your Handset (go to the Model menu in EdgeTX, and inspect the Telemetry page to make sure you are getting GPS coordinates). The Sentinel Antenna Tracker will be able to read GPS data and other telemetry information from the telemetry feed provided by the ELRS transmitter.

## Advanced Use Cases
This new telemetry feature can be expanded for various applications, e.g.:

- Real-time flight data monitoring.
- Integration with other ESP Backpack-compatible devices.

An Espressif ESP-based microcontroller, like the ESP32 or ESP8266 (and many variants) is capable of receiving ESPNOW frames. Custom firmware could be written to decode the CRSF telemetry and consume it in your own custom solution. See [this ESPNOW guide](https://randomnerdtutorials.com/esp-now-esp32-arduino-ide/) for an example of developing using ESPNOW.

## Troubleshooting
If you encounter issues:

- **No Telemetry Data:** Ensure the "Telemetry" option is set to `ESPNOW` in the Backpack section of the LUA script and that the firmware is up to date. Also check that your Telemetry Ratio is set to a value that is able to provide frequent telemetry packets. As a rule of thumb, a ratio somewhere between 1:2 to about 1:16 (depending on your packet rate) will suffice. See [Packet Rate and Telemetry Ratio](https://www.expresslrs.org/quick-start/transmitters/lua-howto/#packet-rate-and-telemetry-ratio) and [Telemetry](https://www.expresslrs.org/quick-start/pre-1stflight/#telemetry)

- **Binding Issues:** Verify that the bind phrase is correctly set and matches between the Backpack on your transmitter and the Sentinel receiver.

- **Interference:** The Backpack Telemetry feature uses a point to point WiFi-based link to forward telemetry. The Sentinel tracker (or other Backpack receiver type) should be within 10m of the ELRS transmitter (ideally 5m or less) for good WiFi signal. Some ELRS transmitters have better Backpack WiFi antennas than others, so your mileage may vary depending on your hardware. If you are experiencing drops in the link between ELRS and the Sentinel tracker (or other Backpack receiver type), try moving the two closer, or move to an area with less WiFi noise.
