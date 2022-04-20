---
template: main.html
---

![Setup-Banner](https://raw.githubusercontent.com/ExpressLRS/ExpressLRS-hardware/master/img/quick-start.png)

Targets:

- `FM30_RX_MINI_via_STLINK` (First-time Flash)
- `FM30_RX_MINI_via_BetaflightPassthrough` (Updates)

**Note: only guaranteed to work on the v3.0 of the receiver.**

## Initial Flashing

The only way to flash the FR Mini is using STLINK. Note this is a one-way process, there is no returning to the stock firmware after flashing.
<figure markdown>
![pinout](https://github.com/ExpressLRS/ExpressLRS-Hardware/blob/master/img/siyi/jupa/Siyi-12.JPG?raw=true)
</figure>
<figure markdown>
![stlink](https://github.com/ExpressLRS/ExpressLRS-Hardware/blob/master/img/siyi/jupa/Siyi-13.JPG?raw=true)
</figure>

* Connect wires to DIO (SWDIO), CLK (SWCLK), RST, and GND to the header points on the RX
* Attach 3.3V to the VDD pad on the flashing header. Do not connect 5V here! :fire:
* Flash using the `FM30_RX_MINI_via_STLINK` target in the ExpressLRS Configurator

![via STLink](../../assets/images/Method_RX_STLink-stm.png)

For more information and troubleshooting of the STLINK connection, see the detail on the [FM30 Initial Flashing](../transmitters/tx-siyifm30.md) page.

Once flashing is complete, wire the receiver to your flight controller using the images below.

| Flight Controller | FR Mini Receiver |
|---|---|
| 5V | VDD |
| GND | GND |
| RX | TX2 |
| TX | RX2 |

<figure markdown>
![pinout](https://github.com/ExpressLRS/ExpressLRS-Hardware/blob/master/img/siyi/jupa/Siyi-16.JPG?raw=true)
</figure>
<figure markdown>
![pinout](https://github.com/ExpressLRS/ExpressLRS-Hardware/blob/master/img/siyi/jupa/Siyi-17.JPG?raw=true)
</figure>

Thank you to [@JupaCreations](http://www.jupacreations.com/)

## Updating via Passthrough

Updating is done via Betaflight Passthrough with the receiver wired to the flight controller. Be sure the transmitter is off, use the `FM30_RX_MINI_via_BetaflightPassthrough` target in the ExpressLRS Configurator, then click on **Build and Flash**.

![via Passthrough](../../assets/images/Method_RX_Passthrough-stm.png)
