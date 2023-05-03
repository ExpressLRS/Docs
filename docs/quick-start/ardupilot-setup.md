---
template: main.html
description: ExpressLRS can be used with Ardupilot! This guide got you covered with the correct Ardupilot Parameters.
---

![Setup-Banner](https://github.com/ExpressLRS/ExpressLRS-Hardware/raw/master/img/quick-start.png)

## Ardupilot Serial Setup

Ardupilot Firmware must be 4.1 or higher to run CRSF protocol.
As with any serial-based receiver, you need to attach the TX/RX pads to a UART on your flight controller, then enable Serial RX in the corresponding UART in Ardupilot.
In mission planner, you will need to go to the ```config tab -> parameter tree```
```
SERIALx_PROTOCOL = 23 (RCIN)
RSSI_TYPE = 3 (ReceiverProtocol)
```
our packet rate is different than CRSF packet rate, and ardupilot will keep on reporting the missmatch, but recently they have an option to suppress the report. Currently Ardupilot provide a way to suppress this notification with the parameter below. (this will not cause any effect to RC link or telemetry Link.)
```
RC_OPTIONS turn on Bit 9th which is  "Suppress CRSF mode/rate message for ELRS systems".
```

Once you have set the parameter above, power-cycle the flight controller by disconnecting and reconnecting your battery and USB. Ardupilot should automatically run with ELRS, but if it fails, set ``RC_PROTOCOL`` parameter 9th bit to 1 (CRSF option)
 and set the other parameter as below:
```
SERIALx_PROTOCOL = 23 (RCIN)
SERIALx_BAUD = 115
RSSI_TYPE = 3 (ReceiverProtocol)
```

## Ardupilot Flightmodes
Ardupilot default flightmodes channel is channel 8, but ELRS 8 position channel is on channel 12 (in hybrid switchMode). you will need to set your handset to use channel 12 as flightmodes and set Ardupilot parameter:
```
FLTMODE_CH=12
```
if you are using WideSwitch mode (only available in elrs V2 and above), you can use any channel for your 8 flightmode selection (beside channel 15 which is LQ and channel 16 which is RSSI).
## Ardupilot RSSI and Link Quality
To get RSSI and LQ shown in OSD (in %) set:
```
RSSI_TYPE = 3 (ReceiverProtocol)
```

and go to your OSD tab, and place your RSSI and LQ element where you want them to be.

If you feel any delay or lag in the control, check the RX connection to the Flight Controller.
On some Flight Controllers you have to use full DMA supported input pin.

Happy Flying! :airplane:
