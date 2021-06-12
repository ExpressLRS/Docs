---
template: main.html
---

![Setup-Banner](https://github.com/ExpressLRS/ExpressLRS-Hardware/raw/master/img/quick-start.png)

## Contents:

- [FrSky R9 RXes](#frsky-recievers)
- [FrSky R9 TXes](#frsky-transmitters)
- [Ghost Hardware](#)
- [Jumper R900mini](#)
- [SIYI FM30](#)

## FrSky Recievers
This guide applies for the R9mm, R9mini, R9mx, R9Slim, R9Slim+, R9Slim+ OTA, if you have a `OpenTX` transmitter with a `SmartPort` output, you can flash your RXes bootloader.

Download the bootloader `.frk` file for your respective reciever. The files are as follows:

- R9mm/mini: [`r9mm_elrs_bl.frk`](https://github.com/AlessandroAU/ExpressLRS/blob/master/src/bootloader/r9mm_elrs_bl.frk?raw=true) or [`r9mm_no_btn_elrs_bl.frk`](https://github.com/ExpressLRS/ExpressLRS/raw/master/src/bootloader/r9mm_no_btn_elrs_bl.frk)
- R9mx: [`r9mx_elrs_bl.frk`](https://github.com/ExpressLRS/ExpressLRS/blob/master/src/bootloader/r9mx_elrs_bl.frk?raw=true)
- R9Slim+ (ACCST): [`r9slim_plus_elrs_bl.frk`](https://github.com/ExpressLRS/ExpressLRS/blob/master/src/bootloader/r9slim_plus_elrs_bl.frk?raw=true)
- R9Slim+ (ACCESS/OTA): [`r9slim_plus_ota_elrs_bl.frk`](https://github.com/ExpressLRS/ExpressLRS/blob/master/src/bootloader/r9slim_plus_ota_elrs_bl.frk?raw=true)

Copy the relevant file to your handset's SD card 

Wire the reciever to your radio's smartport, as shown (r9mm/r9mx/r9slim):

 <img src = "https://github.com/ExpressLRS/ExpressLRS-Hardware/raw/master/img/wiki-from-discord/r9mm-to-tx.jpeg" width = "20%"> <img src = "https://github.com/ExpressLRS/ExpressLRS-Hardware/raw/master/img/wiki-from-discord/r9mx-to-tx.png" width = "20%"> <img src="https://raw.githubusercontent.com/ExpressLRS/ExpressLRS-Hardware/master/img/wiki-from-discord/r9slim-to-tx.jpeg" width = "20%">

 Next, flash the `.frk` via the `S.port` flashing option in `OpenTX` :zap:

 Unplug the reciever, bootloader is flashed. Continue to the next page to set up your user defines.


## FrSky Transmitters