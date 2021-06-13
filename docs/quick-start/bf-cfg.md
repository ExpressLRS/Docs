---
template: main.html
---

![Setup-Banner](https://github.com/ExpressLRS/ExpressLRS-Hardware/raw/master/img/quick-start.png)

## Serial Setup

As with any serial-based receiver, you need to attach the TX/RX pads to a UART on your flight controller, then enable the corresponding UART as a serial receiver in Betaflight:

![](https://icantfly.xyz/wp-content/uploads/2019/01/image-58.png)

## Protocol

Similar to in OpenTX, we use the CRSF protocol to communicate between the ExpressLRS receiver and Betaflight, so on the "Configuration" tab, you need to select "Serial-based receiver" on the "Receiver" panel, and select "CRSF" as the protocol. Telemetry is optional here and will reduce your stick update rate due to those transmit slots being used for telemetry.

![](https://icantfly.xyz/wp-content/uploads/2019/01/image-59.png)

## Modes

By default, ExpressLRS uses one-bit switches for the AUX channels. This means a three-position switch will only send two positions (fully off, or 1000, and fully on, or 2000) to Betaflight on the AUX channels. Set your modes appropriately if you are using one-bit switches, or enable HYBRID_SWITCHES_8 for expanded position options. For more information, read the <a href="/software/switch-config"> switch modes page </a>.
![](https://oscarliang.com/ctt/uploads/2018/09/betaflight-configurator-modes-tab-empty.jpg)

## RSSI and Link Quality

To get RSSI and Link Quality displayed in the OSD, set RSSI Channel to "Disabled" in the Receiver tab of the Betaflight Configurator, and RSSI_ADC 
 should be disabled on the Configuration tab. Both of these are the default. On the OSD menu, use the "Link Quality" and "RSSI **dBm value**" elements (not "RSSI Value").

If you wish to enable the rssi dBm warning, you'll have to change the alarm level using `set osd_rssi_dbm_alarm = -100` in CLI. A sensible value is 5-10 higher than the sensitivity shown in the ELRS.lua for the packet rate (e.g. 250Hz=-108, so -103 to -98 for the alarm). If using DJI Goggles, you're required to use "RSSI Value" as the OSD element. Therefore you have to decide between LQ or RSSI, by selecting either AUX11 (LQ) or AUX12 (RSSI) as RSSI Channel on the Receiver tab. More information about signal metrics is found in <a href="/info/signal-health"> this article on signal health </a>.

## Blackbox

Blackbox is handy for evaluating the performance of the RF link for a flight. Set your BB to debug mode `RC_SMOOTHING_RATE`, which will capture the rate that Betaflight is receiving RC Packets from the RX.

## Telemetry

Initially ExpressLRS had very limited telemetry support but with Version `1.0.0-RC1` this changed and **full telemetry was added as optional feature**.
The default setting only includes the link status message that includes the RSSI and Link quality.

To receive all messages the feature telemetry has to be enabled in the <a href="/quick-start/user-defines/#telemetry"> user defines </a>
It's possible to flash your TX module *with telemetry support enabled* and use it with a RX *without telemetry enabled*.
So you can flash certain receivers with telemetry support and others without it and use it with the same TX module.

The RX transmits a subset of telemetry it receives from the flight controller. Disabling certain messages only works if the flight controller
firmware does support it. For Betaflight this is possible with the telemetry_disabled_* cli settings:

```
# Disable Attitude telemetry item
set telemetry_disabled_pitch = ON
set telemetry_disabled_roll = ON
set telemetry_disabled_heading = ON
# Disable Battery telemetry item
set telemetry_disabled_voltage = ON
set telemetry_disabled_current = ON
set telemetry_disabled_fuel = ON
# Disable GPS telemetry item
set telemetry_disabled_altitude = ON
set telemetry_disabled_lat_long = ON
set telemetry_disabled_ground_speed = ON
set telemetry_disabled_heading = ON
# Disable Flight Mode telemetry item (BF >4.2.9)
set telemetry_disabled_mode = ON 
```

Since telemetry messages are sent with low priority it takes some time to transmit the data. The telemetry rate in the lua settings script controls how often a telemetry message should be sent. So a ratio of 1:2 means that every second message is a telemetry message, so the telemetry data is transferred very fast. A ratio 1:64 means that only one of 64 messages is a telemetry message and so the transfer happens much slower.

The refresh rate also impacts the transfer speed. 50 Hz is slower compared to 200 Hz. So if you need fast a fast telemetry update rate
choose high refresh rate, and a ratio that favors telemetry messages e.g. 200 Hz and 1:16 usually works good. For detailed information on telemetry bandwidth at different rates and ratios, see <a href="/info/telem-bandwidth/"> this page on telemetry bandwidth </a>.

To finish the telemetry setup open the telemetry page on your transmitter and select "Discover new sensors" and wait for the list to fill.
You will notice that there is a * sign for each row. This star indicates that this telemetry sensor was just updated. 
If you see a row that does not change, and the name of the row is in square brackets it means that this sensor was not updated for some time.

The first values (including RSSI and link quality) should always be updated (flashing stars). If this does not happen multiple times per second 
the transmitter will issue a "telemetry warning". To prevent this warning use the setting TLM_REPORT_INTERVAL_MS.

It should look like this (and if it does not there is something wrong with your setup):

![Link data update speed](https://github.com/ExpressLRS/ExpressLRS-Hardware/raw/master/img/wiki-from-discord/link.gif)

The remaining values are updated at a different rate (depending on refresh rate and tlm ratio). So if you use 50 Hz and 1:64 it will happen really slow, and the update takes multiple seconds for each sensor:

![Slow update rate](https://github.com/ExpressLRS/ExpressLRS-Hardware/raw/master/img/wiki-from-discord/slow.gif)

If you use 200Hz and 1:2 tlm ratio the stars will not even blink because the update happens so fast:

![Fast update rate](https://github.com/ExpressLRS/ExpressLRS-Hardware/raw/master/img/wiki-from-discord/fast.gif)

## MSP

To configure betaflight from your transmitter it's possible to use the betaflight lua scripts. 
This requires the telemetry feature enabled for the RX+TX. If the telemetry page of OpenTx does not show regular updates for all sensors the LUA script will also not work.

Mavlink is **not supported** and currently **not planned** to be added.

To get a responsive UI configure ExpressLRS for fast data transfer so make sure to use something like `200Hz/250Hz` with `1:2` tlm and 
a serial baud rate of `400000`. Currently MSP is limited to `50Hz` on `11520` Baud and does not work with `500 Hz` refresh rate.
The initial VTX tables download does take long - but is cached after that. 

If you get a "retrying" message while saving changes it means that the lua script did not receive a response fast enough. But the change usually still goes through so try reloading the page to check if the change was saved. With the recommended settings this does not happen but with slower settings it could happen.