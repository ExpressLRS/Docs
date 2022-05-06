---
template: main.html
---

![Setup-Banner](https://github.com/ExpressLRS/ExpressLRS-Hardware/raw/master/img/quick-start.png)

## Flashing via EdgeTX Passthrough

!!! info ""
    This method is the result of the collaborative effort between EdgeTX, RadioMaster and ExpressLRS.

Targets:

- `RadioMaster_Zorro_2400_TX_via_ETX`
- `RadioMaster_TX16S_2400_TX_via_ETX`

Device Category: `RadioMaster 2.4 GHz`

Device: `RadioMaster Zorro 2400 TX`, `RadioMaster TX16S 2400 TX`

With your handset turned on, connect a USB data cable on the USB data port of the Radio. Select `USB Serial(Debug)` or `USB Serial(VCP)` in the option window that pops up. 

![usb picture](../../assets/images/tx-internalUSBPlugged.jpg)

![Debug option](../../assets/images/tx-internalSerialDebug.jpg)

Windows users should check Device Manager and make sure your device is being detected as STMicroelectronics Virtual COM Port device. 

![Device Manager](../../assets/images/DeviceMngr.png)

If not and you're seeing a bunch of Yellow Warning icons for the RadioMaster Serial Port, install the drivers from [here](https://www.st.com/en/development-tools/stsw-stm32102.html). Windows 10 users can use the `VCP_V1.5.0_Setup_W7_x64_64bits` executable.

Using the ExpressLRS Configurator, select the appropriate version and the correct Device Target and set the Flashing method to `EdgeTXPassthrough`.

![via EdgeTX Passthrough](../../assets/images/Method_intTX_EdgeTXPassthrough.png)

Select the `Regulatory Domain` appropriate for your location.

Set your Binding Phrase (optional) and other relevant [Firmware Options] like Local WiFi Network SSID and password.

Once that's done, click **Build and Flash** and wait for the Success banner from the Configurator.

![Build & Flash](../../assets/images/BuildFlash.png)

Unplug the USB and verify with the [ExpressLRS Lua Script](https://github.com/ExpressLRS/ExpressLRS/blob/2.1.0/src/lua/elrsV2.lua?raw=true) (right-click, save as) you have a working internal module and that you have updated to the version you have selected.

![Lua Running](../../assets/images/tx-internalLuaCheck.jpg)

## Flashing via Wifi

Targets:

- `RadioMaster_Zorro_2400_TX_via_WIFI`
- `RadioMaster_TX16S_2400_TX_via_WIFI`

Device Category: `RadioMaster 2.4 GHz`

Device: `RadioMaster Zorro 2400 TX`, `RadioMaster TX16S 2400 TX`

![via WiFi](../../assets/images/Method_intTX_WiFi.png)

### Method 1

With the correct target selected and [Firmware Options] set, **Build** your firmware using the ExpressLRS Configurator.

![Build](../../assets/images/Build.png)

Once it's done, it should open the Target folder for you where the `RadioMaster_Zorro_2400_TX-<version>.bin` or `RadioMaster_TX16S_2400_TX-<version>.bin` file is. Do not close this window so you can easily locate the correct file to upload to the module.

Execute the ExpressLRS lua script by pressing "System Menu" in your radio and then under Tools, select `ExpressLRS`. If the ExpressLRS Lua Script is not in the list, download it from [here](https://github.com/ExpressLRS/ExpressLRS/blob/2.1.0/src/lua/elrsV2.lua?raw=true) (right-click, save as) and save it to your Radio's `/Scripts/Tools` folder.

![Lua Script](../../assets/images/lua1.jpg)

Select **WiFi Connectivity** from the Lua script and then select **Enable WiFi**. Press OK once more to activate the WiFi on the Tx Module. Connect to the Access Point the module will create called `ExpressLRS TX Module`, with the password being `expresslrs`.

![Lua3](../../assets/images/lua/wifi-bw.png)

Using your browser, navigate to the correct page (typically http://10.0.0.1/) and it should show an upload form (you will have to scroll down a bit). You can drag-and-drop the `RadioMaster_Zorro_2400_TX-<version>.bin` or `RadioMaster_TX16S_2400_TX-<version>.bin` file that the ExpressLRS Configurator created. You can also click the `Choose File` button and navigate to the folder where the firmware was created. Ensure that you have selected the correct firmware file and click `Update`.

![Firmware Update](../../assets/images/web-firmwareupdate.png)

Once the file is uploaded, a pop-up confirmation will show up.

![Update Success](../../assets/images/web-firmwareupdateSuccess.png)

Wait for the Lua script screen to close the "WiFi Running" screen and your module should be updated now.

Verify the version and hash in the main screen of ExpressLRS Lua script (you will first need to close it and relaunch the script).

**Join Local Network**

You can configure Home Network SSID and Password if you chose not to use ExpressLRS Configurator to set them. Once these are set, you can use the next two methods below.

![JoinNetwork](../../assets/images/web-joinnetwork.png)

### Method 2

With the correct target selected and [Firmware Options] set, **Build** your firmware using the ExpressLRS Configurator.

![Build](../../assets/images/Build.png)

Once it's done, it should open the Target folder for you where the `RadioMaster_Zorro_2400_TX-<version>.bin` or `RadioMaster_TX16S_2400_TX-<version>.bin` file is. Do not close this window so you can easily locate the correct file to upload to the module.

Using the [ExpressLRS Lua Script](https://github.com/ExpressLRS/ExpressLRS/blob/2.1.0/src/lua/elrsV2.lua?raw=true) (right-click, save as), select `Wifi Connectivity` then choose `Enable WiFi` and if you have flashed your Tx Module with your Home WiFi Network details or have set it in Join Network section of the Update Page, it will connect to the local network automatically.

![Lua3](../../assets/images/lua/wifi-bw.png)

Using your browser, navigate to http://elrs_tx.local and the WiFi Update page should show up. Scroll down towards the Firmware Update section, as shown below:

![Firmware Update](../../assets/images/web-firmwareupdate.png)

Drag-and-drop the `RadioMaster_Zorro_2400_TX-<version>.bin` or `RadioMaster_TX16S_2400_TX-<version>.bin` file created by the ExpressLRS Configurator into the Choose File field, or manually navigate to the Folder by clicking the `Choose File` button. Once the correct file is selected, click the `Update`. Wait for the process to complete, and once the file is uploaded, a pop-up confirmation will show up.

![Update Success](../../assets/images/web-firmwareupdateSuccess.png)

Wait for the Lua script screen to close the "WiFi Running" screen and your module should be updated now.

Verify the version and hash in the main screen of ExpressLRS Lua script (you will first need to close it and relaunch the script).

### Method 3

Using the [ExpressLRS Lua Script](https://github.com/ExpressLRS/ExpressLRS/blob/2.1.0/src/lua/elrsV2.lua?raw=true) (right-click, save as), select `Wifi Connectivity` then choose `Enable WiFi` and if you have flashed your Tx Module with your Home WiFi Network details or have set it in Join Network section of the Update Page, it will connect to the network automatically.

![Lua3](../../assets/images/lua/wifi-bw.png)

Using the ExpressLRS Configurator, select the correct Target and set your [Firmware Options]. Click **Build and Flash** and wait for the compile process to complete. 

![Build & Flash](../../assets/images/BuildFlash.png)

You should see a section as pictured below and the Success message marking the update process complete.

![Wifi Update Log](../../assets/images/WifiUpdateLog.png)

Wait for the Lua script screen to close the "WiFi Running" screen and your module should be updated now.

Verify the version and hash in the main screen of ExpressLRS Lua script (you will first need to close it and relaunch the script).

[Firmware Options]: ../firmware-options.md
[Radio Preparation]: tx-prep.md