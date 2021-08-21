---
template: main.html
---

![Setup-Banner](https://raw.githubusercontent.com/ExpressLRS/ExpressLRS-hardware/master/img/quick-start.png)

## Flashing via Wifi

Target: `NamimnoRC_Voyager_900_TX_via_WiFi`

### Method 1

With the correct target selected and [Firmware Options](/quick-start/firmware-options) set, **Build** your firmware using the ExpressLRS Configurator. Once it's done, it should open the Target folder for you where the `firmware.bin` file is. Do not close this window so you can easily locate the correct file to upload to the module.

These Tx Modules are STM32-based so they require a separate ESP "backpack" device for Wifi Flashing/Updating. The `Wifi Update` option in the ExpressLRS Lua script will not work with these devices. The steps that follow will be used instead.

Attach the module to your JR Bays and power it up. Connect to the `ESP Wifi Manager` Hotspot that the device will activate. Once connected, navigate to http://elrs_tx.local/ (IP: 192.168.4.1). 

![Wifi Manager](../assets/images/WifiManager.png)

Press `Configure WiFi` and set your home network SSID and password. This will enable your Tx Module to connect to your local home network.

On your browser, refresh the http://elrs_tx.local/ and scroll towards the STM32 Firmware Update section, as shown below:

![STM32 Firmware Update](../assets/images/STM32-updater.png)

Drag-and-drop the `firmware.bin` file created by the ExpressLRS Configurator into the Choose File field, or manually navigate to the Folder by clicking the Choose File button. Once the correct file is selected, click the `Upload and Flash STM32`. Wait for the process to complete, and the module will reboot (~2-3min). Using the [ELRS.lua](/quick-start/tx-prep/#troubleshooting-lua-script) script, verify that you have the latest version.

### Method 2

These Tx Modules are STM32-based so they require a separate ESP "backpack" device for Wifi Flashing/Updating. The `Wifi Update` option in the ExpressLRS Lua script will not work with these devices. The steps that follow will be used instead.

Attach the module to your JR Bays and power it up. Connect to the `ESP Wifi Manager` Hotspot that the device will activate. Once connected, navigate to http://elrs_tx.local/ (IP: 192.168.4.1). 

![Wifi Manager](../assets/images/WifiManager.png)

Press `Configure WiFi` and set your home network SSID and password. This will enable your Tx Module to connect to your local home network.

Using the ExpressLRS Configurator, select the correct Target and set your [Firmware Options](/quick-start/firmware-options). Click **Build and Flash** and wait for the compile process to complete. You should see a section as pictured below and the Success message marking the update process complete.

![Wifi Update Log](../assets/images/WifiUpdateLog.png)

Using the [ELRS.lua](/quick-start/tx-prep/#troubleshooting-lua-script) script, verify that you have the latest version.

## Flashing via OpenTX Radio

*Note: The `NamimnoRC_Flash_2400_TX_via_WiFi` Target will work for this method too!*

With the correct target selected and [Firmware Options](/quick-start/firmware-options) set, **Build** your firmware using the ExpressLRS Configurator. Once it's done, it should open the Target folder for you where the `firmware.elrs` file is. Do not close this window so you can easily locate the correct file to upload to the module.

Copy the `firmware.elrs` file into your radio's SD Card `/FIRMWARE` folder.

Once copied, navigate to the `/FIRMWARE` Folder on your Radio and select/highlight the `firmware.elrs` file, long-press the Enter key and select `Flash external ELRS`. Radio should show a `Flash Successful` message and you're done!

Using the [ELRS.lua](/quick-start/tx-prep/#troubleshooting-lua-script) script, verify that you have the latest version.

## Flashing via STLink

Target: `NamimnoRC_Voyager_900_TX_via_STLINK`

**ONLY USE THIS METHOD IF THE FIRMWARE HAS BEEN CORRUPTED** 

Begin by disassembling the module by unscrewing the 4 screws at the rear of the module with a 1.5mm hex wrench. Carefully seperate the parts of the module and detach the cable from the main PCB.

<img src="https://github.com/ExpressLRS/ExpressLRS-Hardware/blob/master/img/namimnoback.jpg?raw=true" width="30%">
<img src="https://github.com/ExpressLRS/ExpressLRS-Hardware/blob/master/img/cable.jpg?raw=true" width="30%">

Wire your `STLink v2` to the module's pins as show below:

<img src="https://github.com/ExpressLRS/ExpressLRS-Hardware/blob/master/img/namimnopinout.png?raw=true" width="40%">

With the module connected shown above, and your configuration set, hit **Build & Flash** in the ExpressLRS Configurator and wait for the process to finish. Once that's done, and the Success Message showing, you can now remove/unsolder the STLink, and re-assemble the module, and put it into your Radio's Module Bay. If the Radio has CRSF selected, the light should turn green meaning the module has communication with your radio.

Verification can be done using the ELRS.lua script. It should show the Version Hash at the top, as well as the options you can set. If it's showing "Connecting", check if External Module is set to CRSF for the selected model in your radio, and that internal RF module is set to off. See general Troubleshooting section for other ways to determine your module is flashed and ready for flying.