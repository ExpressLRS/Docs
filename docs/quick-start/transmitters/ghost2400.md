---
template: main.html
---

![Setup-Banner](https://raw.githubusercontent.com/ExpressLRS/ExpressLRS-hardware/master/img/quick-start.png)

## Flashing via STLink

- Targets:
    - `GHOST_2400_TX_via_STLINK`
    - `GHOST_2400_TX_LITE_via_STLINK`

- Device Category:
    - `ImmersionRC Ghost`

- Device:
    - `GHOST 2400 TX`
    - `GHOST 2400 TX LITE`

<figure markdown>
![via STLink](../../assets/images/Method_TX_STLink.png)
<figcaption>Flashing via STLink</figcaption>
</figure>

## Initial Flash

Here is a 10 minute video, showing the steps required to both flash the TX if you would rather watch than read:

<figure markdown>
<iframe width="560" height="315" src="https://www.youtube.com/embed/fHxx2Cc3Hz0" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>
</figure>

Flashing the Ghost TX's is currently a **1 WAY** flash once you flash ExpressLRS to the TX you **will not** be able to use it with stock Ghost RX's (running stock firmware, they **will work** while running ELRS).  You will need a `StLink V2` to flash the TX

Wire `3.3v`, `GND`, `CLK`, and `DIO` to their respective pins on your part from the StLink. (You can power with the StLink but in the first two image the radio is used to power the module). 

<figure markdown>
<img class="center-img" src="https://i.imgur.com/58wxHZe.png" width = "49%">
</figure>

<figure markdown>
<img class="center-img" src="https://i.imgur.com/vztruRj.png" width = "49%">
</figure>

<figure markdown>
![antenna](https://camo.githubusercontent.com/49b7f4a41eb507189f92f792520a7dccad624df24a63db3ee119b284e2d41def/68747470733a2f2f692e696d6775722e636f6d2f724f6e7a6e6d592e706e67)
<figcaption>Output/Input antennas of the TX</figcaption>
</figure>

## Updating

Updating can be done by building an updated version on the configurator and then flashing the `firmware.bin` file using OpenTX.