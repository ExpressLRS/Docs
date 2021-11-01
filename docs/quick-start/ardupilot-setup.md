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
```
Crossfire rate's enum is different with elrs enum, Since Ardupilot doesn't have a way to differentiate ELRS from Crossfire yet, when the telemetry count differs from the reported packet rate's enum, Ardupilot will notify ("CRSF Packet rate is X, telemetry Rate is X"). Currently Ardupilot provide a way to suppress this notification with the parameter below. (this will not cause any effect to RC link or telemetry Link.)
```
RC_OPTIONS turn on Bit 9th which is  "Suppress CRSF mode/rate message for ELRS systems".
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