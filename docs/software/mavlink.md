---
template: main.html
description: ExpressLRS Bi-directional MAVLink support
---

![Software Banner](https://raw.githubusercontent.com/ExpressLRS/ExpressLRS-Hardware/master/img/software.png)

!!! warning "Warning"
    Although MAVLink has been in development for some time, and has been tested by a community of early adopters using ArduPilot crafts, MAVLink support is still a recent addition. There may be unexpected bugs; Exercise due caution.

!!! note "NOTE"
    Enabling MAVLink forces the use of Hybrid or 16ch/2 switch mode. Wide switch mode is not supported.

## Description

ExpressLRS now has full bi-directional [MAVLink](https://mavlink.io/en/) support, enabling native MAVLink telemetry downlink and RC control uplink. Users can now enjoy seamless integration of telemetry and RC control.

## Hardware Requirements

Unlike airport, you do **NOT** need a second RX/TX pair for RC control, since ELRS' implementation allows you to do BOTH telemetry and RC control over **one** link. 

To start using MAVLink, you just need one ESP ELRS transmitter, and one ESP ELRS receiver. The majority of recent ELRS hardware is ESP based, and will be compatible with MAVLink. An easy way to check is, if the RX/TX have WiFi, then it is ESP based. 

!!! note "NOTE"
    If you are planning to use 915/868MHz, note that the data rate will be significantly slower than on 2.4GHz. This will result in especially slow parameter downloading, and with 200Hz packet rate at 915MHz, it takes about 2.5 minutes to pull parameters.

## Flashing and Configuring the MAVLink branch

1. From the "Settings" tab on the left hand side, make sure "Expert Mode" is selected.

1. Back in the "Configurator" tab, at the top, select "GIT BRANCH"

1. Select the `master` branch, and flash it to both the RX and TX

1. Turn on both the RX and TX, and ensure they connect properly

1. In ELRS LUA script, select `Other Devices`, select your receiver, and set the `serial protocol` to MAVLink

1. Back out to the LUA scripts main menu, and select the new `Link Mode` option. Change it from `Normal` to `MAVLink`

1. Configure your usual power, packet rate, etc. Use 1:2 for telemetry ratio (it will be auto-set)

1. Wire the RX to a free UART that is suitable for TLM + RC


=== "ArduPilot"
    For the below steps, when a UART connection is mentioned, it will be written as `SERIALx`. Replace `x` with the UART number you are using.

    1. Configure `SERIALx_PROTOCOL=2`, `SERIALx_BAUD=460`, and `RSSI_TYPE=5`
    1. Connect the TX module to the computer running the Ground Control Station via a USB cable
    1. Select the COM port on the GCS, and connect using `460800` baud
    1. If connecting from Backpack WiFi to Mission Planner, select "UDP" and and ensure the port is 14550, and connect. (This step requires Backpack to be on Master branch)
    - Some radios are not able to connect on USB for hardware related reasons, like the Radiomaster Pocket. Those radios will require WiFi to be used instead of USB. Instructions are below.

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


## Enabling WiFi connectivity from ELRS Backpack

To enable WiFi connection of the backpack to the GCS you will also need to update the ELRS Backpack to the master branch. This will be very similar to how you flashed the master branch onto the TX & RX. To do this:

1. On the left hand side of the ELRS Configurator, select "Backpack"

2. Select Git branch, select the `master` branch, and flash it onto the backpack.

3. Once the backpack is flashed, either connect to the backpacks network or connect to the network the backpack is flashed onto. You can now connect from the GCS.


## Implementation Details

### RC Interleaving

When set to MAVLink mode, ELRS changes the allocation of uplink and downlink frame as follows:

- Uplink frames from TX to RX continue to include stick/switch data in the standard ELRS format
- Uplink frames are opportunistically replaced with MAVLink data from your GCS to your aircraft, which is limited to a maximum of 50% of the link's upstream bandwidth. In general, MAVLink from GCS to the aircraft consumes very little bandwidth, due to it being mainly GCS heartbeats.


- Downlink telemetry frames from RX to TX are completely replaced by MAVLink data
- Your TX converts the MAVLink telemetry into standard CRSF format which is understood by EdgeTX

### Stubborn Sender

ELRS uses its stubborn telemetry sender system for MAVLink messages - this system retries packets which weren't delivered, keeping MAVLink link quality high over longer distances and/or with interference.
