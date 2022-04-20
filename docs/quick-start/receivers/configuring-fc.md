---
template: main.html
---

![Setup-Banner](https://raw.githubusercontent.com/ExpressLRS/ExpressLRS-hardware/master/img/quick-start.png)

## Serial RX Setup

Once wired up to our Flight Controller, we need to setup the UART for Serial RX. In the example below, the Receiver is wired to a Tx1/Rx1 (UART1) Pad, and so the Serial RX column should be activated on UART1.

![](https://icantfly.xyz/wp-content/uploads/2019/01/image-58.png)

## Protocol

Similar to your OpenTX Radio, we are using the CRSF protocol between the receiver and the FC firmware (Betaflight/iNav/emuflight), so on the "Configuration" tab, you need to select "Serial-based receiver" on the "Receiver" panel, and select "CRSF" as the protocol. Telemetry is optional here and will reduce your stick update rate due to those transmit slots being used for telemetry.

!!! Note
    Betaflight 4.3.0 has moved the Receiver configuration into the Receiver Tab.

![](https://icantfly.xyz/wp-content/uploads/2019/01/image-59.png)

## Software Inversion and Duplex Modes

The CRSF Protocol requires a full UART pair, uninverted and in full-duplex mode. To check for these settings, use the CLI of your Flight Controller firmware and execute `get serialrx`.

- `serialrx_inverted` should be **OFF**; configure it with `set serialrx_inverted = off`.
- `serialrx_halfduplex` should be **OFF**; configure it with `set serialrx_halfduplex = off`.
- Don't forget to use `save` once you're done setting these up.

**Use the Navigation Menu to proceed to the Flashing Guides (under the section `Flashing Receivers`).**