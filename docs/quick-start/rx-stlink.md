---
template: main.html
---

![Setup-Banner](https://raw.githubusercontent.com/ExpressLRS/ExpressLRS-hardware/master/img/quick-start.png)

## R9Slim
This RX requires an StLink v2 to be flashed. 

Wire up the RX to the STLink using `+ = 3v3`, `- = GND`, `C = CLK` and `D = DIO`. 

## Jumper R900 Mini
This also requires an STLink, so the wiring is as follows: 
Wire `+ = 3v3`, `- = GND`, `C = CLK` and `D = DIO` to their respective pins on the RX from the StLink.
<img src="https://raw.githubusercontent.com/ExpressLRS/ExpressLRS-hardware/master/img/r900mini-rx/r900mini-side2-closeup.jpg" width = "60%">

Because those pins are so small one option is to only solder a wire on the `CLK` and `DIO` then power it with the 5v pin with an external power source. 