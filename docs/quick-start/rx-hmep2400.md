---
template: main.html
---

![Setup-Banner](https://raw.githubusercontent.com/ExpressLRS/ExpressLRS-hardware/master/img/quick-start.png)

## Flashing via Wifi 

**(Recommended as first-flash method)**

Target: `HappyModel_EP_2400_RX_via_WIFI`

[Wire up your receiver](../../quick-start/rx-fcprep/#happymodel-ep1-ep2-pp) to a free UART on your Flight Controller. Wire TX on receiver to an RX pad on the FC, and the RX on receiver to a TX pad on the FC in the same UART. Wire 5v and Gnd as normal (5v to a 5v pad on FC and Gnd to a Gnd pad on the FC).

*Note: There are Flight Controllers that will pull the RX pads `LOW` which will put the ESP-based receivers into `Bootloader Mode` unintentionally. A solid LED light on these receivers even with the TX module off is a sign they are in Bootloader Mode. If this is the case, rewire the receiver to a different UART.*

**Build** the firmware using the ExpressLRS Configurator using the correct Target and [options](../../quick-start/firmware-options). Once done, it should open a new window where the `firmware.bin` is. Do not close this window so you can easily navigate to it once it's time to upload the firmware into the receiver.

Power your Flight Controller by either connecting a LiPo or attaching the USB cable (if receiver gets powered from USB via a 4v5 pad). Receiver's LED will blink slow at first, and after 20s or 30s (can be adjusted via ExpressLRS Configurator using `AUTO_WIFI_ON_INTERVAL`), it should blink fast indicating it's on Wifi Hotspot Mode.

Connect to the Wifi Network the receiver has created. It should be named something like `ExpressLRS RX` with the same `expresslrs` password as the TX Module Hotspot. Navigate to the same web address as the TX Module (usually http://10.0.0.1). The Firmware upload page should load, and using the File Upload Form, navigate where the correct Receiver `firmware.bin` is (like with the Tx module, you can also drag-and-drop the firmware file into the form field or use the `Browse` or `Choose File` button). Click on **Update** button and the firmware file will be uploaded and the update process should commence. 

A white page should load momentarily with the message **Update Success! Rebooting...**. You should wait until the LED on the receiver starts to blink slowly (waiting some more will put the receiver into WiFi mode). Power cycle your FC and turn on your radio to verify you are bound and have connection.

## Flashing via Passthrough

Target: `HappyModel_EP_2400_RX_via_BetaflightPassthrough`

[Wire up your receiver](../../quick-start/rx-fcprep/#happymodel-ep1-ep2-pp) to a free uart in your Flight Controller. Wire TX on receiver to an RX pad on the FC, and the RX on receiver to a TX pad on the FC in the same UART. Wire 5v and Gnd as normal (5v to a 5v pad on FC and Gnd to a Gnd pad on the FC).

You will need to bridge the `Boot` pads on the receiver the first time you'll be updating via this method. The [wiring guide](../../quick-start/rx-fcprep/#happymodel-ep1-ep2-pp) shows where the `Boot` pads are. A solid LED indicates the receiver is in `Bootloader` mode when the TX module is OFF (Solid LED also indicates Radio+module & Receiver is bound and has connection). 

*Note: if you haven't bridged the `Boot` pads but the receiver has solid LED light, your FC is probably pulling the current UART's RX pad `LOW` which will interfere with the normal and passthrough flashing of this receiver. Find another UART and wire your receiver there instead*

Bridging the `Boot` pads is no longer needed past 1.0.0-RC6. 

Power your FC with a LiPo, or if receiver is powered via USB (receiver is connected to a 4v5 pad), connect the FC to your USB port. Using the ExpressLRS Configurator, with the correct Target selected and [Firmware Options](../../quick-start/firmware-options) set, click on **Build & Flash**. Wait for the process to finish and you should be greeted with the "Success" banner.

Unplug USB and LiPo, and removed the solder on the bridged `Boot` pads. You no longer need it (past 1.0.0-RC6). Power your TX Module and then your FC to verify you are bound and has connection.

## Flashing via FTDI

Target: `HappyModel_EP_2400_RX_via_UART`

Wire the receiver into the FTDI, with TX on receiver connected to the Rx on the FTDI, and RX on receiver connected to the Tx of the FTDI. Wire 5V and GND of the FTDI to 5V and GND of the Receiver. Short the boot pad while powering the RX on, and release - the LED should now be solid.

Select the target and set your [Firmware Options](../../quick-start/firmware-options) and once done, click on **Build and Flash**.