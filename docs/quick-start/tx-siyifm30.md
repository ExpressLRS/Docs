---
template: main.html
---

![Setup-Banner](https://raw.githubusercontent.com/ExpressLRS/ExpressLRS-hardware/master/img/quick-start.png)

Targets:

- `FM30_TX_via_STLINK` (Initial Flash)
- `FM30_TX_via_DFU` (Updating)

## Initial Flash

Begin by opening the TX module by removing the 4 screws at the corners using a small phillips screwdriver.
Lift the cover from the case and unscrew the antenna holder from the cover. Remove the 2 screws around the edges and remove the PCB module from the case.

Solder 4 STLink wires to the `JP4` holes (CLK-DIO-RST-GND) and 1 wire to `VCC` pad as shown:
![wiring](https://github.com/ExpressLRS/ExpressLRS-Hardware/blob/master/img/siyi/jupa/Siyi-4.JPG?raw=true)

Attach to an STLink as shown:

![stlinked](https://github.com/ExpressLRS/ExpressLRS-Hardware/blob/master/img/siyi/jupa/Siyi-5.JPG?raw=true)

With the module connected shown above, and your [Firmware Options](/quick-start/firmware-options) set, hit **Build & Flash** in the ExpressLRS Configurator and wait for the process to finish. Once that's done, and the Success Message showing, you can now remove/unsolder the STLink, and re-assemble the module, and put it into your Radio's Module Bay.

Verification can be done using the ELRS.lua script. It should show the Version Hash at the top, as well as the options you can set. If it's showing "Connecting", check if External Module is set to CRSF for the selected model in your radio, and that internal RF module is set to off. See general Troubleshooting section for other ways to determine your module is flashed and ready for flying.

## Updating
Plug the FM30 into the USB of your computer. Then select `FM30_TX_via_DFU` and press **Build & Flash** to update the TX.