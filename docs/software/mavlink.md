---
template: main.html
description: ExpressLRS can be configured as a bi-directional transparent serial data link, over the air.
---

![Software Banner](https://raw.githubusercontent.com/ExpressLRS/ExpressLRS-Hardware/master/img/software.png)

!!! warning "Warning"
    Although Mavlink has been in development for some time, and has been tested by a community of early adopters using Ardupilot crafts, Mavlink support is *not yet an official feature*. There may be unexpected bugs and/or missing features. 
    **Use at your own risk**

!!! note "NOTE"
    Mavlink is only available to recievers with ESP hardware and **NOT STM32**. Mavlink support is also Limited to Hybrid / 16ch/2 switch mode; Wide switch mode is not supported.

## Description

ExpressLRS now has full bi-directional [Mavlink](https://mavlink.io/en/) support in the mavlink-rc branch, enabling native MAVLink telemetry downlink and RC control uplink. Users can now enjoy seamless integration of telemetry and RC control.


## Flashing and Configuring Mavlink

1. At the top of the ExpressLRS configurator, select "GIT BRANCH"

2. Select the `mavlink-rc` branch, and flash it to both the RX and TX

3. In the RX LUA script (under `Other Devices`), set the serial protocol to MAVLink

4. In the TX LUA script, select the new `Link Mode` option, and change it from `Normal` to `MAVLink`

5. Configure your usual power, packet rate, etc. Use 1:2 for telemetry ratio (it will be auto-set)

6. Wire the RX to the telemetry port (or a free UART that is suitable for TLM + RC)


## Using Mavlink

=== "Ardupilot"

      1. Configure the UART in ardupilot for MAVLink 2, at 460800 baud

      2. Connect the TX module to the computer running the Ground Control Station via a USB cable

      3. Select the COM port on the GCS, and connect using 460800 baud

