---
template: main.html
---

![Setup-Banner](https://raw.githubusercontent.com/ExpressLRS/ExpressLRS-hardware/master/img/quick-start.png)

## 2nd Gen, OLED-equipped

These newer devices are now using an ESP-based MCU compared to the first version. With this in mind, the Flashing method will differ slightly, and should now be the same as with other ESP-based Tx Modules.

### Flashing via WiFi

Target: `NamimnoRC_FLASH_2400_OLED_TX_via_WIFI`

Device Category: `NamimnoRC FLASH 2.4 GHz`

Device: `NamimnoRC FLASH 2400 OLED TX`

![via WiFi](../../assets/images/Method_TX_WiFi.png)

#### Method 1

With the correct target selected and [Firmware Options] set, **Build** your firmware using the ExpressLRS Configurator.

![Build](../../assets/images/Build.png)

Once it's done, it should open the Target folder for you where the `NamimnoRC_FLASH_2400_OLED_TX-<version>.bin` file is. Do not close this window so you can easily locate the correct file to upload to the module.

The next steps will require the [ExpressLRS Lua Script](https://github.com/ExpressLRS/ExpressLRS/blob/2.1.0/src/lua/elrsV2.lua?raw=true) (right-click, save as). Download the ExpressLRS lua script and save it to your Radio's `/Scripts/Tools` folder. Insert/attach your module into your module bay and make sure it's not loose and there's proper connection with the radio (see the [Radio Preparation] page). Execute the ExpressLRS lua script by pressing "System Menu" in your radio and then under Tools, select `ExpressLRS`.

![Lua Script](../../assets/images/lua1.jpg)
![Lua Script T16](../../assets/images/lua2.jpg)

If the script is stuck at `Loading...`, then there's a chance your module is still in v1.x firmware, your External RF module is not set to CRSF or that your module is not well-connected to the module bay pins.

![Lua3](../../assets/images/lua3.jpg)

Select **WiFi Connectivity** from the Lua script and then select **Enable WiFi**. Press OK once more to activate the WiFi on the Tx Module. Connect to the Access Point the module will create called `ExpressLRS TX`, with the password being `expresslrs`.

<figure markdown>
![WiFi Hotspot](../../assets/images/WifiHotspotTX.png)
</figure>

Using your browser, navigate to the correct page (typically http://10.0.0.1/) and it should show an upload form (you will have to scroll down a bit). You can drag-and-drop the `NamimnoRC_FLASH_2400_OLED_TX-<version>.bin` file that the ExpressLRS Configurator created. You can also click the `Choose File` button and navigate to the folder where the firmware was created. Ensure that you have selected the correct firmware file and click `Update`.

Once the file is uploaded, a pop-up confirmation will show up. Wait for the Lua script screen to close the "WiFi Running" screen and your module should be updated now.

Verify the version and hash in the main screen of ExpressLRS Lua script.

**Join Local Network**

You can configure Home Network SSID and Password if you chose not to use ExpressLRS Configurator to set them. Once these are set, you can use the next two methods below.

![JoinNetwork](../../assets/images/web-joinnetwork.png)

#### Method 2

With the correct target selected and [Firmware Options] set, **Build** your firmware using the ExpressLRS Configurator.

![Build](../../assets/images/Build.png)

Once it's done, it should open the Target folder for you where the `NamimnoRC_FLASH_2400_OLED_TX-<version>.bin` file is. Do not close this window so you can easily locate the correct file to upload to the module.

Using the [ExpressLRS Lua Script](https://github.com/ExpressLRS/ExpressLRS/blob/2.1.0/src/lua/elrsV2.lua?raw=true) (right-click, save as), select `Wifi Connectivity` then choose `Enable WiFi` and if you have flashed your Tx Module with your Home WiFi Network details or have set it in Join Network section of the Update Page, it will connect to the local network automatically.

Using your browser, navigate to http://elrs_tx.local and the WiFi Update page should show up. Scroll down towards the Firmware Update section, as shown below:

![Firmware Update](../../assets/images/web-firmwareupdate.png)

Drag-and-drop the `NamimnoRC_FLASH_2400_OLED_TX-<version>.bin` file created by the ExpressLRS Configurator into the Choose File field, or manually navigate to the Folder by clicking the `Choose File` button. Once the correct file is selected, click the `Update`. Wait for the process to complete, and the module will reboot (~1min).

Verify the version and hash in the main screen of ExpressLRS Lua script.

#### Method 3

Using the [ExpressLRS Lua Script](https://github.com/ExpressLRS/ExpressLRS/blob/2.1.0/src/lua/elrsV2.lua?raw=true) (right-click, save as), select `Wifi Connectivity` then choose `Enable WiFi` and if you have flashed your Tx Module with your Home WiFi Network details or have set it in Join Network section of the Update Page, it will connect to the network automatically.

Using the ExpressLRS Configurator, select the correct Target and set your [Firmware Options]. Click **Build and Flash** and wait for the compile process to complete. You should see a section as pictured below and the Success message marking the update process complete.

![Build & Flash](../../assets/images/BuildFlash.png)

![Wifi Update Log](../../assets/images/WifiUpdateLog.png)

Verify the version and hash in the main screen of ExpressLRS Lua script.

### Flashing via USB/UART

![Uart Select Switch](../../assets/images/flash_backpack.png)

!!! attention
    The left position of the switch is for flashing the [backpack](../../hardware/backpack/backpack-tx-setup.md). The right position of the switch is for flashing the TX itself. The right position is default, so there is no need to open your module unless you need to unbrick your TX backpack!

Target: `NamimnoRC_FLASH_2400_OLED_TX_via_UART`

Device Category: `NamimnoRC FLASH 2.4 GHz`

Device: `NamimnoRC FLASH 2400 OLED TX`

![via UART](../../assets/images/Method_TX_UART.png)

Attach your USB cable into the module and your computer. [CH340 Drivers](https://sparks.gogo.co.nz/assets/_site_/downloads/CH34x_Install_Windows_v3_4.zip) will have to be downloaded (Right-click, Save-as) and installed (Unzip the contents of the file; Run the executable installer) for this to work properly (Windows). Make sure your computer recognizes the module as a USB-SERIAL CH340 device, otherwise, this method will not work. 

Using the ExpressLRS Configurator with the correct Target selected and [Firmware Options] set, hit **Build & Flash**. Wait for the process to finish, and you should be greeted with the "Success" message.

![Build & Flash](../../assets/images/BuildFlash.png)

Verification can be done using the [ExpressLRS lua] script. It should show the Version Number and Hash at the bottom, as well as the options you can set. If it's showing "Loading" at the top, check if External Module is set to CRSF for the selected model in your radio, and that internal RF module is set to off. See [General Troubleshooting] section for other ways to determine your module is flashed and ready for flying.

## First Gen, No OLED Screen

### Flashing via Wifi

Target: `NamimnoRC_Flash_2400_TX_via_WiFi`

Device Category: `NamimnoRC FLASH 2.4 GHz`

Device: `NamimnoRC FLASH 2400 TX`

![via WiFi](../../assets/images/Method_TX_WiFi-stm.png)

#### Method 1

With the correct target selected and [Firmware Options] set, **Build** your firmware using the ExpressLRS Configurator.

![Build](../../assets/images/Build.png)

Once it's done, it should open the Target folder for you where the `firmware.elrs` file is. Do not close this window so you can easily locate the correct file to upload to the module.

These Tx Modules are STM32-based so they require a separate ESP "backpack" device for Wifi Flashing/Updating. 

Attach the module to your JR Bays and power it up. Connect to the `ESP Wifi Manager` Hotspot that the device will activate. Once connected, navigate to http://elrs_tx.local/.

![Wifi Manager](../../assets/images/WifiManager.png)

Press `Configure WiFi` and set your home network SSID and password. This will enable your Tx Module to connect to your local home network.

On your browser, refresh the http://elrs_tx.local/ and scroll towards the STM32 Firmware Update section, as shown below:

![STM32 Firmware Update](../../assets/images/STM32-updater.png)

Drag-and-drop the `firmware.elrs` file created by the ExpressLRS Configurator into the Choose File field, or manually navigate to the Folder by clicking the Choose File button. You can also upload the `firmware.bin` file but change the offset to *0x4000*.Once the correct file is selected, click the `Upload and Flash STM32`. Wait for the process to complete, and the module will reboot (~1min). Using the [ExpressLRS lua] script, verify that you have the latest version.

#### Method 2

These Tx Modules are STM32-based so they require a separate ESP "backpack" device for Wifi Flashing/Updating. 

Attach the module to your JR Bays and power it up. Connect to the `ESP Wifi Manager` Hotspot that the device will activate. Once connected, navigate to http://elrs_tx.local/.

![Wifi Manager](../../assets/images/WifiManager.png)

Press `Configure WiFi` and set your home network SSID and password. This will enable your Tx Module to connect to your local home network.

Using the ExpressLRS Configurator, select the correct Target and set your [Firmware Options]. Click **Build and Flash** and wait for the compile process to complete. You should see a section as pictured below and the Success message marking the update process complete.

![Build & Flash](../../assets/images/BuildFlash.png)

![Wifi Update Log](../../assets/images/WifiUpdateLog.png)

Using the [ExpressLRS lua] script, verify that you have the latest version.

### Flashing via OpenTX Radio

!!! note
    The `NamimnoRC_Flash_2400_TX_via_WiFi` Target will work for this method too!

Device Category: `NamimnoRC FLASH 2.4 GHz`

Device: `NamimnoRC FLASH 2400 TX`

![via WiFi](../../assets/images/Method_TX_WiFi-stm.png)

With the correct target selected and [Firmware Options] set, **Build** your firmware using the ExpressLRS Configurator.

![Build](../../assets/images/Build.png)

Once it's done, it should open the Target folder for you where the `NamimnoRC_Flash_2400_TX-<version>.elrs` file is. Do not close this window so you can easily locate the correct file to copy to your Radio's SD Card.

Copy the `NamimnoRC_Flash_2400_TX-<version>.elrs` file into your radio's SD Card `/FIRMWARE` folder.

Once copied, navigate to the `/FIRMWARE` Folder on your Radio and select/highlight the `NamimnoRC_Flash_2400_TX-<version>.elrs` file, long-press the Enter key and select `Flash external ELRS`. Flashing will then commence and after a few seconds, radio should show a `Flash Successful` message and you're done!

Using the [ExpressLRS lua] script, verify that you have the latest version.

### Flashing via STLink

Target: `NamimnoRC_Flash_2400_TX_via_STLINK`

Device Category: `NamimnoRC FLASH 2.4 GHz`

Device: `NamimnoRC FLASH 2400 TX`

![via STLink](../../assets/images/Method_TX_STLink.png)

**ONLY USE THIS METHOD IF THE FIRMWARE HAS BEEN CORRUPTED** 

Begin by disassembling the module by unscrewing the 4 screws at the rear of the module with a 1.5mm hex wrench. Carefully seperate the parts of the module and detach the cable from the main PCB.

<img src="https://github.com/ExpressLRS/ExpressLRS-Hardware/blob/master/img/namimnoback.jpg?raw=true" width="30%">
<img src="https://github.com/ExpressLRS/ExpressLRS-Hardware/blob/master/img/cable.jpg?raw=true" width="30%">

Wire your `STLink v2` to the module's pins as show below:

<img src="https://github.com/ExpressLRS/ExpressLRS-Hardware/blob/master/img/namimnopinout.png?raw=true" width="40%">

With the module connected shown above, and your configuration set, hit **Build & Flash** in the ExpressLRS Configurator and wait for the process to finish.

![Build & Flash](../../assets/images/BuildFlash.png)

Once that's done, and the Success Message showing, you can now remove/unsolder the STLink, and re-assemble the module, and put it into your Radio's Module Bay. If the Radio has CRSF selected, the light should turn green meaning the module has communication with your radio.

Verification can be done using the [ExpressLRS lua] script. It should show the Version Number and Hash at the bottom, as well as the options you can set. If it's showing "Loading" at the top, check if External Module is set to CRSF for the selected model in your radio, and that internal RF module is set to off. See [General Troubleshooting] section for other ways to determine your module is flashed and ready for flying.

[Firmware Options]: ../firmware-options.md
[Radio Preparation]: tx-prep.md
[ExpressLRS lua]: lua-howto.md
[General Troubleshooting]: ../troubleshooting.md#general-troubleshooting