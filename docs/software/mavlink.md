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

To start using MAVLink, you just need one ESP ELRS transmitter, and one ESP ELRS reciever. The majority of recent ELRS hardware is ESP based, and will be compatible with MAVLink. An easy way to check is, if the RX/TX have WiFi, then it is ESP based. 

!!! note "NOTE"
    If you are planning to use 915/868MHz, note that the data rate will be significantly slower than on 2.4GHz. This will result in especially slow parameter downloading, and with 200Hz packet rate at 915MHz, it takes about 2.5 minutes to pull parameters.

## Flashing and Configuring the MAVLink branch

1. At the top of the ExpressLRS configurator, select "GIT BRANCH"

1. Select the `master` branch, and flash it to both the RX and TX

1. Turn on both the RX and TX, and ensure they connect properly

1. In ELRS LUA script, select `Other Devices`, select your receiver, and set the `serial protocol` to MAVLink

1. Back out to the LUA scripts main menu, and select the new `Link Mode` option. Change it from `Normal` to `MAVLink`

1. Configure your usual power, packet rate, etc. Use 1:2 for telemetry ratio (it will be auto-set)

1. Wire the RX to a free UART that is suitable for TLM + RC


## Using MAVLink on ArduPilot

1. Configure the UART in ArduPilot for MAVLink 2, at `460800` baud
    - For example, if you're using UART 3, you'd set `SERIAL3_PROTOCOL=2` and `SERIAL3_BAUD=460`
2. Connect the TX module to the computer running the Ground Control Station via a USB cable

3. Select the COM port on the GCS, and connect using `460800` baud

## Using MAVLink on INAV / Betaflight

- INAV and Betaflight contain an incomplete implementation of the MAVLink protocol standard (lacking RADIO_STATUS flow control). This causes an INAV/Betaflight aircraft to saturate the bandwidth of a telemetry link using soft flow control, and renders it unusable, ergo breaking support with ExpressLRS MAVLink.

## Implementation Details

### RC Interleaving

When set to MAVLink mode, ELRS changes the allocation of uplink and downlink frame as follows:

- Uplink frames from TX to RX continue to include stick/switch data in the standard ELRS format
- Uplink frames are opportunistically replaced with MAVLink data from your GCS to your aircraft, which is limited to a maximum of 50% of the link's upstream bandwidth. In general, MAVLink from GCS to the aircraft consumes very little bandwidth, due to it being mainly GCS heartbeats.


- Downlink telemetry frames from RX to TX are completely replaced by MAVLink data
- Your TX converts the MAVLink telemetry into standard CRSF format which is understood by EdgeTX

### Stubborn Sender

ELRS uses its stubborn telemetry sender system for MAVLink messages - this system retries packets which weren't delivered, keeping MAVLink link quality high over longer distances and/or with interference.