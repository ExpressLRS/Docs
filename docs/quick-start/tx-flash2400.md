---
template: main.html
---

![Setup-Banner](https://raw.githubusercontent.com/ExpressLRS/ExpressLRS-hardware/master/img/quick-start.png)

## Flashing via Wifi

Target: `NamimnoRC_Flash_2400_TX_via_WiFi`

### Method 1

With the correct target selected and [Firmware Options](../../quick-start/firmware-options) set, **Build** your firmware using the ExpressLRS Configurator. Once it's done, it should open the Target folder for you where the `firmware.elrs` file is. Do not close this window so you can easily locate the correct file to upload to the module.

These Tx Modules are STM32-based so they require a separate ESP "backpack" device for Wifi Flashing/Updating. 

Attach the module to your JR Bays and power it up. Connect to the `ESP Wifi Manager` Hotspot that the device will activate. Once connected, navigate to http://elrs_tx.local/.

![Wifi Manager](../assets/images/WifiManager.png)

Press `Configure WiFi` and set your home network SSID and password. This will enable your Tx Module to connect to your local home network.

On your browser, refresh the http://elrs_tx.local/ and scroll towards the STM32 Firmware Update section, as shown below:

![STM32 Firmware Update](../assets/images/STM32-updater.png)

Drag-and-drop the `firmware.elrs` file created by the ExpressLRS Configurator into the Choose File field, or manually navigate to the Folder by clicking the Choose File button. You can also upload the `firmware.bin` file but change the offset to *0x4000*.Once the correct file is selected, click the `Upload and Flash STM32`. Wait for the process to complete, and the module will reboot (~1min). Using the [ExpressLRS lua](../../quick-start/lua-howto/) script, verify that you have the latest version.

### Method 2

These Tx Modules are STM32-based so they require a separate ESP "backpack" device for Wifi Flashing/Updating. 

Attach the module to your JR Bays and power it up. Connect to the `ESP Wifi Manager` Hotspot that the device will activate. Once connected, navigate to http://elrs_tx.local/.

![Wifi Manager](../assets/images/WifiManager.png)

Press `Configure WiFi` and set your home network SSID and password. This will enable your Tx Module to connect to your local home network.

Using the ExpressLRS Configurator, select the correct Target and set your [Firmware Options](../../quick-start/firmware-options). Click **Build and Flash** and wait for the compile process to complete. You should see a section as pictured below and the Success message marking the update process complete.

![Wifi Update Log](../assets/images/WifiUpdateLog.png)

Using the [ExpressLRS lua](../../quick-start/lua-howto/) script, verify that you have the latest version.

## Flashing via OpenTX Radio

*Note: The `NamimnoRC_Flash_2400_TX_via_WiFi` Target will work for this method too!*

With the correct target selected and [Firmware Options](../../quick-start/firmware-options) set, **Build** your firmware using the ExpressLRS Configurator. Once it's done, it should open the Target folder for you where the `NamimnoRC_Flash_2400_TX-<version>.elrs` file is. Do not close this window so you can easily locate the correct file to copy to your Radio SD Card.

Copy the `NamimnoRC_Flash_2400_TX-<version>.elrs` file into your radio's SD Card `/FIRMWARE` folder.

Once copied, navigate to the `/FIRMWARE` Folder on your Radio and select/highlight the `NamimnoRC_Flash_2400_TX-<version>.elrs` file, long-press the Enter key and select `Flash external ELRS`. Flashing will then commence and after a few seconds, radio should show a `Flash Successful` message and you're done!

Using the [ExpressLRS lua](../../quick-start/lua-howto/) script, verify that you have the latest version.

## Flashing via STLink

Target: `NamimnoRC_Flash_2400_TX_via_STLINK`

**ONLY USE THIS METHOD IF THE FIRMWARE HAS BEEN CORRUPTED** 

Begin by disassembling the module by unscrewing the 4 screws at the rear of the module with a 1.5mm hex wrench. Carefully seperate the parts of the module and detach the cable from the main PCB.

<img src="https://github.com/ExpressLRS/ExpressLRS-Hardware/blob/master/img/namimnoback.jpg?raw=true" width="30%">
<img src="https://github.com/ExpressLRS/ExpressLRS-Hardware/blob/master/img/cable.jpg?raw=true" width="30%">

Wire your `STLink v2` to the module's pins as show below:

<img src="https://github.com/ExpressLRS/ExpressLRS-Hardware/blob/master/img/namimnopinout.png?raw=true" width="40%">

With the module connected shown above, and your configuration set, hit **Build & Flash** in the ExpressLRS Configurator and wait for the process to finish. Once that's done, and the Success Message showing, you can now remove/unsolder the STLink, and re-assemble the module, and put it into your Radio's Module Bay. If the Radio has CRSF selected, the light should turn green meaning the module has communication with your radio.

Verification can be done using the [ExpressLRS lua](../../quick-start/lua-howto/) script. It should show the Version Number and Hash at the bottom, as well as the options you can set. If it's showing "Loading" at the top, check if External Module is set to CRSF for the selected model in your radio, and that internal RF module is set to off. See [General Troubleshooting](../../quick-start/troubleshooting/#general-troubleshooting) section for other ways to determine your module is flashed and ready for flying.

## OLED-equipped

These newer devices are now using an ESP-based MCU compared to the first version. With this in mind, the Flashing method will differ slightly, and should now be the same as with other ESP-based Tx Modules.

## Flashing via WiFi

Target: `NamimnoRC_FLASH_2400_OLED_TX_via_WIFI`

### Method 1

With the correct target selected and [Firmware Options](../../quick-start/firmware-options) set, **Build** your firmware using the ExpressLRS Configurator. Once it's done, it should open the Target folder for you where the `NamimnoRC_FLASH_2400_OLED_TX-<version>.bin` file is. Do not close this window so you can easily locate the correct file to upload to the module.

The next steps will require the [ELRS Lua Script](https://github.com/ExpressLRS/ExpressLRS/blob/master/src/lua/ELRS.lua?raw=true) (right-click, save as). Download the ELRS.lua script and save it to your Radio's `/Scripts/Tools` folder. Insert/attach your module into your module bay and make sure it's not loose and there's proper connection with the radio. Execute the ELRS.lua script by pressing "System Menu" in your radio and then under Tools, select ELRS.lua.

![Lua Script](https://github.com/ExpressLRS/ExpressLRS-Hardware/raw/master/img/wiki-from-discord/lua1.jpeg)
![Lua Script T16](https://github.com/ExpressLRS/ExpressLRS-Hardware/raw/master/img/wiki-from-discord/lua2)

At first, it will show "Mismatch"; it's normal. Tap `Enter` once on your radio to "Force Use" the script. If it's showing a "Connecting" message, then recheck the connection of the module to your radio.

![Lua3](../assets/images/lua3.jpg)

Select "Wifi Update" from the lua script. The Lua script will instruct you to go to a specific Ip Address, but you have to first connect to the Wifi Hotspot it created. It will show up in your network as `ExpressLRS TX Module`, and the password is simply `expresslrs`.

Using your browser, navigate to the correct page (typically http://10.0.0.1/) and it should show an upload form (you will have to scroll down a bit). You can drag-and-drop the `NamimnoRC_FLASH_2400_OLED_TX-<version>.bin` file that the ExpressLRS Configurator created. You can also click the `Choose File` button and navigate to the folder where the firmware was created. Ensure that you have selected the correct firmware file and click `Update`.

Once the file is uploaded, the webserver should load a White page, with the message **Update Success! Rebooting...**

As it rebooted, the connection to the Webserver got terminated. Verify with the [ELRS.lua](../../quick-start/tx-prep/#troubleshooting-lua-script) script if you have successfully updated your module using the Git commit hash for the firmware version you have on the module.

**Update for version 2.0**

Once you have updated to firmware version 2.0 or newer, the Web Update page on the Hotspot will get a few updates of its own. It will get the Update progress bar, and a Popup will be shown for Success or Error messages. Additionally, you can configure Home Network SSID and Password if you chose not to use ExpressLRS Configurator to set them. Once these are set, you can use the two methods below.

![JoinNetwork](../assets/images/web-joinnetwork.png)

### Method 2

With the correct target selected and [Firmware Options](../../quick-start/firmware-options) set, **Build** your firmware using the ExpressLRS Configurator. Once it's done, it should open the Target folder for you where the `NamimnoRC_FLASH_2400_OLED_TX-<version>.bin` file is. Do not close this window so you can easily locate the correct file to upload to the module.

Using the [ELRS Lua Script](https://github.com/ExpressLRS/ExpressLRS/blob/master/src/lua/ELRS.lua?raw=true) (right-click, save as), select `Wifi Update` and if you have flashed your Tx Module with your Home WiFi Network details, it will connect to the network automatically.

Using your browser, navigate to http://elrs_tx.local and the WiFi Update page should show up. Scroll down towards the Firmware Update section, as shown below:

![Firmware Update](../assets/images/web-firmwareupdate.png)

Drag-and-drop the `NamimnoRC_FLASH_2400_OLED_TX-<version>.bin` file created by the ExpressLRS Configurator into the Choose File field, or manually navigate to the Folder by clicking the `Choose File` button. Once the correct file is selected, click the `Update`. Wait for the process to complete, and the module will reboot (~2-3min). Using the [ELRS.lua](../../quick-start/tx-prep/#troubleshooting-lua-script) script, verify that you have the latest version.

### Method 3

Using the [ELRS Lua Script](https://github.com/ExpressLRS/ExpressLRS/blob/master/src/lua/ELRS.lua?raw=true) (right-click, save as), select `Wifi Update` and if you have flashed your Tx Module with your Home WiFi Network details, it will connect to the network automatically.

Using the ExpressLRS Configurator, select the correct Target and set your [Firmware Options](../../quick-start/firmware-options). Click **Build and Flash** and wait for the compile process to complete. You should see a section as pictured below and the Success message marking the update process complete.

![Wifi Update Log](../assets/images/WifiUpdateLog.png)

Using the [ELRS.lua](../../quick-start/tx-prep/#troubleshooting-lua-script) script, verify that you have the latest version.

## Flashing via USB/UART

Target: `NamimnoRC_FLASH_2400_OLED_TX_via_UART`

Attach your USB cable into the module and your computer. [CP210x Drivers](https://www.silabs.com/developers/usb-to-uart-bridge-vcp-drivers) will have to be installed for this to work properly (Windows). Make sure your computer recognizes the module as a USB-to-UART Bridge device, otherwise, this method will not work.

Using the ExpressLRS Configurator with the correct Target selected and [options](../../quick-start/firmware-options) set, hit **Build & Flash**. Wait for the process to finish, and you should be greeted with the "Success" message.

Assemble the module back together and attach it to your radio module bay and verify with the [ELRS.lua](../../quick-start/tx-prep/#troubleshooting-lua-script) script if you have successfully updated your module using the Git commit hash for the firmware version you have on the module.
