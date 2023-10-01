---
template: main.html
---

![Setup-Banner](https://raw.githubusercontent.com/ExpressLRS/ExpressLRS-hardware/master/img/quick-start.png)

## Flashing/Updating the TX Module Firmware

=== "via Stock_BL"

    <figure markdown>
    ![via BL](../../assets/images/Method_TX_StockBL.png)
    </figure>

    1. Launch the [ExpressLRS Configurator](../installing-configurator.md) on your Computer.
        ![Configurator Release]{ align=right }

        - Make sure `Official Releases` is active from the horizontal tab.
        - Ensure you select the Released version you want to flash into your TX module.

        <br clear="right" />
    2. Select the Device Category and Device target matching your hardware.

        - Device Category: 
            - `NamimnoRC 900 MHz`

        - Device: 
            - `NamimnoRC Voyager 900MHz TX`

    3. Set the Flashing Method to `Stock_BL`

        <figure markdown>
        ![via BL](../../assets/images/Method_TX_StockBL.png)
        </figure>

    4. Set the [firmware options](../firmware-options.md) for your device.
        - Regulatory Domain (Mandatory. Choose the domain appropriate for the location or country you're flying).
        - Binding Phrase (Optional, but Highly Recommended. Note this phrase as it should be the same on your other devices, or they will not bind or sync).

    5. Click the ++"Build"++ button.

        <figure markdown>
        ![Build]
        </figure>
        
    6. Wait for the process to finish. A Green Success bar will show up in the ExpressLRS Configurator.

    7. A Temp folder will open up with the **firmware.elrs** file. Copy-paste the firmware.elrs file into your Radio's SD Card (preferably to the `/FIRMWARE` folder for easy access).

    8. On your radio, open the System Menu. 

        - On newer radios, you can press the ++"SYS"++ key to open the System Menu
        - On older radios, or radios that only have a menu key, long-press the ++context-menu++ key to open the System Menu

    9. Using the ++"Page"++ key/s, navigate to the SD-HC Card page, scroll-down and open the `FIRMWARE` folder where you can find the **firmware.elrs** file.

    10. Highlight the file and press-hold the ++"Enter"++ button and select "Flash External ELRS". Wait for the firmware to be written.

        ??? tip "No Sync"
            - Make sure you have updated the OpenTX/EdgeTX firmware of your radio to a newer version
            - Make sure the current model selected on the radio is set up for ExpressLRS Use. See the [Radio Preparation] guide.

    11. With the [ExpressLRS Lua Script] in the Tools page, verify if the firmware version has been updated.

=== "via STLink"

    <figure markdown>
    ![via STLink](../../assets/images/Method_TX_STLink.png)
    </figure>

    !!! attention 
        Only use this method if the firmware has been corrupted.

    1. Disassemble your TX Module to get access to the mainboard.

        <figure markdown>
            ![NamimnoRC Voyager Backside](https://github.com/ExpressLRS/ExpressLRS-Hardware/blob/master/img/namimnoback.jpg?raw=true){ style="width:40%;display: inline-block; margin:0 auto;" class="center-img" }
        </figure>

        <figure markdown>
            ![NamimnoRC Voyager cable](https://github.com/ExpressLRS/ExpressLRS-Hardware/blob/master/img/cable.jpg?raw=true){ style="width:40%;display: inline-block; margin:0 auto;" class="center-img" }
        </figure>

    2. Connect your STLink V2 dongle to the pads shown in the image below.

        <figure markdown>
        ![NamimnoRC Pinout](https://github.com/ExpressLRS/ExpressLRS-Hardware/blob/master/img/namimnopinout.png?raw=true){ style="width:40%;display: inline-block; margin:0 auto;" class="center-img" }
        </figure>

    3. Connect your STLink V2 dongle to your Computer's USB Port. Make sure it is being detected correctly.

    4. Launch the [ExpressLRS Configurator](../installing-configurator.md) on your Computer.
        ![Configurator Release]{ align=right }

        - Make sure `Official Releases` is active from the horizontal tab.
        - Ensure you select the Released version you want to flash into your TX module.

        <br clear="right" />
    5. Select the Device Category and Device target matching your hardware.

        - Device Category: 
            - `NamimnoRC 900 MHz`

        - Device: 
            - `NamimnoRC Voyager 900MHz TX`

    6. Set the Flashing Method to `STLink`

        <figure markdown>
        ![via STLink](../../assets/images/Method_TX_STLink.png)
        </figure>

    7. Set the [firmware options](../firmware-options.md) for your device.
        - Regulatory Domain (Mandatory. Choose the domain appropriate for the location or country you're flying).
        - Binding Phrase (Optional, but Highly Recommended. Note this phrase as it should be the same on your other devices, or they will not bind or sync).

    8. Click the ++"Flash"++ button.

        <figure markdown>
        ![Flash]
        </figure>
        
    9. Wait for the process to finish. A Green Success bar will show up in the ExpressLRS Configurator.

    10. Disconnect the STLink V2 dongle from the TX Module PCB and reassemble the module.
    11. Reattach your TX Module into your Radio and, using the [ExpressLRS Lua Script], verify if the firmware version has been updated.

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
[ExpressLRS Lua Script]: firmware-version.md#via-lua-script
