---
template: main.html
---

![Setup-Banner](https://raw.githubusercontent.com/ExpressLRS/ExpressLRS-hardware/master/img/quick-start.png)

!!! note 
    This guide applies to all of the following HappyModel TX modules: ES24TX, ES24TX Lite, ES24TX Iron Man, ES24TX Slim Pro and ES24TX Pro Micro. Any module with "Pro" in the name uses the `_Pro_Series` target.

!!! danger "Advisory"
    If you are flashing/updating your TX module via WiFi for the first time from the factory firmware, or from an older firmware, to ExpressLRS 3.x firmware you will first need to flash it to version 2.5.2 then flash it with the [Repartitioner](https://github.com/ExpressLRS/repartitioner) binary [file](https://github.com/ExpressLRS/repartitioner/releases/download/1.0/repartitioner.bin) (right click, save as/save file as). Should it complain about Target Mismatch, just click `Flash Anyway`. Only then you can flash to 3.x firmware following method 1 or 2 from the WiFi Flashing Guide below.

    Joshua Bardwell has a video about it [here](https://www.youtube.com/watch?v=2kcRi1cHejM).

    You can update straight to 3.2.0 without repartitioner or going to 2.5.2 first if flashing via UART.

## Flashing via WiFi

- Targets:
    - `HappyModel_ES24TX_2400_TX_via_WIFI`
    - `HM_ES24TX_Pro_Series_2400_TX_via_WIFI`

- Device Category: 
    - `Happymodel 2.4 GHz`

- Device:
    - `HappyModel ES24TX 2400 TX` for ES24TX (non-Pro), ES24TX Lite, ES24TX Slim
    - `HM ES24TX Pro Series 2400 TX` for ES24TX Pro & Slim Pro

<figure markdown>
![via WiFi](../../assets/images/Method_TX_WiFi.png)
<figcaption>Flashing via WiFi</figcaption>
</figure>

!!! attention
    The methods below apply if you've already updated your Tx modules to 2.x. For modules still in firmwares pre 2.x, you should use [1.x WiFi flashing method](https://www.expresslrs.org/1.0/quick-start/tx-es24tx/) to update to 2.x. Or update to 2.x via USB instead.

### Method 1

With the correct target selected and [Firmware Options] set, **Build** your firmware using the ExpressLRS Configurator.

<figure markdown>
![Build]
</figure>

Once it's done, it should open the Target folder for you where the `HappyModel_ES24TX_2400_TX-<version>.bin` or `HM_ES24TX_Pro_Series_2400_TX-<version>.bin` file is. Do not close this window so you can easily locate the correct file to upload to the module.

The next steps will require the [ExpressLRS Lua script] (right-click, save as). Download the ExpressLRS Lua script and save it to your Radio's `/Scripts/Tools` folder. Insert/attach your module into your module bay and make sure it's not loose and there's a proper connection with the radio (see the [Radio Preparation] page). Execute the ExpressLRS Lua script by pressing "System Menu" on your radio and then under Tools, select `ExpressLRS`.

<figure markdown>
![Lua Script](../../assets/images/lua1.jpg)
</figure>

<figure markdown>
![Lua Script T16](../../assets/images/lua2.jpg)
</figure>

If the script is stuck at `Loading...`, then there's a chance your module is still in v1.x firmware, your External RF module is not set to CRSF or your module is not well-connected to the module bay pins.

<figure markdown>
![Lua3](../../assets/images/lua3.jpg)
</figure>

Select **WiFi Connectivity** from the Lua script and then select **Enable WiFi**. Press OK once more to activate the WiFi on the Tx Module. Connect to the Access Point the module will create called `ExpressLRS TX`, with the password being `expresslrs`.

<figure markdown>
![WiFi Hotspot](../../assets/images/WifiHotspotTX.png)
</figure>

Using your browser, navigate to the correct page (typically http://10.0.0.1/) and it should show an upload form (you will have to scroll down a bit). You can drag-and-drop the `HappyModel_ES24TX_2400_TX-<version>.bin` or `HM_ES24TX_Pro_Series_2400_TX-<version>.bin` file that the ExpressLRS Configurator created. You can also click the `Choose File` button and navigate to the folder where the firmware was created. Ensure that you have selected the correct firmware file and click `Update`.

Once the file is uploaded, a pop-up confirmation will show up. Wait for the Lua script screen to close the "WiFi Running" screen and your module should be updated now.

Verify the version and hash in the main screen of the ExpressLRS Lua script.

!!! Info "Update for version 2.0"
    Once you have updated to firmware version 2.0 or newer, the Web Update page on the Hotspot will get a few updates of its own. It will get the Update progress bar, and a Popup will be shown for Success or Error messages. Additionally, you can configure Home Network SSID and Password if you chose not to use ExpressLRS Configurator to set them. Once these are set, you can use the two methods below.

<figure markdown>
![JoinNetwork](../../assets/images/web-joinnetwork.png)
</figure>

### Method 2

With the correct target selected and [Firmware Options] set, **Build** your firmware using the ExpressLRS Configurator.

<figure markdown>
![Build]
</figure>

Once it's done, it should open the Target folder for you where the `HappyModel_ES24TX_2400_TX-<version>.bin` or `HM_ES24TX_Pro_Series_2400_TX-<version>.bin` file is. Do not close this window so you can easily locate the correct file to upload to the module.

Using the [ExpressLRS Lua script] (right-click, save as), select `Wifi Connectivity` then choose `Enable WiFi` and if you have flashed your Tx Module with your Home WiFi Network details or have set it in the Join Network section of the Update Page, it will connect to the local network automatically.

Using your browser, navigate to http://elrs_tx.local and the WiFi Update page should show up. Scroll down towards the Firmware Update section, as shown below:

<figure markdown>
![Firmware Update](../../assets/images/web-firmwareupdate.png)
</figure>

Drag-and-drop the `HappyModel_ES24TX_2400_TX-<version>.bin` or `HM_ES24TX_Pro_Series_2400_TX-<version>.bin` file created by the ExpressLRS Configurator into the Choose File field, or manually navigate to the Folder by clicking the `Choose File` button. Once the correct file is selected, click the `Update`. Wait for the process to complete, and the module will reboot (~1min).

Verify the version and hash in the main screen of the ExpressLRS Lua script.

### Method 3

Using the [ExpressLRS Lua script] (right-click, save as), select `Wifi Connectivity` then choose `Enable WiFi` and if you have flashed your Tx Module with your Home WiFi Network details or have set it in the Join Network section of the Update Page, it will connect to the network automatically.

Using the ExpressLRS Configurator, select the correct Target and set your [Firmware Options]. Click **Build and Flash** and wait for the compile process to complete. You should see a section as pictured below and the Success message marking the update process complete.

<figure markdown>
![Build & Flash]
</figure>

<figure markdown>
![Wifi Update Log](../../assets/images/WifiUpdateLog.png)
</figure>

Verify the version and hash in the main screen of the ExpressLRS Lua script.

## Flashing via USB/UART

- Targets:
    - `HappyModel_ES24TX_2400_TX_via_UART`
    - `HM_ES24TX_Pro_Series_2400_TX_via_UART`

- Device Category: 
    - `Happymodel 2.4 GHz`

- Device:
    - `HappyModel ES24TX 2400 TX` for ES24TX (non-Pro), ES24TX Lite, ES24TX Slim
    - `HM ES24TX Pro Series 2400 TX` for ES24TX Pro & Slim Pro

<figure markdown>
![via UART](../../assets/images/Method_TX_UART.png)
<figcaption>Flashing via UART</figcaption>
</figure>

This method requires you to move two jumpers or dipswitches into specific pins or positions in the module board. See the following images for the jumper or dipswitch location and which pin/switches should be toggled for this method to work.

<figure markdown>
![JumperFS](../../assets/images/jumper-es24Micro.png)
<figcaption>ES24TX Full Size, Non Pro</figcaption>
</figure>

<figure markdown>
![JumperLite](../../assets/images/jumper-es24Lite.png)
<figcaption>ES24TX Lite, for Jumper T-Lite</figcaption>
</figure>

<figure markdown>
![DipswitchSlim](../../assets/images/dipswitch-es24slim.png)
<figcaption>ES24TX Slim, Iron Man</figcaption>
</figure>

<figure markdown>
![DipswitchSlimPro](../../assets/images/dipswitch-es24slimPro.png)
<figcaption>ES24TX Slim Pro</figcaption>
</figure>

<figure markdown>
![DipswitchPro](../../assets/images/dipswitch-Pro.png)
<figcaption>ES24TX Pro 1W</figcaption>
</figure>

Attach your USB cable to the module and your computer. [CP210x Drivers](https://www.silabs.com/developers/usb-to-uart-bridge-vcp-drivers) will have to be installed for this to work properly (Windows). Make sure your computer recognizes the module as a CP210x USB-to-UART Bridge device (check Device Manager; or the Actions section of the ExpressLRS Configurator should show another Com Port with Silabs CP210x designation), otherwise, this method will not work.

!!! tip "Important"
    Check Device Manager on your Windows system before proceeding. Ensure the correct drivers are installed. Some Linux distros might also need drivers. The drivers can be downloaded [here](https://www.silabs.com/developers/usb-to-uart-bridge-vcp-drivers).

<figure markdown>
![CP210x Drivers](../../assets/images/CP210xDriverDownload.png)
</figure>

Using the ExpressLRS Configurator with the correct Target selected and [Firmware Options] set, hit **Build & Flash**. Wait for the process to finish, and you should be greeted with the "Success" message.

<figure markdown>
![Build & Flash]
</figure>

Assemble the module back together (ensure the module PCB is not loose from its mounting points) and attach it to your radio module bay and verify the version and hash in the main screen of the ExpressLRS Lua script.

[ExpressLRS Lua script]: https://github.com/ExpressLRS/ExpressLRS/blob/3.x.x-maintenance/src/lua/elrsV3.lua?raw=true
[Build]: ../../assets/images/Build.png
[Build & Flash]: ../../assets/images/BuildFlash.png
[Firmware Options]: ../firmware-options.md
[Radio Preparation]: tx-prep.md
