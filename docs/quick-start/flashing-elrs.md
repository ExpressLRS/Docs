---
template: main.html
---

![Setup-Banner](https://raw.githubusercontent.com/ExpressLRS/ExpressLRS-hardware/master/img/quick-start.png)

## Non-ELRS Hardware
### FrSky TXes  
- For a stock R9M use the **[TX Method](https://github.com/AlessandroAU/ExpressLRS/wiki/Flashing-R9M-TX)**  
  - If you previously flashed your device with an **`STLink`** you will need to use the **[old method](https://github.com/AlessandroAU/ExpressLRS/wiki/Flashing-TX-with-STLink#r9m)**  
- For a stock R9M Lite use the **[TX Method](https://github.com/AlessandroAU/ExpressLRS/wiki/Flashing-R9M-TX)**, with the R9M bootloader and R9M_Lite Target in platformio  
  - As with the regular R9M, if you've previously flashed your device with an **`STLink`**, you will need to use the **[old method](https://github.com/AlessandroAU/ExpressLRS/wiki/Flashing-TX-with-STLink#r9m-lite)**.  
### FrSky RXes  
- The R9MM / Mini can be flashed via many methods depending on available hardware and preferences. However, **[Flashing With TX](https://github.com/AlessandroAU/ExpressLRS/wiki/Flashing-R9MM-R9MINI-with-TX)** is the current easiest method. Updating is easiest via **[Passthrough](https://github.com/ExpressLRS/ExpressLRS/wiki/BF-Passthrough)**  
- The R9MX can be flashed using similar methods to the R9MM / Mini, and again **[Flashing with a TX](https://github.com/AlessandroAU/ExpressLRS/wiki/Flashing-R9mx-with-TX)** is the current easiest method. Updating is easiest via **[Passthrough](https://github.com/ExpressLRS/ExpressLRS/wiki/BF-Passthrough)**  
- The R9 Slim+ can also be **[flashed using a TX](https://github.com/AlessandroAU/ExpressLRS/wiki/Flashing-R9slim-PLUS-(2-Antennas)-with-TX)**. Updating is easiest via **[Passthrough](https://github.com/ExpressLRS/ExpressLRS/wiki/BF-Passthrough)**

### Jumper RXes  
- The R900mini can be flashed using the **[StLink Method](https://github.com/AlessandroAU/ExpressLRS/wiki/Flashing-Jumper-R900-Mini-with-STLink)** and updated via **[Passthrough](https://github.com/ExpressLRS/ExpressLRS/wiki/BF-Passthrough)**

## ELRS Hardware
### Happymodel TX
- The 900Mhz Happymodel TX is identical to an R9M and can use the **[TX Method](https://github.com/AlessandroAU/ExpressLRS/wiki/Flashing-R9M-TX)**. The bootloader is already flashed from the factory.  
### Happymodel RX
- Update your 900Mhz Happymodel RX via **[BF Passthrough](https://github.com/ExpressLRS/ExpressLRS/wiki/BF-Passthrough)**. The bootloader is already flashed from the factory.  
### Happy Model EP RXes
- Are factory delivered with ELRS bootlader installed. Can be updated by **[WiFi](https://github.com/ExpressLRS/ExpressLRS/wiki/Wi%E2%80%90Fi-Updating)**, **[Passthrough](https://github.com/ExpressLRS/ExpressLRS/wiki/BF-Passthrough)** and UART.
### Happy Model PP RXes
- Are factory delivered with ELRS bootlader installed. Can be updated by **[Passthrough](https://github.com/ExpressLRS/ExpressLRS/wiki/BF-Passthrough)** and UART.




## DIY Hardware
### DIY 900M RXes  
- All DIY RXes can be flashed using the **[FTDI Method](https://github.com/ExpressLRS/ExpressLRS/wiki/Building-an-Esp-Rx#flashing-custom-rx)** and updated via **[WiFi](https://github.com/ExpressLRS/ExpressLRS/wiki/Wi%E2%80%90Fi-Updating)**




### ImmersionRC RXes  
- The Atto / Zepto can be flashed using the **[StLink Method](https://github.com/AlessandroAU/ExpressLRS/wiki/Flashing-Ghost-Rx)** and updated via **[Passthrough](https://github.com/ExpressLRS/ExpressLRS/wiki/BF-Passthrough)**  
### ImmersionRC TXes  
- The GHOST TX can be flashed using the **[StLink Method](https://github.com/AlessandroAU/ExpressLRS/wiki/Flashing-Ghost-TX)** 

### SIYI FM30 TX
- The FM30 TX ELRS bootloader can be flashed by STLink method and updated by USB (DFU) by the following link [SIYI FM30 + FRmini flash and update manual](http://www.jupacreations.com/ExpressLRS_with_SIYI_FM30_TX_and_RX-23-4-2021.pdf).


### SIYI FRmini RX
- The FRmini RX ELRS bootloader can be flashed by STLink method and updated by Passthrough by the following link [SIYI FM30 + FRmini flash and update manual](http://www.jupacreations.com/ExpressLRS_with_SIYI_FM30_TX_and_RX-23-4-2021.pdf)


### DIY 2.4G RXes  
- All DIY RXes can be flashed using the **[FTDI Method](https://github.com/ExpressLRS/ExpressLRS/wiki/Building-an-Esp-Rx#flashing-custom-rx)** and updated via **[WiFi](https://github.com/ExpressLRS/ExpressLRS/wiki/Wi%E2%80%90Fi-Updating)**

### DIY 2.4G TXes  
- All DIY TXes can be flashed using the **[USB Method](https://github.com/ExpressLRS/ExpressLRS/wiki/Flashing-DIY-TXes-via-USB)** and updated via **[WiFi](https://github.com/ExpressLRS/ExpressLRS/wiki/Wi%E2%80%90Fi-Updating)**
