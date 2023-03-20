---
template: main.html
---

![Setup-Banner](https://github.com/ExpressLRS/ExpressLRS-Hardware/raw/master/img/quick-start.png)

!!! danger "Advisory"
    If you are flashing/updating your TX module via WiFi for the first time from the factory firmware, or from an older firmware, to ExpressLRS 3.x firmware you will first need to flash it to version 2.5.2 then flash it with the [Repartitioner](https://github.com/ExpressLRS/repartitioner) binary [file](https://github.com/ExpressLRS/repartitioner/releases/download/1.0/repartitioner.bin) (right click, save as/save file as). Should it complain about Target Mismatch, just click `Flash Anyway`. Only then you can flash to 3.x firmware following method 1 or 2 from the WiFi Flashing Guide below.

    Joshua Bardwell has a video about it [here](https://www.youtube.com/watch?v=2kcRi1cHejM).

    You can update straight to 3.2.0 without repartitioner or going to 2.5.2 first if flashing via UART.

## Flashing via WiFi

- Target: `Jumper_AION_T-Pro_2400_TX_via_WIFI`

- Device Category: `Jumper 2.4 GHz`

- Device: `Jumper AION T-Pro 2400 TX`

<figure markdown>
![via WiFi](../../assets/images/Method_intTX_WiFi.png)
<figcaption>Flashing via WiFi</figcaption>
</figure>

### Method 1

With the correct target selected and [Firmware Options] set, **Build** your firmware using the ExpressLRS Configurator.

<figure markdown>
![Build]
</figure>

Once it's done, it should open the Target folder for you where the `Jumper_AION_T-Pro_2400_TX-<version>.bin` file is. Do not close this window so you can easily locate the correct file to upload to the module.

The next steps will require the [ExpressLRS Lua script] (right-click, save as). Download the ExpressLRS Lua script and save it to your Radio's `/Scripts/Tools` folder. Execute the ExpressLRS Lua script by pressing "System Menu" on your radio and then under Tools, select `ExpressLRS`.

<figure markdown>
![Lua Script](../../assets/images/lua1.jpg)
</figure>

Select **WiFi Connectivity** from the Lua script and then select **Enable WiFi**. Press OK once more to activate the WiFi on the Tx Module. Connect to the Access Point the module will create called `ExpressLRS TX`, with the password being `expresslrs`.

<figure markdown>
![Lua3](../../assets/images/lua/wifi-bw.png)
</figure>

<figure markdown>
![WiFi Hotspot](../../assets/images/WifiHotspotTX.png)
</figure>

Using your browser, navigate to the correct page (typically http://10.0.0.1/) and it should show an upload form (you will have to scroll down a bit). You can drag-and-drop the `Jumper_AION_T-Pro_2400_TX-<version>.bin` file that the ExpressLRS Configurator created. You can also click the `Choose File` button and navigate to the folder where the firmware was created. Ensure that you have selected the correct firmware file and click `Update`.

If a Popup appears warning you're flashing the wrong target, click `Flash Anyway`. These units came pre-flashed from the factory with an older Target before these specific targets are available. Once the file is uploaded, a pop-up confirmation will show up.

<figure markdown>
![Update Success](../../assets/images/web-firmwareupdateSuccess.png)
</figure>

Wait for the Lua script screen to close the "WiFi Running" screen and your module should be updated now.

Verify the version and hash in the main screen of the ExpressLRS Lua script (you will first need to close it and relaunch the script).

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

Once it's done, it should open the Target folder for you where the `Jumper_AION_T-Pro_2400_TX-<version>.bin` file is. Do not close this window so you can easily locate the correct file to upload to the module.

Using the [ExpressLRS Lua script] (right-click, save as), select `Wifi Connectivity` then choose `Enable WiFi` and if you have flashed your Tx Module with your Home WiFi Network details or have set it in the Join Network section of the Update Page, it will connect to the local network automatically.

Using your browser, navigate to http://elrs_tx.local and the WiFi Update page should show up. Scroll down towards the Firmware Update section, as shown below:

<figure markdown>
![Firmware Update](../../assets/images/web-firmwareupdate.png)
</figure>

Drag-and-drop the `Jumper_AION_T-Pro_2400_TX-<version>.bin` file created by the ExpressLRS Configurator into the Choose File field, or manually navigate to the Folder by clicking the `Choose File` button. Once the correct file is selected, click the `Update`. Wait for the process to complete, and once the file is uploaded, a pop-up confirmation will show up.

<figure markdown>
![Update Success](../../assets/images/web-firmwareupdateSuccess.png)
</figure>

Wait for the Lua script screen to close the "WiFi Running" screen and your module should be updated now.

Verify the version and hash in the main screen of the ExpressLRS Lua script (you will first need to close it and relaunch the script).

### Method 3

Using the [ExpressLRS Lua script] (right-click, save as), select `Wifi Connectivity` then choose `Enable WiFi` and if you have flashed your Tx Module with your Home WiFi Network details or have set it in the Join Network section of the Update Page, it will connect to the network automatically.

Using the ExpressLRS Configurator, select the correct Target and set your [Firmware Options]. Click **Build and Flash** and wait for the compile process to complete. You should see a section as pictured below and the Success message marking the update process complete.

<figure markdown>
![Build & Flash]
</figure>

<figure markdown>
![Wifi Update Log](../../assets/images/WifiUpdateLog.png)
</figure>

Wait for the Lua script screen to close the "WiFi Running" screen and your module should be updated now.

Verify the version and hash in the main screen of the ExpressLRS Lua script (you will first need to close it and relaunch the script).

## HELP! I think I bricked my internal module!

Okay, breathe. The module is recoverable.

You will need a couple of files:

1. An EdgeTX binary that allows you to use the USB port on the radio to reflash the module. Download it from [here](../../assets/recovery/tpro-ada778ee4.bin) (Right-click, Save-as) and save it into your Jumper T-Pro SD Card `/firmware` folder. **NOTE** if your radio is already updated to EdgeTX 2.7.0, this package is no longer needed.
2. A zip file with all the recovery scripts and firmwares. Download it from [here](../../assets/recovery/jumper-recover.zip) (Right-click, Save-as) and extract it into a folder on your hard drive. If you want your `Binding Phrase` and other [Firmware Options] set for you when you flash via this method, **Build** your `firmware.bin` file first via the ExpressLRS Configurator and replace the `firmware.bin` in this folder.

### Procedure

With the EdgeTX binary in your `/firmware` SD Card folder, reboot the radio into DFU/Bootloader mode. You can get to this mode by holding the trim switches inwards and pressing the power button. Release the button and trim switches and you should be in DFU/Bootloader mode. Write the firmware into the radio and reboot to ensure it got written. One way to check is to plug-in a USB cable and a new menu item should be available to you: USB Serial (Debug/VCP). You will need this menu item in the next steps.

Turn off the radio.

The next steps will require you to take the radio apart. You will need a small Philips screwdriver for this. 10 small Philips screws keep both halves of the radio together.

<figure markdown>
![tPro screws](../../assets/images/tpro_screws.jpg)
</figure>

!!! warning "Handle with Care"
    There are a couple of wires connecting the module to the main board of the radio, along with battery leads. Do not yank out the back cover of the radio from its front half. You can leave the battery in its cradle as you will need to power up the radio in the next steps.

Leave all the wiring intact, you will need a still-functional radio for the next steps!

Power up the radio and make sure the internal ExpressLRS module is the active one. Plug in a USB cable and select `USB Serial (Debug)` or `USB Serial (VCP)` as shown in the photo below. Windows users should check Device Manager and make sure your device is being detected as STMicroelectronics Virtual COM Port device. If not and you're seeing a bunch of Yellow Warning icons for the RadioMaster Serial Port, install the drivers from [here](https://www.st.com/en/development-tools/stsw-stm32102.html). Windows 10 users can use the `W7_x64` executable.

<figure markdown>
![tPro serial debug](../../assets/images/tpro_serialdebug.jpg)
</figure>

Open up the folder where you extracted the Recovery scripts.

Locate the Boot button in the Internal ExpressLRS module and Press and Hold it while you double-click the `recover.bat` script. Release the button when you see the `Features:` line appears.

<figure markdown>
![tPro boot](../../assets/images/tpro_BootButton.png)
</figure>

<figure markdown>
![tPro flashing](../../assets/images/tpro_successFlash.png)
</figure>

Wait for the process to finish. A `Hard resetting via RTS pin...` will show up once done and the script should terminate on its own.

Unplug the USB cable from the T-Pro and check with the Lua Script whether you have your Internal module back.

If you chose to use the `firmware.bin` file in the original Recovery zip file, it doesn't have your `Binding Phrase` and other [Firmware Options]. You will need to reflash the module via WiFi using the steps above.

Do not forget to reassemble the T-Pro. Let's hope you didn't lose a screw!

## Recovery Method via EdgeTX Passthrough

!!! note
    This could soon supersede the steps above. This method could also change slightly in the near future.

You'll need the following:

1. A piece of wire about 4" (10cm) in length.
2. An EdgeTX Build that gives the `USB Serial(Debug)` or `USB Serial (VCP)` option when a USB Data cable is connected. You can download it [here](../../assets/recovery/tpro-ada778ee4.bin) (Right-click, Save-as). **NOTE** if your radio is already updated to EdgeTX 2.7.0, this package is no longer needed.

### Procedure

With the EdgeTX binary in your `/firmware` SD Card folder, reboot the radio into DFU/Bootloader mode. You can get to this mode by holding the trim switches inwards and pressing the power button. Release the button and trim switches and you should be in DFU/Bootloader mode. Write the firmware into the radio and reboot to ensure it got written. One way to check is to plug in a USB cable and a new menu item should be available to you: USB Serial (Debug/VCP). You will need this menu item in the next steps.

Turn off the radio.

The next steps will require you to take the radio apart. You will need a small Philips screwdriver for this. 10 small Philips screws keep both halves of the radio together.

<figure markdown>
![tPro screws](../../assets/images/tpro_screws.jpg)
</figure>

!!! warning "Handle with Care"
    There are a couple of wires connecting the module to the main board of the radio, along with battery leads. Do not yank out the back cover of the radio from its front half. You don't need to disconnect the wires from the mainboard.

Once you have both halves of the radio apart, you will need to solder a piece of wire on the Boot pad into one of the momentary switches on the radio. Refer to the image below where to solder the ends of the wire.

<figure markdown>
![tPro janky boot](../../assets/images/tpro_bootOnSwitch.jpg)
</figure>

Once the wire is properly soldered, reassemble the radio. Tighten up the 10 screws to secure both halves of the radio. 

!!! note
    If you're planning to use the switch as an Aux channel, you might want to remove the wire afterward. Leaving this wire connected means the Aux channel will output a constant "High" signal.

Replace the battery if you removed it and power up the radio and make sure the internal ExpressLRS module is the active one. Plug in a USB cable and select `USB Serial (Debug)` or `USB Serial (VCP)` as shown in the photo below.

<figure markdown>
![tPro serial debug](../../assets/images/tpro_serialdebug.jpg)
</figure>

Windows users should check Device Manager and make sure your device is being detected as STMicroelectronics Virtual COM Port device. 

<figure markdown>
![Device Manager](../../assets/images/DeviceMngr.png)
</figure>

If not and you're seeing a bunch of Yellow Warning icons for the Jumper T-Pro Serial Port, install the drivers from [here](https://www.st.com/en/development-tools/stsw-stm32102.html). Windows 10 users can use the `VCP_V1.5.0_Setup_W7_x64_64bits` executable.

On the ExpressLRS Configurator, select the correct Device Type and Device (`Jumper AION T-Pro 2400 TX`) and choose the `EdgeTXPassthrough` flashing method. Set your [Firmware Options] and click **Build and Flash**.

<figure markdown>
![via EdgeTX Passthrough](../../assets/images/Method_intTX_EdgeTXPassthrough.png)
<figcaption>Flashing via EdgeTXPassthrough</figcaption>
</figure>

Wait for the Passthrough Init or Passthrough Done section of the log and Press the switch in the radio where you wired up the boot button and hold it until the script has connected. See the image below for the correct timing.

<figure markdown>
![tPro press it](../../assets/images/tpro_viaETXPress.png)
</figure>

If you didn't get it right and it fails, don't worry. Just retry and it should go through.

<figure markdown>
![tPro flashed](../../assets/images/tpro_viaETXSuccess.png)
</figure>

Unplug the USB and check via the ExpressLRS Lua script your module is flashed and working properly again.

## Recovery Method via FTDI or USB to Serial Adapter

You need an FTDI dongle or a USB to Serial Adapter for this method. Make sure the Serial Adapter has its drivers installed and is being recognized by your Computer properly.

You will also have to take apart the radio to get to the module connections and the boot button.

### Procedure

Make sure your radio is turned off, and the battery removed. You won't need to power up the radio with this method.

Take off the back cover of the radio by loosening 10 small Philips screws. Don't lose one!

<figure markdown>
![tPro screws](../../assets/images/tpro_screws.jpg)
</figure>

!!! warning "Handle with Care"
    There are a couple of wires connecting the module to the main board of the radio, along with battery leads. Do not yank out the back cover of the radio from its front half. You don't need to disconnect the wires from the mainboard, but if you do so, be very careful!

What you need is just the 4 wires connecting the ExpressLRS internal module to the Module daughterboard. The pin-out is as follows: White wire is the RX, Yellow wire is the TX, Red wire is the 5v pin, and the Black wire is the Gnd pin.

<figure markdown>
![tPro duplex](../../assets/images/tproUART.jpg)
</figure>

Connect these 4 wires into your FTDI dongle or a USB to Serial Adapter as follows: RX pin into the TX pin; TX pin into the RX pin; 5v to 5v and Gnd to Gnd.

<figure markdown>
![tPro on Serial](../../assets/images/tproUART-USB.jpg)
</figure>

Before you connect the FTDI dongle/Serial Adapter to the USB port of your Computer, hold down the Boot button. Keep the button pressed until you have connected the Serial Adapter to your USB port. 

On the ExpressLRS Configurator, select the `via UART` Flashing method. Set your [Firmware Options] and click **Build and Flash** then wait for the process to complete.

<figure markdown>
![via UART](../../assets/images/Method_intTX_UART.png)
<figcaption>Flashing via UART</figcaption>
</figure>

Incorrect or loose connections can cause this method to fail. If it does, disconnect the Serial Adapter from the USB, ensure you have the right connection and repeat the process. Don't forget to press and hold the boot button before connecting the Serial Adapter to the USB. 

Once complete and a `Success` banner appears, carefully unplug the Serial Adapter and disconnect the module pins. Reinsert the connector into the module port as shown below.

<figure markdown>
![tPro Connection](../../assets/images/tproUART-AllSet.jpg)
</figure>

Reassemble the radio (but do not put in the screws yet) and verify you have a working module once again by running the Lua script.

Once you've verified you have your Internal ExpressLRS module back, replace the screws and tighten things up. Chug one down and celebrate!

[ExpressLRS Lua script]: https://github.com/ExpressLRS/ExpressLRS/blob/3.x.x-maintenance/src/lua/elrsV3.lua?raw=true
[Build]: ../../assets/images/Build.png
[Build & Flash]: ../../assets/images/BuildFlash.png
[Firmware Options]: ../firmware-options.md
