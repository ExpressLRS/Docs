---
template: main.html
description: ExpressLRS Bi-directional MAVLink support
---

![Software Banner](https://raw.githubusercontent.com/ExpressLRS/ExpressLRS-Hardware/master/img/software.png)

!!! warning "Warning"
    Although MAVLink has been in development for some time, and has been tested by a community of early adopters using ArduPilot crafts, MAVLink support is still a recent addition. There may be unexpected bugs; Exercise due caution.

!!! note "NOTE"
    Enabling MAVLink forces the use of Hybrid or 16ch/2 switch mode. Wide switch mode is not supported.
    Enabling MAVLink forces a telemetry ratio of 1:2
    If you are using an internal TX module (e.g. a TX16S with internal ELRS), you will be required to use the TX Backpack to connect to you GCS via WiFi (USB cable between the TX and the PC is not an option for internal modules).

## Description

ExpressLRS now has full bi-directional [MAVLink](https://mavlink.io/en/) support, enabling native MAVLink telemetry downlink and RC control uplink. Users can now enjoy seamless integration of telemetry and RC control.

## Hardware Requirements

Unlike airport, you do **NOT** need a second RX/TX pair for RC control, since ELRS' implementation allows you to do BOTH telemetry and RC control over **one** link. 

To start using MAVLink, you just need one ESP ELRS transmitter, and one ESP ELRS receiver. The majority of recent ELRS hardware is ESP based, and will be compatible with MAVLink. An easy way to check is, if the RX/TX have WiFi, then it is ESP based.

!!! note "NOTE"
    If you are using an internal TX module (e.g. a TX16S with internal ELRS), you will be required to use the TX Backpack to connect to you GCS via WiFi (USB cable between the TX and the PC is not an option for internal modules). See WiFi Connectivity below.

!!! note "NOTE"
    If you are planning to use 915/868MHz, note that the data rate will be significantly slower than on 2.4GHz. This will result in especially slow parameter downloading, and with 200Hz packet rate at 915MHz, it takes  2+ minutes to pull parameters.

## Flashing and Configuring MAVLink-RC

Ensure both your transmitter module, the embedded TX-Backpack (if using WiFi forwarding), and your receiver are up to date with the latest release versions:

- For the main ELRS firmware, follow the [Firmware Update Guide](https://www.expresslrs.org/quick-start/getting-started/) for detailed instructions.
- For the TX-Backpack, follow the [Transmitter Backpack Firmware Guide](https://www.expresslrs.org/hardware/backpack/backpack-tx-setup/) for detailed instructions.

The minimum versions to use this feature are:
- Transmitter / receiver firmware: `3.5.0`
- TX Backpack firmware: `1.5.0`

1. Using the guides above, flash both the RX and TX

1. Turn on both the RX and TX, and ensure they connect properly

1. In ELRS LUA script, select `Other Devices`, select your receiver, and set the `serial protocol` to `MAVLink`. This configures the RX to output MAVLink protocol on the UART.

1. Back out to the LUA scripts main menu, and select the new `Link Mode` option. Change it from `Normal` to `MAVLink`. This configures the TX module to send / receive MAVLink.

1. Configure your usual power, packet rate, etc. The telemetry ratio will be preset to 1:2 (and cannot be changed while in MAVLink mode).

1. Wire the RX to a free UART on your flight controller that is suitable for TLM + RC. A DMA-capable UART is recommended.


=== "ArduPilot"
    For the below steps, when a UART connection is mentioned, it will be written as `SERIALx`. Replace `x` with the UART number you are using.

    1. Configure `SERIALx_PROTOCOL=2`, `SERIALx_BAUD=460`, and `RSSI_TYPE=5`
    1. Connect the TX module to the computer running the Ground Control Station via a USB cable (or alternatively via WiFi - See WiFi Connectivity below)
    1. Select the COM port on the GCS, and connect using `460800` baud

=== "PX4"
    For the below steps, when a UART connection is mentioned, it will be written as `SER_TELx`. Replace `x` with the UART number you are using.

    1. Configure SER_TELx_BAUD to `460800 8N1`
    1. Configure MAVLink with MAV_0_CONFIG to `TELEM2`
    1. Configure MAVLink sending rate with MAV_0_RATE to `9600 B/s`

=== "INAV"
    **CURRENTLY IN DEVELOPMENT** -
    As of update 8.0, which is currently not released yet, INAV has support for proper MAVLink integrations. Until then, refer to the Betaflight tab.

    For the below steps, when a UART connection is mentioned, it will be written as `UARTx`. Replace `x` with the UART number you are using.

    1. In the Ports tab, set the UARTx `Telemetry Protocol` to `MAVLink`, and the baud rate to `460800`. Make sure `RX Serial` is disabled.
    1. In the Receiver tab, set the Receiver type to `SERIAL` and the `Serial Receiver Provider` to `MAVLink`. Leave inverted & half-duplex `disabled`.

=== "Betaflight"

    Betaflight contains an incomplete implementation of the MAVLink protocol standard (lacking RADIO_STATUS flow control). This causes an Betaflight aircraft to saturate the bandwidth of a telemetry link using soft flow control, and renders it unusable, ergo breaking support with ExpressLRS MAVLink.


## WiFi Connectivity

For TX modules that have an onboard Backpack, the MAVLink data can be sent / received via WiFi to a PC or tablet etc. that is running the GCS software. This provides for a cable-free solution on your handset, as it removes the need for a USB cable between the TX and the GCS device.

To setup WiFi forwarding for MAVLink:

1. Ensure the TX Backpack is running version `1.5.0` or later

1. In the ELRS LUA script, select `Backpack`, scroll to the `Telemetry` option, and change the value to `WiFi`

1. If you are NOT using Home WiFi on the Backpack, a new WiFi access point will be available to connect to. Use your PC or tablet etc. to search for and connect to a WiFi network with SSID of `ExpressLRS TX Backpack xxx` (where `xxx` will be part of your UID). The WiFi password is `expresslrs`. Alternatively, if you ARE using Home WiFi on the Backpack, the Backpack will automatically start WiFi and connect to your router.

1. Power on the craft, so that the TX and RX have an active link.

1. On your PC or other GCS device, open your GCS software (e.g. Mission Planner) and set the connection type to `UDP`. Click connect, and use the default UDP port of `14550`. The GCS should successfully connect to the craft and start downloading params.

## Implementation Details

### RC Interleaving

When set to MAVLink mode, ELRS changes the allocation of uplink and downlink frame as follows:

- Uplink frames from TX to RX continue to include stick/switch data in the standard ELRS format
- Uplink frames are opportunistically replaced with MAVLink data from your GCS to your aircraft, which is limited to a maximum of 50% of the link's upstream bandwidth. In general, MAVLink from GCS to the aircraft consumes very little bandwidth, due to it being mainly GCS heartbeats.


- Downlink telemetry frames from RX to TX are completely replaced by MAVLink data
- Your TX converts the MAVLink telemetry into standard CRSF format which is understood by EdgeTX

### Stubborn Sender

ELRS uses its stubborn telemetry sender system for MAVLink messages - this system retries packets which weren't delivered, keeping MAVLink link quality high over longer distances and/or with interference.