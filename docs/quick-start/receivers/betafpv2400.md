---
template: main.html
---

![Setup-Banner](https://raw.githubusercontent.com/ExpressLRS/ExpressLRS-hardware/master/img/quick-start.png)

!!! danger "Advisory"
    If this is the first time you're flashing/updating your receiver or you're updating it from a previous 2.x firmware via WiFi, first ensure that it has version 2.5.2. Once it has the 2.5.2 flashed, update to 3.x.

    If you've flashed it straight to 3.x and you're getting "Not Enough Space" popup during WiFi flashing, flash the receiver to 2.5.2 first, and then flash it to 3.x.

    You can update straight to 3.x via Passthrough or via UART.

    The Repartitioner is for **TX only**.

## Wiring up your receiver

!!! attention "Note"
    There are Flight Controllers that will pull the RX pads `LOW` which will put the ESP-based receivers into `Bootloader Mode` unintentionally. A solid LED light on these receivers even with the TX module off is a sign they are in Bootloader Mode. If this is the case, rewire the receiver to a different UART.

<figure markdown>
![BetaFPV RX connection](../../assets/images/betaFPVrx2400.png)
<figcaption>BetaFPV Nano</figcaption>
</figure>

<figure markdown>
![BetaFPV RX Lite connection](../../assets/images/betaFPVrxLite.png)
<figcaption>BetaFPV Lite (Flat & Tower)</figcaption>
</figure>

The images above show the receiver pinouts and their connections. As we're dealing with UART connection, Rx on receiver goes to a TX pad on the FC, and Tx on the receiver goes to an uninverted Rx pad on the FC.

There are Flight Controllers that put their Receiver UART's RX pads Low, which in turn, puts the ESP-based (e.g. EP1 and EP2) receivers to Bootloader mode unintentionally. One remedy is to wire them into a different UART, or wire a pull-up resistor (300-1k ohm) between the Rx pad of the FC and a 3.3v or 5v pad, as shown below.

<figure markdown>
![pull up](../../assets/images/pull-up.png)
<figcaption>Wiring up receiver</figcaption>
</figure>

## Configuring your Flight Controller

To configure your flight controller properly, please go through [Configure FC page](configuring-fc.md). These settings apply on INAV, Betaflight and other flight controller software.

Ports Tab should be setup so that Serial RX is on the UART where you have soldered the receiver.

Receiver protocol is `CRSF` with `serialrx_inverted = off` and `serialrx_halfduplex = off`.

The next step will not be able to proceed properly and you'll have issues later if any of these are set differently. Once you have configured your Flight Controller software, close its Configurator and unplug-replug the USB cable from the FC or your computer. This will refresh the connection and you'll be ensured that the port is not busy (of high importance with the Passthrough Flashing Method).

## Flashing via WiFi

- Target: `BETAFPV_Nano_2400_RX_via_WIFI`

- Device Category: `BETAFPV 2.4 GHz`

- Device: `BETAFPV Nano 2400 RX`, `BETAFPV Lite 2400 RX` (Tower & Flattie)

<figure markdown>
![via WiFi](../../assets/images/Method_RX_WiFi.png)
<figcaption>Flashing via WiFi</figcaption>
</figure>

### Method 1

With the receiver [wired properly] to your FC, select the correct target and set the [Firmware Options] in the ExpressLRS Configurator.

**Build** the firmware. Once done, it should open a new window where the `BETAFPV_Nano_2400_RX-<version>.bin` is. Do not close this window so you can easily navigate to it once it's time to upload the firmware into the receiver.

<figure markdown>
![Build]
</figure>

Power your Flight Controller by either connecting a LiPo or attaching the USB cable (if the receiver gets powered from USB via a 4v5 pad). The receiver's LED will blink slowly at first, and after 20s or 30s (can be adjusted via ExpressLRS Configurator using `AUTO_WIFI_ON_INTERVAL`), it should blink fast indicating it's on Wifi Hotspot Mode.

<figure markdown>
![LEDSEQ_WIFI_UPDATE](https://cdn.discordapp.com/attachments/738450139693449258/921065813983760384/LEDSEQ_WIFI_UPDATE_2_3.gif)
</figure>

Connect to the Wifi Network the receiver has created. It should be named something like `ExpressLRS RX` with the same `expresslrs` password as the TX Module Hotspot.

<figure markdown>
![WiFi Hotspot](../../assets/images/WifiHotspot.png)
</figure>

Navigate to the same web address as the TX Module (usually http://10.0.0.1). The Firmware upload page should load, and using the File Upload Form, navigate where the correct Receiver `BETAFPV_Nano_2400_RX-<version>.bin` is (like with the Tx module, you can also drag-and-drop the firmware file into the form field or use the `Browse` or `Choose File` button). Click on the **Update** button and the firmware file will be uploaded and the update process should commence.

A white page should load momentarily with the message **Update Success! Rebooting...**. Wait a little bit (**you can wait until the LED on the Receiver starts to blink slowly again**) and the receiver should be updated. Power cycle the receiver and it should be able to bind with your TX module now (given you have updated the Tx Module as well, and that they have the same binding phrase and options).

!!! Info "Update for version 2.0"
    Once you have updated to firmware version 2.0 or newer, the Web Update page on the Hotspot will get a few updates of its own. It will get the Update progress bar, and a Popup will be shown for Success or Error messages. Additionally, you can configure Home Network SSID and Password if you chose not to use ExpressLRS Configurator to set them. Once these are set, you can use the two methods below.

<figure markdown>
![JoinNetwork](../../assets/images/web-joinnetwork.png)
</figure>

### Method 2

!!! note "Note"
    This method will only work once the Home Network SSID and Password has been configured with the receiver.

With the receiver [wired properly] to your FC, select the right target and set your [Firmware Options] in the ExpressLRS Configurator.

**Build** the firmware. Once done, it should open a new window where the `BETAFPV_Nano_2400_RX-<version>.bin` is. Do not close this window so you can easily navigate to it once it's time to upload the firmware into the receiver.

<figure markdown>
![Build]
</figure>

Power up your Flight Controller by either connecting a LiPo or attaching the USB cable (if the receiver gets powered from USB via a 4v5 pad). The receiver's LED will blink slowly at first, and after 20s or 30s (can be adjusted via ExpressLRS Configurator using `AUTO_WIFI_ON_INTERVAL`), it should blink fast indicating it's on Wifi AP Mode. The fast blink will pause and flash fast once again, indicating connection to your Home Network.

<figure markdown>
![LEDSEQ_WIFI_UPDATE](https://cdn.discordapp.com/attachments/738450139693449258/921065813983760384/LEDSEQ_WIFI_UPDATE_2_3.gif)
</figure>

Using your browser, navigate to http://elrs_rx.local/. The Wifi Update page should load. It should show your device target along with the version of the firmware it currently has.

Scroll down to the Firmware Update section, shown below:

<figure markdown>
![Firmware Update](../../assets/images/web-firmwareupdate.png)
</figure>

Drag-and-drop the `BETAFPV_Nano_2400_RX-<version>.bin` file created by the ExpressLRS Configurator into the Choose File field, or manually navigate to the Folder by clicking the `Choose File` button. Once the correct file is selected, click the `Update`. Wait for the process to complete, indicated by a Green popup screen. 

Wait a little bit (**you can wait until the LED on the Receiver starts to blink slowly again**) and the receiver should be updated.

You can now power down your Flight Controller along with the receiver.

### Method 3

!!! note "Note"
    This method will only work once the Home Network SSID and Password has been configured with the receiver.

With the receiver [wired properly] to your FC, select the right target and set your [Firmware Options] in the ExpressLRS Configurator.

Power up your Flight Controller by either connecting a LiPo or attaching the USB cable (if the receiver gets powered from USB via a 4v5 pad). The receiver's LED will blink slowly at first, and after 20s or 30s (can be adjusted via ExpressLRS Configurator using `AUTO_WIFI_ON_INTERVAL`), it should blink fast indicating it's on Wifi Mode.

<figure markdown>
![LEDSEQ_WIFI_UPDATE](https://cdn.discordapp.com/attachments/738450139693449258/921065813983760384/LEDSEQ_WIFI_UPDATE_2_3.gif)
</figure>

**Build & Flash** the firmware using the ExpressLRS Configurator. Wait for the process to complete, indicated by the "Success" prompt and the Receiver LED has gone back to the Slow Blink mode. You can now power down the Flight Controller.

<figure markdown>
![Build & Flash]
</figure>

<figure markdown>
![RXUpload Log](../../assets/images/RXWifiUpdateLog.png)
</figure>

## Flashing via Passthrough

- Target: `BETAFPV_Nano_2400_RX_via_BetaflightPassthrough`

- Device Category: `BETAFPV 2.4 GHz`

- Device: `BETAFPV Nano 2400 RX`, `BETAFPV Lite 2400 RX` (Tower & Flattie)

<figure markdown>
![via Passthrough](../../assets/images/Method_RX_Passthrough.png)
<figcaption>Flashing via Passthrough</figcaption>
</figure>

Make sure you have your receiver [wired properly]. Rx pad on the Receiver wired up to a Tx pad on the FC, and the Tx pad on the Receiver wired up to an Rx pad on the FC. Also make sure you have setup your FC firmware to use CRSF Protocol, and that the UART is not inverted or running in half duplex.

For the following steps, you should be disconnected from Betaflight or INAV Configurator. Close the FC Configurator and unplug the FC from USB to refresh the connection.

If the receiver gets powered up when you connect the FC to USB, you will need to Press and Hold the button on the receiver, connect USB and let go of the button once the LED stopped blinking and goes SOLID.

If the receiver needs a LiPo attached to get powered up, then Press and Hold the button on the receiver, attach a LiPo, then let go once the LED in the receiver stopped blinking and goes SOLID. Then connect your FC to USB.

!!! attention "Note"
    If you powered the receiver and has solid LED light, your FC is probably pulling the current UART's RX pad `LOW` which will interfere with the normal and passthrough flashing of this receiver. Find another UART and wire your receiver there instead.

These procedures will not be needed in subsequent passthrough flashing. This is only needed on the first time you'd update the receiver from its factory firmware.

Select the corresponding target in the ExpressLRS Configurator, set your [Firmware Options] and then click **Build and Flash**. For first time flashing/updating, it would normally take a while.

<figure markdown>
![Build & Flash]
</figure>

A `Success` message will be shown once the process is complete.

## Flashing via FTDI

- Target: `BETAFPV_Nano_2400_RX_via_UART`

- Device Category: `BETAFPV 2.4 GHz`

- Device: `BETAFPV Nano 2400 RX`, `BETAFPV Lite 2400 RX` (Tower & Flattie)

<figure markdown>
![via UART](../../assets/images/Method_RX_UART.png)
<figcaption>Flashing via UART</figcaption>
</figure>

Wire the receiver into the FTDI, with TX on receiver connected to the Rx on the FTDI, and RX on receiver connected to the Tx of the FTDI. Wire 5V and GND of the FTDI to 5V and GND of the Receiver. Press the button while powering the RX on, and release - the LED should now be solid.

<figure markdown>
![FTDI Wiring](../../assets/images/FTDIConn.png)
</figure>

Select the target and set your [Firmware Options] and once done, click on **Build and Flash**.

<figure markdown>
![Build & Flash]
</figure>

[Build]: ../../assets/images/Build.png
[Build & Flash]: ../../assets/images/BuildFlash.png
[Firmware Options]: ../firmware-options.md
[wired properly]: #wiring-up-your-receiver