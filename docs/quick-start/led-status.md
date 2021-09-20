---
template: main.html
---

<img src="https://raw.githubusercontent.com/ExpressLRS/ExpressLRS-Hardware/master/img/software.png">

## Transmitter Module LED Status

If fitted with an RGB LED, ExpressLRS uses it to communicate the status of the transmitter module.

The conditions and status LED are as follows:

| LED Indication | Status |
|---|---|
| Rainbow fade effect | Starting Up |
| Green heartbeat | Web update mode enabled |
| Blue heartbeat | Bluetooth joystick enabled |
| Red flashing 100ms on/off | Radio chip not detected |
| One Red flash every second | No handset Connection |

## Receiver LED Status

Receivers with a single color LED communicate their status as follows:

| LED Indication | Status |
|---|---|
| Slow blink 500ms on/off | Waiting for connection from transmitter |
| Fast blinking 25ms on/off | WiFi mode enabled |
| Medium speed blink 100ms on/off | Radio chip not detected |
| Double blink then wait | Binding mode enabled |

