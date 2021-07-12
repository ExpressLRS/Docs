---
template: main.html
---

![Setup-Banner](https://raw.githubusercontent.com/ExpressLRS/ExpressLRS-hardware/master/img/quick-start.png)

##Flashing Ghost Modules via STLink

Here is a 10 minute video, showing the steps required to both flash the bootloader and the ELRS firmware itself.
<iframe width="560" height="315" src="https://www.youtube.com/embed/fHxx2Cc3Hz0" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>

Flashing the Ghost RX's is currently a **1 WAY** flash once you flash ExpressLRS to the TX you **will not** be able to use them with stock Ghost RX's (running stock firmware, they **will work** while running ELRS).  You will need a `StLink V2` to flash the TX

Wire `3.3v`, `GND`, `CLK`, and `DIO` to their respective pins on your part from the StLink. (You can power with the StLink but in the first two image the radio is used to power the module). 
<img src="https://i.imgur.com/58wxHZe.png" width = "49%">
<img src="https://i.imgur.com/vztruRj.png" width = "49%">