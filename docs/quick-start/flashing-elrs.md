---
template: main.html
---

![Setup-Banner](https://raw.githubusercontent.com/ExpressLRS/ExpressLRS-hardware/master/img/quick-start.png)

Now that you've installed the bootloader on your non-ELRS hardware and have set up your user defines it's time to flash your hardware. Your configurator window should look something like this:

![Configurator](https://raw.githubusercontent.com/ExpressLRS/ExpressLRS-Hardware/master/img/wiki/configurator%20setup.png)

*Notes: The Compiling and Firmware build will take a while the first time. It could take up to 10 minutes if there aren't any issues. Ensure you are connected to the Internet and aren't behind any firewalls that could prevent data transfer from Github, or platformIO dependency repositories. Also note that the process will use up some disk space for these libraries as well as Memory (RAM) and CPU cycles.*

## Non-ELRS Hardware
### FrSky TXes 
#### Flashing via OpenTX (Requires OpenTX 2.3.12)

Using **Build** in the ExpressLRS Configurator, wait for the firmware to be compiled. After that's done, ExpressLRS Configurator Log should show the Success Message, and it will automatically open the folder where the **firmware.elrs** can be found. Put (copy-paste) the firmware.elrs to your Radio's SD Card (preferably to the `/FIRMWARE` folder for easy access). Once on your radio, navigate to the `/FIRMWARE` folder, select the firmware.elrs and click-hold the Enter button and select "Flash External ELRS".

By this point, the bootloader (r9m_elrs_bl.frk) should've been flashed already. Wait for the flashing to finish, and if your module is equipped with a speaker (full size R9Ms), you should hear the tune and two beeps (if external module is now set to CRSF protocol).

#### Flashing using STLink

With the module connected as described in [Flashing Bootloader](../flashing-bootloader), and your configuration set, hit **Build & Flash** in the ExpressLRS Configurator and wait for the process to finish. Once that's done, and the Success Message showing, you can now remove/unsolder the STLink, and re-assemble the module, and put it into your Radio's Module Bay. The ExpressLRS tune should play and then two beeps after that can be heard, for units that has a speaker (R9Ms) and if the External Module is set to CRSF Protocol.

Verification can be done using the ELRS.lua script. It should show the Version Hash at the top, as well as the options you can set. If it's showing "Connecting", check if External Module is set to CRSF for the selected model in your radio, and that internal RF module is set to off. See general Troubleshooting section for other ways to determine your module is flashed and ready for flying.

### FrSky RXes  
![FC Wiring](/assets/images/FC-Wiring.jpg)
*Note: This will be the same wiring you'll use for flying and the next firmware updates (via Passthrough). Forget the factory wiring guide!*

#### Passthrough Flashing (works with Betaflight, iNav)

Make sure the correct [Bootloader](../flashing-bootloader) has been flashed to the receiver prior to wiring it up to your flight controller. Using the wiring guide above, find a free, uninverted UART in your FC. You can use your FC's wiring guide for a Crossfire or Ghost receiver.

Once wired to your FC, connect USB. Did your receiver powered up too (with both LEDs lit)? If so, disconnect USB, hold the bind button on your receiver, and reconnect to USB. The LED should start alternating between the Green and Red LEDs. Once it's alternating, you can then let go of the Bind Button.

If your receiver didn't get powered from USB, have a lipo ready and continue with the next steps. On the ExpressLRS Configurator, with your Options set, click on **Build & Flash**. Like on the TX module, it will take a while on the first time. Watch out for the `Passthrough Init` stage. This stage will check your FC Configuration for the Serial RX UART (Software Inversion via "set serialrx_inverted" and Half Duplex mode via "set serialrx_halfduplex" will be checked; both should be off.)

If `Retry... ` lines appear, connect a LiPo if your receiver isn't powered by the USB (i.e. power up your receiver and FC).

Wait for this process to finish. It's done once the "Success" prompt is shown.

#### Flashing via STLink (only recommended as last resort)

This method is irreversible. It will remove the ability to reflash back to Frsky firmware. You have been warned!
Make sure your STLink dongle is properly recognized by your System as such (Drivers are installed, etc.).

Disable 'Readout Protection'. To do this download the [ST-LINK Utility](https://www.st.com/en/development-tools/stsw-link004.html) and follow this quick [how to video](https://youtu.be/SEYQ1HpRmk0). Or alternatively under linux you can use <a href="/software/open-ocd">OpenOCD</a>. 

Connect your STLink to the receiver as shown in the wiring guides below. You'll need the GND, DIO (Data), CLK (Clock) and 3.3v.

<small>r9mm/r9mini</small>
<img src="https://raw.githubusercontent.com/ExpressLRS/ExpressLRS-Hardware/master/Doc/r9mm_mini_pinout.png" width="60%" alt="r9mm/r9mini STLink connection" />

<small>r9mx</small>
<img src="/Website/assets/images/r9mxstlink.png" alt="r9mx STLink connection" />

Using the correct target specific for your receiver, hit "Build & Flash".

Once done, wire your receiver to your Flight Controller. Passthrough flashing can now be used for updating the receiver.


### Jumper RX  
Disable 'Readout Protection'. To do this download the [ST-LINK Utility](https://www.st.com/en/development-tools/stsw-link004.html) and follow this quick [how to video](https://youtu.be/SEYQ1HpRmk0). Or alternatively under linux you can use <a href="/software/open-ocd">OpenOCD</a>.

Using the correct target specific for your receiver, hit "Build & Flash".

<img src="https://raw.githubusercontent.com/ExpressLRS/ExpressLRS-hardware/master/img/r900mini-rx/r900mini-side2-closeup.jpg" width = "60%" alt = "R900 wiring diagram">

After the flash is successful, desolder the STLink and connect RX2 and TX2 (you will need to solder on the STM32 pins, see picture) to a flight controller and setting up the receiver with the CRSF serial protocol, the `env:Jumper_RX_R900MINI_via_Passthrough` target may now be used for future uploads through Betaflight Passthrough.


### ImmersionRC RXes  
TODO

### ImmersionRC TXes  
TODO

### SIYI FM30 TX
TODO

### SIYI FRmini RX
TODO

## ELRS Hardware
### Happymodel TX
#### ES900TX

(ES915TX/ES868TX)

TODO

#### ES24TX (inc. Lite)
##### Flashing via WiFi

**Build** your firmware using the ExpressLRS Configurator. Once it's done, it should open the Target folder for you where the `firmware.bin` file is. Do not close this window so you can easily locate the correct file to upload to the module.

The next steps will require the [ELRS Lua Script](https://github.com/ExpressLRS/ExpressLRS/blob/master/src/lua/ELRS.lua?raw=true) (right-click, save as). Download the ELRS.lua script and save it to your Radio's `/Scripts/Tools` folder. Insert/attach your module into your module bay and make sure it's not loose and there's proper connection with the radio. Execute the ELRS.lua script by pressing "System Menu" in your radio and then under Tools, select ELRS.lua.

![Lua Script](https://github.com/ExpressLRS/ExpressLRS-Hardware/raw/master/img/wiki-from-discord/lua1.jpeg)
![Lua Script T16](https://github.com/ExpressLRS/ExpressLRS-Hardware/raw/master/img/wiki-from-discord/lua2)

At first, it will show "Mismatch"; it's normal. Tap `Enter` once on your radio to "Force Use" the script. If it's showing a "Connecting" message, then recheck the connection of the module to your radio.

Select "Wifi Update" from the lua script. Lua script will instruct you to go to a specific Ip Address, but you have to first connect to the Wifi Hotspot it created. It will show up in your network as `ExpressLRS TX Module`, and the password is simply `expresslrs`.

Using your browser, navigate to the correct page (typically http://10.0.0.1/) and it should show an upload form (you will have to scroll down a bit). You can drag-and-drop the firmware.bin file from the folder that ExpressLRS Configurator opened for you, or you can manually navigate to it via the `Browse` or `Choose File` button on the Upload form. Click on Update once and the update process should commence. Take note that you should be taking a TX firmware.bin file. The folder name where you can get this file is the same as the Target you have selected in the ExpressLRS Configurator.

Once the file is uploaded, the webserver should load a White page, with the message **Update Success! Rebooting...**

As it rebooted, the connection to the Webserver got terminated. Check via the Lua Script whether you have successfully updated the TX module. The first line of the lua script should show a 6-character hash that corresponds to the Git commit hash for the firmware version you have on the module. There should be no more "Mismatch" messages as well.

##### Flashing via USB/UART

This method requires you move two jumpers into specific pins in the module board. See the following image for the jumper location and which pin should be bridged for this method to work.

![JumperFS](/assets/images/Jumper.jpg)
![JumperLite](/assets/images/Jumper-Lite.jpg)

The jumpers should be moved into the USB/UART (Green) position from the image above. Attach your USB cable into the module and your computer. [CP210x Drivers](https://www.silabs.com/developers/usb-to-uart-bridge-vcp-drivers) will have to be installed for this to work properly (Windows). Make sure your computer recognizes the module as a USB-to-UART Bridge device, otherwise, this method will not work.

Using the ExpressLRS Configurator with the correct Target selected and options set, hit **Build & Flash**. Wait for the process to finish, and you should be greeted with the "Success" message.

Assemble the module back together and attach it to your radio module bay and verify with the [ELRS.lua](https://github.com/ExpressLRS/ExpressLRS/blob/master/src/lua/ELRS.lua?raw=true) script if you have successfully updated your module.

### Happymodel RX
#### Happymodel ES900RX
TODO

#### Happymodel EP RXes
![EP1 connection](/assets/images/ep1boot.png)
![EP2 connection](/assets/images/ep2boot.png)

- Flashing via Wifi (Recommended as first-flash method)

Wire up your receiver to a free uart in your Flight Controller. The image above shows the pinouts for these receivers. Wire TX on receiver to an RX pad on the FC, and the RX on receiver to a TX pad on the FC in the same UART. Wire 5v and Gnd as normal (5v to a 5v pad on FC and Gnd to a Gnd pad on the FC).

*Note: There are Flight Controllers that will pull the RX pads `LOW` which will put the ESP-based receivers into `Bootloader Mode` unintentionally. A solid LED light on these receivers even with the TX module off is a sign they are in Bootloader Mode. If this is the case, rewire the receiver to a different UART.*

**Build** the firmware using the ExpressLRS Configurator using the correct Target and options. Once done, it should open a new window where the `firmware.bin` is. Do not close this window so you can easily navigate to it once it's time to upload the firmware into the receiver.

Power your Flight Controller by either connecting a LiPo or attaching the USB cable (if receiver gets powered from USB via a 4v5 pad). Receiver's LED will blink slow at first, and after 20s or 30s (can be adjusted via ExpressLRS Configurator using `AUTO_WIFI_ON_INTERVAL`), it should blink fast indicating it's on Wifi Hotspot Mode.

Connect to the Wifi Network the receiver has created. It should be named something like `ExpressLRS RX` with the same `expresslrs` password as the TX Module Hotspot. Navigate to the same web address as the TX Module (usually http://10.0.0.1). The Firmware upload page should load, and using the File Upload Form, navigate where the correct Receiver `firmware.bin` is (like with the Tx module, you can also drag-and-drop the firmware file into the form field or use the `Browse` or `Choose File` button). Click on **Update** button and the firmware file will be uploaded and the update process should commence. 

A white page should load momentarily with the message **Update Success! Rebooting...**. Wait a little bit and the receiver should be updated. Power cycle and your module and receiver should now be bound (given you have updated the Tx Module as well, and that they have the same binding phrase and options).

- Flashing via Passthrough

Wire up your receiver to a free uart in your Flight Controller. The image above shows the pinouts for these receivers. Wire TX on receiver to an RX pad on the FC, and the RX on receiver to a TX pad on the FC in the same UART. Wire 5v and Gnd as normal (5v to a 5v pad on FC and Gnd to a Gnd pad on the FC).

You will need to bridge the `Boot` pads on the receiver the first time you'll be updating via this method. The image above shows where the `Boot` pads are. A solid LED indicates the receiver is in `Bootloader` mode when the TX module is OFF (Solid LED also indicates Radio+module & Receiver is bound and has connection). 

*Note: if you haven't bridged the `Boot` pads but the receiver has solid LED light, your FC is probably pulling the current UART's RX pad `LOW` which will interfere with the normal and passthrough flashing of this receiver. Find another UART and wire your receiver there instead*

Bridging the `Boot` pads is no longer needed past 1.0.0-RC6. 

Power your FC with a LiPo, or if receiver is powered via USB (receiver is connected to a 4v5 pad), connect the FC to your USB port. Using the ExpressLRS Configurator, with the correct Target selected and options set, click on **Build & Flash**. Wait for the process to finish and you should be greeted with the "Success" banner.

Unplug USB and LiPo, and removed the solder on the bridged `Boot` pads. You no longer need it (past 1.0.0-RC6). Power your TX Module and then your FC to verify you are bound and has connection.

#### Happymodel PP RXes
The PP receivers do not have Wifi, and so, it can only be updated via Passthrough. 

Follow the same wiring as that of the EP receivers. The PP has a silkscreened "RT5G" on one of its side indicating the order of the pads, with R = Rx, T = Tx, 5 = 5v and G = Gnd,  respectively. Connect the Rx pad to a Tx pad on the FC, and the Tx pad to an RX pad on the FC, with 5v and Gnd to their usual connections.

The PP **doesn't** have a `Boot` pad either so there's no need to bridge any pads.

Once wired, power up your FC by connecting a LiPo or, if the receiver is getting powered via USB, connect your USB cable to a vacant port.

Using the ExpressLRS Configurator, with the correct Target selected and options set, hit **Build & Flash**. Wait a bit for the process to finish and you should see a "Success" banner. 

Power-cycle the FC and verify receiver connects to the Tx module (power up the Tx first, then the Receiver).


## DIY Hardware
### DIY 2.4G TXes  
TODO


### DIY 2.4G RXes  
TODO

### DIY 900M RXes  
TODO