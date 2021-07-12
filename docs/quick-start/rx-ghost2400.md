---
template: main.html
---

![Setup-Banner](https://raw.githubusercontent.com/ExpressLRS/ExpressLRS-hardware/master/img/quick-start.png)

# Flashing Ghost Atto/Zepto RX's

Flashing the Ghost RX's is currently a **1 WAY** flash once you flash ExpressLRS to these RX's you **will not** be able to use them with Ghost TX.  You will need a `StLink V2` to flash the RX's

<img src="https://github.com/ExpressLRS/ExpressLRS-Hardware/raw/master/img/GHST_ATTO_V1.1_PINOUT.png" width = "30%">

1. Wire `3.3v`, `GND`, `CLK`, and `DIO` to their respective pins on the RX from the StLink.
2. Select the `GHOST_ATTO_2400_via_STLINK` target.
3. Set your Firmware Options and click on `Build and Flash`.
4. Connect your receiver to your Flight Controller as normal (i.e. Rx to Tx, and Tx to Rx);

Subsequent Firmware Updates can now be done using `via_BetaflightPassthrough` target.

