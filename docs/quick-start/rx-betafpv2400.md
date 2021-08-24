---
template: main.html
---

![Setup-Banner](https://raw.githubusercontent.com/ExpressLRS/ExpressLRS-hardware/master/img/quick-start.png)

## Flashing via Passthrough

Target: `BETAFPV_2400_RX_via_BetaflightPassthrough`

Make sure you have [wired](../../quick-start/rx-fcprep/#betafpv-receivers) your receiver properly. Rx pad on the Receiver wired up to a Tx pad on the FC, and the Tx pad on the Receiver wired up to an Rx pad on the FC. Also make sure you have setup your FC firmware to use CRSF Protocol, and that the UART is not inverted or running in half duplex.

If the receiver gets powered up when you connect the FC to USB, you will need to Press and Hold the button on the receiver, connect USB and let go of the button once the LED stopped blinking and goes SOLID.

If the receiver needs a LiPo attached to get powered up, then Press and Hold the button on the receiver, attach a LiPo, then let go once the LED in the receiver stopped blinking and goes SOLID. Then connect your FC to USB.

These procedures will not be needed in subsequent passthrough flashing. This is only needed on the first time you'd update the receiver from its factory firmware.

Select the corresponding target in the ExpressLRS Configurator, set your [Firmware Options](../../quick-start/firmware-options) and then click **Build and Flash**. For first time flashing/updating, it would normally take a while.

A `Success` message will be shown once the process is complete.

## Flashing via WiFi

Target: `BETAFPV_2400_RX_via_WIFI`

With the receiver [wired](../../quick-start/rx-fcprep/#betafpv-receivers) properly to your FC, select the correct target and set the [Firmware Options](../../quick-start/firmware-options) in the ExpressLRS Configurator.

**Build** the firmware. Once done, it should open a new window where the `BETAFPV_2400_RX-<version>.bin` is. Do not close this window so you can easily navigate to it once it's time to upload the firmware into the receiver.

Power your Flight Controller by either connecting a LiPo or attaching the USB cable (if the receiver gets powered from USB via a 4v5 pad). The receiver's LED will blink slowly at first, and after 20s or 30s (can be adjusted via ExpressLRS Configurator using `AUTO_WIFI_ON_INTERVAL`), it should blink fast indicating it's on Wifi Hotspot Mode.

Connect to the Wifi Network the receiver has created. It should be named something like `ExpressLRS RX` with the same *expresslrs* password as the TX Module Hotspot. Navigate to the same web address as the TX Module (usually http://10.0.0.1). The Firmware upload page should load, and using the File Upload Form, navigate where the correct Receiver `BETAFPV_2400_RX-<version>.bin` is (like with the Tx module, you can also drag-and-drop the firmware file into the form field or use the `Browse` or `Choose File` button). Click on the **Update** button and the firmware file will be uploaded and the update process should commence.

A white page should load momentarily with the message **Update Success! Rebooting...** Wait a little bit (you can wait until the LED on the Receiver starts to blink slowly again) and the receiver should be updated. Power cycle and your module and receiver should now be bound (given you have updated the Tx Module as well, and that they have the same binding phrase and options).

**Update for version 1.1.0**

Once you have updated to firmware version 1.1.0 or newer, the Web Update page on the Hotspot will get a few updates of its own. It will get the Update progress bar, and a Popup will be shown for Success or Error messages. Additionally, you can configure Home Network SSID and Password if you chose not to use ExpressLRS Configurator to set them. Once these are set, you can use the two methods below.

![JoinNetwork](../assets/images/web-joinnetwork.png)

### Method 2

*Note: This method will only work once the Home Network SSID and Password has been configured with the receiver*

With the receiver [wired properly](/quick-start/rx-fcprep/#namimnorc-voyager-flash) to your FC, select the right target and set your [Firmware Options](/quick-start/firmware-options) in the ExpressLRS Configurator.

**Build** the firmware. Once done, it should open a new window where the `BETAFPV_2400_RX-<version>.bin` is. Do not close this window so you can easily navigate to it once it's time to upload the firmware into the receiver.

Power up your Flight Controller by either connecting a LiPo or attaching the USB cable (if the receiver gets powered from USB via a 4v5 pad). The receiver's LED will blink slowly at first, and after 20s or 30s (can be adjusted via ExpressLRS Configurator using `AUTO_WIFI_ON_INTERVAL`), it should blink fast indicating it's on Wifi AP Mode. The fast blink will pause and flash fast once again, indicating connection to your Home Network.

Using your browser, navigate to http://elrs_rx.local/. The Wifi Update page should load. It should show your device target along with the version of the firmware it currently has.

Scroll down to the Firmware Update section, shown below:

![Firmware Update](../assets/images/web-firmwareupdate.png)

Drag-and-drop the `BETAFPV_2400_RX-<version>.bin` file created by the ExpressLRS Configurator into the Choose File field, or manually navigate to the Folder by clicking the `Choose File` button. Once the correct file is selected, click the `Update`. Wait for the process to complete, indicated by a Green popup screen. 

You can now power down your Flight Controller along with the receiver.

### Method 3

*Note: This method will only work once the Home Network SSID and Password has been configured with the receiver*

With the receiver [wired properly](/quick-start/rx-fcprep/#namimnorc-voyager-flash) to your FC, select the right target and set your [Firmware Options](/quick-start/firmware-options) in the ExpressLRS Configurator.

Power up your Flight Controller by either connecting a LiPo or attaching the USB cable (if the receiver gets powered from USB via a 4v5 pad). The receiver's LED will blink slowly at first, and after 20s or 30s (can be adjusted via ExpressLRS Configurator using `AUTO_WIFI_ON_INTERVAL`), it should blink fast indicating it's on Wifi Mode.

**Build & Flash** the firmware using the ExpressLRS Configurator. Wait for the process to complete, indicated by the "Success" prompt and the Receiver LED has gone back to the Slow Blink mode. You can now power down the Flight Controller.

![RXUpload Log](../assets/images/RXWifiUpdateLog.png)

## Flashing via FTDI

Target: `BETAFPV_2400_RX_via_UART`

Wire the receiver into the FTDI, with TX on receiver connected to the Rx on the FTDI, and RX on receiver connected to the Tx of the FTDI. Wire 5V and GND of the FTDI to 5V and GND of the Receiver. Press the button while powering the RX on, and release - the LED should now be solid.

Select the target and set your [Firmware Options](../../quick-start/firmware-options) and once done, click on **Build and Flash**.