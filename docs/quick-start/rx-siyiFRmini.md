---
template: main.html
---

![Setup-Banner](https://raw.githubusercontent.com/ExpressLRS/ExpressLRS-hardware/master/img/quick-start.png)

Targets:

- `FM30_RX_MINI_via_STLINK` (First-time Flash)
- `FM30_RX_MINI_via_BetaflightPassthrough` (Updates)

The STLink solderpads on the FRmini RX are very tiny and very close together. The picture below is very enlarged.
Solder 5  (preferable Silicon) wires to the GND-RST-VDD-CLK-DIO pads. Solder the open ends to a female 2.54 mm pin connector. (Use 3.3V NOT 5V :fire:).

![pinout](https://github.com/ExpressLRS/ExpressLRS-Hardware/blob/master/img/siyi/jupa/Siyi-12.JPG?raw=true)
![stlink](https://github.com/ExpressLRS/ExpressLRS-Hardware/blob/master/img/siyi/jupa/Siyi-13.JPG?raw=true)

Using the correct target specific for your receiver, set your [Firmware Options](/quick-start/firmware-options) and hit **Build & Flash** on the ExpressLRS Configurator.

Once done, wire your receiver to your Flight Controller. Passthrough flashing can now be used for updating the receiver. The wiring is show below, where the FC TX goes to RX2 and the FC RX goes to TX2.

![pinout](https://github.com/ExpressLRS/ExpressLRS-Hardware/blob/master/img/siyi/jupa/Siyi-16.JPG?raw=true)
![pinout](https://github.com/ExpressLRS/ExpressLRS-Hardware/blob/master/img/siyi/jupa/Siyi-17.JPG?raw=true)

Thank you to [@JupaCreations](http://www.jupacreations.com/)