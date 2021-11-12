---
template: main.html
---
![Hardware-Banner](https://raw.githubusercontent.com/ExpressLRS/ExpressLRS-Hardware/master/img/hardware.png)

Addon for **R9M modules** and **HappyModel ELRS915TX** to allow:

* Wireless firmware update via ExpressLRS Configurtor
* Flashing ESP Backpack (self)
* Flashing R9M TX locally via browser
* Logging to Browser and via Websocket
* Possibly more.. wireless trainer mode? Please contribute 🥇 

This is a convenience feature for development purposes and "power users" - soldering can be tricky - please be careful. 👮 
This feature is built into most off-the-shelf ELRS TXes now too.

## Parts

- USB to **Serial Dongle** (aka FTDI Stick)
- **R9M** (previously flashed with ExpressLRS) 📡 
- any ESP 8266/8285 based chip should work, recommended are
  - **ESP01F** for quick install (internal resistors ease initial flashing, but wire antenna)
  - **ESP12F** for pcb wifi antenna, FCC/CE certififed (but more complex circuit required for initial flashing)
- very _thin_ **wire** (AWG30 "kynar"); or [enameled wire](https://www.youtube.com/watch?v=gMi0-YtpwM4) if you are good with routing (0.5mm holes in PCB)
- depending on your **soldering skill** using flux and leaded solder is recommended

## Board ESP01F (ESP8285)

* Connect the serial adapter to `3.3V`, `GND`, `TX` and `RX`
  * 🔥 `3.3V` **NOT** `5V`
* Additionally, connect `IO0` to `GND` to activate the bootloader and enable flashing
* Quite some serial adapters have `TX` and `RX` swapped, mislabeled, or both 😸. Please double check!

## Board ESP12F (ESP8266)

This module needs a more complex circuit to get flashed:

![](https://image.easyeda.com/histories/61110e5f31b344acaa668114f65cce9a.png)

## ESP module firmware

Before connecting the ESP module to the TX module, you need to [flash the ESP module with the latest TX Backpack firmware.](https://github.com/ExpressLRS/Backpack/wiki/Flashing-the-TX-Backpack-Firmware)
To transfer the ESP module to the firmware mode, it is necessary to connect the `IO0` and `GND` pins before connecting the programmer to the computer.

## Connecting to R9M 2018 (Old version) Module

Let's get together:

* Solder wires connecting `RX1`, `TX1`, `NRESET`, and `BOOT0` pins 🔌 
* ❗ Removing transistor `J6` is not required in contrary to as shown on the picture
* Please note the alternative location to reach `TX1` to keep you from having to solder on the chip's leg 💁

![solder map](https://raw.githubusercontent.com/ExpressLRS/ExpressLRS-Hardware/master/img/r9m_backpack_pins.jpg)
![alessandros version](https://github.com/ExpressLRS/ExpressLRS-Hardware/blob/master/img/wiki-from-discord/sandro%20backpack.jpeg)

## Connecting to R9M 2019 Module

The ESP module is wired:

* GPIO5 -> ESP IO5
* GPIO4 -> ESP IO4
* GPIO0 -> ESP IO0 (It is necessary to cut the wiring leading to the button.)
* GPIO16 -> ESP IO16 (If desired, an LED and a current-limiting resistor of 0.5-1.5kOm must be added to the circuit.)
* TX -> ESP RX
* RX -> ESP TX
* 3.3v -> ESP 3.3v
* GND -> ESP GND

* The button is required to enable the access point mode on the ESP.
* The LED is required to indicate the operation of the ESP access point mode. If it is not needed, it can be omitted.

![R9M2019BackpackMod1](https://user-images.githubusercontent.com/32848699/141538176-e2d33228-cc60-4fe7-989e-6928974daf55.png)
![R9M2019BackpackMod2](https://user-images.githubusercontent.com/32848699/141538188-6c18b2d9-c925-47cf-8d4f-9a4fbbbe5fb7.png)


## Connecting to Happymodel ELRS915TX

The ESP module is wired:

* NRSET -> ESP DIO5
* BOOT0 -> ESP DIO4
* TX -> ESP RX
* RX -> ESP TX
* 3.3v -> ESP 3.3v
* GND -> ESP GND

Updating the ELRS915TX over wifi is supported from 1.0.0 RC8 onwards.

<img src="https://github.com/ExpressLRS/ExpressLRS-Hardware/blob/master/img/wiki-from-discord/es915%20pinout.jpeg?raw=true" width = "30%">
<img src="https://github.com/ExpressLRS/ExpressLRS-Hardware/blob/master/img/wiki-from-discord/quibic%20mod.jpeg?raw=true" width = "30%">

## Connect via WiFi

Initially, the module will open an accesspoint for you to connect and change the settings to your desire. This accesspoint is available at the `ESP Wifi Manager` wifi network. Then navigate to http://elrs_tx.local/, and after building your firmware, upload the file to the website and flash.

<img src="https://github.com/ExpressLRS/ExpressLRS-Hardware/blob/master/img/wiki-from-discord/web%20fronted.png?raw=true" width = "30%">

## Why does the ES24TX have a wifi AP, is there any way to turn it off?

No, there is no way to disable it, HappyModel should not have put any firmware on it. You're welcome to wipe it with esptool.
