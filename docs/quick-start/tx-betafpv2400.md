---
template: main.html
---

![Setup-Banner](https://raw.githubusercontent.com/ExpressLRS/ExpressLRS-hardware/master/img/quick-start.png)

## Flashing via Wifi

Target: `BETAFPV_2400_TX_via_WIFI`

### Method 1

With the correct target selected and [Firmware Options](../../quick-start/firmware-options) set, **Build** your firmware using the ExpressLRS Configurator. Once it's done, it should open the Target folder for you where the `firmware.bin` file is. Do not close this window so you can easily locate the correct file to upload to the module.

The next steps will require the [ELRS Lua Script](https://github.com/ExpressLRS/ExpressLRS/blob/master/src/lua/ELRS.lua?raw=true) (right-click, save as). Download the ELRS.lua script and save it to your Radio's `/Scripts/Tools` folder. Insert/attach your module into your module bay and make sure it's not loose and there's proper connection with the radio. Execute the ELRS.lua script by pressing "System Menu" in your radio and then under Tools, select ELRS.lua.

![Lua Script](https://github.com/ExpressLRS/ExpressLRS-Hardware/raw/master/img/wiki-from-discord/lua1.jpeg)
![Lua Script T16](https://github.com/ExpressLRS/ExpressLRS-Hardware/raw/master/img/wiki-from-discord/lua2)

At first, it will show "Mismatch"; it's normal. Tap `Enter` once on your radio to "Force Use" the script. If it's showing a "Connecting" message, then recheck the connection of the module to your radio.

![Lua3](../assets/images/lua3.jpg)

Select **Wifi Update** from the lua script. The Lua script will instruct you to go to a specific Ip Address, but you have to first connect to the Wifi Hotspot it created. It will show up in your network as `ExpressLRS TX Module`, and the password is simply `expresslrs`.

Using your browser, navigate to the correct page (typically http://10.0.0.1/) and it should show an upload form (you will have to scroll down a bit). You can drag-and-drop the `BETAFPV_2400_TX-<version>.bin` file that the ExpressLRS Configurator created. You can also click the `Choose File` button and navigate to the folder where the firmware was created. Ensure that you have selected the correct firmware file and click `Update`.

Once the file is uploaded, the webserver should load a White page, with the message **Update Success! Rebooting...**

As it rebooted, the connection to the Webserver got terminated. Verify with the [ELRS.lua](../../quick-start/tx-prep/#troubleshooting-lua-script) script if you have successfully updated your module using the Git commit hash for the firmware version you have on the module.

**Update for version 1.1.0**

Once you have updated to firmware version 1.1.0 or newer, the Web Update page on the Hotspot will get a few updates of its own. It will get the Update progress bar, and a Popup will be shown for Success or Error messages. Additionally, you can configure Home Network SSID and Password if you chose not to use ExpressLRS Configurator to set them. Once these are set, you can use the two methods below.

![JoinNetwork](../assets/images/web-joinnetwork.png)

### Method 2

With the correct target selected and [Firmware Options](../../quick-start/firmware-options) set, **Build** your firmware using the ExpressLRS Configurator. Once it's done, it should open the Target folder for you where the `BETAFPV_2400_TX-<version>` file is. Do not close this window so you can easily locate the correct file to upload to the module.

Using the [ELRS Lua Script](https://github.com/ExpressLRS/ExpressLRS/blob/master/src/lua/ELRS.lua?raw=true) (right-click, save as), select `Wifi Update` and if you have flashed your Tx Module with your Home WiFi Network details, it will connect to the network automatically.

Using your browser, navigate to http://elrs_tx.local and the WiFi Update page should show up. Scroll down towards the Firmware Update section, as shown below:

![Firmware Update](../assets/images/web-firmwareupdate.png)

Drag-and-drop the `BETAFPV_2400_TX-<version>` file created by the ExpressLRS Configurator into the Choose File field, or manually navigate to the Folder by clicking the `Choose File` button. Once the correct file is selected, click the `Update`. Wait for the process to complete, and the module will reboot (~2-3min). Using the [ELRS.lua](../../quick-start/tx-prep/#troubleshooting-lua-script) script, verify that you have the latest version.

### Method 3

Using the [ELRS Lua Script](https://github.com/ExpressLRS/ExpressLRS/blob/master/src/lua/ELRS.lua?raw=true) (right-click, save as), select `Wifi Update` and if you have flashed your Tx Module with your Home WiFi Network details, it will connect to the network automatically.

Using the ExpressLRS Configurator, select the correct Target and set your [Firmware Options](../../quick-start/firmware-options). Click **Build and Flash** and wait for the compile process to complete. You should see a section as pictured below and the Success message marking the update process complete.

![Wifi Update Log](../assets/images/WifiUpdateLog.png)

Using the [ELRS.lua](../../quick-start/tx-prep/#troubleshooting-lua-script) script, verify that you have the latest version.

## Flashing via USB/UART

Target: `BETAFPV_2400_TX_via_UART`

Attach a USB Data Cable to your module and Computer. Windows users might have to install [CP210x Drivers](https://www.silabs.com/developers/usb-to-uart-bridge-vcp-drivers) to ensure the device is properly detected and initialized.

Using the ExpressLRS Configurator with the correct Target selected and [Firmware Options](../../quick-start/firmware-options) set, hit **Build & Flash**. Wait for the process to finish, and you should be greeted with the "Success" message.

Verify with the [ELRS.lua](../../quick-start/tx-prep/#troubleshooting-lua-script) script if you have successfully updated your module using the Git commit hash for the firmware version you have on the module.

## Can't flash?

If you've followed any of the steps above and still can't get your devices flashed and updated, see this video for the explanation why and the fix to get your devices flashed and updated.

<iframe width="688" height="387" src="https://www.youtube.com/embed/Pt5rMp7Zs8s" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>