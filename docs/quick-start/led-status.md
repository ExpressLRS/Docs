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
| One Orange flash every second | No handset connection |
| Solid single color | Connected to receiver, color indicates packet rate |
| Fading single color | No connection to receiver, color indicates packet rate |

## Receiver LED Status

Receivers with a single color LED communicate their status as follows:

| LED Indication | Status |
|---|---|
| Slow blink 500ms on/off | Waiting for connection from transmitter |
| Fast blinking 25ms on/off | WiFi mode enabled |
| Medium speed blink 100ms on/off | Radio chip not detected |
| Double blink then pause | Binding mode enabled |
| Triple blink then pause | Conntected to transmitter but mismatched model-match configuration |

Receivers with RGB LED show status as indicated below:

| LED Indication | Status |
|---|---|
| Rainbow fade effect | Starting Up |
| Green heartbeat | Web update mode enabled |
| Slow blink 500ms on/off | Waiting for connection from transmitter |
| Red flashing 100ms on/off | Radio chip not detected |
| Orange Double blink then pause | Binding mode enabled |
| Orange Triple blink then pause | Conntected to transmitter but mismatched model-match configuration |
| Solid single color | Connected to transmitter, color indicates packet rate |
