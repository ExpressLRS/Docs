---
template: main.html
---
![Hardware-Banner](https://raw.githubusercontent.com/ExpressLRS/ExpressLRS-Hardware/master/img/hardware.png)

Addon for **R9M modules**, **HappyModel ELRS915TX**, and **HappyModel ES24TX** to allow:

* Logging to Browser and via Websocket
* Flashing ESP Backpack (self)
* Flashing R9M TX
* Possibly more.. wireless trainer mode? Please contribute 🥇 

This is a convenience feature for development purposes and "power users" - soldering can be tricky - please be careful. 👮 

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

## PlatformIO

The platformio sub-project is in [`src/ESPbackpack`](https://github.com/ExpressLRS/ExpressLRS/tree/master/src/ESPbackpack), please get into there first.

Now, please call

```shell
pio run -e ESP_BACKPACK_ESP8266 -t upload
```

or optionally specify the serial adapter to be used

```shell
pio run -e ESP_BACKPACK_ESP8266 -t upload --upload-port /dev/cu.SLAB_USBtoUART
```

For 8285 please set the value of parameter `-e` to `ESP_BACKPACK_ESP8285`.

## Connecting to R9M Module

Let's get together:

* Solder wires connecting `RX1`, `TX1`, `NRESET`, and `BOOT0` pins 🔌 
* ❗ Removing transistor `J6` is not required in contrary to as shown on the picture
* Please note the alternative location to reach `TX1` to keep you from having to solder on the chip's leg 💁

![solder map](https://raw.githubusercontent.com/ExpressLRS/ExpressLRS-Hardware/master/img/r9m_backpack_pins.jpg)
![alessandros version](https://github.com/ExpressLRS/ExpressLRS-Hardware/blob/master/img/wiki-from-discord/sandro%20backpack.jpeg)

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