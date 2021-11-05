---
template: main.html
---

![Setup-Banner](https://raw.githubusercontent.com/ExpressLRS/ExpressLRS-hardware/master/img/quick-start.png)

## Flashing via Wifi 

Target: `HappyModel_EP_2400_RX_via_WIFI`

### Method 1

**(Recommended as first-flash method)**

[Wire up your receiver](../../quick-start/rx-fcprep/#happymodel-ep1-ep2-pp) to a free UART on your Flight Controller. Wire TX on receiver to an RX pad on the FC, and the RX on receiver to a TX pad on the FC in the same UART. Wire 5v and Gnd as normal (5v to a 5v pad on FC and Gnd to a Gnd pad on the FC).

!!! attention ""
    *Note: There are Flight Controllers that will pull the RX pads `LOW` which will put the ESP-based receivers into `Bootloader Mode` unintentionally. A solid LED light on these receivers even with the TX module off is a sign they are in Bootloader Mode. If this is the case, rewire the receiver to a different UART.*

**Build** the firmware using the ExpressLRS Configurator using the correct Target and [options](../../quick-start/firmware-options). Once done, it should open a new window where the `HappyModel_EP_2400_RX-<version>.bin` is. Do not close this window so you can easily navigate to it once it's time to upload the firmware into the receiver.

Power your Flight Controller by either connecting a LiPo or attaching the USB cable (if receiver gets powered from USB via a 4v5 pad). Receiver's LED will blink slow at first, and after 20s or 30s (can be adjusted via ExpressLRS Configurator using `AUTO_WIFI_ON_INTERVAL`), it should blink fast indicating it's on Wifi Hotspot Mode.

Connect to the Wifi Network the receiver has created. It should be named something like `ExpressLRS RX` with the same `expresslrs` password as the TX Module Hotspot. Navigate to the same web address as the TX Module (usually http://10.0.0.1). The Firmware upload page should load, and using the File Upload Form, navigate where the correct Receiver `HappyModel_EP_2400_RX-<version>.bin` is (like with the Tx module, you can also drag-and-drop the firmware file into the form field or use the `Browse` or `Choose File` button). Click on **Update** button and the firmware file will be uploaded and the update process should commence. 

A white page should load momentarily with the message **Update Success! Rebooting...**. Wait a little bit (**you can wait until the LED on the Receiver starts to blink slowly again**) and the receiver should be updated. Power cycle and your module and receiver should now be bound (given you have updated the Tx Module as well, and that they have the same binding phrase and options).

**Update for version 2.0**

Once you have updated to firmware version 2.0 or newer, the Web Update page on the Hotspot will get a few updates of its own. It will get the Update progress bar, and a Popup will be shown for Success or Error messages. Additionally, you can configure Home Network SSID and Password if you chose not to use ExpressLRS Configurator to set them. Once these are set, you can use the two methods below.

![JoinNetwork](../assets/images/web-joinnetwork.png)

### Method 2

!!! note ""
    Note: This method will only work once the Home Network SSID and Password has been configured with the receiver

With the receiver [wired properly](../../quick-start/rx-fcprep/#namimnorc-voyager-flash) to your FC, select the right target and set your [Firmware Options](../../quick-start/firmware-options) in the ExpressLRS Configurator.

**Build** the firmware. Once done, it should open a new window where the `HappyModel_EP_2400_RX-<version>.bin` is. Do not close this window so you can easily navigate to it once it's time to upload the firmware into the receiver.

Power up your Flight Controller by either connecting a LiPo or attaching the USB cable (if the receiver gets powered from USB via a 4v5 pad). The receiver's LED will blink slowly at first, and after 20s or 30s (can be adjusted via ExpressLRS Configurator using `AUTO_WIFI_ON_INTERVAL`), it should blink fast indicating it's on Wifi AP Mode. The fast blink will pause and flash fast once again, indicating connection to your Home Network.

Using your browser, navigate to http://elrs_rx.local/. The Wifi Update page should load. It should show your device target along with the version of the firmware it currently has.

Scroll down to the Firmware Update section, shown below:

![Firmware Update](../assets/images/web-firmwareupdate.png)

Drag-and-drop the `HappyModel_EP_2400_RX-<version>.bin` file created by the ExpressLRS Configurator into the Choose File field, or manually navigate to the Folder by clicking the `Choose File` button. Once the correct file is selected, click the `Update`. Wait for the process to complete, indicated by a Green popup screen. 

Wait a little bit (**you can wait until the LED on the Receiver starts to blink slowly again**) and the receiver should be updated.

You can now power down your Flight Controller along with the receiver.

### Method 3

!!! note ""
    Note: This method will only work once the Home Network SSID and Password has been configured with the receiver

With the receiver [wired properly](../../quick-start/rx-fcprep/#namimnorc-voyager-flash) to your FC, select the right target and set your [Firmware Options](../../quick-start/firmware-options) in the ExpressLRS Configurator.

Power up your Flight Controller by either connecting a LiPo or attaching the USB cable (if the receiver gets powered from USB via a 4v5 pad). The receiver's LED will blink slowly at first, and after 20s or 30s (can be adjusted via ExpressLRS Configurator using `AUTO_WIFI_ON_INTERVAL`), it should blink fast indicating it's on Wifi Mode.

**Build & Flash** the firmware using the ExpressLRS Configurator. Wait for the process to complete, indicated by the "Success" prompt and the Receiver LED has gone back to the Slow Blink mode. You can now power down the Flight Controller.

![RXUpload Log](../assets/images/RXWifiUpdateLog.png)

## Flashing via Passthrough

Target: `HappyModel_EP_2400_RX_via_BetaflightPassthrough`

[Wire up your receiver](../../quick-start/rx-fcprep/#happymodel-ep1-ep2-pp) to a free uart in your Flight Controller. Wire TX on receiver to an RX pad on the FC, and the RX on receiver to a TX pad on the FC in the same UART. Wire 5v and Gnd as normal (5v to a 5v pad on FC and Gnd to a Gnd pad on the FC).

You will need to bridge the `Boot` pads on the receiver the first time you'll be updating via this method. The [wiring guide](../../quick-start/rx-fcprep/#happymodel-ep1-ep2-pp) shows where the `Boot` pads are. A solid LED indicates the receiver is in `Bootloader` mode when the TX module is OFF (Solid LED also indicates Radio+module & Receiver is bound and has connection). 

!!! attention ""
    Note: if you haven't bridged the `Boot` pads but the receiver has solid LED light, your FC is probably pulling the current UART's RX pad `LOW` which will interfere with the normal and passthrough flashing of this receiver. Find another UART and wire your receiver there instead.

Bridging the `Boot` pads is no longer needed past 1.0.0-RC6. 

Power your FC with a LiPo, or if receiver is powered via USB (receiver is connected to a 4v5 pad), connect the FC to your USB port. Using the ExpressLRS Configurator, with the correct Target selected and [Firmware Options](../../quick-start/firmware-options) set, click on **Build & Flash**. Wait for the process to finish and you should be greeted with the "Success" banner.

Unplug USB and LiPo, and removed the solder on the bridged `Boot` pads. You no longer need it (past 1.0.0-RC6). Power your TX Module and then your FC to verify you are bound and has connection.

## Flashing via FTDI

Target: `HappyModel_EP_2400_RX_via_UART`

Wire the receiver into the FTDI, with TX on receiver connected to the Rx on the FTDI, and RX on receiver connected to the Tx of the FTDI. Wire 5V and GND of the FTDI to 5V and GND of the Receiver. Short the boot pad while powering the RX on, and release - the LED should now be solid.

Select the target and set your [Firmware Options](../../quick-start/firmware-options) and once done, click on **Build and Flash**.