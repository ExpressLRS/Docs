---
template: main.html
---

![Setup-Banner](https://github.com/ExpressLRS/ExpressLRS-Hardware/raw/master/img/quick-start.png)

## Ardupilot Serial Setup

Ardupilot Firmware must be 4.1 or higher to run CRSF protocol.
As with any serial-based receiver, you need to attach the TX/RX pads to a UART on your flight controller, then enable Serial RX in the corresponding UART in Ardupilot.
In mission planner, you will need to go to the ```config tab -> parameter tree```
```
SERIALx_PROTOCOL = 23 (RCIN)
RSSI_TYPE = 3 (ReceiverProtocol)
RC_OPTIONS = 9
```

Once you have set the parameter above, power-cycle the flight controller by disconnecting and reconnecting your battery and USB. Ardupilot should automatically run with ELRS, but if it fails, set the other parameter as below:
```
SERIALx_PROTOCOL = 23 (RCIN)
SERIALx_BAUDRATE = 115
RC_PROTOCOL = 9 (CRSF)
RSSI_TYPE = 3 (ReceiverProtocol)
```

## Ardupilot Flightmodes
Ardupilot default flightmodes channel is channel 8, but ELRS 8 position channel is on channel 12. you will need to set your handset to use channel 12 as flightmodes and set Ardupilot parameter:
```
FLTMODE_CH=12
```

## Ardupilot RSSI and Link Quality
To get RSSI and LQ shown in OSD (in %) set:
```
RSSI_TYPE = 3 (ReceiverProtocol)
```

and go to your OSD tab, and place your RSSI and LQ element where you want them to be.


Happy Flying! :airplane: