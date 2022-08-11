---
template: main.html
---

![Setup-Banner](https://raw.githubusercontent.com/ExpressLRS/ExpressLRS-hardware/master/img/quick-start.png)

## Serial RX Setup

Once you've [wired up](./wiring-up.md) your Receiver to your Flight Controller, you need to setup the UART for Serial RX. In the example below, the Receiver is wired to UART1 (Tx1 and Rx1 pads), and so the Serial RX column should be enabled on UART1 in the Ports Tab.

![Ports Tab](../../assets/images/PortsTab.png)

![INAV Ports](../../assets/images/FC-portsconfig-INAV.png)

## Protocol

Similar to your OpenTX/EdgeTX Radio, ExpressLRS will be using the CRSF protocol between the receiver and the FC firmware (Betaflight/iNav/emuflight), so on the "Configuration" tab, you need to select "Serial-based Receiver" on the "Receiver" panel, and select "CRSF" as the Protocol. Telemetry is optional here and will enable your Flight Controller to send Flight Data back to your Radio like Battery Level, GPS Data, etc. but sending Telemetry will reduce your Channel update rate as it will use up bandwidth and time frames.

!!! Note
    Betaflight 4.3.0 has moved the Receiver configuration into the Receiver Tab.

![Conf Tab](../../assets/images/ConfigurationTab.png)

![INAV Config](../../assets/images/FC-config-INAV.png)

![INAV Config](../../assets/images/FC-rxconfig-INAV.png)

## Software Inversion and Duplex Modes

The CRSF Protocol requires a full UART pair, uninverted and in full-duplex mode. To check for these settings, use the CLI of your Flight Controller firmware and execute `get serialrx`.

- `serialrx_inverted` should be **OFF**; configure it with `set serialrx_inverted = off`.
- `serialrx_halfduplex` should be **OFF**; configure it with `set serialrx_halfduplex = off`.
- Don't forget to use `save` once you're done setting these up.

!!! important
    Close your Flight Controller Configurator once you've set it up for ExpressLRS. Keeping it open could prevent the next steps from completing properly, particularly flashing via Passthrough. You must also unplug the FC from USB before proceeding to the next steps to refresh the connection.

**Use the Navigation Menu to proceed to the Flashing Guides (under the section `Flashing Receivers`).**