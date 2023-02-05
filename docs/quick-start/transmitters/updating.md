---
template: main.html
description: General Guidelines for ExpressLRS TX module firmware updating.
---

![Setup-Banner](https://raw.githubusercontent.com/ExpressLRS/ExpressLRS-hardware/master/img/quick-start.png)

## ESP-based TX Module Updating Methods

=== "via WiFi"

    <figure markdown>
    ![via WiFi](../../assets/images/Method_TX_WiFi.png)
    </figure>

    === "Manual Upload via AP"

        !!! Info "Heads up!"
            This option is only possible if you haven't previously flashed or configured your TX Module with your Home WiFi SSID and Password or it's unable to connect to said WiFi Network because the router is Off or unreachable.

        1. Launch the [ExpressLRS Configurator](../installing-configurator.md) on your Computer.
            - Make sure Official Releases is active from the horizontal tab.
            - Make sure you have selected the Released version you want to flash into your TX module.
        2. Select the Device Category and Device target matching your hardware.
        3. Set the [firmware options](../firmware-options.md) for your device.
            - Regulatory Domain (choose the domain appropriate for the location or country you're flying).
            - Binding Phrase (take note of this phrase as this should be the same on your other devices or they will not bind or sync).
            - Local WiFi Network Credentials (will be used the next time the device goes into WiFi mode).
        4. Click the ++"Build"++ button.
            
            <figure markdown>
            ![Build](../../assets/images/Build.png)
            </figure>
            
        5. Once the Build process is done, a Temp folder window should popup containing your firmware binaries.
            - You can use any of these files.
            - Do not close this Temp folder unless you have already copied the firmware file somewhere safe, like into your smartphone folder if you're planning to use your smartphone to upload the file in the next steps.
            - the firmware file named with the format `<device target name> + <version>.bin` is best used if you'll be moving these firmware files into one folder, so you know what firmware version it is and for which device it is.
        6. On your Radio, press the ++"SYS"++ Key to display the Tools Menu where Lua Scripts can be found.
        7. Scroll down and select `ExpressLRS` Lua Script.
            - If the script is nowhere to be found, download it from [this page](../transmitters/lua-howto.md) and save it into your Radio SD Card Scripts/Tools/ folder.
        8. Press ++enter++ to Load it.
            - If the script is stuck on a "Loading..." screen, go back to the [Radio Preparation](../transmitters/tx-prep.md) Page and make sure you have configured your radio properly for ExpressLRS use.
        9. Scroll down and select `Wifi Connectivity` and press ++enter++.
        10. Select `Enable WiFi` and press ++enter++.
        11. The `WiFi Running` screen will show up. Your TX module is now in WiFi mode.
            - If the Script stopped and is showing a Syntax Error, do not worry. The module is still in WiFi mode. The Syntax Error could be because you're on an older radio, older EdgeTX/OpenTX firmware or both. It could also be due to the fact your TX module is on an earlier firmware version and you're using a more recent Lua Script.

        12. Using a WiFi-capable device such as your smartphone or laptop, scan for the `ExpressLRS TX` Access Point. Connect to this Access Point.

            ![WiFi Hotspot](../../assets/images/WifiHotspotTX.png){ align=right }

            - If your TX Module is previously flashed with your Home WiFi SSID and Password, and it is able to connect to that WiFi Network, then the Access Point will not show up.
            - `expresslrs` is the Password for this Access Point.

            <br clear="right" />

        13. Once you have connected to the `ExpressLRS TX` Access Point, open up a Browser window and type in the IP Address `10.0.0.1` on the Address Bar and press ++enter++. The ExpressLRS Web UI will load.
        14. Activate the `Update` Tab.
        15. Drag-and-drop the Firmware file from the Temp folder into the File Upload field.
            - You can also use the Browse or Choose File button and browse for the file yourself, specially if you've copied it somewhere else on an earlier step.
        16. Click the ++"Update"++ button to start the Updating procedure.
        17. Wait for the firmware file to get uploaded and flashed into your device. It would only take a minute or two and you will see the Success Popup Message.
        18. On your Radio, the `WiFi Running` screen should disappear and it should be back to the WiFi Connectivity Menu of the ExpressLRS Lua Script.
        19. Long-press the ++"RTN"++ Key to exit the ExpressLRS Lua Script. Reload it to check for the ExpressLRS Firmware version and verify your TX module has been updated.

    === "Manual Upload via Local WiFi"

        !!! Info "Heads up!"
            This option is only possible if you have previously flashed or configured your TX Module with your Home WiFi SSID and Password and it's able to connect to said WiFi Network.

        1. Launch the [ExpressLRS Configurator](../installing-configurator.md) on your Computer.
            - Make sure Official Releases is active from the horizontal tab.
            - Make sure you have selected the Released version you want to flash into your TX module.
        2. Select the Device Category and Device target matching your hardware.
        3. Set the [firmware options](../firmware-options.md) for your device.
            - Regulatory Domain (choose the domain appropriate for the location or country you're flying).
            - Binding Phrase (take note of this phrase as this should be the same on your other devices or they will not bind or sync).
            - Local WiFi Network Credentials (will be used the next time the device goes into WiFi mode).
        4. Click the ++"Build"++ button.
            
            <figure markdown>
            ![Build](../../assets/images/Build.png)
            </figure>
            
        5. Once the Build process is done, a Temp folder window should popup containing your firmware binaries.
            - You can use any of these files.
            - Do not close this Temp folder unless you have already copied the firmware file somewhere safe, like into your smartphone folder if you're planning to use your smartphone to upload the file in the next steps.
            - the firmware file named with the format `<device target name> + <version>.bin` is best used if you'll be moving these firmware files into one folder, so you know what firmware version it is and for which device it is.
        6. On your Radio, press the ++"SYS"++ Key to display the Tools Menu where Lua Scripts can be found.
        7. Scroll down and select `ExpressLRS` Lua Script.
            - If the script is nowhere to be found, download it from [this page](../transmitters/lua-howto.md) and save it into your Radio SD Card Scripts/Tools/ folder.
        8. Press ++enter++ to Load it.
            - If the script is stuck on a "Loading..." screen, go back to the [Radio Preparation](../transmitters/tx-prep.md) Page and make sure you have configured your radio properly for ExpressLRS use.
        9. Scroll down and select `Wifi Connectivity` and press ++enter++.
        10. Select `Enable WiFi` and press ++enter++.
        11. The `WiFi Running` screen will show up. Your TX module is now in WiFi mode.
            - If the Script stopped and is showing a Syntax Error, do not worry. The module is still in WiFi mode. The Syntax Error could be because you're on an older radio, older EdgeTX/OpenTX firmware or both. It could also be due to the fact your TX module is on an earlier firmware version and you're using a more recent Lua Script.

        12. With your module now in WiFi Mode and it was able to connect to your Local WiFi Network, open a Browser window on any WiFi-capable device that is also connected to the same Local WiFi Network. Type in the Address http://elrs_tx.local on your browser's Address Bar. The ExpressLRS Web UI should load.
            - If your browser cannot resolve this address and it cannot load the ExpressLRS Web UI, this means that MDNS is not working on your device or network.

            ??? tip "Use the IP Address instead!"
                === "The `arp` Command"

                    1. Open up a Command Prompt window on your computer.
                    2. Execute the command `arp -a` which will list all the devices in the Network.
                    3. Use each of the IP Addresses marked as `Dynamic` as URL into your Browser until you get to the ExpressLRS Web UI.

                === "Router DHCP List"
                    1. Log in into your Router dashboard.
                    2. Check the DHCP List and look for the "elrs" device.
                    3. Take note of the IP Address given by your router.
                    4. Use this IP address into your Browser as the URL.

        13. Activate the `Update` Tab.
        14. Drag-and-drop the Firmware file from the Temp folder into the File Upload field.
            - You can also use the Browse or Choose File button and browse for the file yourself, specially if you've copied it somewhere else on an earlier step.
        15. Click the ++"Update"++ button to start the Updating procedure.
        16. Wait for the firmware file to get uploaded and flashed into your device. It would only take a minute or two and you will see the Success Popup Message.
        17. On your Radio, the `WiFi Running` screen should disappear and it should be back to the WiFi Connectivity Menu of the ExpressLRS Lua Script.
        18. Long-press the ++"RTN"++ Key to exit the ExpressLRS Lua Script. Reload it to check for the ExpressLRS Firmware version and verify your TX module has been updated.

    === "Auto Upload"

        !!! Info "Heads up!"
            This option is only possible if you have previously flashed or configured your TX Module with your Home WiFi SSID and Password and it's able to connect to said WiFi Network. 
            
            MDNS must also be working and that your browser can resolve the address http://elrs_tx.local and it can load the ExpressLRS Web UI from said address.

        1. On your Radio, press the ++"SYS"++ Key to display the Tools Menu where Lua Scripts can be found.
        2. Scroll down and select `ExpressLRS` Lua Script.
            - If the script is nowhere to be found, download it from [this page](../transmitters/lua-howto.md) and save it into your Radio SD Card Scripts/Tools/ folder.
        3. Press ++enter++ to Load it.
            - If the script is stuck on a "Loading..." screen, go back to the [Radio Preparation](../transmitters/tx-prep.md) Page and make sure you have configured your radio properly for ExpressLRS use.
        4. Scroll down and select `Wifi Connectivity` and press ++enter++.
        5. Select `Enable WiFi` and press ++enter++.
        6. The `WiFi Running` screen will show up. Your TX module is now in WiFi mode.
            - If the Script stopped and is showing a Syntax Error, do not worry. The module is still in WiFi mode. The Syntax Error could be because you're on an older radio, older EdgeTX/OpenTX firmware or both. It could also be due to the fact your TX module is on an earlier firmware version and you're using a more recent Lua Script.
        7. Launch the [ExpressLRS Configurator](../installing-configurator.md) on your Computer.
            - Make sure Official Releases is active from the horizontal tab.
            - Make sure you have selected the Released version you want to flash into your TX module.
        8. Select the Device Category and Device target matching your hardware.
        9. Set the [firmware options](../firmware-options.md) for your device.
            - Regulatory Domain (choose the domain appropriate for the location or country you're flying).
            - Binding Phrase (take note of this phrase as this should be the same on your other devices or they will not bind or sync).
            - Local WiFi Network Credentials (will be used the next time the device goes into WiFi mode).
        10. Click the ++"Build & Flash"++ button.

            <figure markdown>
            ![Build & Flash](../../assets/images/BuildFlash.png)
            </figure>
        
        11. Wait for the upload to finish. A Green Success bar will show up in the ExpressLRS Configurator.

            <figure markdown>
            ![Wifi Update Log](../../assets/images/WifiUpdateLog.png)
            </figure>

        12. On your Radio, the `WiFi Running` screen should disappear and it should be back to the WiFi Connectivity Menu of the ExpressLRS Lua Script.
        13. Long-press the ++"RTN"++ Key to exit the ExpressLRS Lua Script. Reload it to check for the ExpressLRS Firmware version and verify your TX module has been updated.


=== "via UART"

    <figure markdown>
    ![via UART](../../assets/images/Method_TX_UART.png)
    </figure>

    1. Connect your TX Module to your Computer via a USB Data Cable. Best if you remove it from your Radio.
    2. Determine whether your TX Module is being detected properly as a USB-to-UART Device.
        - Windows Users can check via Device Manager, Ports device grouping.
        - Drivers will be needed if the TX Module is not being detected properly. This is indicated by a Yellow Caution Triangle :material-alert-outline: in Device Manager.
        - Commonly used USB-to-UART chip for ExpressLRS Modules include: [CP210x](https://www.silabs.com/developers/usb-to-uart-bridge-vcp-drivers?tab=downloads), [CH340](https://sparks.gogo.co.nz/ch340.html) and the [CH9102](https://sparks.gogo.co.nz/ch340.html) (driver download pages linked).
    3. Some TX Modules have switches to change how the USB port interacts with the different components in the module. Make sure to set it in the position for "Flashing the TX Module via UART".
        - The ES24TX line of modules from Happymodel have jumper blocks or dipswitches inside the module.
        - The BetaFPV Micro modules have dipswitches at the back.
    4. Launch the [ExpressLRS Configurator](../installing-configurator.md) on your Computer.
        - Make sure Official Releases is active from the horizontal tab.
        - Make sure you have selected the Released version you want to flash into your TX module.
    5. Select the Device Category and Device target matching your hardware.
    6. Set the [firmware options](../firmware-options.md) for your device.
        - Regulatory Domain (choose the domain appropriate for the location or country you're flying).
        - Binding Phrase (take note of this phrase as this should be the same on your other devices or they will not bind or sync).
        - Local WiFi Network Credentials (will be used the next time the device goes into WiFi mode).
    7. Click the ++"Build & Flash"++ button.

        <figure markdown>
        ![Build & Flash](../../assets/images/BuildFlash.png)
        </figure>
        
    8. Wait for the process to finish. A Green Success bar will show up in the ExpressLRS Configurator.
    9. Unplug your module from USB. Return any dipswitches or jumper blocks to their "Normal Operation" position.
    10. Reconnect your TX module into your Radio's External Module bay.

=== "via ETX Passthrough"

    <figure markdown>
    ![via EdgeTX Passthrough](../../assets/images/Method_intTX_EdgeTXPassthrough.png)
    </figure>

    !!! info "Info"
        ETX Passthrough is the result of the collaborative effort between RadioMaster, EdgeTX and ExpressLRS.

        It is only available on Radios with Internal ExpressLRS Modules.
    
    Before you start, ensure you have the latest EdgeTX firmware version on your Radio. Consult the EdgeTX [documentation](https://github.com/EdgeTX/edgetx.github.io/wiki/EdgeTX-Installation-Guide) regarding the updating process.

    - `TX16S MK2`: Update it to at least EdgeTX 2.7.0 (f79978b) or EdgeTX 2.7.1 (a55aff0).
    - `Zorro`: Update it to at least EdgeTX 2.7.0 (f79978b) or EdgeTX 2.7.1 (a55aff0). It often comes with an earlier EdgeTX 2.7.0 version (2bdd4974) which results in unsuccessful flashing.
    - `TX12 MK2`: Update it to at least EdgeTX 2.8.0 (f6d140e) for full EdgeTX support.
    - `Boxer`: The factory EdgeTX firmware should be based off an early EdgeTX 2.8.0 and wouldn't need an update.
    - `BetaFPV Lite Radio 3 Pro`: Update it to at least EdgeTX 2.8.0 (f6d140e) for full EdgeTX support.
    - `Jumper T-Lite V2`: Update it to at least EdgeTX 2.8.0 (f6d140e) for full EdgeTX support.

    ??? Tip "Simplest EdgeTX Updating Procedure"
        1. Visit http://buddy.edgetx.org/.
        2. Select the EdgeTX version and the Radio Model you want to update from the Left-hand side column.
        3. Click the ++"Download .bin"++ button at the bottom of the page.
        4. Save the firmware file into your Radio's SD Card, inside the `Firmware` Folder.
        5. Reboot the Radio into DFU/Bootloader mode.
            - Start by turning off your radio.
            - Press and hold the two horizontal Trim switches then press the Power button. The Screen should Light up. Release the buttons.
            - Some Radios have a different procedure, like the BetaFPV Lite Radio 3 Pro. Consult the Manual for the steps to get it into this DFU/Bootloader mode.
        6. Select `Write Firmware`.
        7. Navigate to the EdgeTx firmware file you just downloaded.
        8. Follow the screen prompts.
        9. Once Writing is complete, reboot the radio.
        10. Check the Radio's Version Page to verify you have the version you need.

    Also make sure you have an internal ELRS module on your Radio. The following steps only applies to handsets with ExpressLRS-specific internal modules. There are stickers marked with "ELRS" attached into your radio packaging or boxes, as well as on the JR module bays indicating the type of internal rf module the radio have.

    The current Model on the radio should be using the [Internal ExpressLRS Module](../transmitters/tx-prep.md#rf-protocol). You can test this by loading the ExpressLRS Lua Script from the Tools Menu.

    There's one more setting you want to make sure is set properly before you proceed.

    1. Press the ++"SYS"++ Key on the Radio.
        - Radios without a dedicated ++"SYS"++ Key will need to long-press the ++context-menu++ Key to access the System Menu.
        - Consult your Radio User's Manual on how to get to the System Menu.
    2. Press the ++"PAGE"++ Key until you reach the Hardware Page.
    3. Scroll down until you get to the Serial Ports settings.
    4. Scroll down and select USB-VCP. Press ++enter++ and use the Scroll Wheel to set it to `CLI` mode if it is set to a different setting. Press ++enter++ once more to confirm the changes.
    5. Exit the Hardware menu by long-pressing ++"RTN"++ Key.

    Now follow the next steps to get your Internal ExpressLRS Module Updated:

    1. Connect your powered up Radio to your Computer via a USB Data Cable.

        <figure markdown>
        ![usb picture](../../assets/images/tx-internalUSBPlugged.jpg)
        </figure>

    2. On your Radio, scroll down and select the option `USB Serial(VCP)` then press the ++enter++ Key. Set your Radio aside in the meantime.

        <figure markdown>
        ![Debug option](../../assets/images/tx-internalSerialDebug.jpg)
        </figure>

    3. On your Computer, check whether your Radio is being recognized properly as a {==STMicroelectronics Virtual COM Port==} device.

        !!! tip "Important"
            This is a vital step and a common failure point. Pay attention.

        Windows Users can use Device Manager to check whether the Radio is being detected properly.

        <figure markdown>
        ![Device Manager](../../assets/images/DeviceMngr.png)
        </figure>

        :material-alert-outline: Yellow Caution Triangles in the Device Manager, or any mention of `<Radio Name> Serial Port` means that drivers aren't installed.

        [Download](https://www.st.com/en/development-tools/stsw-stm32102.html) the Driver package first. Unzip/extract the contents of the package and run/execute (double-click) the installer file (`VCP_V1.5.0_Setup_W7_x64_64bits.exe` for Windows Users). 
        
        Once Drivers are installed, check again if the Radio is now being recognized properly. You may have to unplug-replug the USB Cable first or even reboot your computer.

        You only have to do this once usually.
    
    4. Launch the [ExpressLRS Configurator](../installing-configurator.md) on your Computer.
        - Make sure Official Releases is active from the horizontal tab.
        - Make sure you have selected the Released version you want to flash into your TX module.
    5. Select the Device Category and Device target matching your hardware.
    6. Set the [firmware options](../firmware-options.md) for your device.
        - Regulatory Domain (choose the domain appropriate for the location or country you're flying).
        - Binding Phrase (take note of this phrase as this should be the same on your other devices or they will not bind or sync).
        - Local WiFi Network Credentials (will be used the next time the device goes into WiFi mode).
    7. Click the ++"Build & Flash"++ button.

        <figure markdown>
        ![Build & Flash](../../assets/images/BuildFlash.png)
        </figure>
        
    8. Wait for the process to finish. A Green Success bar will show up in the ExpressLRS Configurator.
    9. Unplug your Radio from USB.
    10. Using the ExpressLRS Lua Script from the Tools Menu, check  if the firmware version got updated.

