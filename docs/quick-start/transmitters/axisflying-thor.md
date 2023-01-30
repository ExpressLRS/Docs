---
template: main.html
---

![Setup-Banner](https://raw.githubusercontent.com/ExpressLRS/ExpressLRS-hardware/master/img/quick-start.png)

!!! danger "Flashing ExpressLRS 3.x Firmware"
    1. If flashing/updating for the first time from the factory firmware or an older firmware, flash the module to version 2.5.1.
    2. Use the [Repartitioner](https://github.com/ExpressLRS/repartitioner) binary [file](https://github.com/ExpressLRS/repartitioner/releases/download/1.0/repartitioner.bin) (right click, save as/save file as) to flash it.
        - If Target Mismatch error appears, click `Flash Anyway`.
    3. Follow method 1 or 2 from the WiFi Flashing Guide to flash to the 3.x firmware.
    
    !!! info "Repartitioner is not necessary when flashing via USB/UART."

    **Reference**: Joshua Bardwell's video on the topic can be found [here](https://www.youtube.com/watch?v=2kcRi1cHejM).

## Flashing Axisflying Thor

Following are the flashing methods for Axisflying thor.

### <span class="custom-heading" data-id="1">Flashing via WiFi</span>
??? Note "Flashing via WiFi"

    - Target: `AXIS_THOR_2400_TX_via_WIFI`

    - Device Category: `AXIS 2.4 GHz`

    - Device: `AXIS THOR 2400TX`

    <figure markdown>
    ![via WiFi](../../assets/images/Method_TX_WiFi.png)
    <figcaption>Flashing via WiFi</figcaption>
    </figure>

    !!! attention
        The methods below apply+ if you've already updated your Tx modules to 2.x. For modules still in firmwares pre 2.x, you should use 1.x WiFi flashing method to update to 2.x. Or update to 2.x via USB instead.

    #### <span class="custom-heading" data-id="2">Method 1</span>
    ??? Note "Method 1"

        1. Select the correct target and set [Firmware Options] using the ExpressLRS Configurator.
        2. Build the firmware, which will open the Target folder where the `AXIS_THOR_2400_TX-<version>.bin` file is located. Do not close this window so you can easily locate the correct file to upload to the module.

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
        9. Drag and drop the firmware file, `AXIS_THOR_2400_TX-<version>.bin`, created by the ExpressLRS Configurator. Alternatively, use the `Choose File` button to select the file from the folder where the firmware was created.
        10. Ensure that you have selected the correct firmware file and click `Update`.
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
        2. Build the firmware, which will open the Target folder where the `AXIS_THOR_2400_TX-<version>` file is located. Do not close this window so you can easily locate the correct file to upload to the module.

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

        7. Drag-and-drop the `AXIS_THOR_2400_TX-<version>` file created by the ExpressLRS Configurator into the "Choose File" field, or manually navigate to the folder and select the file.
        8. Click the "Update" button. Wait for the process to complete (approx. 1 minute).
        9. Verify the version and hash in the main screen of the ExpressLRS Lua script.

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

    - Target: `AXIS_THOR_2400_TX_via_UART`

    - Device Category: `AXIS 2.4 GHz`

    - Device: `AXIS THOR 2400TX`

    <figure markdown>
    ![via UART](../../assets/images/Method_TX_UART.png)
    <figcaption>Flashing via UART</figcaption>
    </figure>

    1. Attach a USB Data Cable to your module and computer.
    2. Windows users may need to install the [CP210x Drivers](https://www.silabs.com/developers/usb-to-uart-bridge-vcp-drivers) to ensure the device is properly recognized and initialized.

        !!! tip "Important"
            Check Device Manager on your Windows system before proceeding. Ensure the correct drivers are installed. Some Linux distros might also need drivers. The drivers can be downloaded [here](https://www.silabs.com/developers/usb-to-uart-bridge-vcp-drivers).

        <figure markdown>
        ![CP210x Drivers](../../assets/images/CP210xDriverDownload.png)
        </figure>

        !!! note
            To flash the TX itself, the switch on the back side of the module must be set to the **leftmost** position. To flash the TX backpack, the switch must be set to the **rightmost** position. For normal operation, the switch must be **centered**.
        
        <figure markdown>
        <img class="center-img" src="../../../assets/images/thor-switch.png" width="30%">
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

    6. Close and relaunch the script.
    7. Verify the version and hash in the main screen of the ExpressLRS Lua script.


## Using the module on a DX9

- Install the latest DX9 firmware with CRSF v2 support via Serial port.
- Wire up Power (Vbat & GND) as per Crossfire install instructions.
- Use Signal from DX9 to S.Port pin of the Thor TX module.
- Optional: Connect an external power source via XT30.
- Flash the TX module with `UART_INVERTED` **unchecked**.
- Adjust your Packet Rate to 250Hz using the Screen & Joystick.

## Acknowledgement

This guide is contributed by discord user ChaserP.

[ExpressLRS Lua script]: https://github.com/ExpressLRS/ExpressLRS/blob/3.x.x-maintenance/src/lua/elrsV3.lua?raw=true
[Build]: ../../assets/images/Build.png
[Build & Flash]: ../../assets/images/BuildFlash.png
[Firmware Options]: ../firmware-options.md

<script src="../../../assets/javascripts/admonition-enhancement.js"></script>