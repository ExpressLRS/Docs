---
template: main.html
---

![Setup-Banner](https://raw.githubusercontent.com/ExpressLRS/ExpressLRS-hardware/master/img/quick-start.png)

## Serial RX Setup

Once wired up to our Flight Controller, we need to setup the UART for Serial RX. In the example below, the Receiver is wired to a Tx1/Rx1 (UART1) Pad, and so the Serial RX column should be activated on UART1.

![](https://icantfly.xyz/wp-content/uploads/2019/01/image-58.png)

## Protocol

Similar to your OpenTX Radio, we are using the CRSF protocol between the receiver and the FC firmware (Betaflight/iNav/emuflight), so on the "Configuration" tab, you need to select "Serial-based receiver" on the "Receiver" panel, and select "CRSF" as the protocol. Telemetry is optional here and will reduce your stick update rate due to those transmit slots being used for telemetry.

![](https://icantfly.xyz/wp-content/uploads/2019/01/image-59.png)

## Inversion (Software & Hardware) and Duplex Modes

The CRSF Protocol requires a full UART pair, uninverted and in full-duplex mode. Using the CLI, check if `serialrx_inverted` is **OFF** and `serialrx_halfduplex` is **OFF**. To do this, simply type `get serialrx` in the CLI to see the settings for both at the same time. You can use `set serialrx_inverted=off` or `set serialrx_halfduplex=off` to turn them off respectively. Don't forget to also type in `save` after the change.

You can't use an RX pad that is shared to an SBUS pad, unless you remove the inversion or reroute the line (by bridging pads in the FC although not all FC have this). The easiest way to determine which UART can be used with ExpressLRS is to check which UART the manufacturer suggests you wire a Crossfire/Ghost receiver to.

**Use the Navigation Menu to proceed to the Flashing Guides for these Receivers (under the section `Flashing Receivers`).**

[below]: #serial-rx-setup