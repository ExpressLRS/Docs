---
template: main.html
---

![Setup-Banner](https://raw.githubusercontent.com/ExpressLRS/ExpressLRS-hardware/master/img/quick-start.png)

!!! note 
    This guide applies to all of the following HappyModel TX modules: ES24TX, ES24TX Lite, ES24TX Iron Man, ES24TX Slim Pro and ES24TX Pro Micro. Any module with "Pro" in the name uses the `_Pro_Series` target. Some Pro Series targets may come unflashed, which requires [USB Flashing](#flashing-via-usbuart).

## Flashing via Wifi

Targets:

- `HappyModel_ES24TX_2400_TX_via_WIFI`
- `HM_ES24TX_Pro_Series_2400_TX_via_WIFI`

Device Category: `Happymodel 2.4 GHz`

Device:

- `HappyModel ES24TX 2400 TX` for ES24TX (non-Pro), ES24TX Lite, ES24TX Slim
- `HM ES24TX Pro Series 2400 TX` for ES24TX Pro & Slim Pro

![via WiFi](../../assets/images/Method_TX_WiFi.png)

!!! attention

    The methods below applies if you've already updated your Tx modules to 2.x. For modules still in firmwares pre 2.x, you should use [1.x WiFi flashing method](https://www.expresslrs.org/1.0/quick-start/tx-es24tx/) to update to 2.x. Or update to 2.x via USB instead.

### Method 1

With the correct target selected and [Firmware Options] set, **Build** your firmware using the ExpressLRS Configurator.

![Build](../../assets/images/Build.png)

Once it's done, it should open the Target folder for you where the `HappyModel_ES24TX_2400_TX-<version>.bin` or `HM_ES24TX_Pro_Series_2400_TX-<version>.bin` file is. Do not close this window so you can easily locate the correct file to upload to the module.

The next steps will require the [ExpressLRS Lua Script](https://github.com/ExpressLRS/ExpressLRS/blob/2.1.0/src/lua/elrsV2.lua?raw=true) (right-click, save as). Download the ExpressLRS lua script and save it to your Radio's `/Scripts/Tools` folder. Insert/attach your module into your module bay and make sure it's not loose and there's proper connection with the radio (see the [Radio Preparation] page). Execute the ExpressLRS lua script by pressing "System Menu" in your radio and then under Tools, select `ExpressLRS`.

![Lua Script](../../assets/images/lua1.jpg)
![Lua Script T16](../../assets/images/lua2.jpg)

If the script is stuck at `Loading...`, then there's a chance your module is still in v1.x firmware, your External RF module is not set to CRSF or that your module is not well-connected to the module bay pins.

![Lua3](../../assets/images/lua3.jpg)

Select **WiFi Connectivity** from the Lua script and then select **Enable WiFi**. Press OK once more to activate the WiFi on the Tx Module. Connect to the Access Point the module will create called `ExpressLRS TX Module`, with the password being `expresslrs`.

Using your browser, navigate to the correct page (typically http://10.0.0.1/) and it should show an upload form (you will have to scroll down a bit). You can drag-and-drop the `HappyModel_ES24TX_2400_TX-<version>.bin` or `HM_ES24TX_Pro_Series_2400_TX-<version>.bin` file that the ExpressLRS Configurator created. You can also click the `Choose File` button and navigate to the folder where the firmware was created. Ensure that you have selected the correct firmware file and click `Update`.

Once the file is uploaded, a pop-up confirmation will show up. Wait for the Lua script screen to close the "WiFi Running" screen and your module should be updated now.

Verify the version and hash in the main screen of ExpressLRS Lua script.

**Update for version 2.0**

Once you have updated to firmware version 2.0 or newer, the Web Update page on the Hotspot will get a few updates of its own. It will get the Update progress bar, and a Popup will be shown for Success or Error messages. Additionally, you can configure Home Network SSID and Password if you chose not to use ExpressLRS Configurator to set them. Once these are set, you can use the two methods below.

![JoinNetwork](../../assets/images/web-joinnetwork.png)

### Method 2

With the correct target selected and [Firmware Options] set, **Build** your firmware using the ExpressLRS Configurator.

![Build](../../assets/images/Build.png)

Once it's done, it should open the Target folder for you where the `HappyModel_ES24TX_2400_TX-<version>.bin` or `HM_ES24TX_Pro_Series_2400_TX-<version>.bin` file is. Do not close this window so you can easily locate the correct file to upload to the module.

Using the [ExpressLRS Lua Script](https://github.com/ExpressLRS/ExpressLRS/blob/2.1.0/src/lua/elrsV2.lua?raw=true) (right-click, save as), select `Wifi Connectivity` then choose `Enable WiFi` and if you have flashed your Tx Module with your Home WiFi Network details or have set it in Join Network section of the Update Page, it will connect to the local network automatically.

Using your browser, navigate to http://elrs_tx.local and the WiFi Update page should show up. Scroll down towards the Firmware Update section, as shown below:

![Firmware Update](../../assets/images/web-firmwareupdate.png)

Drag-and-drop the `HappyModel_ES24TX_2400_TX-<version>.bin` or `HM_ES24TX_Pro_Series_2400_TX-<version>.bin` file created by the ExpressLRS Configurator into the Choose File field, or manually navigate to the Folder by clicking the `Choose File` button. Once the correct file is selected, click the `Update`. Wait for the process to complete, and the module will reboot (~1min).

Verify the version and hash in the main screen of ExpressLRS Lua script.

### Method 3

Using the [ExpressLRS Lua Script](https://github.com/ExpressLRS/ExpressLRS/blob/2.1.0/src/lua/elrsV2.lua?raw=true) (right-click, save as), select `Wifi Connectivity` then choose `Enable WiFi` and if you have flashed your Tx Module with your Home WiFi Network details or have set it in Join Network section of the Update Page, it will connect to the network automatically.

Using the ExpressLRS Configurator, select the correct Target and set your [Firmware Options]. Click **Build and Flash** and wait for the compile process to complete. You should see a section as pictured below and the Success message marking the update process complete.

![Build & Flash](../../assets/images/BuildFlash.png)

![Wifi Update Log](../../assets/images/WifiUpdateLog.png)

Verify the version and hash in the main screen of ExpressLRS Lua script.

## Flashing via USB/UART

Targets:

- `HappyModel_ES24TX_2400_TX_via_UART`
- `HM_ES24TX_Pro_Series_2400_TX_via_UART`

Device Category: `Happymodel 2.4 GHz`

Device:

- `HappyModel ES24TX 2400 TX` for ES24TX (non-Pro), ES24TX Lite, ES24TX Slim
- `HM ES24TX Pro Series 2400 TX` for ES24TX Pro & Slim Pro

![via UART](../../assets/images/Method_TX_UART.png)

This method requires you move two jumpers or dipswitches into specific pins or positions in the module board. See the following images for the jumper or dipswitch location and which pin/switches should be toggled for this method to work.

<small>ES24TX Full Size, Non Pro</small>

![JumperFS](../../assets/images/jumper-es24Micro.png)

<small>ES24TX Lite, for Jumper T-Lite</small>

![JumperLite](../../assets/images/jumper-es24Lite.png)

<small>ES24TX Slim, Iron Man</small>

![DipswitchSlim](../../assets/images/dipswitch-es24slim.png)

<small>ES24TX Slim Pro</small>

![DipswitchSlimPro](../../assets/images/dipswitch-es24slimPro.png)

<small>ES24TX Pro 1W</small>

![DipswitchPro](../../assets/images/dipswitch-Pro.png)

Attach your USB cable into the module and your computer. [CP210x Drivers](https://www.silabs.com/developers/usb-to-uart-bridge-vcp-drivers) will have to be installed for this to work properly (Windows). Make sure your computer recognizes the module as a CP210x USB-to-UART Bridge device (check Device Manager; or the Actions section of the ExpressLRS Configurator should show another Com Port with Silabs CP210x designation), otherwise, this method will not work.

![CP210x Drivers](../../assets/images/CP210xDriverDownload.png)

Using the ExpressLRS Configurator with the correct Target selected and [Firmware Options] set, hit **Build & Flash**. Wait for the process to finish, and you should be greeted with the "Success" message.

![Build & Flash](../../assets/images/BuildFlash.png)

Assemble the module back together (ensure the module PCB is not loose from its mounting points) and attach it to your radio module bay and verify the version and hash in the main screen of ExpressLRS Lua script.

[Firmware Options]: ../firmware-options.md
[Radio Preparation]: tx-prep.md