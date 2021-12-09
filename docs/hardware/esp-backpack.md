---
template: main.html
---
![Hardware-Banner](https://raw.githubusercontent.com/ExpressLRS/ExpressLRS-Hardware/master/img/hardware.png)

## What is a Backpack?

A Backpack is an add-on device that facilitates wireless communication between an ExpressLRS module and another device (e.g. a Video Receiver on your goggles) using ESPnow as protocol.

![Backpack Comms](https://github.com/ExpressLRS/Backpack/raw/master/img/flow-diagram-backpack.jpg)

## Usage Scenario

You are setting up to fly with others and your favorite video channel is already in use. You're asked to use R2 as that's the vacant one. Using the [ExpressLRS lua script](../../quick-start/lua-howto/#vtx-administrator), you change the setting into R2 (this while your aircraft is still unpowered). You power up your goggles equipped with a VRX Backpack. Then plug in your aircraft. Upon establishment of the connection, the VTX and the VRX are automatically set into R2. You're now ready to fly. No fiddling of channels on the OSD or on your goggles.

## Okay, I'm sold. What do I need to get this working?

You already have the majority of the hardware needed. Most of the ESP-based ExpressLRS modules come with the TX Backpack. For the VRX Backpack, you can reuse any ESP-based ExpressLRS receiver (recommended are the EP1/EP2 receivers as they have boot pads, instead of boot buttons), or for a complete DIY route, you'll need an ESP-01F module.

See the tables below for the list of supported devices:

### Supported TX-Backpack Targets

| TX Module    | Support |
| ---------------------- | ---------------- |
| Happy Model ES24TX  | ✔️ Fully supported  |
| Happy Model Slim Pro  | ✔️ Fully supported  |
| Happy Model Slim Ironman | ✔️ Fully supported  |
| Happy Model Slim T-Lite| ✔️ Fully supported  |
| Happy Model ES900TX  | ✔️ Fully supported  |
| Happy Model ES915TX (STM32 version)  | ❌ Not compatible  |
| FrSky R9 (all)  | ❌ Not compatible  |
| Namimno Flash (STM32 version)  | ✔️ Fully supported |
| Namimno Flash OLED(ESP version)  | ✔️ Fully supported |
| Namimno Voyager (STM32 version)  | ✔️ Fully supported |
| Namimno Voyager OLED(ESP version)  | ✔️ Fully supported |
| Axis Flying THOR  | ✔️ Fully supported |
| HGLRC Hermes | ❌ Not compatible  |
| BETAFPV 2.4 TX | ❌ Not compatible  |
| BETAFPV 900 TX | ❌ Not compatible  |
| ImmersionRC Ghost TX | ❌ Not compatible  |
| QuadKopters 2.4 TX | ❌ Not compatible  |
| SIYI FM30 | ❌ Not compatible  |
| DIY TX  | ✔️ Fully supported with addition of a ESP8285  |

### Supported VRx-Backpack Targets

| Backpack Target | Compatibility | Tested?|
| ---------------------- | ---------------- | ---------------- |
| Happy Model EP1/EP2 | ✔️ Compatible | Yes |
| Happy Model ES900RX | ✔️ Compatible | Yes |
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
| Namimno Flash (ESP) | ✔️ Compatible | No |
| QuadKopters Nano | ✔️ Compatible | No |
| SIYI FR Mini | ❌ Not compatible | N/A |

### Video Receivers currently supported include:

| VRX Module    | Support |
| ---------------------- | ---------------- |
| ImmersionRC Rapidfire  | ✔️ Fully supported (Versions 1.2.5 of the rapidFIRE firmware and later)  |
| SkyZone SteadyView | ✔️ Fully supported  |
| TBS Fusion  | ❌  Not yet supported (check back soon)  |
| Generic RX5808 Module  | ✔️ Fully supported  |
| FENIX Module  | ✔️ Fully supported  |

## I'm Ready to Proceed. What do I do next?

If you're TX module is already equipped with a TX backpack (see list above), your next step is to update the firmware of the backpack. Proceed to the [next page](../../hardware/backpack-tx-setup/) for more details.

If you're using a DIY module and want to add a backpack into it, proceed to the [Backpack Wiki](https://github.com/ExpressLRS/Backpack/wiki).

For the VRX Backpack, you will need to first update the firmware on the device. The firmware will highly depend on which VRX module you will use it on. Proceed to [this page](../../hardware/backpack-vrx-setup/) for more info.

[TX Backpack Setup](../../hardware/backpack-tx-setup/){.md-button} 

[VRx Backpack Setup](../../hardware/backpack-vrx-setup/){.md-button}

