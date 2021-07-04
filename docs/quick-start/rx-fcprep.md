---
template: main.html
---

![Setup-Banner](https://raw.githubusercontent.com/ExpressLRS/ExpressLRS-hardware/master/img/quick-start.png)

## Wiring your Receiver

### R9MM/mini, R9mx, R9Slim+

![FC Wiring](../assets/images/FC-Wiring.jpg" width ="100%")
*Note: This will be the same wiring you'll use for flying and the subsequent firmware updates (via Passthrough). Forget the factory wiring guide!*
\
### Happymodel EP1, EP2, PP

![HM2400 connection](../assets/images/hm2400.png)

Labels show the receiver pinouts and not to which pads to connect them (in case of the RX and Tx pads). As we're dealing with UART connection, Rx on receiver goes to a TX pad in the FC, and Tx on Receiver goes to an uninverted Rx pad on the FC.

There are certain FCs that puts their Receiver UART's RX pads Low, which in turn, puts the EP-based (e.g. EP1 and EP2) receivers to Bootloader mode unintentionally. One remedy is to wire them into a different UART, or wire a pull-up resistor (300-1k ohm) into the RX pad.

Also of note is that the EP receivers require their Boot pads (see figure above) be bridged on first time Passthrough Flash from their factory firmwares. After the first passthrough flashing, the bridge needs to be removed, and is no longer needed for subsequent passthrough flashing.

### Happymodel ES915/868RX

TODO

### Happymodel ES900RX

TODO

### NamimnoRC Voyager & Flash

TODO

## Serial Setup

As with any serial-based receiver, you need to attach the TX/RX pads to a UART on your flight controller, then enable the corresponding UART as a serial receiver in Betaflight:

![](https://icantfly.xyz/wp-content/uploads/2019/01/image-58.png)

## Inversion (Software & Hardware) and Duplex Modes

The CRSF Protocol requires a full UART pair, uninverted and in full-duplex mode. Using the CLI, check if `serialrx_inverted` is OFF and `serialrx_halfduplex` is OFF.

You can't use an RX pad that is shared to an SBUS pad, unless you remove the inversion or reroute the line (by bridging pads in the FC). The easiest way to determine which UART can be used with ExpressLRS is to check which UART the manufacturer suggests you wire a Crossfire/Ghost receiver to.