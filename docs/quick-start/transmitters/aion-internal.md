---
template: main.html
---

![Setup-Banner](https://github.com/ExpressLRS/ExpressLRS-Hardware/raw/master/img/quick-start.png)

!!! danger "Advisory"
    Not all Jumper T Pros come with an internal ELRS transmitter. Some come with a "JP4in1 multi-protocol module" or "CC2500 multi-protocol module". This tutorial does not apply to those Jumper T Pros. Check the page you bought it from to determine which unit you purchased.

!!! danger "Advisory"
    If you are flashing/updating your TX module via WiFi for the first time from the factory firmware, or from an older firmware, to ExpressLRS 3.x firmware, you will first need to flash it to version 2.5.2, then flash it with the [Repartitioner](https://github.com/ExpressLRS/repartitioner) binary [file](https://github.com/ExpressLRS/repartitioner/releases/download/1.0/repartitioner.bin) (right click, save as/save file as). Should it complain about Target Mismatch, just click `Flash Anyway`. Only then you can flash to 3.x firmware via WiFi.

    Joshua Bardwell has a video about it [here](https://www.youtube.com/watch?v=2kcRi1cHejM).

    Updating to 3.x via UART or ETX Passthrough doesn't require 2.5.2 firmware or the Repartitioner.

## Updating and Recovery Procedures

=== "via WiFi Updating"

    <figure markdown>
    ![via WiFi](../../assets/images/Method_intTX_WiFi.png)
    </figure>

    === "Manual Upload via AP"

        !!! Info "Heads up!"
            This option is only possible if you haven't previously flashed or configured your TX Module with your Home WiFi SSID and Password or if it's unable to connect to said WiFi Network because the router is Off or unreachable.

        1. Launch the [ExpressLRS Configurator](../installing-configurator.md) on your Computer.
            ![Configurator Release]{ align=right }

            - Make sure `Official Releases` is active from the horizontal tab.
            - Ensure you select the Released version you want to flash into your TX module.

            <br clear="right" />

        2. Select the Device Category and Device Target matching your hardware.

            - Device Category: 
                - `Jumper 2.4 GHz`

            - Device: 
                - `Jumper AION T-Pro 2.4GHz TX`

        3. Set the Flashing Method to `WiFi`.

            <figure markdown>
            ![via WiFi](../../assets/images/Method_TX_WiFi.png)
            </figure>

        4. Set the [firmware options](../firmware-options.md) for your device.
            - Regulatory Domain (Mandatory. Choose the domain appropriate for the location or country you're flying).
            - Binding Phrase (Optional, but Highly Recommended. Note this phrase as it should be the same on your other devices, or they will not bind or sync).
            - Local WiFi Network Credentials (Optional. Will be used the next time the device goes into WiFi mode).
        5. Click the ++"Build"++ button.
            
            <figure markdown>
            ![Build]
            </figure>
            
        6. Once the Build process is done, a Temp folder window containing your firmware binaries should pop up.

            ![Temp TX]{ align=right }

            - Do not close this Temp folder because this is where you will take your firmware from in the later steps. If you are planning on using your phone or tablet to upload the firmware file later, copy the firmware file into your device.

            !!! tip "NOTICE"
                With the release of ExpressLRS 3.3.0 and ExpressLRS Configurator 1.6.0, only one file will show up. Use the `firmware.bin` file for the next steps.

            <br clear="right" />
            
        7. Press the ++"SYS"++ Key on your Radio to display the Tools Menu, where you can find the Lua Scripts.
            - Older Radios or those with only one Menu Key must long-press the ++context-menu++ Key to access the System Menu.
            - Consult your Radio User's Manual on how to access the System Menu.

        8. Scroll down and select `ExpressLRS` Lua Script.

            <figure markdown>
            ![Lua Script]
            </figure>

            - If the script is nowhere to be found, download it from [this page](../transmitters/lua-howto.md) and save it into your Radio SD Card Scripts/Tools/ folder.

        9. Press ++enter++ to Load it.

            <figure markdown>
            ![Lua Running]
            </figure>

            - If the script is stuck on a "Loading..." screen, return to the [Radio Preparation](../transmitters/tx-prep.md) Page and make sure you have configured your radio properly for ExpressLRS use.
        10. Scroll down and select `WiFi Connectivity` and press ++enter++.
        11. Select `Enable WiFi` and press ++enter++.

            <figure markdown>
            ![Lua WiFi]
            </figure>

        12. The `WiFi Running` screen will show up. Your TX module is now in WiFi mode.
            - Do not worry if the Script stops and shows a Syntax Error. The module is still in WiFi mode. The Syntax Error could be because you're on an older radio, older EdgeTX/OpenTX firmware, or both. It could also be because your TX module is on an earlier firmware version, and you're using a more recent Lua Script.

        13. Using a WiFi-capable device such as your smartphone or laptop, scan for the `ExpressLRS TX` Access Point. Connect to this Access Point.

            ![WiFi Hotspot](../../assets/images/WifiHotspotTX.png){ align=right }

            - If your TX Module is previously flashed with your Home WiFi SSID and Password, and it is able to connect to that WiFi Network, then the Access Point will not show up.
            - `expresslrs` is the Password for this Access Point.

            ??? question "Where's the Access Point?"
                If you cannot find the Access Point, make sure the device you're using is capable of connecting to 2.4GHz WiFi Networks. Also try putting the devices closer together.
                
                If you still cannot find the Access Point, chances are that you have set it with your WiFi SSID and Password before, and it has connected to your WiFi Network.

            <br clear="right" />

        14. Once connected to the `ExpressLRS TX` Access Point, open up a Browser window, type in the IP Address `10.0.0.1` on the Address Bar, and press ++enter++. The ExpressLRS Web UI will load.
        15. Activate the `Update` Tab.

            <figure markdown>
            ![TX update tab]
            </figure>

            - If your TX Module is still on an earlier firmware version, then there's no Update Tab, and instead, you will need to scroll down to find the Firmware Update section.

            <figure markdown>
            ![Old File Upload]
            </figure>

        16. Drag and drop the Firmware file from the Temp folder into the File Upload field.
            - You can also use the Browse or Choose File button and browse for the file yourself, especially if you've copied/moved it somewhere else on an earlier step.
        17. Click the ++"Update"++ button to start the Updating procedure.
        18. Wait for the firmware file to get uploaded and flashed into your device. It only takes a minute or two, and you will see the Success Popup Message.

            <figure markdown>
            ![Success WiFi]
            </figure>

        19. On your Radio, the `WiFi Running` screen should disappear and should be back to the WiFi Connectivity Menu of the ExpressLRS Lua Script.
        20. Long-press the ++"RTN"++ Key to exit the ExpressLRS Lua Script. Then reload it to check for the ExpressLRS Firmware version and verify your TX module has been updated.

    === "Manual Upload via Local WiFi"

        !!! Info "Heads up!"
            This option is only possible if you have previously flashed or configured your TX Module with your Home WiFi SSID and Password and the module is able to connect to said WiFi Network.

        1. Launch the [ExpressLRS Configurator](../installing-configurator.md) on your Computer.
            ![Configurator Release]{ align=right }

            - Make sure `Official Releases` is active from the horizontal tab.
            - Ensure you select the Released version you want to flash into your TX module.

            <br clear="right" />
        2. Select the Device Category and Device Target matching your hardware.

            - Device Category: 
                - `Jumper 2.4 GHz`

            - Device: 
                - `Jumper AION T-Pro 2.4GHz TX`

        3. Set the Flashing Method to `WiFi`.

            <figure markdown>
            ![via WiFi](../../assets/images/Method_TX_WiFi.png)
            </figure>

        4. Set the [firmware options](../firmware-options.md) for your device.
            - Regulatory Domain (Mandatory. Choose the domain appropriate for the location or country you're flying).
            - Binding Phrase (Optional, but Highly Recommended. Note this phrase as it should be the same on your other devices, or they will not bind or sync).
            - Local WiFi Network Credentials (Optional. Will be used the next time the device goes into WiFi mode).
        5. Click the ++"Build"++ button.
            
            <figure markdown>
            ![Build]
            </figure>
            
        6. Once the Build process is done, a Temp folder window containing your firmware binaries should pop up.
            ![Temp TX]{ align=right }

            - Do not close this Temp folder because this is where you will take your firmware from in the later steps. If you are planning on using your phone or tablet to upload the firmware file later, copy the firmware file into your device.

            !!! tip "NOTICE"
                With the release of ExpressLRS 3.3.0 and ExpressLRS Configurator 1.6.0, only one file will show up. Use the `firmware.bin` file for the next steps.

            <br clear="right" />
        7. Press the ++"SYS"++ Key on your Radio to display the Tools Menu, where you can find the Lua Scripts.
            - Older Radios or those with only one Menu Key must long-press the ++context-menu++ Key to access the System Menu.
            - Consult your Radio User's Manual on how to access the System Menu.

        8. Scroll down and select `ExpressLRS` Lua Script.

            <figure markdown>
            ![Lua Script]
            </figure>

            - If the script is nowhere to be found, download it from [this page](../transmitters/lua-howto.md) and save it into your Radio SD Card Scripts/Tools/ folder.

        9. Press ++enter++ to Load it.

            <figure markdown>
            ![Lua Running]
            </figure>

            - If the script is stuck on a "Loading..." screen, return to the [Radio Preparation](../transmitters/tx-prep.md) Page and make sure you have configured your radio properly for ExpressLRS use.
        10. Scroll down and select `WiFi Connectivity` and press ++enter++.
        11. Select `Enable WiFi` and press ++enter++.
            
            <figure markdown>
            ![Lua WiFi]
            </figure>

        12. The `WiFi Running` screen will show up. Your TX module is now in WiFi mode.
            - Do not worry if the Script stops and shows a Syntax Error. The module is still in WiFi mode. The Syntax Error could be because you're on an older radio, older EdgeTX/OpenTX firmware, or both. It could also be because your TX module is on an earlier firmware version, and you're using a more recent Lua Script.

        13. With your module now in WiFi Mode and it was able to connect to your Local WiFi Network, open a Browser window on any WiFi-capable device that is also connected to the same Local WiFi Network. Type in the Address http://elrs_tx.local on your browser's Address Bar. The ExpressLRS Web UI should load.
            - If your browser cannot resolve this address and it cannot load the ExpressLRS Web UI, this means that MDNS is not working on your device or network.

            ??? tip "MDNS is not working!"
                === "The `arp` Command"

                    1. Open up a Command Prompt window on your computer.
                    2. Execute the command `arp -a`, which will list all the devices in the Network.
                    3. Use each of the IP Addresses marked as `Dynamic` as a URL in your Browser until you get to the ExpressLRS Web UI.

                === "Router DHCP List"
                    1. Log in into your Router dashboard.
                    2. Check the DHCP List and look for the "elrs" device.
                    3. Take note of the IP Address given by your router.
                    4. Use this IP address in your Browser as the URL.

        14. Activate the `Update` Tab.

            <figure markdown>
            ![TX update tab]
            </figure>

            - If your TX Module is still on an earlier firmware version, then there's no Update Tab, and instead, you will need to scroll down to find the Firmware Update section.

            <figure markdown>
            ![Old File Upload]
            </figure>

        15. Drag and drop the Firmware file from the Temp folder into the File Upload field.
            - You can also use the Browse or Choose File button and browse for the file yourself, especially if you've copied/moved it somewhere else on an earlier step.
        16. Click the ++"Update"++ button to start the Updating procedure.
        17. Wait for the firmware file to get uploaded and flashed into your device. It only takes a minute or two, and you will see the Success Popup Message.

            <figure markdown>
            ![Success WiFi]
            </figure>

        18. On your Radio, the `WiFi Running` screen should disappear and should be back to the WiFi Connectivity Menu of the ExpressLRS Lua Script.
        19. Long-press the ++"RTN"++ Key to exit the ExpressLRS Lua Script. Then reload it to check for the ExpressLRS Firmware version and verify your TX module has been updated.

    === "Auto Upload"

        !!! Info "Heads up!"
            This option is only possible if you have previously flashed or configured your TX Module with your Home WiFi SSID and Password and the module is able to connect to said WiFi Network.
            
            MDNS must also be working so your browser can resolve the address http://elrs_tx.local and load the ExpressLRS Web UI from said address.

        1. Press the ++"SYS"++ Key on your Radio to display the Tools Menu, where you can find the Lua Scripts.
            - Older Radios or those with only one Menu Key must long-press the ++context-menu++ Key to access the System Menu.
            - Consult your Radio User's Manual on how to access the System Menu.

        2. Scroll down and select `ExpressLRS` Lua Script.

            <figure markdown>
            ![Lua Script]
            </figure>

            - If the script is nowhere to be found, download it from [this page](../transmitters/lua-howto.md) and save it into your Radio SD Card Scripts/Tools/ folder.

        3. Press ++enter++ to Load it.

            <figure markdown>
            ![Lua Running]
            </figure>

            - If the script is stuck on a "Loading..." screen, return to the [Radio Preparation](../transmitters/tx-prep.md) Page and make sure you have configured your radio properly for ExpressLRS use.
        4. Scroll down and select `WiFi Connectivity` and press ++enter++.
        5. Select `Enable WiFi` and press ++enter++.
            
            <figure markdown>
            ![Lua WiFi]
            </figure>
            
        6. The `WiFi Running` screen will show up. Your TX module is now in WiFi mode.
            - Do not worry if the Script stops and shows a Syntax Error. The module is still in WiFi mode. The Syntax Error could be because you're on an older radio, older EdgeTX/OpenTX firmware, or both. It could also be because your TX module is on an earlier firmware version, and you're using a more recent Lua Script.
        7. Launch the [ExpressLRS Configurator](../installing-configurator.md) on your Computer.
            ![Configurator Release]{ align=right }

            - Make sure `Official Releases` is active from the horizontal tab.
            - Ensure you select the Released version you want to flash into your TX module.

            <br clear="right" />
        8. Select the Device Category and Device Target matching your hardware.

            - Device Category: 
                - `Jumper 2.4 GHz`

            - Device: 
                - `Jumper AION T-Pro 2.4GHz TX`

        9. Set the Flashing Method to `WiFi`.

            <figure markdown>
            ![via WiFi](../../assets/images/Method_TX_WiFi.png)
            </figure>

        10. Set the [firmware options](../firmware-options.md) for your device.
            - Regulatory Domain (Mandatory. Choose the domain appropriate for the location or country you're flying).
            - Binding Phrase (Optional, but Highly Recommended. Note this phrase as it should be the same on your other devices, or they will not bind or sync).
            - Local WiFi Network Credentials (Optional. Will be used the next time the device goes into WiFi mode).
        11. Click the ++"Flash"++ button.

            <figure markdown>
            ![Flash]
            </figure>
        
        12. Wait for the upload to finish. A Green Success bar will show up in the ExpressLRS Configurator.

            <figure markdown>
            ![WiFi Update Log](../../assets/images/WifiUpdateLog.png)
            </figure>

        13. On your Radio, the `WiFi Running` screen should disappear and should be back to the WiFi Connectivity Menu of the ExpressLRS Lua Script.
        14. Long-press the ++"RTN"++ Key to exit the ExpressLRS Lua Script. Then reload it to check for the ExpressLRS Firmware version and verify your TX module has been updated.

=== "via ETX Passthrough Recovery"

    <figure markdown>
    ![via EdgeTX Passthrough](../../assets/images/Method_intTX_EdgeTXPassthrough.png)
    </figure>

    !!! info "Info"
        ETX Passthrough is the result of the collaborative effort between RadioMaster, EdgeTX and ExpressLRS.

        It is only available on Radios with Internal ExpressLRS Modules.
    
    Before you start, ensure you have the latest EdgeTX firmware version on your Radio. Consult the EdgeTX [documentation](https://github.com/EdgeTX/edgetx.github.io/wiki/EdgeTX-Installation-Guide) regarding the updating process.

    For the `Jumper T-Pro`, update it to at least EdgeTX 2.7.1 (a55aff0) for full EdgeTX support.

    !!! tip "Hot Tip"
        To ensure updating success with this method, update the EdgeTX firmware on the radio to at least EdgeTX 2.7.1 (a55aff0). The EdgeTx Firmware that comes with this radio is a pre-release version.

    ??? Tip "Simplest EdgeTX Updating Procedure"
        1. Visit http://buddy.edgetx.org/.
        2. Select the EdgeTX version and the Radio Model you want to update from the Left-hand side column.
        3. Click the ++"Download .bin"++ button at the bottom of the page.
        4. Save the firmware file into your Radio's SD Card, inside the `Firmware` Folder.
        5. Reboot the Radio into DFU/Bootloader mode.
            - Turn off your radio.
            - Press and hold the two horizontal Trim switches then press the Power button. The Screen should Light up. Let go of the buttons.
            - Some Radios have a different procedure, like the BetaFPV Lite Radio 3 Pro. Consult the Manual for the steps to get it into this DFU/Bootloader mode.
        6. Select `Write Firmware`.
        7. Navigate to the EdgeTx firmware file you just downloaded.
        8. Follow the screen prompts.
        9. Once Writing is complete, reboot the radio.
        10. Check the Radio's Version Page to verify you have the version you need.

    Also, make sure you have an internal ELRS module on your Radio. The following steps only apply to handsets with ExpressLRS-specific internal modules. 

    The current Model on the radio should be using the [Internal ExpressLRS Module](../transmitters/tx-prep.md#rf-protocol). Test this by loading the ExpressLRS Lua Script from the Tools Menu.

    There's one more setting you want to make sure is set properly before proceeding.

    1. Press the ++"SYS"++ Key on the Radio.
        - Radios without a dedicated ++"SYS"++ Key must long-press the ++context-menu++ Key to access the System Menu.
        - Consult your Radio User's Manual on how to get to the System Menu.
    2. Press the ++"PAGE"++ Key until you reach the Hardware Page.
    3. Scroll down until you see the Serial Ports settings.
    4. Select or highlight USB-VCP. Press ++enter++ and use the Scroll Wheel to set it to `CLI` mode if it is set to a different setting. Press ++enter++ once more to confirm the changes.
    5. Exit the Hardware menu by long-pressing ++"RTN"++ Key.

    Before proceeding, you will need to disassemble the radio. You will need a small Philips screwdriver for this. Ten(10) small Philips screws keep both halves of the radio together.

    <figure markdown>
    ![tPro screws](../../assets/images/tpro_screws.jpg)
    </figure>

    !!! warning "Handle with Care"
        There are wires connecting the module to the main board of the radio, along with battery leads. Do not yank out the back cover of the radio from its front half. You don't need to disconnect the wires from the mainboard.

    Once you have both halves of the radio apart, you will need to solder a piece of wire on the Boot pad into one of the momentary switches on the radio. Refer to the image below where to solder the ends of the wire.

    <figure markdown>
    ![tPro janky boot](../../assets/images/tpro_bootOnSwitch.jpg)
    </figure>

    Once the wire is soldered adequately, reassemble the radio. Tighten up the ten(10) screws to secure both halves of the radio. 

    !!! note
        If you plan to use the switch as an Aux channel, remove the wire afterward. Leaving this wire connected means the Aux channel will output a constant "High" signal.

    Now follow the next steps to get your Internal ExpressLRS Module Updated or Recovered:

    1. Connect your powered-up Radio to your Computer via a USB Data Cable.

    2. On your Radio, scroll down and select `USB Serial(VCP)` then press the ++enter++ Key. Set your Radio aside in the meantime.

        <figure markdown>
        ![Debug option](../../assets/images/tx-internalSerialDebug.jpg)
        </figure>

    3. On your Computer, check whether your Radio is being recognized correctly as a {==STMicroelectronics Virtual COM Port==} device.

        !!! tip "Important"
            This is a vital step and a common failure point. Pay attention.

        Windows Users can use Device Manager to check whether the Radio is being recognized correctly.

        <figure markdown>
        ![Device Manager](../../assets/images/DeviceMngr.png)
        </figure>

        :material-alert-outline: Yellow Caution Triangles in the Device Manager, or any mention of `<Radio Name> Serial Port` means drivers aren't installed.

        [Download](https://www.st.com/en/development-tools/stsw-stm32102.html) the Driver package first. Unzip/extract the contents of the package and run/execute (double-click) the installer file (`VCP_V1.5.0_Setup_W7_x64_64bits.exe` for Windows Users). 
        
        Once Drivers are installed, check again if the Radio is now being recognized correctly. You may have to first unplug-replug the USB Cable or even reboot your computer.

        You only have to do this once usually.
    
    4. Launch the [ExpressLRS Configurator](../installing-configurator.md) on your Computer.
        ![Configurator Release]{ align=right }

        - Make sure `Official Releases` is active from the horizontal tab.
        - Ensure you select the Released version you want to flash into your TX module.

        <br clear="right" />
    5. Select the Device Category and Device Target matching your hardware.

        - Device Category: 
            - `Jumper 2.4 GHz`

        - Device: 
            - `Jumper AION T-Pro 2.4GHz TX`

    6. Set the Flashing Method to `EdgeTXPassthrough`

        <figure markdown>
        ![via EdgeTX Passthrough](../../assets/images/Method_intTX_EdgeTXPassthrough.png)
        </figure>

    7. Set the [firmware options](../firmware-options.md) for your device.
        - Regulatory Domain (Mandatory. Choose the domain appropriate for the location or country you're flying).
        - Binding Phrase (Optional, but Highly Recommended. Note this phrase as it should be the same on your other devices, or they will not bind or sync).
        - Local WiFi Network Credentials (Optional. Will be used the next time the device goes into WiFi mode).
    8. Click the ++"Flash"++ button.

        <figure markdown>
        ![Flash]
        </figure>
    
    9. Wait for the Passthrough Init or Passthrough Done section of the log and Press the switch in the radio where you wired up the boot button and hold it until the script has connected. See the image below for the correct timing.

        <figure markdown>
        ![tPro press it](../../assets/images/tpro_viaETXPress.png)
        </figure>

    10. Wait for the process to finish. A Green Success bar will show up in the ExpressLRS Configurator.

        <figure markdown>
        ![tPro flashed](../../assets/images/tpro_viaETXSuccess.png)
        </figure>

        - If you didn't get it right and it fails, don't worry. Just retry and it should go through.

    11. Unplug your Radio from USB.
    12. Using the [ExpressLRS Lua Script] from the Tools Menu, check if the firmware version got updated or you have it recovered.

=== "via UART Recovery"

    <figure markdown>
    ![via UART](../../assets/images/Method_intTX_UART.png)
    </figure>

    1. Disassemble the radio. You will need a small Philips screwdriver for this. Ten(10) small Philips screws keep both halves of the radio together.

        <figure markdown>
        ![tPro screws](../../assets/images/tpro_screws.jpg)
        </figure>

        !!! warning "Handle with Care"
            There are wires connecting the module to the main board of the radio, along with battery leads. Do not yank out the back cover of the radio from its front half. You don't need to disconnect the wires from the mainboard.

    2. Disconnect the internal module from the mainboard of the radio. The pin-out is as follows: 
        - White wire is the RX.
        - Yellow wire is the TX.
        - Red wire is the 5v pin.
        - The Black wire is the Gnd pin.

        <figure markdown>
        ![tPro duplex](../../assets/images/tproUART.jpg)
        </figure>

    3. Connect these four wires into your FTDI dongle or a USB to Serial Adapter: RX pin into the TX pin; TX pin into the RX pin; 5v to 5v, and Gnd to Gnd.

        <figure markdown>
        ![tPro on Serial](../../assets/images/tproUART-USB.jpg)
        </figure>

    4. Before you connect the FTDI dongle/Serial Adapter to the USB port of your Computer, hold down the Boot button. Keep the button pressed until you have connected the Serial Adapter to your USB port. 

    5. Launch the [ExpressLRS Configurator](../installing-configurator.md) on your Computer.
        ![Configurator Release]{ align=right }

        - Make sure `Official Releases` is active from the horizontal tab.
        - Ensure you select the Released version you want to flash into your TX module.

        <br clear="right" />
    6. Select the Device Category and Device Target matching your hardware.

        - Device Category: 
            - `Jumper 2.4 GHz`

        - Device: 
            - `Jumper AION T-Pro 2.4GHz TX`

    7. Set the Flashing Method to `UART`

        <figure markdown>
        ![via UART](../../assets/images/Method_intTX_UART.png)
        </figure>

    8. Set the [firmware options](../firmware-options.md) for your device.
        - Regulatory Domain (Mandatory. Choose the domain appropriate for the location or country you're flying).
        - Binding Phrase (Optional, but Highly Recommended. Note this phrase as it should be the same on your other devices, or they will not bind or sync).
        - Local WiFi Network Credentials (Optional. Will be used the next time the device goes into WiFi mode).
    9. Click the ++"Flash"++ button.

        <figure markdown>
        ![Flash]
        </figure>
        
    10. Wait for the process to finish. A Green Success bar will show up in the ExpressLRS Configurator.

        !!! info "Attention"
            Incorrect or loose connections can cause this method to fail. If it does, disconnect the Serial Adapter from the USB, ensure you have the proper connection, and repeat the process. Press and hold the boot button before connecting the Serial Adapter to the USB. 

    11. Disconnect the FTDI/UART Adapter and reconnect the module back to the radio mainboard, as shown below.
    
        <figure markdown>
        ![tPro Connection](../../assets/images/tproUART-AllSet.jpg)
        </figure>

    11. Reassemble the radio (but do not put in the screws yet) and verify you have a working module once by running the [ExpressLRS Lua script].
    12. Once you've verified that your Internal ExpressLRS module is working, replace the screws and tighten things up. Chug one down and celebrate!

[Lua Script]: ../../assets/images/lua1.jpg
[Lua Running]: ../../assets/images/lua/config-bw.png
[Lua WiFi]: ../../assets/images/lua/wifi-bw.png
[Configurator Release]: ../../assets/images/ConfiguratorRelease.png
[Temp TX]: ../../assets/images/build-temp-tx.png
[Flash]: ../../assets/images/BuildFlash.png
[Build]: ../../assets/images/Build.png
[CP210x]: ../../assets/images/device-mngr-cp210x.png
[TX update tab]: ../../assets/images/web-update-tx.png
[Success WiFi]: ../../assets/images/txmoduleWiFiUpdateSuccess.jpg
[Old File Upload]: ../../assets/images/web-firmwareupdate.png
[ExpressLRS Lua Script]: lua-howto.md
