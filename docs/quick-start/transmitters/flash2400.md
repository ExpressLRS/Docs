---
template: main.html
---

<figure markdown>
![Setup-Banner](https://raw.githubusercontent.com/ExpressLRS/ExpressLRS-hardware/master/img/quick-start.png)
</figure>

!!! danger "Advisory"
    If you are flashing/updating your TX module via WiFi for the first time from the factory firmware, or from an older firmware, to ExpressLRS 3.x firmware you will first need to flash it to version 2.5.2 then flash it with the [Repartitioner](https://github.com/ExpressLRS/repartitioner) binary [file](https://github.com/ExpressLRS/repartitioner/releases/download/1.0/repartitioner.bin) (right click, save as/save file as). Should it complain about Target Mismatch, just click `Flash Anyway`. Only then you can flash to 3.x firmware following method 1 or 2 from the WiFi Flashing Guide below.

    Joshua Bardwell has a video about it [here](https://www.youtube.com/watch?v=2kcRi1cHejM).

    You can update straight to 3.2.0 without repartitioner or going to 2.5.2 first if flashing via UART.

## 2nd Gen, OLED-equipped

These newer devices are now using an ESP-based MCU compared to the first version. With this in mind, the Flashing method will differ slightly, and should now be the same as with other ESP-based Tx Modules.

### Flashing via WiFi

- Target: `NamimnoRC_FLASH_2400_OLED_TX_via_WIFI`

- Device Category: `NamimnoRC FLASH 2.4 GHz`

- Device: `NamimnoRC FLASH 2400 OLED TX`

<figure markdown>
![via WiFi](../../assets/images/Method_TX_WiFi.png)
<figcaption>Flashing via WiFi</figcaption>
</figure>

#### Method 1

With the correct target selected and [Firmware Options] set, **Build** your firmware using the ExpressLRS Configurator.

<figure markdown>
![Build]
</figure>

Once it's done, it should open the Target folder for you where the `NamimnoRC_FLASH_2400_OLED_TX-<version>.bin` file is. Do not close this window so you can easily locate the correct file to upload to the module.

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

Using your browser, navigate to the correct page (typically http://10.0.0.1/) and it should show an upload form (you will have to scroll down a bit). You can drag-and-drop the `NamimnoRC_FLASH_2400_OLED_TX-<version>.bin` file that the ExpressLRS Configurator created. You can also click the `Choose File` button and navigate to the folder where the firmware was created. Ensure that you have selected the correct firmware file and click `Update`.

Once the file is uploaded, a pop-up confirmation will show up. Wait for the Lua script screen to close the "WiFi Running" screen and your module should be updated now.

Verify the version and hash in the main screen of the ExpressLRS Lua script.

**Join Local Network**

You can configure Home Network SSID and Password if you chose not to use ExpressLRS Configurator to set them. Once these are set, you can use the next two methods below.

<figure markdown>
![JoinNetwork](../../assets/images/web-joinnetwork.png)
</figure>

#### Method 2

With the correct target selected and [Firmware Options] set, **Build** your firmware using the ExpressLRS Configurator.

<figure markdown>
![Build]
</figure>

Once it's done, it should open the Target folder for you where the `NamimnoRC_FLASH_2400_OLED_TX-<version>.bin` file is. Do not close this window so you can easily locate the correct file to upload to the module.

Using the [ExpressLRS Lua script] (right-click, save as), select `Wifi Connectivity` then choose `Enable WiFi` and if you have flashed your Tx Module with your Home WiFi Network details or have set it in the Join Network section of the Update Page, it will connect to the local network automatically.

Using your browser, navigate to http://elrs_tx.local and the WiFi Update page should show up. Scroll down towards the Firmware Update section, as shown below:

<figure markdown>
![Firmware Update](../../assets/images/web-firmwareupdate.png)
</figure>

Drag-and-drop the `NamimnoRC_FLASH_2400_OLED_TX-<version>.bin` file created by the ExpressLRS Configurator into the Choose File field, or manually navigate to the Folder by clicking the `Choose File` button. Once the correct file is selected, click the `Update`. Wait for the process to complete, and the module will reboot (~1min).

Verify the version and hash in the main screen of the ExpressLRS Lua script.

#### Method 3

Using the [ExpressLRS Lua script] (right-click, save as), select `Wifi Connectivity` then choose `Enable WiFi` and if you have flashed your Tx Module with your Home WiFi Network details or have set it in the Join Network section of the Update Page, it will connect to the network automatically.

Using the ExpressLRS Configurator, select the correct Target and set your [Firmware Options]. Click **Build and Flash** and wait for the compile process to complete. You should see a section as pictured below and the Success message marking the update process complete.

<figure markdown>
![Build & Flash]
</figure>

<figure markdown>
![Wifi Update Log](../../assets/images/WifiUpdateLog.png)
</figure>

Verify the version and hash in the main screen of the ExpressLRS Lua script.

### Flashing via USB/UART

<figure markdown>
![Uart Select Switch](../../assets/images/flash_backpack.png)
</figure>

!!! attention
    The left position of the switch is for flashing the [backpack](../../hardware/backpack/backpack-tx-setup.md). The right position of the switch is for flashing the TX itself. The right position is the default, so there is no need to open your module unless you need to unbrick your TX backpack!

- Target: `NamimnoRC_FLASH_2400_OLED_TX_via_UART`

- Device Category: `NamimnoRC FLASH 2.4 GHz`

- Device: `NamimnoRC FLASH 2400 OLED TX`

<figure markdown>
![via UART](../../assets/images/Method_TX_UART.png)
<figcaption>Flashing via UART</figcaption>
</figure>

Attach your USB cable to the module and your computer. [CH340 Drivers](https://sparks.gogo.co.nz/assets/_site_/downloads/CH34x_Install_Windows_v3_4.zip) will have to be downloaded (Right-click, Save-as) and installed (Unzip the contents of the file; Run the executable installer) for this to work properly (Windows). Make sure your computer recognizes the module as a USB-SERIAL CH340 device, otherwise, this method will not work. For other Operating Systems, head to this [site](http://www.wch-ic.com/downloads/CH341SER_ZIP.html) to download your needed drivers.

!!! tip "Important"
    Check Device Manager on your Windows system before proceeding. Ensure the correct drivers are installed. Some Linux distros might also need drivers. The drivers can be downloaded [here](https://sparks.gogo.co.nz/assets/_site_/downloads/CH34x_Install_Windows_v3_4.zip).

Using the ExpressLRS Configurator with the correct Target selected and [Firmware Options] set, hit **Build & Flash**. Wait for the process to finish, and you should be greeted with the "Success" message.

<figure markdown>
![Build & Flash]
</figure>

Verification can be done using the [ExpressLRS Lua] script. It should show the Version Number and Hash at the bottom, as well as the options you can set. If it's showing "Loading" at the top, check if External Module is set to CRSF for the selected model in your radio, and that the internal RF module is set to off. See the [General Troubleshooting] section for other ways to determine whether your module is flashed and ready for flying.

## First Gen, No OLED Screen

### Flashing via WiFi

- Target: `NamimnoRC_Flash_2400_TX_via_WiFi`

- Device Category: `NamimnoRC FLASH 2.4 GHz`

- Device: `NamimnoRC FLASH 2400 TX`

<figure markdown>
![via WiFi](../../assets/images/Method_TX_WiFi-stm.png)
<figcaption>Flashing via WiFi</figcaption>
</figure>

#### Method 1

With the correct target selected and [Firmware Options] set, **Build** your firmware using the ExpressLRS Configurator.

<figure markdown>
![Build]
</figure>

Once it's done, it should open the Target folder for you where the `firmware.elrs` file is. Do not close this window so you can easily locate the correct file to upload to the module.

These Tx Modules are STM32-based so they require a separate ESP "backpack" device for Wifi Flashing/Updating. 

Attach the module to your JR Bays and power it up. Connect to the `ESP Wifi Manager` Hotspot that the device will activate. Once connected, navigate to http://elrs_tx.local/.

<figure markdown>
![Wifi Manager](../../assets/images/WifiManager.png)
</figure>

Press `Configure WiFi` and set your home network SSID and password. This will enable your Tx Module to connect to your local home network.

On your browser, refresh the http://elrs_tx.local/ and scroll towards the STM32 Firmware Update section, as shown below:

<figure markdown>
![STM32 Firmware Update](../../assets/images/STM32-updater.png)
</figure>

Drag-and-drop the `firmware.elrs` file created by the ExpressLRS Configurator into the Choose File field, or manually navigate to the Folder by clicking the Choose File button. You can also upload the `firmware.bin` file but change the offset to _0x4000_. Once the correct file is selected, click `Upload`` and Flash` STM32`. Wait for the process to complete, and the module will reboot (~1min). Using the [ExpressLRS Lua] script, verify that you have the latest version.

#### Method 2

These Tx Modules are STM32-based so they require a separate ESP "backpack" device for Wifi Flashing/Updating. 

Attach the module to your JR Bays and power it up. Connect to the `ESP Wifi Manager` Hotspot that the device will activate. Once connected, navigate to http://elrs_tx.local/.

<figure markdown>
![Wifi Manager](../../assets/images/WifiManager.png)
</figure>

Press `Configure WiFi` and set your home network SSID and password. This will enable your Tx Module to connect to your local home network.

Using the ExpressLRS Configurator, select the correct Target and set your [Firmware Options]. Click **Build and Flash** and wait for the compile process to complete. You should see a section as pictured below and the Success message marking the update process complete.

<figure markdown>
![Build & Flash]
</figure>

<figure markdown>
![Wifi Update Log](../../assets/images/WifiUpdateLog.png)
</figure>

Using the [ExpressLRS Lua] script, verify that you have the latest version.

### Flashing via OpenTX Radio

- Target: `NamimnoRC_Flash_2400_TX_via_WiFi`

- Device Category: `NamimnoRC FLASH 2.4 GHz`

- Device: `NamimnoRC FLASH 2400 TX`

<figure markdown>
![via WiFi](../../assets/images/Method_TX_WiFi-stm.png)
<figcaption>Flashing via WiFi</figcaption>
</figure>

With the correct target selected and [Firmware Options] set, **Build** your firmware using the ExpressLRS Configurator.

<figure markdown>
![Build]
</figure>

Once it's done, it should open the Target folder for you where the `NamimnoRC_Flash_2400_TX-<version>.elrs` file is. Do not close this window so you can easily locate the correct file to copy to your Radio's SD Card.

Copy the `NamimnoRC_Flash_2400_TX-<version>.elrs` file into your radio's SD Card `/FIRMWARE` folder.

Once copied, navigate to the `/FIRMWARE` Folder on your Radio and select/highlight the `NamimnoRC_Flash_2400_TX-<version>.elrs` file, long-press the Enter key and select `Flash external ELRS`. Flashing will then commence and after a few seconds, the radio should show a `Flash Successful` message and you're done!

Using the [ExpressLRS Lua] script, verify that you have the latest version.

### Flashing via STLink

- Target: `NamimnoRC_Flash_2400_TX_via_STLINK`

- Device Category: `NamimnoRC FLASH 2.4 GHz`

- Device: `NamimnoRC FLASH 2400 TX`

<figure markdown>
![via STLink](../../assets/images/Method_TX_STLink.png)
<figcaption>Flashing via STLink</figcaption>
</figure>

!!! attention 
    Only use this method if the firmware has been corrupted.

Begin by disassembling the module by unscrewing the 4 screws at the rear of the module with a 1.5mm hex wrench. Carefully separate the parts of the module and detach the cable from the main PCB.

<figure markdown>
<img class="center-img" src="https://github.com/ExpressLRS/ExpressLRS-Hardware/blob/master/img/namimnoback.jpg?raw=true" width="30%">
</figure>

<figure markdown>
<img class="center-img" src="https://github.com/ExpressLRS/ExpressLRS-Hardware/blob/master/img/cable.jpg?raw=true" width="30%">
</figure>

Wire your `STLink v2` to the module's pins as shown below:

<figure markdown>
<img class="center-img" src="https://github.com/ExpressLRS/ExpressLRS-Hardware/blob/master/img/namimnopinout.png?raw=true" width="40%">
</figure>

With the module connected shown above, and your configuration set, hit **Build & Flash** in the ExpressLRS Configurator and wait for the process to finish.

<figure markdown>
![Build & Flash]
</figure>

Once that's done, and the Success Message showing, you can now remove/unsolder the STLink, re-assemble the module, and put it into your Radio's Module Bay. If the Radio has CRSF selected, the light should turn green meaning the module has communication with your radio.

Verification can be done using the [ExpressLRS Lua] script. It should show the Version Number and Hash at the bottom, as well as the options you can set. If it's showing "Loading" at the top, check if External Module is set to CRSF for the selected model in your radio, and that the internal RF module is set to off. See the [General Troubleshooting] section for other ways to determine whether your module is flashed and ready for flying.

[ExpressLRS Lua script]: https://github.com/ExpressLRS/ExpressLRS/blob/3.x.x-maintenance/src/lua/elrsV3.lua?raw=true
[Build]: ../../assets/images/Build.png
[Build & Flash]: ../../assets/images/BuildFlash.png
[Firmware Options]: ../firmware-options.md
[Radio Preparation]: tx-prep.md
[ExpressLRS Lua]: lua-howto.md
[General Troubleshooting]: ../troubleshooting.md#general-troubleshooting
