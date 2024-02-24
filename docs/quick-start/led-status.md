---
template: main.html
description: The LEDs on both the ExpressLRS Receivers and Transmitter Modules are very helpful diagnostic tool in determining the current status of the device.
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

|| LED Indication | Status |
|---|---|---|
|![LEDSEQ_DISCONNECTED](https://cdn.discordapp.com/attachments/738450139693449258/921065812985520268/LEDSEQ_DISCONNECTED_50_50.gif)| Slow blink 500ms on/off | Waiting for connection from transmitter |
|![LEDSEQ_WIFI_UPDATE](https://cdn.discordapp.com/attachments/738450139693449258/921065813983760384/LEDSEQ_WIFI_UPDATE_2_3.gif)| Fast blinking 25ms on/off | WiFi mode enabled |
|![LEDSEQ_RADIO_FAILED](https://cdn.discordapp.com/attachments/738450139693449258/921065813719527464/LEDSEQ_RADIO_FAILED_20_100.gif)| Medium speed blink 100ms on/off | Radio chip not detected |
|![LEDSEQ_BINDING](https://cdn.discordapp.com/attachments/738450139693449258/921065812763218010/LEDSEQ_BINDING_10_10_10_100.gif)| Double blink then pause | Binding mode enabled |
|![LEDSEQ_MODEL_MISMATCH](https://cdn.discordapp.com/attachments/738450139693449258/921065813425934446/LEDSEQ_MODEL_MISMATCH_10_10_10_10_10_100.gif)| Triple blink then pause | Connected to transmitter but mismatched model-match configuration |
|![CONNECTED](https://cdn.discordapp.com/attachments/738450139693449258/921065812507373568/LED_ON.gif)| Solid on | Connected to a transmitter, or bootloader mode enabled |

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
