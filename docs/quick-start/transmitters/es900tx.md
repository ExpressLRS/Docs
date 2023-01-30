---
template: main.html
---

![Setup-Banner](https://raw.githubusercontent.com/ExpressLRS/ExpressLRS-hardware/master/img/quick-start.png)

## Flashing ES900TX

Following are the flashing methods for ES900TX.

!!! danger "Flashing ExpressLRS 3.x Firmware"
    1. If flashing/updating for the first time from the factory firmware or an older firmware, flash the module to version 2.5.1.
    2. Use the [Repartitioner](https://github.com/ExpressLRS/repartitioner) binary [file](https://github.com/ExpressLRS/repartitioner/releases/download/1.0/repartitioner.bin) (right click, save as/save file as) to flash it.
        - If Target Mismatch error appears, click `Flash Anyway`.
    3. Follow method 1 or 2 from the WiFi Flashing Guide to flash to the 3.x firmware.
    
    !!! info "Repartitioner is not necessary when flashing via USB/UART."

    **Reference**: Joshua Bardwell's video on the topic can be found [here](https://www.youtube.com/watch?v=2kcRi1cHejM).

### <span class="custom-heading" data-id="1">Flashing via WiFi</span>
??? Note "Flashing via WiFi"

    - Target: `HappyModel_TX_ES900TX_via_WIFI`

    - Device Category: `Happymodel 900 MHz`

    - Device: `HappyModel TX ES900TX`

    <figure markdown>
    ![via WiFi](../../assets/images/Method_TX_WiFi.png)
    <figcaption>Flashing via WiFi</figcaption>
    </figure>

    !!! attention
        The methods below applies if you've already updated your Tx modules to 2.x. For modules still in firmwares pre 2.x, you should use [1.x WiFi flashing method](https://www.expresslrs.org/1.0/quick-start/tx-es900tx/) to update to 2.x. Or update to 2.x via USB instead.

    #### <span class="custom-heading" data-id="2">Method 1</span>
    ??? Note "Method 1"

        1. Select the correct target and set [Firmware Options] using the ExpressLRS Configurator.
        2. Build the firmware, which will open the Target folder where the `HappyModel_TX_ES900TX-<version>.bin` file is located. Do not close this window so you can easily locate the correct file to upload to the module.

            <figure markdown>
            ![Build]
            </figure>

        3. Download the [ExpressLRS Lua script] (right-click, save as) and save it to your Radio's `/Scripts/Tools` folder.
        4. Insert the module into the module bay and make sure it's securely connected to the radio (see the [Radio Preparation](tx-prep.md) page).
        5. Execute the ExpressLRS Lua script by going to "System Menu" on your radio, then under Tools, select `ExpressLRS`.

            <figure markdown>
            ![Lua Script](../../assets/images/lua1.jpg)
            </figure>

            <figure markdown>
            ![Lua Script T16](../../assets/images/lua2.jpg)
            </figure>

            !!! Info "Troubleshooting the ExpressLRS Lua Script"
                If you encounter an issue where the script is stuck at `Loading...`, please refer to the [troubleshooting guide](http://localhost:8000/quick-start/troubleshooting/#expresslrs-lua-script-is-stuck-at-loading) for help.

            <figure markdown>
            ![Lua3](../../assets/images/lua3.jpg)
            </figure>

        6. From the ExpressLRS Lua script, select "WiFi Connectivity" and then "Enable WiFi". Confirm by pressing OK.

            <figure markdown>
            ![Lua4](../../assets/images/lua/wifi-bw.png)
            </figure>

        7. Connect to the Access Point created by the module, named `ExpressLRS TX`, using the password `expresslrs`.

            <figure markdown>
            ![WiFi Hotspot](../../assets/images/WifiHotspotTX.png)
            </figure>

        8. Open your browser and navigate to http://10.0.0.1/ to access the upload form. Scroll down to find the form.
        9. Drag and drop the firmware file, `HappyModel_TX_ES900TX-<version>.bin`, created by the ExpressLRS Configurator. Alternatively, use the `Choose File` button to select the file from the folder where the firmware was created.
        10. Ensure that you have selected the correct firmware file and click `Update`.

            <figure markdown>
            ![Firmware Update](../../assets/images/web-firmwareupdate.png)
            </figure>

        11. Once the file is uploaded, a pop-up confirmation will show up.

            <figure markdown>
            ![Update Success](../../assets/images/web-firmwareupdateSuccess.png)
            </figure>
            
        12. Wait for the confirmation pop-up and for the "WiFi Running" screen to close.
        13. Close and relaunch the script.
        14. Verify the firmware version and hash in the main screen of the ExpressLRS Lua script.

        !!! info
            You can configure Home Network SSID and Password if you chose not to use ExpressLRS Configurator to set them. Once these are set, you can use the next two methods below.

        <figure markdown>
        ![JoinNetwork](../../assets/images/web-joinnetwork.png)
        </figure>

    #### <span class="custom-heading" data-id="3">Method 2</span>
    ??? Note "Method 2"

        1. Select the correct target and set [Firmware Options] using the ExpressLRS Configurator.
        2. Build the firmware, which will open the Target folder where the `HappyModel_TX_ES900TX-<version>.bin` file is located. Do not close this window so you can easily locate the correct file to upload to the module.

            <figure markdown>
            ![Build]
            </figure>

        3. Using the [ExpressLRS Lua script] (right-click, save as), select "WiFi Connectivity" and then "Enable WiFi". Confirm by pressing OK.

            <figure markdown>
            ![Lua4](../../assets/images/lua/wifi-bw.png)
            </figure>

        4. If you have previously set up your Tx Module with your home WiFi network details, it will connect automatically.
        5. Using a browser, navigate to http://elrs_tx.local.
        6. The WiFi Update page will appear. Scroll down to the "Firmware Update" section.

            <figure markdown>
            ![Firmware Update](../../assets/images/web-firmwareupdate.png)
            </figure>

        7. Drag-and-drop the `HappyModel_TX_ES900TX-<version>.bin` file created by the ExpressLRS Configurator into the "Choose File" field, or manually navigate to the folder and select the file.
        8. Click the "Update" button. Wait for the process to complete (approx. 1 minute).
        9. Close and relaunch the script.
        10. Verify the version and hash in the main screen of the ExpressLRS Lua script.

    #### <span class="custom-heading" data-id="4">Method 3</span>
    ??? Note "Method 3"

        1. Using the [ExpressLRS Lua script] (right-click, save as), select "WiFi Connectivity" and then "Enable WiFi". Confirm by pressing OK.

            <figure markdown>
            ![Lua4](../../assets/images/lua/wifi-bw.png)
            </figure>

        2. If you have previously set up your Tx Module with your home WiFi network details, it will connect automatically.
        3. Select the correct target and set [Firmware Options] using the ExpressLRS Configurator.
        4. Click **Build and Flash**. Wait for the compile process to complete.

            <figure markdown>
            ![Build & Flash]
            </figure>

        5. Once done, you should see a Success message, marking the update process complete.

            <figure markdown>
            ![Wifi Update Log](../../assets/images/WifiUpdateLog.png)
            </figure>

        6. Close and relaunch the script.
        7. Verify the version and hash in the main screen of the ExpressLRS Lua script.

### <span class="custom-heading" data-id="5">Flashing via USB/UART</span>
??? Note "Flashing via USB/UART"

    - Target: `HappyModel_TX_ES900TX_via_UART`

    - Device Category: `Happymodel 900 MHz`

    - Device: `HappyModel TX ES900TX`

    <figure markdown>
    ![via UART](../../assets/images/Method_TX_UART.png)
    <figcaption>Flashing via UART</figcaption>
    </figure>

    This method requires you to move two jumpers into specific pins in the module board. See the following image for the jumper location and which pin should be bridged for this method to work. The 2 bottom-most dipswitches should be moved into the position as shown in the following image. 

    <figure markdown>
    ![JumperES900](../../assets/images/Jumper-es900tx.png)
    </figure>

    1. Attach a USB Data Cable to your module and computer.
    2. Windows users may need to install the [CP210x Drivers](https://www.silabs.com/developers/usb-to-uart-bridge-vcp-drivers) to ensure the device is properly recognized and initialized.

        !!! tip "Important"
            Check Device Manager on your Windows system before proceeding. Ensure the correct drivers are installed. Some Linux distros might also need drivers. The drivers can be downloaded [here](https://www.silabs.com/developers/usb-to-uart-bridge-vcp-drivers).

        <figure markdown>
        ![CP210x Drivers](../../assets/images/CP210xDriverDownload.png)
        </figure>

    3. Select the correct target and set [Firmware Options] using the ExpressLRS Configurator.
    4. Click **Build and Flash**. Wait for the compile process to complete.

        <figure markdown>
        ![Build & Flash]
        </figure>

    5. Once done, you should see a Success message, marking the update process complete.

        <figure markdown>
        ![Wifi Update Log](../../assets/images/WifiUpdateLog.png)
        </figure>

    6. Assemble the module back together (ensure the module PCB is not loose from its mounting points) and attach it to your radio module bay
    7. Close and relaunch the script.
    8. Verify the version and hash in the main screen of the ExpressLRS Lua script.

## Flashing ES915/868TX (Discontinued)

Following are the flashing methods for ES915/868TX.

### <span class="custom-heading" data-id="6">Flashing via OpenTX</span>
??? Note "Flashing via OpenTX"

    - Target: `HappyModel_TX_ES915TX_via_stock_BL`

    - Device Category: `Happymodel 900 MHz`

    - Device: `HappyModel TX ES915TX`

    <figure markdown>
    ![via BL](../../assets/images/Method_TX_StockBL.png)
    <figcaption>Flashing via Stock_BL</figcaption>
    </figure>

    1. Using **Build** in the ExpressLRS Configurator, wait for the firmware to be compiled.

        <figure markdown>
        ![Build]
        </figure>

    2. After successful compilation, the ExpressLRS Configurator Log should show a `Success` message and automatically open the folder where the **firmware.elrs** is located.
    3. Copy the firmware.elrs to the `/FIRMWARE` folder on the Radio's SD Card.
    4. On the Radio, navigate to the `/FIRMWARE` folder, select the firmware.elrs, and click-hold the Enter button. Select "Flash External ELRS".
    5. Wait for the flashing process to finish. The module will reboot and you should hear a tune and two beeps (if the external module is set to CRSF protocol).

### <span class="custom-heading" data-id="7">Flashing via STLink</span>
??? Note "Flashing via STLink"

    - Target: `HappyModel_TX_ES915TX_via_STLINK`

    - Device Category: `Happymodel 900 MHz`

    - Device: `HappyModel TX ES915TX`

    <figure markdown>
    ![via STLink](../../assets/images/Method_TX_STLink.png)
    <figcaption>Flashing via STLink</figcaption>
    </figure>

    1. Connect your STLink v2 to the pads shown in the image below.

        <figure markdown>
        ![ES915tx](../../assets/images/ES915tx.jpg)
        </figure>

    2. Connect the module as shown above and set the configuration.
    3. Click **Build & Flash** in the ExpressLRS Configurator and wait for the process to finish.

        <figure markdown>
        ![Build & Flash]
        </figure>

    4. Once the Success Message appears, remove/unsolder the STLink, re-assemble the module, and place it in your Radio's Module Bay.
    5. Verify the flash by ExpressLRS tune and hearing two beeps.
    6. Use the ExpressLRS Lua script to verify that the Version Number and Hash are displayed at the bottom, along with the options you set. If "Loading" is displayed at the top, check if External Module is set to CRSF for the selected model in your radio, and that the internal RF module is turned off.

    !!! Note
        For further troubleshooting, refer to the [General Troubleshooting](../troubleshooting.md#general-troubleshooting).

[ExpressLRS Lua script]: https://github.com/ExpressLRS/ExpressLRS/blob/3.x.x-maintenance/src/lua/elrsV3.lua?raw=true
[Build]: ../../assets/images/Build.png
[Build & Flash]: ../../assets/images/BuildFlash.png
[Firmware Options]: ../firmware-options.md
[ExpressLRS Lua]: lua-howto.md
[Radio Preparation]: tx-prep.md

<script src="../../../assets/javascripts/admonition-enhancement.js"></script>