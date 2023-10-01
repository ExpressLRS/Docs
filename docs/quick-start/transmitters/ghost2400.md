---
template: main.html
---

![Setup-Banner](https://raw.githubusercontent.com/ExpressLRS/ExpressLRS-hardware/master/img/quick-start.png)

## Flashing/Updating TX Module Firmware

=== "via STLink"

    <figure markdown>
    ![via STLink](../../assets/images/Method_TX_STLink.png)
    </figure>

    !!! warning "Warning"
        This method is an **irreversible** one. You will not be able to go back to ImmersionRC Ghost firmware with this method. You have been warned!

    Video Guide(10 min):
    
    <figure markdown>
    <iframe width="560" height="315" src="https://www.youtube.com/embed/fHxx2Cc3Hz0" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>
    </figure>

    1. Carefully disassemble your TX Module to get access to the mainboard.

    2. Connect your STLink V2 dongle to the pads shown in the images below:

        - Wire `3.3v`, `GND`, `CLK`, and `DIO` to their respective pins on your part from the StLink. (You can power with the StLink but in the second image, the radio is used to power the module). 

        <figure markdown>
        <img class="center-img" src="https://i.imgur.com/58wxHZe.png" width = "49%">
        </figure>

        <figure markdown>
        <img class="center-img" src="https://i.imgur.com/vztruRj.png" width = "49%">
        </figure>

    3. Connect your STLink V2 dongle to your Computer's USB Port. Make sure it is being detected correctly.

    4. Before flashing, disable `'Readout Protection'`. To do this, download the [ST-LINK Utility](https://www.st.com/en/development-tools/stsw-link004.html) and follow this quick [how to video](https://youtu.be/SEYQ1HpRmk0). After such, you can now disconnect (Target -> Disconnect) and close the ST-Link Utility.

    5. Launch the [ExpressLRS Configurator](../installing-configurator.md) on your Computer.
        ![Configurator Release]{ align=right }

        - Make sure `Official Releases` is active from the horizontal tab.
        - Ensure you select the Released version you want to flash into your TX module.

        <br clear="right" />
    6. Select the Device Category and Device target matching your hardware.

        - Device Category:
            - `ImmersionRC 2.4 GHz`

        - Device:
            - `Ghost 2.4GHz TX`
            - `Ghost Lite 2.4GHz TX`

    7. Set the Flashing Method to `STLink`

        <figure markdown>
        ![via STLink](../../assets/images/Method_TX_STLink.png)
        </figure>

    8. Set the [firmware options](../firmware-options.md) for your device.
        - Regulatory Domain (Mandatory. Choose the domain appropriate for the location or country you're flying).
        - Binding Phrase (Optional, but Highly Recommended. Note this phrase as it should be the same on your other devices, or they will not bind or sync).

    9. Click the ++"Flash"++ button.

        <figure markdown>
        ![Flash]
        </figure>
        
    10. Wait for the process to finish. A Green Success bar will show up in the ExpressLRS Configurator.

    11. Disconnect the STLink V2 dongle from the TX Module PCB and reassemble the module.
    12. Reattach your TX Module into your Radio and, using the [ExpressLRS Lua Script], verify if the firmware version has been updated.

=== "via Stock_BL"

    <figure markdown>
    ![via BL](../../assets/images/Method_TX_StockBL.png)
    </figure>

    !!! info
        This method requires OpenTX 2.3.12 or newer; or EdgeTX 2.4.0 or newer.

        This method can only be used to UPDATE the firmware on an already-converted Ghost Module

    1. Launch the [ExpressLRS Configurator](../installing-configurator.md) on your Computer.
        ![Configurator Release]{ align=right }

        - Make sure `Official Releases` is active from the horizontal tab.
        - Ensure you select the Released version you want to flash into your TX module.

        <br clear="right" />
    2. Select the Device Category and Device target matching your hardware.

        - Device Category:
            - `ImmersionRC 2.4 GHz`

        - Device:
            - `Ghost 2.4GHz TX`
            - `Ghost Lite 2.4GHz TX`

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

[Configurator Release]: ../../assets/images/ConfiguratorRelease.png
[Flash]: ../../assets/images/BuildFlash.png
[Build]: ../../assets/images/Build.png
[Radio Preparation]: tx-prep.md
[ExpressLRS Lua Script]: firmware-version.md#via-lua-script
