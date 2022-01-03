---
template: main.html
---

![Setup-Banner](https://raw.githubusercontent.com/ExpressLRS/ExpressLRS-hardware/master/img/quick-start.png)

## Wiring your Receiver

### R9MM/mini, R9mx, R9Slim+

![FC Wiring](../../assets/images/FC-Wiring.jpg" width ="100%")

!!! attention ""
    Note: This will be the same wiring you'll use for flying and the subsequent firmware updates (via Passthrough). Forget the factory wiring guide!

After you've flashed the [bootloader](rx-bootloader.md) and wired your receiver as above, proceed to configure up your flight controller as shown [below].

!!! note ""
    Note: R9 Slim requires flashing via STLink first. Passthrough should work for updates.

### Happymodel EP1, EP2, PP

![HM2400 connection](../../assets/images/hm2400.png)

Labels show the receiver pinouts and not to which pads to connect them (in case of the RX and Tx pads). As we're dealing with UART connection, Rx on receiver goes to a TX pad in the FC, and Tx on Receiver goes to an uninverted Rx pad on the FC.

There are certain FCs that puts their Receiver UART's RX pads Low, which in turn, puts the EP-based (e.g. EP1 and EP2) receivers to Bootloader mode unintentionally. One remedy is to wire them into a different UART, or wire a pull-up resistor (300-1k ohm) into the RX pad (FC Rx pad -> Resistor -> 3v3 pad).

Also of note is that the EP receivers require their Boot pads (see figure above) be bridged on first time Passthrough Flash from their factory firmwares. After the first passthrough flashing, the bridge needs to be removed, and is no longer needed for subsequent passthrough flashing.

Flashing via Wifi doesn't need the Boot Pads bridged. Moreover, if it is bridged, the receiver will stay in bootloader mode and won't activate the wifi hotspot.

Connect your FC to USB and configure your FC firmware as [below].

### Happymodel ES900RX

![ES900RX](../../assets/images/es900rx-conn.png)

Shown above is the pinouts for the ES900RX receivers. Connect Rx to a Tx pad on the FC and Tx to an Rx pad on the FC. Additionally, the Boot Pads, encircled in the photo above, needs to be bridged in the first-time passthrough flash from the factory firmware.

As this is an ESP-based receiver, be aware that there are certain FCs that puts their Receiver UART's RX pads Low, which in turn, puts the receiver to Bootloader mode unintentionally. One remedy is to wire them into a different UART, or wire a pull-up resistor (300-1k ohm) into the RX pad (FC Rx pad -> Resistor -> 3v3 pad).

Should you be updating via Wifi, the bridging of the boot pads is not needed. 

Connect your FC to USB and configure your FC firmware as shown [below].

### Happymodel ES915/868RX (Discontinued)

![ES915RX](../../assets/images/ES915rx.jpg)

Labels in the receiver show the pinouts. Connect Rx to a Tx pad in the FC and the Tx to an Rx pad in the FC. Of course, don't forget to connect VCC to a 5V pad, and GND to a GND pad on the FC.

Connect your FC to USB and configure your FC firmware as shown [below].

### NamimnoRC Voyager & Flash

<small>Namimno Voyager ExpressLRS Receiver</small>

<img src="https://github.com/ExpressLRS/ExpressLRS-Hardware/blob/master/img/Voyager%20Pinout.png?raw=true" width="70%">

<small>Namimno Flash ExpressLRS Receiver</small>

<img src="https://github.com/ExpressLRS/ExpressLRS-Hardware/blob/master/img/Flash%20Pinout.png?raw=true" width="70%">

Labels in the receiver show the pinouts. Connect Rx to a Tx pad in the FC and the Tx to an Rx pad in the FC. Of course, don't forget to connect VCC to a 5V pad, and GND to a GND pad on the FC.

Connect your FC to USB and configure your FC firmware as shown [below].

### BetaFPV Receivers

<small >BetaFPV 900MHz ExpressLRS Receiver</small>

![betafpv 900Mhz](../../assets/images/betaFPVrx900.png)

<small>BetaFPV 2.4GHz ExpressLRS Receiver</small>

![betafpv 2.4Ghz](../../assets/images/betaFPVrx2400.jpg)

Shown above are the pinouts and various components of the receivers. Connect Rx to a Tx pad on the FC and Tx to an Rx pad on the FC. Don't forget to also wire up 5v(VCC) and Gnd.

Updating via WiFi is supported by these receivers.

Connect your FC to USB and configure your FC firmware as shown [below].

### MatekSys R24-D and R24-S

<small>R24-D</small>

![mateksys r24-d](../../assets/images/ELRS-R24-D.jpg)

<small>R24-S</small>

![mateksys r24-d](../../assets/images/ELRS-R24-S.jpg)

Shown above are the pinouts and dimensions of the receivers. Connect Rx/R to a Tx pad on the FC and Tx/T to an Rx pad on the FC. Don't forget to also wire up 5v and Gnd.

Updating via WiFi is supported by these receivers.

Connect your FC to USB and configure your FC firmware as shown [below].

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