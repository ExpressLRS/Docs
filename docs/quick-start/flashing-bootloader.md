---
template: main.html
---

![Setup-Banner](https://github.com/ExpressLRS/ExpressLRS-Hardware/raw/master/img/quick-start.png)

For hardware that requires STLink v2 flashing, this guide simply explains how to wire the given piece of hardware to the StLink before that flashing.

## FrSky Recievers
### R9mm/mini, R9mx, R9Slim+
This guide applies for the R9mm, R9mini, R9mx, R9Slim+, R9Slim+ OTA, if you have a `OpenTX` transmitter with a `SmartPort` output, you can flash your RXes bootloader.

Download the bootloader `.frk` file for your respective receiver. The files are as follows:

- R9mm/mini: [`r9mm_elrs_bl.frk`](https://github.com/AlessandroAU/ExpressLRS/blob/master/src/bootloader/r9mm_elrs_bl.frk?raw=true) (14kb) or [`r9mm_no_btn_elrs_bl.frk`](https://github.com/ExpressLRS/ExpressLRS/raw/master/src/bootloader/r9mm_no_btn_elrs_bl.frk?raw=true) (14kb) (no_btn bootloader is only used if your bind/boot button on the receiver is faulty or has gone bad, and is indicated by both LEDs (red and green) being constantly illuminated.)
- R9mx: [`r9mx_elrs_bl.frk`](https://github.com/ExpressLRS/ExpressLRS/blob/master/src/bootloader/r9mx_elrs_bl.frk?raw=true) (20kb)
- R9Slim+ (ACCST): [`r9slim_plus_elrs_bl.frk`](https://github.com/ExpressLRS/ExpressLRS/blob/master/src/bootloader/r9slim_plus_elrs_bl.frk?raw=true) (14kb)
- R9Slim+ (ACCESS/OTA): [`r9slim_plus_ota_elrs_bl.frk`](https://github.com/ExpressLRS/ExpressLRS/blob/master/src/bootloader/r9slim_plus_ota_elrs_bl.frk?raw=true) (18kb)

Copy the relevant file to your handset's SD card (You can put it inside `/FIRMWARE` folder for easy access).

Wire the receiver to your radio's Smart Port, as shown:

<img src="../../assets/images/Bootloader-Flashing.jpg" width="100%" />

<br />

Next, flash the `.frk` via the `S.port` flashing option in `OpenTX`. :zap: (It helps if the External RF module is set to `PPM` mode.) 

  * Navigate in OpenTX to the TOOLS menu (hold SYS button)
  * Page to the SD-HC CARD page, then the `FIRMWARE` folder
  * Flash the frk file by holding OK and selecting "Flash external module"

Unplug the receiver, and your bootloader is flashed. Now, wire the RX to your flight controller as shown below:
<img src="../../assets/images/FC-Wiring.jpg" width ="100%"/>


**Continue to the next page to set up your user defines.**

### R9Slim
This RX requires an StLink v2 to be flashed. 

Wire up the RX to the STLink using `+ = 3v3`, `- = GND`, `C = CLK` and `D = DIO`. 

 Then, **Continue to the next page to set up your user defines.**


## FrSky Transmitters
### R9M & R9M Lite
The R9M and R9M Lite can be flashed in a similar way to their corresponding RXes. Using an `OpenTX` transmitter, you flash the bootloader, and then flash ELRS.

Here is a quick 2 minute demo if you would rather watch a video than read the steps:
<iframe width="560" height="315" src="https://www.youtube.com/embed/DG3f-lnNlms" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>

To do this you need a new version of OpenTX - you can either use the ELRS fork or a nightly build: <a href="/faq/#why-do-i-need-to-update-opentx">FAQ: Why do I need a custom version of OpenTX?</a>

- Currently, the most stable version of OpenTX to use with ExpressLRS is 2.3.10 ExpressLRS version found here: [ExpressLRS OpenTX 2.3.10](https://github.com/ExpressLRS/ExpressLRS/tree/250-500-race-modes/OpenTX)
- If your radio isn't supported by the 2.3.10 ExpressLRS Binaries, your next best option at the moment is the OpenTX Nightly. Using the [OpenTX Nightly Companion Software](https://www.open-tx.org/2019/05/17/2.3-nightlies), download the .bin file

Flash the bin to your radio using normal OpenTX updating protocols (remember to back everything up!)

Then, with your new version of OpenTX, copy [`r9m_elrs_bl.frk`](https://github.com/ExpressLRS/ExpressLRS/blob/master/src/bootloader/r9m_elrs_bl.frk?raw=true) onto the SD card of your radio, in the `/FIRMWARE` folder.

Flash `r9m_elrs_bl.frk` (14kb) to your TX module:

  * Navigate in OpenTX to the TOOLS menu (hold SYS button)
  * Page to the SD-HC CARD page, then the `FIRMWARE` folder
  * Flash the frk file by holding OK and selecting "Flash external module"

**Done! Continue to the next page to set up your user defines.**

### R9M Lite Pro
The R9M Lite Pro must be flashed using STLINK. This is non-reversible and requires an `STLink v2`. 
That means solder your STLINK to `+ = 3v3`, `- = GND`, `C = CLK` and `D = DIO`. (`-` may also be labeled as `G`). This does not require a seperate bootloader step, so **continue to the next page to set up your user defines.** The flashing process will flash the bootloader as well as the firmware.

## Ghost Hardware
Here is a 10 minute video, showing the steps required to both flash the bootloader and the ELRS firmware itself.
<iframe width="560" height="315" src="https://www.youtube.com/embed/fHxx2Cc3Hz0" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>

Flashing the Ghost RX's is currently a **1 WAY** flash once you flash ExpressLRS to the TX you **will not** be able to use them with stock Ghost RX's (running stock firmware, they **will work** while running ELRS).  You will need a `StLink V2` to flash the TX

Wire `3.3v`, `GND`, `CLK`, and `DIO` to their respective pins on your part from the StLink. (You can power with the StLink but in the first two image the radio is used to power the module). 
<img src="https://i.imgur.com/58wxHZe.png" width = "30%">
<img src="https://i.imgur.com/vztruRj.png" width = "30%">
<img src="https://github.com/ExpressLRS/ExpressLRS-Hardware/raw/master/img/GHST_ATTO_V1.1_PINOUT.png" width = "20%">

**Done! You're ready to set up your user defines and flash the firmware to your Ghost hardware**

## Jumper R900 Mini
This also requires an STLink, so the wiring is as follows: 
Wire `+ = 3v3`, `- = GND`, `C = CLK` and `D = DIO` to their respective pins on the RX from the StLink.
<img src="https://raw.githubusercontent.com/ExpressLRS/ExpressLRS-hardware/master/img/r900mini-rx/r900mini-side2-closeup.jpg" width = "60%">

Because those pins are so small one option is to only solder a wire on the `CLK` and `DIO` then power it with the 5v pin with an external power source. 

**Done! You're ready to set up your user defines and flash the firmware to your R900mini**


## SIYI FM30
[Here is a full guide on how to flash the FM30/FRminiRX](http://www.jupacreations.com/ExpressLRS_with_SIYI_FM30_TX_and_RX-23-4-2021.pdf). Thank you to [@Jupa Creations](http://www.jupacreations.com/)