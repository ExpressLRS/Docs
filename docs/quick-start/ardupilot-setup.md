---
template: main.html
---

![Setup-Banner](https://github.com/ExpressLRS/ExpressLRS-Hardware/raw/master/img/quick-start.png)

## Ardupilot Serial Setup

As with any serial-based receiver, you need to attach the TX/RX pads to a UART on your flight controller, then enable Serial RX in the corresponding UART in Ardupilot.
In mission planner, you will need to go to the ```config tab -> parameter tree```
```
SERIALx_PROT = 23 (RCIN)
RSSI_TYPE = 3 (ReceiverProtocol)
```

Once you have set the parameter above, power-cycle the flight controller by disconnecting and reconnecting your battery and USB. Ardupilot should automatically run with ELRS, but if it fails, set the other parameter as below:
```
SERIALx_PROT = 23 (RCIN)
SERIALx_BAUD = 115
RC_PROT = 9 (CRSF)
RSSI_TYPE = 3 (ReceiverProtocol)
```

## Ardupilot Flightmodes
Ardupilot default flightmodes channel is channel 8, but ELRS 8 position channel is on channel 12. you will need to set your handset to use channel 12 as flightmodes and set Ardupilot parameter:
```
FLTMODE_CH=12
```

## Ardupilot RSSI and Link Quality
To show RSSI (in %) set:
```
RSSI_TYPE = 3 (ReceiverProtocol)
```
But if you prefer to see the LQ instead of RSSI, you need to set:
```
RSSI_TYPE = 2 (RC Channel PWM value)
RSSI_CHANNEL = 15 (channel 15 is LQ)
```
And if you prefer to see all Rfmode, LQ, and RSSI dBm simultaneously, you will need a custom firmware of Ardupilot that has a small snippet to show RFmode, LQ, and RSSI. You can get your Ardupilot .hex files for the custom firmware here:
https://github.com/StonedDawg/ardupilot/tree/4.1devrssi/release

Click on the FC firmware you need, and then right click on the download button and save link as. and set:
```
RSSI_TYPE = 3 (ReceiverProtocol)
```
This custom firmware will show the OSD LQ ELEMENT as XX.YYY (RFmode.LQ) and the OSD RSSI ELEMENT as dBm. It will also bypass the Ardupilot crossfire serial number check, that causes a notification message to keep popping up (CRSF: RFmode is x, rate is xx).

Happy Flying! :airplane: