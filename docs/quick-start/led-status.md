---
template: main.html
description: The LEDs on both the ExpressLRS Receivers and Transmitter Modules are very helpful diagnostic tool in determining the current status of the device.
---

![Setup-Banner](https://github.com/ExpressLRS/ExpressLRS-Hardware/raw/master/img/quick-start.png)

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

|| LED Indication | Status |
|---|---|---|
|![LEDSEQ_DISCONNECTED](../assets/images/LEDSEQ_DISCONNECTED_50_50.gif)| Slow blink 500ms on/off | Waiting for connection from transmitter |
|![LEDSEQ_WIFI_UPDATE](../assets/images/LEDSEQ_WIFI_UPDATE_2_3.gif)| Fast blinking 25ms on/off | WiFi mode enabled |
|![LEDSEQ_RADIO_FAILED](../assets/images/LEDSEQ_RADIO_FAILED_20_100.gif)| Medium speed blink 100ms on/off | Radio chip not detected |
|![LEDSEQ_BINDING](../assets/images/LEDSEQ_BINDING_10_10_10_100.gif)| Double blink then pause | Binding mode enabled |
|![LEDSEQ_MODEL_MISMATCH](../assets/images/LEDSEQ_MODEL_MISMATCH_10_10_10_10_10_100.gif)| Triple blink then pause | Connected to transmitter but mismatched model-match configuration |
|![CONNECTED](../assets/images/LED_ON.gif)| Solid on | Connected to a transmitter, or bootloader mode enabled |

Receivers with RGB LED show status as indicated below:

| LED Indication | Status |
|---|---|
| Rainbow fade effect | Starting Up |
| Green heartbeat | Web update mode enabled |
| Slow blink 500ms on/off | Waiting for connection from transmitter |
| Red flashing 100ms on/off | Radio chip not detected |
| Orange Double blink then pause | Binding mode enabled |
| Orange Triple blink then pause | Connected to transmitter but mismatched model-match configuration |
| Solid single color | Connected to a transmitter, color indicates packet rate |
