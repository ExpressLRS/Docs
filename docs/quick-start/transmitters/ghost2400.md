---
template: main.html
---

![Setup-Banner](https://raw.githubusercontent.com/ExpressLRS/ExpressLRS-hardware/master/img/quick-start.png)

## Flashing and Updating IMRC Ghost

Following are the flashing and updating methods for IMRC Ghost.

### <span class="custom-heading" data-id="1">Flashing via STLink</span>
??? Note "Flashing via STLink"

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

    #### <span class="custom-heading" data-id="2">Initial Flash</span>
    ??? Note "Initial Flash"

        Watch this 10-minute video to learn the step-by-step process of flashing the TX if you prefer visual instructions over reading.

        <figure markdown>
        <iframe width="560" height="315" src="https://www.youtube.com/embed/fHxx2Cc3Hz0" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>
        </figure>

        1. The Ghost TX is a **ONE-WAY** flash, meaning it cannot be used with stock Ghost RXs after being flashed with ExpressLRS
        2. A StLink V2 is required for flashing the Ghost TX
        3. Connect `3.3v`, `GND`, `CLK`, and `DIO` pins on the StLink to the corresponding pins on the Ghost TX
        4. The module can be powered through the StLink or the radio.

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

### <span class="custom-heading" data-id="3">Updating</span>
??? Note "Updating"

    1. To update the firmware, build an updated version using the ExpressLRS Configurator
    2. The configurator will produce a `firmware.bin` file upon successful build
    3. Use OpenTX to flash the `firmware.bin` file to the module

<script src="../../../assets/javascripts/admonition-enhancement.js"></script>