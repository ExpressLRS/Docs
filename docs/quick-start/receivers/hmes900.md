---
template: main.html
---

![Setup-Banner](https://raw.githubusercontent.com/ExpressLRS/ExpressLRS-hardware/master/img/quick-start.png)

## ES900RX

### Wiring up your receiver

!!! attention ""
    *Note: There are Flight Controllers that will pull the RX pads `LOW` which will put the ESP-based receivers into `Bootloader Mode` unintentionally. A solid LED light on these receivers even with the TX module off is a sign they are in Bootloader Mode. If this is the case, rewire the receiver to a different UART.*

<figure markdown>
![HM2400 connection](../../assets/images/es900rx-conn.png)
</figure>

The image above show the receiver pinouts and their connections. As we're dealing with UART connection, Rx on receiver goes to a TX pad on the FC, and Tx on the receiver goes to an uninverted Rx pad on the FC.

There are Flight Controllers that put their Receiver UART's RX pads Low, which in turn, puts the ESP-based (e.g. EP1 and EP2) receivers to Bootloader mode unintentionally. One remedy is to wire them into a different UART, or wire a pull-up resistor (300-1k ohm) between the Rx pad of the FC and a 3.3v or 5v pad, as shown below.

<figure markdown>
![pull up](../../assets/images/pull-up.png)
</figure>

Also of note is that the ESP-based receivers require their Boot pads (see figure above) be bridged on first time Passthrough Flash from their factory firmwares. After the first passthrough flashing, the bridge needs to be removed, and is no longer needed for subsequent passthrough flashing.

Flashing via Wifi doesn't need the Boot Pads bridged. Moreover, if it is bridged, the receiver will stay in bootloader mode and won't activate its WiFi Mode.

### Configuring your Flight Controller

See this [page](configuring-fc.md) on how your flight controller should be configured. These settings apply on both INAV and Betaflight (and other flight controller software).

Ports Tab should be setup so that Serial RX is on the UART where you have soldered the receiver.

Receiver protocol is `CRSF`, with `serialrx_inverted = off` and `serialrx_halfduplex = off`.

The next step will not be able to proceed properly and you'll have issues later if any of these are set differently. Once you have configured your Flight Controller software, close its Configurator and unplug-replug the USB cable from the FC or your computer. This will refresh the connection and you'll be ensured that the port is not busy (of high importance with the Passthrough Flashing Method).

### Flashing via Passthrough

Target: `HappyModel_RX_ES900RX_via_BetaflightPassthrough`

Device Category: `Happymodel 900 MHz`

Device: `HappyModel RX ES900RX`

![via Passthrough](../../assets/images/Method_RX_Passthrough.png)

Make sure you have your receiver [wired properly]. Rx pad on the Receiver wired up to a Tx pad on the FC, and the Tx pad on the Receiver wired up to an Rx pad on the FC. Also make sure you have setup your FC firmware to use CRSF Protocol, and that the UART is not inverted or running in half duplex.

For the following steps, you should be disconnected from Betaflight or INAV Configurator. Close the FC Configurator and unplug the FC from USB to refresh the connection.

You will need to bridge the `Boot` pads on the receiver the first time you'll be updating via this method. The [Wiring Guide] shows where the `Boot` pads are. A solid LED indicates the receiver is in `Bootloader` mode when the TX module is OFF (Solid LED also indicates Radio+module & Receiver is bound and has connection). 

!!! attention ""
    Note: if you powered the receiver and has solid LED light, your FC is probably pulling the current UART's RX pad `LOW` which will interfere with the normal and passthrough flashing of this receiver. Find another UART and wire your receiver there instead.

These procedures will not be needed in subsequent passthrough flashing. This is only needed on the first time you'd update the receiver from its factory firmware.

Select the corresponding target in the ExpressLRS Configurator, set your [Firmware Options] and then click **Build and Flash**. For first time flashing/updating, it would normally take a while.

![Build & Flash](../../assets/images/BuildFlash.png)

A `Success` message will be shown once the process is complete.

### Flashing via Wifi

Target: `HappyModel_RX_ES900RX_via_Wifi`

Device Category: `Happymodel 900 MHz`

Device: `HappyModel RX ES900RX`

![via WiFi](../../assets/images/Method_RX_WiFi.png)

#### Method 1

**(Recommended as first-flash method)**

With the receiver [wired properly] to your FC, select the right target and set your [Firmware Options] in the ExpressLRS Configurator.

**Build** the firmware. Once done, it should open a new window where the `HappyModel_RX_ES900RX-<version>.bin` is. Do not close this window so you can easily navigate to it once it's time to upload the firmware into the receiver.

![Build](../../assets/images/Build.png)

Power your Flight Controller by either connecting a LiPo or attaching the USB cable (if the receiver gets powered from USB via a 4v5 pad). The receiver's LED will blink slowly at first, and after 20s or 30s (can be adjusted via ExpressLRS Configurator using `AUTO_WIFI_ON_INTERVAL`), it should blink fast indicating it's on Wifi Hotspot Mode.

![LEDSEQ_WIFI_UPDATE](https://cdn.discordapp.com/attachments/738450139693449258/921065813983760384/LEDSEQ_WIFI_UPDATE_2_3.gif)

Connect to the Wifi Network the receiver has created. It should be named something like `ExpressLRS RX` with the same `expresslrs` password as the TX Module Hotspot.

<figure markdown>
![WiFi Hotspot](../../assets/images/WifiHotspot.png)
</figure>

Navigate to the same web address as the TX Module (usually http://10.0.0.1). The Firmware upload page should load, and using the File Upload Form, navigate where the correct Receiver `HappyModel_RX_ES900RX-<version>.bin` is (like with the Tx module, you can also drag-and-drop the firmware file into the form field or use the `Browse` or `Choose File` button). Click on the **Update** button and the firmware file will be uploaded and the update process should commence.

A white page should load momentarily with the message **Update Success! Rebooting...**. Wait a little bit (**you can wait until the LED on the Receiver starts to blink slowly again**) and the receiver should be updated. Power cycle the receiver and it should be able to bind with your TX module now (given you have updated the Tx Module as well, and that they have the same binding phrase and options).

**Update for version 2.0**

Once you have updated to firmware version 2.0 or newer, the Web Update page on the Hotspot will get a few updates of its own. It will get the Update progress bar, and a Popup will be shown for Success or Error messages. Additionally, you can configure Home Network SSID and Password if you chose not to use ExpressLRS Configurator to set them. Once these are set, you can use the two methods below.

![JoinNetwork](../../assets/images/web-joinnetwork.png)

#### Method 2

!!! note ""
    Note: This method will only work once the Home Network SSID and Password has been configured with the receiver

With the receiver [wired properly] to your FC, select the right target and set your [Firmware Options] in the ExpressLRS Configurator.

**Build** the firmware. Once done, it should open a new window where the `HappyModel_RX_ES900RX-<version>.bin` is. Do not close this window so you can easily navigate to it once it's time to upload the firmware into the receiver.

![Build](../../assets/images/Build.png)

Power up your Flight Controller by either connecting a LiPo or attaching the USB cable (if the receiver gets powered from USB via a 4v5 pad). The receiver's LED will blink slowly at first, and after 20s or 30s (can be adjusted via ExpressLRS Configurator using `AUTO_WIFI_ON_INTERVAL`), it should blink fast indicating it's on Wifi AP Mode. The fast blink will pause and flash fast once again, indicating connection to your Home Network.

![LEDSEQ_WIFI_UPDATE](https://cdn.discordapp.com/attachments/738450139693449258/921065813983760384/LEDSEQ_WIFI_UPDATE_2_3.gif)

Using your browser, navigate to http://elrs_rx.local/. The Wifi Update page should load. It should show your device target along with the version of the firmware it currently has.

Scroll down to the Firmware Update section, shown below:

![Firmware Update](../../assets/images/web-firmwareupdate.png)

Drag-and-drop the `HappyModel_RX_ES900RX-<version>.bin` file created by the ExpressLRS Configurator into the Choose File field, or manually navigate to the Folder by clicking the `Choose File` button. Once the correct file is selected, click the `Update`. Wait for the process to complete, indicated by a Green popup screen. 

Wait a little bit (**you can wait until the LED on the Receiver starts to blink slowly again**) and the receiver should be updated.

You can now power down your Flight Controller along with the receiver.

#### Method 3

!!! note ""
    Note: This method will only work once the Home Network SSID and Password has been configured with the receiver

With the receiver [wired properly] to your FC, select the right target and set your [Firmware Options] in the ExpressLRS Configurator.

Power up your Flight Controller by either connecting a LiPo or attaching the USB cable (if the receiver gets powered from USB via a 4v5 pad). The receiver's LED will blink slowly at first, and after 20s or 30s (can be adjusted via ExpressLRS Configurator using `AUTO_WIFI_ON_INTERVAL`), it should blink fast indicating it's on Wifi Mode.

![LEDSEQ_WIFI_UPDATE](https://cdn.discordapp.com/attachments/738450139693449258/921065813983760384/LEDSEQ_WIFI_UPDATE_2_3.gif)

**Build & Flash** the firmware using the ExpressLRS Configurator. Wait for the process to complete, indicated by the "Success" prompt and the Receiver LED has gone back to the Slow Blink mode. You can now power down the Flight Controller.

![Build & Flash](../../assets/images/BuildFlash.png)

![RXUpload Log](../../assets/images/RXWifiUpdateLog.png)

## ES915/868RX (Discontinued)

### Flashing via Passthrough

Target: `HappyModel_RX_ES915RX_via_BetaflightPassthrough`

Device Category: `Happymodel 900 MHz`

Device: `HappyModel RX ES915RX`

![stm Passthrough](../../assets/images/Method_RX_Passthrough-stm.png)

<figure markdown>
![ES915RX](../../assets/images/ES915rx.jpg)
</figure>

Once wired properly to your FC as shown above, connect your FC to USB. Did your receiver powered up too (with both LEDs lit)? If so, disconnect USB, hold the bind button on your receiver, and reconnect to USB. The LED should start alternating between the Green and Red LEDs. Once it's alternating, you can then let go of the Bind Button.

If your receiver didn't get powered from USB, have a lipo ready and continue with the next steps. On the ExpressLRS Configurator, with your [Firmware Options] set, click on **Build & Flash**. Like on the TX module, it will take a while on the first time. Watch out for the `Passthrough Init` stage. This stage will check your FC Configuration for the Serial RX UART (Software Inversion via "set serialrx_inverted" and Half Duplex mode via "set serialrx_halfduplex" will be checked; both should be off.)

![Build & Flash](../../assets/images/BuildFlash.png)

Once `Retry... ` lines appear, connect a LiPo if your receiver isn't powered by the USB (i.e. power up your receiver and FC). On subsequent flash, you can have the LiPo plugged in and receiver powered up from the start.

Wait for this process to finish. It's done once the "Success" prompt is shown.

### Flashing via STLink

Target: `HappyModel_RX_ES915RX_via_STLINK`

Device Category: `Happymodel 900 MHz`

Device: `HappyModel RX ES915RX`

![via STLink](../../assets/images/Method_RX_STLink-stm.png)

<figure markdown>
![ES915RX](../../assets/images/ES915rx.jpg)
</figure>

Connect your STLink into `GND`, `DIO`, `CLK`, `3V3` of the receiver. These pads are marked clearly in the top left of the image above.

Using the correct target specific for your receiver, set your [Firmware Options] and hit **Build & Flash** on the ExpressLRS Configurator.

![Build & Flash](../../assets/images/BuildFlash.png)

Once done, wire your receiver to your Flight Controller. Passthrough flashing can now be used for updating the receiver.

[Firmware Options]: ../firmware-options.md
[wired properly]: #wiring-up-your-receiver
[Wiring Guide]: #wiring-up-your-receiver
