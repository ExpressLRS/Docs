---
template: main.html
---

![Setup-Banner](https://raw.githubusercontent.com/ExpressLRS/ExpressLRS-hardware/master/img/quick-start.png)

## Flashing NamimnoRC Voyager

Following are the flashing methods for NamimnoRC Voyager

### <span class="custom-heading" data-id="1">Flashing via WiFi</span>
??? Note "Flashing via WiFi"

    - Target: `NamimnoRC_Voyager_900_TX_via_WiFi`

    - Device Category: `NamimnoRC VOYAGER 900 MHz`

    - Device: `NamimnoRC VOYAGER 900 TX`

    <figure markdown>
    ![via WiFi](../../assets/images/Method_TX_WiFi-stm.png)
    <figcaption>Flashing via WiFi</figcaption>
    </figure>

    #### <span class="custom-heading" data-id="2">Method 1</span>
    ??? Note "Method 1"

        1. Select the correct target and set [Firmware Options] using the ExpressLRS Configurator.
        2. **Build** your firmware using the ExpressLRS Configurator.

            <figure markdown>
            ![Build]
            </figure>

        3. Once done, it should open the Target folder for you where the `firmware.elrs` file is. 
        4. Do not close this window so you can easily locate the correct file to upload to the module.
        5. STM32-based TX modules require a separate ESP "backpack" device for Wifi Flashing/Updating. 
        6. Attach the module to your JR Bays and power it up. 
        7. Connect to the `ESP Wifi Manager` Hotspot that the device will activate. 
        8. Once connected, navigate to http://elrs_tx.local/.

            <figure markdown>
            ![Wifi Manager](../../assets/images/WifiManager.png)
            </figure>

        9. Press `Configure WiFi` and set your home network SSID and password. This will enable your Tx Module to connect to your local home network.
        10. On your browser, refresh the http://elrs_tx.local/ and scroll towards the STM32 Firmware Update section, as shown below:

            <figure markdown>
            ![STM32 Firmware Update](../../assets/images/STM32-updater.png)
            </figure>

        11. Drag-and-drop the `firmware.elrs` file created by the ExpressLRS Configurator into the "Choose File" field, or manually navigate to the folder and select the file but change the offset to _0x4000_.
        12. click `Upload` and `Flash` STM32. Wait for the process to complete (approx. 1 minute).
        13. Close and relaunch the script.
        14. Verify the version and hash in the main screen of the [ExpressLRS Lua] script.

    #### <span class="custom-heading" data-id="3">Method 2</span>
    ??? Note "Method 2"

        1. STM32-based TX modules require a separate ESP "backpack" device for Wifi Flashing/Updating. 
        2. Attach the module to your JR Bays and power it up. 
        3. Connect to the `ESP Wifi Manager` Hotspot that the device will activate. 
        4. Once connected, navigate to http://elrs_tx.local/.

            <figure markdown>
            ![Wifi Manager](../../assets/images/WifiManager.png)
            </figure>

        5. Press `Configure WiFi` and set your home network SSID and password. This will enable your Tx Module to connect to your local home network.
        6. Select the correct target and set [Firmware Options] using the ExpressLRS Configurator.
        7. **Build and Flash** your firmware using the ExpressLRS Configurator.
        8. Wait for the process to complete. You should see a section as pictured below and the Success message marking the update process complete.

            <figure markdown>
            ![Build & Flash]
            </figure>

            <figure markdown>
            ![Wifi Update Log](../../assets/images/WifiUpdateLog.png)
            </figure>

        9. Verify the version and hash in the main screen of the [ExpressLRS Lua] script.

### <span class="custom-heading" data-id="4">Flashing via OpenTX Radio</span>
??? Note "Flashing via OpenTX Radio"

    - Target: `NamimnoRC_Voyager_900_TX_via_WiFi`

    - Device Category: `NamimnoRC VOYAGER 900 MHz`

    - Device: `NamimnoRC VOYAGER 900 TX`

    <figure markdown>
    ![via WiFi](../../assets/images/Method_TX_WiFi-stm.png)
    <figcaption>Flashing via WiFi</figcaption>
    </figure>

    1. Select the correct target and set [Firmware Options] using the ExpressLRS Configurator.
    2. **Build** your firmware using the ExpressLRS Configurator.

        <figure markdown>
        ![Build]
        </figure>

    3. Once done, it should open the Target folder for you where the `NamimnoRC_Voyager_900_TX-<version>.elrs` file is. 
    4. Do not close this window so you can easily locate the correct file to upload to the module.
    5. Copy the `NamimnoRC_Voyager_900_TX-<version>.elrs` file into your radio's SD Card `/FIRMWARE` folder.
    6. Once copied, navigate to the `/FIRMWARE` Folder on your Radio and select/highlight the `NamimnoRC_Voyager_900_TX-<version>.elrs` file, long-press the Enter key and select `Flash external ELRS`. 
    7. Flashing will then commence and after a few seconds, the radio should show a `Flash Successful` message and you're done!
    8. Verify the version and hash in the main screen of the [ExpressLRS Lua] script.

### <span class="custom-heading" data-id="5">Flashing via STLink</span>
??? Note "Flashing via STLink"

    - Target: `NamimnoRC_Voyager_900_TX_via_STLINK`

    - Device Category: `NamimnoRC VOYAGER 900 MHz`

    - Device: `NamimnoRC VOYAGER 900 TX`

    <figure markdown>
    ![via STLink](../../assets/images/Method_TX_STLink.png)
    <figcaption>Flashing via STLink</figcaption>
    </figure>

    !!! attention 
        Only use this method if the firmware has been corrupted.

    1. Disassembling the module by unscrewing the 4 screws at the rear of the module with a 1.5mm hex wrench. 
    2. Carefully separate the parts of the module and detach the cable from the main PCB.

        <figure markdown>
        <img class="center-img" src="https://github.com/ExpressLRS/ExpressLRS-Hardware/blob/master/img/namimnoback.jpg?raw=true" width="30%">
        </figure>

        <figure markdown>
        <img class="center-img" src="https://github.com/ExpressLRS/ExpressLRS-Hardware/blob/master/img/cable.jpg?raw=true" width="30%">
        </figure>

    3. Wire your `STLink v2` to the module's pins as shown below:

        <figure markdown>
        <img class="center-img" src="https://github.com/ExpressLRS/ExpressLRS-Hardware/blob/master/img/namimnopinout.png?raw=true" width="40%">
        </figure>

    4. With the module connected shown above, and your configuration set, hit **Build & Flash** in the ExpressLRS Configurator and wait for the process to finish.

        <figure markdown>
        ![Build & Flash]
        </figure>

    5. Once the Success Message appears, remove/unsolder the STLink, re-assemble the module, and place it in your Radio's Module Bay.
    6. If the Radio has CRSF selected, the light should turn green meaning the module has communication with your radio.
    7. Use the ExpressLRS Lua script to verify that the Version Number and Hash are displayed at the bottom, along with the options you set. If "Loading" is displayed at the top, check if External Module is set to CRSF for the selected model in your radio, and that the internal RF module is turned off.

    !!! Note
        For further troubleshooting, refer to the [General Troubleshooting](../troubleshooting.md#general-troubleshooting).

[Build]: ../../assets/images/Build.png
[Build & Flash]: ../../assets/images/BuildFlash.png
[Firmware Options]: ../firmware-options.md
[Radio Preparation]: tx-prep.md
[ExpressLRS Lua]: lua-howto.md
[General Troubleshooting]: ../troubleshooting.md#general-troubleshooting

<script src="../../../assets/javascripts/admonition-enhancement.js"></script>