---
template: main.html
---

![Setup-Banner](https://raw.githubusercontent.com/ExpressLRS/ExpressLRS-hardware/master/img/quick-start.png)

!!! warning
    The R9M Lite Pro **can not** be flashed via OpenTx or EdgeTX (Stock_BL method), and therefore requires an STLink v2 to flash. See the guide [below](#via-stlink)

## Flashing/Updating TX Module Firmware

=== "via Stock_BL"

    <figure markdown>
    ![via BL](../../assets/images/Method_TX_StockBL.png)
    </figure>

    !!! info
        This method requires OpenTX 2.3.12 or newer; or EdgeTX 2.4.0 or newer.

    1. Download and save [`r9m_elrs_bl.frk`](https://github.com/ExpressLRS/ExpressLRS/blob/master/src/bootloader/r9m_elrs_bl.frk?raw=true)(14kb) onto the SD card of your radio, in the `/FIRMWARE` folder.

    2. Flash `r9m_elrs_bl.frk` to your TX module:

        - Access the System Menu on your radio. 
            - On newer radios, you can press the ++"SYS"++ key to open the System Menu
            - On older radios, or radios that only have a menu key, long-press the ++context-menu++ key to open the System Menu
        - Using the ++"Page"++ key/s, navigate to the SD-HC Card page.
        - Scroll-down and open the `FIRMWARE` folder where you can find the **r9m_elrs_bl.frk** file.
        - Flash the frk file by holding ++"Enter"++ key and selecting "Flash external module"

        !!! info "FYI"
            You only need to flash the Bootloader ONCE. After it's flashed into the module, you **don't** have to reflash it in every update.

        Video Guide:
        <figure markdown>
        <iframe width="560" height="315" src="https://www.youtube.com/embed/DG3f-lnNlms" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>
        </figure>

    3. Launch the [ExpressLRS Configurator](../installing-configurator.md) on your Computer.
        ![Configurator Release]{ align=right }

        - Make sure `Official Releases` is active from the horizontal tab.
        - Ensure you select the Released version you want to flash into your TX module.

        <br clear="right" />
    4. Select the Device Category and Device target matching your hardware.

        - Device Category: 
            - `Frsky 900 MHz`

        - Device:
            - `FrSky R9M 900MHz TX`
            - `FrSky R9M Lite 900MHz TX`

    5. Set the Flashing Method to `Stock_BL`

        <figure markdown>
        ![via BL](../../assets/images/Method_TX_StockBL.png)
        </figure>

    6. Set the [firmware options](../firmware-options.md) for your device.
        - Regulatory Domain (Mandatory. Choose the domain appropriate for the location or country you're flying).
        - Binding Phrase (Optional, but Highly Recommended. Note this phrase as it should be the same on your other devices, or they will not bind or sync).

    7. Click the ++"Build"++ button.

        <figure markdown>
        ![Build]
        </figure>
        
    8. Wait for the process to finish. A Green Success bar will show up in the ExpressLRS Configurator.

    9. A Temp folder will open up with the **firmware.elrs** file. Copy-paste the firmware.elrs file into your Radio's SD Card (preferably to the `/FIRMWARE` folder for easy access).

    10. On your radio, open the System Menu. 

        - On newer radios, you can press the ++"SYS"++ key to open the System Menu
        - On older radios, or radios that only have a menu key, long-press the ++context-menu++ key to open the System Menu

    11. Using the ++"Page"++ key/s, navigate to the SD-HC Card page, scroll-down and open the `FIRMWARE` folder where you can find the **firmware.elrs** file.

    12. Highlight the file and press-hold the ++"Enter"++ button and select "Flash External ELRS". Wait for the firmware to be written.

        ??? tip "No Sync"
            - Make sure you have updated the OpenTX/EdgeTX firmware of your radio to a newer version
            - Make sure the current model selected on the radio is set up for ExpressLRS Use. See the [Radio Preparation] guide.

    13. With the [ExpressLRS Lua Script] in the System Menu's Tools page, verify if the firmware version has been updated.

=== "via STLink"

    <figure markdown>
    ![via STLink](../../assets/images/Method_TX_STLink.png)
    </figure>

    !!! warning "Warning"
        This method is an **irreversible** one. You will not be able to go back to Frsky firmware with this method. You have been warned!

    1. Carefully disassemble your TX Module to get access to the mainboard.

    2. Connect your STLink V2 dongle to the pads shown in the images below:

        <figure markdown>
        ![R9M-stlink](https://raw.githubusercontent.com/ExpressLRS/ExpressLRS-hardware/master/img/FrSky%20R9M%20(2018%20model)%20st%20link%20connection.png)
        <figcaption>R9M STLink Connection</figcaption>
        </figure>

        <figure markdown>
        ![R9M Lite](https://raw.githubusercontent.com/ExpressLRS/ExpressLRS/de61d9f59d5b606ccd5b92ceb5f666d33646c938/img/stlink_connection_r9m_lite.JPG)
        <figcaption>R9M Lite STLink Connection</figcaption>
        </figure>

        <figure markdown>
        ![R9M Lite Pro](../../assets/images/R9LitePro-STLINK.jpg)
        <figcaption>R9M Lite Pro STLink Connection</figcaption>
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
            - `Frsky 900 MHz`

        - Device:
            - `FrSky R9M 900MHz TX`
            - `FrSky R9M Lite 900MHz TX`
            - `FrSky R9M Lite Pro 900MHz TX`

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

[Configurator Release]: ../../assets/images/ConfiguratorRelease.png
[Flash]: ../../assets/images/BuildFlash.png
[Build]: ../../assets/images/Build.png
[Radio Preparation]: tx-prep.md
[ExpressLRS Lua Script]: firmware-version.md#via-lua-script
