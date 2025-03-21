---
template: main.html
---

![Info Banner](https://github.com/ExpressLRS/ExpressLRS-Hardware/blob/master/img/information.png?raw=true)

## Technical words with explanations

Below you can find a list of terms you might not be sure about, as well as some common abbreviations:

- `BL`: Bootloader, loads the FW
- `CRSF`: TBS Crossfire, more specifically in our case most often referring to the communication protocol between TX and TX module and RX and FC respectively
- `ESC`: Electronic Speed Controller
- `FC`: Flight Controller
- `FW`: Firmware
- `LQ`: Link Quality, percentage of expected packets received. Our preferred method of measuring the quality of the control link
- `Lua`: Means "Moon" in Portuguese. As such, Lua is the correct way to write and not all uppercase. The ExpressLRS Lua script can be installed on a OpenTX radio, to easily alter TX parameters like Packet rate, Telemetry ratio and Output power. But also shows if the radio (OpenTX) is communicating correctly with the module. ( e.g. 0:50, 0:150, 0:200 and so on.)
- `MCU`: Micro Controller Unit, generally denotes an embedded system controller as opposed to big iron CPU
- `OSD`: On Screen Display, refer to [this page for instructions for setup in BF](../quick-start/pre-1stflight.md#rssi-and-link-quality)
- `OTA`: Update your device `Over The Air` (WiFi)
- `OTX`: OpenTX
- `RSSI`: Received Signal Strength Indicator, "arbitrary" scaled version of `RSSI dBm` or LQ. [Signal Health: LQI and RSSI Explained](../info/signal-health.md)
- `RSSI dBm`: Measure of power level measured in dBm. Basically, how strong the signal being received is
- `S.Port`: SmartPort, sometimes referred to as `sport`. FrSky "telemetry" protocol. The `S.Port` also gets used for updating FrSky receivers.
- `DVDA`: Deja Vu Diversity Aid, also referred to as D-mode. This mode sends the same packet multiple times consecutively (2 times for D-250 and 4 for D-500). It increases LQ at the cost of range and latency. 
- `FLRC`: Fast Long Range Communication, also known as F-mode. It is a term that combines a few signal processing techniques (demodulation, forwarding error correction and interleaving) to enable high data rates. This results in lower latency and comparable (or shorter) range.

To be continued.
