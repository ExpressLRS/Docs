---
template: main.html
---

![Setup-Banner](https://github.com/ExpressLRS/ExpressLRS-Hardware/raw/master/img/quick-start.png)

Here are all the target names for the following hardware. We list the name of the target itself, without the final line be it `BetaflightPassthrough`, `UART`, `WiFi`, `Stock_BL`, `DFU` or `STLINK`. 

So what are each of these?

- `BetaflightPassthrough`: once the RX is connected to the FC and has an ELRS bootloader.
- `UART`: used for DIY TXes or flashing via an FTDI.
- `WiFi`: used for Espressif (ESP) based hardware, allows clean web interface for flashing.
- `Stock_BL`: used for R9/similar hardware, where you can flash through the TX.
- `DFU`: can be used to flash the SIYI FM30.
- `STLink`: generally deprecated, used to fully flash hardware that did not originally support ELRS, requires soldering.

 If your hardware is officially ELRS hardware (HappyModel, NamimnoRC, NeutronRC, etc), simply select the target in the dropdown as shown below and skip to the <a href="/quick-start/user-defines/">user defines page</a>. If the hardware is not (R9, SIYI, GHOST, DIY), select the target in the dropdown and then go to the <a href="/quick-start/flashing-bootloader/">bootloader installation page</a>. If the hardware is DIY, skip to <a href="/quick-start/user-defines/">user defines page</a> as well.

## ELRS Hardware
### Happymodel Hardware
- Happymodel EP RXs: `HappyModel_EP_2400_RX_via_XYZ`
- Happymodel PP RX: `HappyModel_PP_2400_RX_via_XYZ`
- Happymodel ES24TX: `HappyModel_ES24TX_2400_TX_via_XYZ`
- Happymodel ES915TX: `HappyModel_ES915TX_via_XYZ`
- Happymodel ES915RX: `HappyModel_ES915RX_via_XYZ`

### NamimnoRC Hardware
- Namimno Voyager TX: `NamimnoRC_Voyager_900_TX_via_XYZ`
- Namimno Voyager ESP RX: `NamimnoRC_Voyager_900_ESP_RX_via_XYZ`
- Namimno Voyager RX: `NamimnoRC_Voyager_900_RX_via_XYZ`
- Namimno Flash TX: `NamimnoRC_FLASH_2400_TX_via_XYZ`
- Namimno Flash ESP RX: `NamimnoRC_FLASH_2400_ESP_RX_via_XYZ`
- Namimno Flash RX: `NamimnoRC_FLASH_2400_RX_via_XYZ`

## Non-ELRS-specific Hardware
### FrSky R9 Hardware
- FrSky R9M: `FrSky_TX_R9M_via_XYZ`
- FrSky R9M Lite: `FrSky_TX_R9M_LITE_via_XYZ`
- FrSky R9M Lite Pro: `FrSky_TX_R9M_LITE_PRO_via_STLink`
- FrSky R9mm/R9mini: `Frsky_RX_R9MM_R9MINI_via_XYZ`
- FrSky R9mx: `Frsky_RX_R9MX_via_XYZ`
- FrSky R9 Slim: `Frsky_RX_R9SLIM_via_XYZ`
- FrSky R9 Slim+: `Frsky_RX_R9SLIMPLUS_via_XYZ`
- FrSky R9 Slim+ OTA: `Frsky_RX_R9SLIMPLUSOTA_via_XYZ`

### Ghost Hardware
- Ghost TX: `GHOST_2400_TX_via_STLINK`
- Ghost TX Lite: `GHOST_2400_TX_LITE_via_STLINK`
- Ghost Atto RX: `GHOST_ATTO_2400_RX_via_XYZ`
- GHOST Zepto RX: `GHOST_ATTO_2400_RX_via_XYZ`

### Other Off The Shelf Hardware
- SIYI FM30 TX: `FM30_TX_via_XYZ`
- SIYI FRMini RX: `FM30_RX_MINI_via_XYZ`
- Jumper R900mini RX: `Jumper_RX_R900MINI_via_XYZ`

## DIY Hardware
### 900 MHz
- TTGO v1: `DIY_900_TX_TTGO_V1_SX127x_via_UART`
- TTGO v2: `DIY_900_TX_TTGO_V2_SX127x_via_UART`
- DIY ESP8285 RX: `DIY_900_RX_ESP8285_SX127x_via_XYZ`
- DIY ESP32 E19 TX: `DIY_900_TX_ESP32_SX127x_E19_via_UART`
- DIY ESP32 RFM95 TX: `DIY_900_TX_ESP32_SX127x_RFM95_via_UART`

### 2.4 GHz
- DIY ESP8285 RX: `DIY_2400_RX_ESP8285_SX1280_via_XYZ`
- DIY STM32 RX: `DIY_2400_RX_STM32_CCG_Nano_v0_5_via_XYZ`
- DIY ESP32 E28 TX: `DIY_2400_TX_ESP32_SX1280_E28_via_UART`
- DIY ESP32 LORAF27 TX: `DIY_2400_TX_ESP32_SX1280_LORA1280F27_via_UART`
- DIY ESP32 SX1280mini TX: `DIY_2400_TX_ESP32_SX1280_Mini_via_UART`
