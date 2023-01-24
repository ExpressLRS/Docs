---
template: main.html
---

![Setup-Banner](https://raw.githubusercontent.com/ExpressLRS/ExpressLRS-hardware/master/img/quick-start.png)

## Wiring up your receiver

!!! attention "Note"
    There are Flight Controllers that will pull the RX pads `LOW` which will put the ESP-based receivers into `Bootloader Mode` unintentionally. As this receiver uses an RGB LED as indicator, it will appear as if the receiver is OFF when in Bootloader mode. The firmware that drives the RGB LED is inactive when the ESP Chip is in Bootloader mode, thus the RGB LED will not function when in this state.

<figure markdown>
![betafpv SuperD](../../assets/images/BetaFPVSuperD.png)
<figcaption>BetaFPV SuperD Diversity Receiver, ESP-based</figcaption>
</figure>

The image above show the receiver pinout and its connections. As we're dealing with UART connection here, Rx on receiver goes to a TX pad on the FC, and Tx on the receiver goes to an uninverted Rx pad on the FC.

There are Flight Controllers that put their Receiver UART's RX pads Low, which in turn, puts the ESP-based (e.g. the SuperD) receivers into Bootloader mode unintentionally. One remedy is to wire them into a different UART, or wire a pull-up resistor (300-1k ohm) between the Rx pad of the FC and a 3.3v or 5v pad, as shown below.

<figure markdown>
![pull up](../../assets/images/pull-up.png)
<figcaption>Wiring up receiver</figcaption>
</figure>

## Configuring your Flight Controller

To configure your flight controller properly, please go through [Configure FC page](configuring-fc.md). These settings apply on INAV, Betaflight and other flight controller software.

Ports Tab should be setup so that Serial RX is on the UART where you have connected the receiver.

Receiver protocol is `CRSF` with `serialrx_inverted = off` and `serialrx_halfduplex = off`.

The next steps will not be able to proceed properly and you'll have issues later if any of these are set differently. Once you have configured your Flight Controller software, close its Configurator and unplug-replug the USB cable from the FC or your computer. This will refresh the connection and you'll be ensured that the port is not busy (of high importance with the Passthrough Flashing Method).

## Flashing via WiFi

- Target: `BETAFPV_SuperD_2400_RX_via_WIFI`

- Device Category: `BETAFPV 2.4 GHz`

- Device: `BETAFPV SuperD 2.4GHz RX`

<figure markdown>
![via WiFi](../../assets/images/Method_RX_WiFi.png)
<figcaption>Flashing via WiFi</figcaption>
</figure>

### Method 1

With the receiver [wired properly] to your FC, select the correct target and set the [Firmware Options] in the ExpressLRS Configurator.

**Build** the firmware. Once done, it should open a new window where the `BETAFPV_SuperD_2400_RX-<version>.bin` is. Do not close this window so you can easily navigate to it once it's time to upload the firmware into the receiver.

<figure markdown>
![Build]
</figure>

Power your Flight Controller by either connecting a LiPo or attaching the USB cable (if the receiver gets powered from USB via a 4v5 pad). The RGB LED on the receiver will light up and show the RGB wave pattern. Then it will blink slow in Orange. Wait for about 60s(can be adjusted via ExpressLRS Configurator using `AUTO_WIFI_ON_INTERVAL` option) and the receiver LED should turn green and display a slow breathing pattern. It's now on Wifi Hotspot Mode.

Connect to the Wifi Network the receiver has created. It should be named something like `ExpressLRS RX` with the same `expresslrs` password as the TX Module Hotspot.

<figure markdown>
![WiFi Hotspot](../../assets/images/WifiHotspot.png)
</figure>

Navigate to the same web address as the TX Module (usually http://10.0.0.1). The ExpressLRS WebUI should load. Activate the Update Tab where the File Upload form is, then navigate to the folder where the `BETAFPV_SuperD_2400_RX-<version>.bin` is (like with the Tx module, you can also drag-and-drop the firmware file into the form field or use the `Browse` or `Choose File` button). Click on the **Update** button and the firmware file will be uploaded and the update process should commence.

A popup will be shown indicating the update has succeeded. Wait for a little bit until the RGB wave pattern on the receiver LED is shown indicating it has rebooted and is working normally. You should be able to get it talking with your TX module now(given you have updated the Tx Module as well, and that they have the same binding phrase and options).

### Method 2

!!! note "Note"
    This method will only work once the Home Network SSID and Password has been configured with the receiver.

With the receiver [wired properly] to your FC, select the right target and set your [Firmware Options] in the ExpressLRS Configurator.

**Build** the firmware. Once done, it should open a new window where the `BETAFPV_SuperD_2400_RX-<version>.bin` is. Do not close this window so you can easily navigate to it once it's time to upload the firmware into the receiver.

<figure markdown>
![Build]
</figure>

Power up your Flight Controller by either connecting a LiPo or attaching the USB cable (if the receiver gets powered from USB via a 4v5 pad). The RGB LED on the receiver will light up and show the RGB wave pattern. Then it will blink slow in Orange. Wait for about 60s(can be adjusted via ExpressLRS Configurator using `AUTO_WIFI_ON_INTERVAL`) and the receiver LED should turn green and display a slow breathing pattern. It's now on Wifi Hotspot Mode.

Using your browser, navigate to http://elrs_rx.local/. The ExpressLRS WebUI should load. It should show your device target along with the version of the firmware it currently has.

Activate the Update Tab where the File Upload form is. Drag-and-drop the `BETAFPV_SuperD_2400_RX-<version>.bin` file created by the ExpressLRS Configurator into the Choose File field, or manually navigate to the Folder by clicking the `Choose File` button. Once the correct file is selected, click the `Update` button. Wait for the process to complete, indicated by a Green popup screen. 

Wait for a little bit until the RGB wave pattern on the receiver LED is shown indicating it has rebooted and is working normally. 

You can now power down your Flight Controller along with the receiver.

### Method 3

!!! note "Note"
    This method will only work once the Home Network SSID and Password has been configured with the receiver.

With the receiver [wired properly] to your FC, select the right target and set your [Firmware Options] in the ExpressLRS Configurator.

Power up your Flight Controller by either connecting a LiPo or attaching the USB cable (if the receiver gets powered from USB via a 4v5 pad). The RGB LED on the receiver will light up and show the RGB wave pattern. Then it will blink slow in Orange. Wait for about 60s(can be adjusted via ExpressLRS Configurator using `AUTO_WIFI_ON_INTERVAL`) and the receiver LED should turn green and display a slow breathing pattern. It's now on Wifi Hotspot Mode.

**Build & Flash** the firmware using the ExpressLRS Configurator. Wait for the process to complete, indicated by the "Success" prompt and the Receiver LED has gone back RGB wave lighting patern. You can now power down the flight controller.

<figure markdown>
![Build & Flash]
</figure>

<figure markdown>
![RXUpload Log](../../assets/images/RXWifiUpdateLog.png)
</figure>

## Flashing via Passthrough

- Target: `BETAFPV_SuperD_2400_RX_via_BetaflightPassthrough`

- Device Category: `BETAFPV 2.4 GHz`

- Device: `BETAFPV SuperD 2.4GHz RX`

<figure markdown>
![via Passthrough](../../assets/images/Method_RX_Passthrough.png)
<figcaption>Flashing via Passthrough</figcaption>
</figure>

Make sure you have your receiver [wired properly]. Rx pad on the Receiver wired up to a Tx pad on the FC, and the Tx pad on the Receiver wired up to an Rx pad on the FC. Also make sure you have setup your FC firmware to use CRSF Protocol, and that the UART is not inverted or running in half duplex.

For the following steps, you should be disconnected from Betaflight or INAV Configurator. Close the FC Configurator and unplug the FC from USB to refresh the connection.

Connect a usb data cable into your Fc and power up your receiver. If your receiver powers up with just the USB cable plugged in, then no need to connect a LiPo. If your receiver only powers up with a LiPo connected, then connect a LiPo. If you have a VTX that heats up while just sitting on the bench, either unplug it temporarily or provide some airflow into it.

Observe the RGB LED on the receiver. The RGB LED on the receiver will light up and show the RGB wave pattern. Then it will blink slow in Orange.

!!! attention "Note"
    If you powered the receiver and no LED lights up, despite not pressing the boot button during power up, it's highly possible the receiver has been put to bootloader mode by the flight controller. Test by disconnecting the RX and Tx wires of the receiver from the FC then power up. If the RGB LED shows the RGB wave pattern on power up, then the UART has put it into bootloader mode. If the LED still didn't light up, it's possible you have a soft-bricked receiver. You'll have to do the [unbricking procedure].

Select the corresponding target in the ExpressLRS Configurator, set your [Firmware Options] and then click **Build and Flash**. For first time flashing/updating, it would normally take a while.

<figure markdown>
![Build & Flash]
</figure>

A `Success` message will be shown once the process is complete.

## Flashing via FTDI

- Target: `BETAFPV_SuperD_2400_RX_via_UART`

- Device Category: `BETAFPV 2.4 GHz`

- Device: `BETAFPV SuperD 2.4GHz RX`

<figure markdown>
![via UART](../../assets/images/Method_RX_UART.png)
<figcaption>Flashing via UART</figcaption>
</figure>

Wire the receiver into the FTDI/UART Adapter, with TX on receiver connected to the Rx on the adapter, and RX on receiver connected to the Tx of the adapter. Wire 5V and GND of the adapter to 5V and GND of the Receiver. Press the button while powering the Receiver on, and release the button after a few seconds. The RGB LED on the Receiver will not light up.

<figure markdown>
![FTDI Wiring](../../assets/images/FTDIConn.png)
</figure>

Select the target and set your [Firmware Options] and once done, click on **Build and Flash**.

<figure markdown>
![Build & Flash]
</figure>

After the Success message shows, the RGB LED on the receiver will light up and show the RGB wave pattern. Then it will blink slow in Orange. Receiver is now flashed and waiting for the TX Sync.

[Build]: ../../assets/images/Build.png
[Build & Flash]: ../../assets/images/BuildFlash.png
[Firmware Options]: ../firmware-options.md
[wired properly]: #wiring-up-your-receiver
[unbricking procedure]: ../unbricking.md