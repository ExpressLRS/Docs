---
template: main.html
---

![Setup-Banner](https://raw.githubusercontent.com/ExpressLRS/ExpressLRS-hardware/master/img/quick-start.png)

### R9mm/mini, R9mx, R9Slim+
This guide applies for the R9mm, R9mini, R9mx, R9Slim+, R9Slim+ OTA, if you have a `OpenTX` transmitter with a `SmartPort` output, you can flash your RXes bootloader.

Download the bootloader `.frk` file for your respective receiver. The files are as follows:

- R9mm/mini: [`r9mm_elrs_bl.frk`](https://github.com/AlessandroAU/ExpressLRS/blob/master/src/bootloader/r9mm_elrs_bl.frk?raw=true) (14kb) or [`r9mm_no_btn_elrs_bl.frk`](https://github.com/ExpressLRS/ExpressLRS/raw/master/src/bootloader/r9mm_no_btn_elrs_bl.frk?raw=true) (14kb) (no_btn bootloader is only used if your bind/boot button on the receiver is faulty or has gone bad, and is indicated by both LEDs (red and green) being constantly illuminated.)
- R9mx: [`r9mx_elrs_bl.frk`](https://github.com/ExpressLRS/ExpressLRS/blob/master/src/bootloader/r9mx_elrs_bl.frk?raw=true) (20kb)
- R9Slim+ (ACCST): [`r9slim_plus_elrs_bl.frk`](https://github.com/ExpressLRS/ExpressLRS/blob/master/src/bootloader/r9slim_plus_elrs_bl.frk?raw=true) (14kb)
- R9Slim+ (ACCESS/OTA): [`r9slim_plus_ota_elrs_bl.frk`](https://github.com/ExpressLRS/ExpressLRS/blob/master/src/bootloader/r9slim_plus_ota_elrs_bl.frk?raw=true) (18kb)

Copy the relevant file to your handset's SD card (You can put it inside `/FIRMWARE` folder for easy access).

Wire the receiver to your radio's Smart Port, as shown:

![BL Flashing](../assets/images/Bootloader-Flashing.jpg)

<br />

Next, flash the `.frk` via the `S.port` flashing option in `OpenTX`. :zap: (It helps if the External RF module is set to `PPM` mode.) 

  * Navigate in OpenTX to the TOOLS menu (hold SYS button)
  * Page to the SD-HC CARD page, then the `FIRMWARE` folder
  * Flash the frk file by holding OK and selecting "Flash external module"

Unplug the receiver, and your bootloader is flashed.

## Troubleshooting No Sync

- Setting the External RF module to PPM mode helps.
- Check if the receiver have its LED lighting up or if it's powered.
- Check whether you've set your Max Bauds to 115200, specially if you're using a QX7 or an X9D (on OneBit Firmwares or EdgeTX). If so, put it back to 400k and try again.

**You can now proceed to the next step!**