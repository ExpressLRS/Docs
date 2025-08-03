---
template: main.html
description: The LEDs on both the ExpressLRS Receivers and Transmitter Modules are very helpful diagnostic tool in determining the current status of the device.
---

![Setup-Banner](https://github.com/ExpressLRS/ExpressLRS-Hardware/raw/master/img/quick-start.png)

## Receiver/Transmitter LED Status

ExpressLRS uses the LED to communicate the status of the transmitter/receiver.

The conditions and status LED are as follows:

=== "Receiver Single Color LED"
    |                                                                                         | LED Indication                  | Status                                                            |
    |-----------------------------------------------------------------------------------------|---------------------------------|-------------------------------------------------------------------|
    | ![CONNECTED](../assets/images/LED_ON.gif)                                               | Solid on                        | Connected to a transmitter, or bootloader mode enabled            |
    | ![LEDSEQ_BINDING](../assets/images/LEDSEQ_BINDING_10_10_10_100.gif)                     | Double blink then pause         | Binding mode enabled                                              |
    | ![LEDSEQ_DISCONNECTED](../assets/images/LEDSEQ_DISCONNECTED_50_50.gif)                  | Slow blink 500ms on/off         | Waiting for connection from transmitter                           |
    | ![LEDSEQ_MODEL_MISMATCH](../assets/images/LEDSEQ_MODEL_MISMATCH_10_10_10_10_10_100.gif) | Triple blink then pause         | Connected to transmitter but mismatched model-match configuration |
    | ![LEDSEQ_RADIO_FAILED](../assets/images/LEDSEQ_RADIO_FAILED_20_100.gif)                 | Medium speed blink 100ms on/off | Radio chip not detected                                           |
    | ![LEDSEQ_WIFI_UPDATE](../assets/images/LEDSEQ_WIFI_UPDATE_2_3.gif)                      | Fast blinking 25ms on/off       | WiFi mode enabled                                                 |

=== "Receiver RGB LED"
    |                                                                                     | LED Indication                 | Status                                                            |
    |-------------------------------------------------------------------------------------|--------------------------------|-------------------------------------------------------------------|
    | ![LEDRGB_STARTUP](../assets/images/LEDSEQRGB_STARTUP.gif)                           | Rainbow fade effect            | Starting Up                                                       |
    | ![LEDRGB_WIFI_UPDATE](../assets/images/LEDSEQRGB_WIFI_UPDATE.gif)                   | Green heartbeat                | Web update mode enabled                                           |
    | ![LEDRGB_WAITING_FOR_CONNECTION](../assets/images/LEDSEQRGB_WAITING_TO_CONNECT.gif) | Slow blink 500ms on/off        | Waiting for connection from transmitter                           |
    | ![LEDRGB_RADIO_FAILED](../assets/images/LEDSEQRGB_RADIO_FAILED.gif)                 | Red flashing 100ms on/off      | Radio chip not detected                                           |
    | ![LEDRGB_BINDING_ENABLED](../assets/images/LEDSEQRGB_BINDING.gif)                   | Orange Double blink then pause | Binding mode enabled                                              |
    | ![LEDRGB_MODEL_MISMATCH](../assets/images/LEDSEQRGB_MODEL_MISMATCH.gif)             | Orange Triple blink then pause | Connected to transmitter but mismatched model-match configuration |
    | ![LEDRGB_CONNECTED](../assets/images/LED_RGB_ON.png)                                | Solid single color             | Connected to a transmitter, color indicates packet rate           |
    | ![BOOTLOADER_OR_OFF](../assets/images/LED_RGB_OFF.png)                              | No Light                       | Off or in Bootloader Mode                                         |

    | LED Color    | 2.4GHz Packet rate (Hz) | 915/868MHz Packet rate (Hz) |
    |--------------|-------------------------|-----------------------------|
    | Red          | F1000                   | 200                         |
    | Yellow       | F500                    |                             |
    | Yellow-Green | D500                    | 100 Full                    |
    | Green        | D250                    | 100                         |
    | Cyan         | 333 Full                |                             |
    | Light Blue   | 500                     | 50                          |
    | Blue         | 250                     | 25                          |
    | Blue-Purple  | 150                     |                             |
    | Purple       | 100 Full                | D50                         |
    | Magenta      | 50                      |                             |
    
=== "Transmitter RGB LED"
    | LED Indication                | Status                                                 |
    |-------------------------------|--------------------------------------------------------|
    | Rainbow fade effect           | Starting Up                                            |
    | Green heartbeat               | Web update mode enabled                                |
    | Blue heartbeat                | Bluetooth joystick enabled                             |
    | Red flashing 100ms on/off     | Radio chip not detected                                |
    | One Orange flash every second | No handset connection                                  |
    | Solid single color            | Connected to receiver, color indicates packet rate     |
    | Fading single color           | No connection to receiver, color indicates packet rate |

    | LED Color    | 2.4GHz Packet rate (Hz) | 915/868MHz Packet rate (Hz) |
    |--------------|-------------------------|-----------------------------|
    | Red          | F1000                   | 200                         |
    | Yellow       | F500                    |                             |
    | Yellow-Green | D500                    | 100 Full                    |
    | Green        | D250                    | 100                         |
    | Cyan         | 333 Full                |                             |
    | Light Blue   | 500                     | 50                          |
    | Blue         | 250                     | 25                          |
    | Blue-Purple  | 150                     |                             |
    | Purple       | 100 Full                | D50                         |
    | Magenta      | 50                      |                             |
