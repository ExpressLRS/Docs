---
template: main.html
description: The ExpressLRS Backpack opens up new possibilities, like the hands-off tuning of your FPV Goggles.
---

![Hardware-Banner](https://raw.githubusercontent.com/ExpressLRS/ExpressLRS-Hardware/master/img/hardware.png)

## What is a Backpack?

A Backpack is an add-on device that facilitates wireless communication between an ExpressLRS module and another device (e.g. a Video Receiver on your goggles) using ESPnow as protocol.

<figure markdown>
![Backpack Comms](https://github.com/ExpressLRS/Backpack/raw/master/img/flow-diagram-backpack.jpg)
<figcaption>Communication between an ExpressLRS module and a Video Receiver<figcaption>
</figure>

## Usage Scenario

You are setting up to fly with others and your favorite video channel is already in use. You're asked to use R2 as that's the vacant one. Using the [ExpressLRS Lua script](../../quick-start/transmitters/lua-howto.md#vtx-administrator), you change the setting into R2 (this while your aircraft is still unpowered). You power up your goggles equipped with a VRX Backpack. Then plug in your aircraft. Upon establishment of the connection, the VTX and the VRX are automatically set into R2. You're now ready to fly. No fiddling with channels on the OSD or your goggles.

## Okay, I'm sold. What do I need to get this working?

You already have the majority of the hardware needed. Most of the ESP-based ExpressLRS modules come with the TX Backpack. For the VRX Backpack, you can reuse any ESP-based ExpressLRS receiver (recommended are the EP1/EP2 receivers as they have boot pads, instead of boot buttons), or for a complete DIY route, you'll need an ESP-01F module.

An off-the-shelf VRX Backpack has also appeared from Happymodel: the [EP82](https://www.happymodel.cn/index.php/2021/11/10/ep82-vrx-backpack-module-for-control-rapidfire-vrx-with-elrs-tx-module/)

See the tables below for the list of supported devices:

### Supported TX-Backpack Targets

| TX Module    | Support |
| ---------------------- | ---------------- |
| Happymodel ES24TX Pro | ✔️ Fully supported  |
| Happymodel ES24TX  | ✔️ Fully supported  |
| Happymodel Slim Pro  | ✔️ Fully supported  |
| Happymodel Slim Ironman | ✔️ Fully supported  |
| Happymodel Slim T-Lite| ✔️ Fully supported  |
| Happymodel ES900TX  | ✔️ Fully supported  |
| Happymodel ES915TX (STM32 version)  | ❌ Not compatible  |
| FrSky R9M | ✔️ Supported with addition of a ESP8285 |
| FrSky R9 (all others)  | ❌ Not compatible  |
| NamimnoRC Flash (STM32 version)  | ✔️ Fully supported |
| NamimnoRC Flash OLED(ESP version)  | ✔️ Fully supported |
| NamimnoRC Voyager (STM32 version)  | ✔️ Fully supported |
| NamimnoRC Voyager OLED(ESP version)  | ✔️ Fully supported |
| Axis Flying THOR  | ✔️ Fully supported |
| HGLRC Hermes | ❌ Not compatible  |
| BETAFPV 2.4 TX 1W Micro | ✔️ Fully supported  |
| BETAFPV 2.4 TX | ❌ Not compatible  |
| BETAFPV 900 TX | ❌ Not compatible  |
| Radiomaster Zorro  | ✔️ Fully supported |
| Jumper Aion T-Pro Internal | ❌ Not compatible  |
| Jumper Aion Nano | ❌ Not compatible  |
| Vantac Lite | ❌ Not compatible  |
| ImmersionRC Ghost TX | ❌ Not compatible  |
| QuadKopters 2.4 TX | ❌ Not compatible  |
| SIYI FM30 | ❌ Not compatible  |
| DIY TX  | ✔️ Fully supported with addition of a ESP8285  |

### Supported VRx-Backpack Targets

| Backpack Target | Compatibility | Tested?|
| ---------------------- | ---------------- | ---------------- |
| Happymodel EP1/EP2 | ✔️ Compatible | Yes |
| Happymodel ES900RX | ✔️ Compatible | Yes |
| Happymodel EP82 | ✔️ Compatible | Yes |
| BETAFPV Nano 2.4 | ✔️ Compatible | No |
| Flywoo EL24E | ✔️ Compatible | No |
| Flywoo EL24P | ✔️ Compatible | No |
| Ghost ATTO | ❌ Not compatible | N/A |
| HappyModel PP | ❌ Not compatible | N/A |
| HGLRC 2400RX | ✔️ Compatible | No |
| JHEMCU / HiYOUNGER EP24S | ✔️ Compatible | No |
| JHEMCU / HiYOUNGER SP24S | ✔️ Compatible | No |
| JHEMCU / HiYOUNGER RX24T | ❓ Unsure | No |
| Matek R24-S | ✔️ Compatible | No |
| Matek R24-D | ✔️ Compatible | No |
| Jumper Aion RX | ✔️ Compatible | No |
| Vantac 2.4GHz RX | ✔️ Compatible | No |
| Namimno Flash (ESP) | ✔️ Compatible | No |
| QuadKopters Nano | ✔️ Compatible | No |
| SIYI FR Mini | ❌ Not compatible | N/A |

### Video Receivers currently supported include:

| VRX Module    | Support |
| ---------------------- | ---------------- |
| ImmersionRC Rapidfire  | ✔️ Fully supported (Versions 1.2.5 of the rapidFIRE firmware and later)  |
| SkyZone SteadyView | ✔️ Fully supported  |
| TBS Fusion  | ✔️ Fully supported (FTDI needed)  |
| Generic RX5808 Module (some)  | ✔️ Fully supported  |
| FENIX Module  | ✔️ Fully supported  |
| HDZero VRX4  | ✔️ Fully supported  |
| HDZero Goggles (built-in, no mods required)  | ✔️ Fully supported  |

## I'm Ready to Proceed. What do I do next?

If your TX module is already equipped with a TX backpack (see list above), your next step is to update the firmware of the backpack. Proceed to the [TX Backpack Setup page](backpack-tx-setup.md) for more details.

If you're using a DIY TX module and want to add a backpack to it, proceed to the [Backpack Wiki](https://github.com/ExpressLRS/Backpack/wiki).

For the VRX Backpack, you will need to first update the firmware on the ESP device. The firmware will highly depend on which VRX module you will use it on. Proceed to [VRx Backpack Setup page](backpack-vrx-setup.md) for more info.

## Backpack Usage

### LED Status codes

* Solid - The backpack is powered up and ready to receive packets.
* Fast Continious Blinking - WiFi Mode is active and either the Access Point is ready for connection or the Backpack has connected to your Local WiFi Network (0.2.0; Home Network SSID and Password have been set).
* Double Blink, Pause - Backpack is in Binding Mode. Using the ExpressLRS Lua Script, press `Bind` and the TX Backpack should bind with the VRx Backpack.

### Button Operation (If present)

* Pressing and Holding down the button during Power Up puts the device into Bootloader mode. From here, you can flash the firmware via UART using an FTDI dongle (USB to UART Bridge). LED on the Backpack device will be SOLID when in this mode.
* Single Press during Normal or Binding mode will put the device into WiFi Mode.
* Single Press during WiFi Mode will put back the device into Normal Mode.

### Binding

Just like any ExpressLRS device, you can set a **Binding Phrase** for both the TX Backpack and VRx Backpack so they automatically bind with each other during power up. This Binding Phrase can be the same as what you used with your other ExpressLRS devices, or can be entirely different. The concept is the same.

Should you choose to bind manually, the procedure is as follows:

1. Make sure you didn't flash the VRx firmware with a Binding Phrase.
2. Power Cycle the VRx Backpack 3 times every ~30s. This interval gives ample time for your goggles and VRx module to power up and down more gracefully. If your VRx Backpack has a button, it can also be used to power-cycle the device by cycling between WiFi Mode and Normal mode 3x (as WiFi mode reboots the device).
3. The LED on the Backpack should now blink twice followed by a brief pause, then repeats, indicating it is in Binding Mode.
4. Using the ExpressLRS Lua script, navigate into the `Bind` option. Press it once and the LED on both Backpacks should blink once and stay SOLID thereafter.
5. Your Backpacks are now bound and connected and you can now use **VTX Administrator** on the ExpressLRS Lua script to sync your VTX and VRx modules.

### Timeouts

When in Binding Mode (Double Blink & Pause) and no Bind packets have been received within 120s, the VRx Backpack will switch into WiFi Mode. This provides the users a means to enter WiFi Mode when their VRx Backpack doesn't have a Button.