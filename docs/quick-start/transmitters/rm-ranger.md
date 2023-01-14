---
template: main.html
---

![Setup-Banner](https://raw.githubusercontent.com/ExpressLRS/ExpressLRS-hardware/master/img/quick-start.png)

!!! Info
    These devices come pre-installed with a 3.x-ready firmware. You don't need to reflash these devices. You can use the Web UI of these devices to update the Binding Phrase or any of the firmware options.

## Flashing via WiFi

- Target:
    - `RadioMaster_Ranger_2400_TX_via_WIFI`
    - `RadioMaster_Ranger_Micro_2400_TX_via_WIFI`
    - `RadioMaster_Ranger_Nano_2400_TX_via_WIFI`

- Device Category: `Radiomaster 2.4 GHz`

- Device: 
    - `RadioMaster Ranger 2400 TX`
    - `RadioMaster Ranger Micro 2400 TX`
    - `RadioMaster Ranger Nano 2400 TX`


<figure markdown>
![via WiFi](../../assets/images/Method_TX_WiFi.png)
<figcaption>Flashing via WiFi</figcaption>
</figure>

### Method 1

With the correct target selected and [Firmware Options] set, **Build** your firmware using the ExpressLRS Configurator.

<figure markdown>
![Build]
</figure>

Once it's done, it should open the Target folder for you where the `RadioMaster_Ranger_2400_TX-<version>.bin`, `RadioMaster_Ranger_Micro_2400_TX-<version>.bin` or `RadioMaster_Ranger_Nano_2400_TX-<version>.bin` file is. Do not close this window so you can easily locate the correct file to upload to the module.

The next steps will require the [ExpressLRS Lua script] (right-click, save as). Download the ExpressLRS Lua script and save it to your Radio's `/Scripts/Tools` folder. Insert/attach your module into your module bay and make sure it's not loose and there's a proper connection with the radio (see the [Radio Preparation] page). Execute the ExpressLRS Lua script by pressing "System Menu" on your radio and then under Tools, select `ExpressLRS`.

<figure markdown>
![Lua Script](../../assets/images/lua1.jpg)
</figure>

<figure markdown>
![Lua Script T16](../../assets/images/lua2.jpg)
</figure>

If the script is stuck at `Loading...`, then there's a chance your Radio External RF module is not set to CRSF or that your module is not well-connected to the module bay pins.

<figure markdown>
![Lua3](../../assets/images/lua3.jpg)
</figure>

Select **WiFi Connectivity** from the Lua script and then select **Enable WiFi**. Press OK once more to activate the WiFi on the Tx Module. Connect to the Access Point the module will create called `ExpressLRS TX`, with the password being `expresslrs`.

<figure markdown>
![WiFi Hotspot](../../assets/images/WifiHotspotTX.png)
</figure>

Using your browser, navigate to the correct page (typically http://10.0.0.1/) and it should show the Web UI. Navigate to the `Update` Tab and you should see a File Upload form. You can now drag-and-drop the `RadioMaster_Ranger_2400_TX-<version>.bin`, `RadioMaster_Ranger_Micro_2400_TX-<version>.bin` or `RadioMaster_Ranger_Nano_2400_TX-<version>.bin` file that the ExpressLRS Configurator created into the File Upload field. You can also click the `Choose File` button and navigate to the folder where the firmware was created. Ensure that you have selected the correct firmware file and click `Update`.

Once the file is uploaded, a pop-up confirmation will show up. Wait for the Lua script screen to close the "WiFi Running" screen and your module should be updated now.

Verify the version and hash in the main screen of the ExpressLRS Lua script.

**Join Local Network**

You can configure Home Network SSID and Password if you chose not to use ExpressLRS Configurator to set them. Once these are set, you can use the next two methods below.

<figure markdown>
![JoinNetwork](../../assets/images/web-joinnetwork.png)
</figure>

### Method 2

With the correct target selected and [Firmware Options] set, **Build** your firmware using the ExpressLRS Configurator.

<figure markdown>
![Build]
</figure>

Once it's done, it should open the Target folder for you where the `RadioMaster_Ranger_2400_TX-<version>.bin`, `RadioMaster_Ranger_Micro_2400_TX-<version>.bin` or `RadioMaster_Ranger_Nano_2400_TX-<version>.bin` file is. Do not close this window so you can easily locate the correct file to upload to the module.

Using the [ExpressLRS Lua script] (right-click, save as), select `Wifi Connectivity` then choose `Enable WiFi` and if you have flashed your Tx Module with your Home WiFi Network details or have set it in the Join Network section of the Update Page, it will connect to the local network automatically.

Using your browser, navigate to http://elrs_tx.local and the WiFi Update page should show up. Navigate to the `Update` Tab and you should see a File Upload form. You can now drag-and-drop the `RadioMaster_Ranger_2400_TX-<version>.bin`, `RadioMaster_Ranger_Micro_2400_TX-<version>.bin` or `RadioMaster_Ranger_Nano_2400_TX-<version>.bin` file that the ExpressLRS Configurator created into the Choose File field, or manually navigate to the Folder by clicking the `Choose File` button. Once the correct file is selected, click the `Update`. 

Once the file is uploaded, a pop-up confirmation will show up. Wait for the Lua script screen to close the "WiFi Running" screen and your module should be updated now.

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

- Target:
    - `RadioMaster_Ranger_2400_TX_via_UART`
    - `RadioMaster_Ranger_Micro_2400_TX_via_UART`
    - `RadioMaster_Ranger_Nano_2400_TX_via_UART`

- Device Category: `Radiomaster 2.4 GHz`

- Device: 
    - `RadioMaster Ranger 2400 TX`
    - `RadioMaster Ranger Micro 2400 TX`
    - `RadioMaster Ranger Nano 2400 TX`

<figure markdown>
![via UART](../../assets/images/Method_TX_UART.png)
<figcaption>Flashing via UART</figcaption>
</figure>

Attach a USB-C Data Cable to your module and Computer. Windows users might have to install [CP210x Windows Drivers](https://www.silabs.com/developers/usb-to-uart-bridge-vcp-drivers) to ensure the device is properly detected and initialized.

!!! tip "Important"
    Check Device Manager on your Windows system before proceeding. Ensure the correct drivers are installed. Some Linux distros might also need drivers. The drivers can be downloaded [here](https://www.silabs.com/developers/usb-to-uart-bridge-vcp-drivers).

<figure markdown>
![CP210x Drivers](../../assets/images/CP210xDriverDownload.png)
</figure>

Using the ExpressLRS Configurator with the correct Target selected and [Firmware Options] set, hit **Build & Flash**. Wait for the process to finish, and you should be greeted with the "Success" message.

<figure markdown>
![Build & Flash]
</figure>

Verify the version and hash in the main screen of the ExpressLRS Lua script.

[ExpressLRS Lua script]: https://github.com/ExpressLRS/ExpressLRS/blob/3.x.x-maintenance/src/lua/elrsV3.lua?raw=true
[Build]: ../../assets/images/Build.png
[Build & Flash]: ../../assets/images/BuildFlash.png
[Firmware Options]: ../firmware-options.md
