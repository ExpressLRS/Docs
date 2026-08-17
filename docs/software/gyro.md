---
template: main.html
description: Use an ExpressLRS receiver as a stabilizer for aircraft without a flight controller.
---

![Software Banner](https://raw.githubusercontent.com/ExpressLRS/ExpressLRS-Hardware/master/img/software.png)

## Overview

ExpressLRS receivers that are equipped with an _inertial measurement unit_ (IMU) / gyro can provide stabilization for aircraft without a flight controller. A DIY gyro can also be added to some receivers, see [Gyro Receiver Mod](../hardware/gyro-receiver-mod.md) for details.

!!! Note
    Use the ExpressLRS Product Finder to list supported receivers with a gyro! https://www.expresslrs.org/product-finder/?search=gyro&classification=receiver

This guide explains how to configure the receiver.

## Main setup


### Enable gyro

When the gyro is disabled, the receiver works normally without Gyro functionality.

=== "WebUI"

    Start the WebUI on the receiver and go to the `Gyro` tab. In the `Main Setup` panel, check `Enable Gyro`. Once enabled, the `Status` panel should indicate that the **gyro state** is OK.

    If the gyro state is not OK, see [Troubleshooting](../../hardware/gyro-receiver-mod/#testing).

    Image TK

=== "Lua script"

    TK

### Rate gain multiplier

The **rate gain multiplier** adjusts the sensitivity of the gyro in **rate mode**, in order to allow the **gyro gain** to provide a meaningful adjusting range (see [Output Channels](#output-channels)). A value of `1x` is usually a good starting point.

If your gyro is too sensitive even when the **gyro gain** is low, it could be useful to lower the sensitivity (`0.5x`). On the contrary, if you reach 100% of the **gyro gain**, it may be useful to increase the sensitivity (`1.5x`, `2x`).

=== "WebUI"

    Start the WebUI on the receiver and go to the `Gyro` tab. In the `Main Setup` panel, select the desired **rate gain multiplier**.

    Image TK

=== "Lua script"

    TK

!!! Note
    Always start testing with a low **gyro gain**.

    - <abbr title="Electric Ducted Fan">EDF</abbr> and fast planes can benefit from a low **rate gain multiplier**: `0.5x`
    - Slow planes on the contrary might require higher a multiplier: `1.5x` or `2x`
    - For testing on the bench, you might need to increase the **rate gain multiplier** in order to see the surfaces move! (`2x`)

### 5-position switch map

Define which gyro **flight modes** are activated by the **gyro mode** channel (see [Output Channels](#output-channels)). A typical three-position switch will use `-100`,`0`,`+100`.


??? tip "EdgeTX: Want more than 3 positions? (click/tap to expand)"
    If you want all 5 positions, setup the **gyro mode** channel with a 3-pos switch to a _weight_ of `50%`. That will give you `-50`,`0`,`+50`.  Use _special functions_ to activate the `-100` or `+100` values as needed.

    Example with 4 positions: set `-50=Off`, `0=Rate`, `+50=Envelope`, `+100=Auto-Level`. Your 3-pos witch will take care of the first three. To activate `Auto-Level`, create a _special function_ on another switch (ex. `SH`) to override the **gyro mode** channel to `+100`.

=== "WebUI"

    Start the WebUI on the receiver and go to the `Gyro` tab. In the `Main Setup` panel, select the desired modes for each of the channel positions.

    Image TK

=== "Lua script"

    TK

## Status

=== "WebUI"

    Start the WebUI on the receiver and go to the `Gyro` tab. The information is displayed in the `Status` panel.

    Image TK

=== "Lua script"

    TK

### IMU type

Displays the name of the sensor, along with some debugging information.

### Gyro state

Indicates when the sensor was detected and initialized correctly,

### Link

Indicates whether the receiver is connected to the transmitter.

!!! Note
    The [**endpoint calibration**](#endpoint-calibration) wizard requires a connection to the transmitter.

!!! Info
    ExpressLRS versions that provide Gyro support allow the receiver to connect to the transmitter while in WiFi mode. While in WiFi mode, turn on your transmitter as usual for the receiver to connect.

## Mechanical setup

### Orientation

TK

??? Warning "Only some gyro orientations are supported. (click/tap to expand)"
    Currently, the gyro **must be oriented along the axes of rotation of the aircraft**.

    Example: if the gyro is aligned with the receiver, the receiver can be installed upside-down or sideways, but _oblique_ positions are unsupported.

=== "WebUI"

    Start the WebUI on the receiver and go to the `Gyro` tab.

    TK

=== "Lua script"

    TK

### Level calibration

=== "WebUI"

    Start the WebUI on the receiver and go to the `Gyro` tab.

    TK

=== "Lua script"

    TK

### Live attitude view

Allows to confirm that the gyro [**orientation**](#orientation) settings, and that the [**level calibration**](#level-calibration) are correct by rendering the measurements performed by the IMU.

=== "WebUI"

    Start the WebUI on the receiver and go to the `Gyro` tab.

    Image TK

=== "EdgeTX telemetry"

    !!! Note
        Requires a [connection to the transmitter](#link), but does not require the receiver to be in WiFi mode.

    The receiver emits three telemetry sensors that reflect the IMU measurements: `Ptch`, `Roll`, and `Yaw`.

    First discover sensors if needed. On the transmitter, in the <kbd>Model</kbd> settings, navigate to `Telemetry` > `Sensors` > `Discover new`.

    Then in <kbd>Model</kbd> settings, navigate go to `Display`, add the sensors to a `Screen`, then exit the model setings.

    Use the <kbd>TELE</kbd> button to display the screen. The motion of the aircraft along each axis should be reflected on the telemetry screen.

    !!! Info
        If you find that the values are not updated often enough, you can increase the [Telemetry ratio](../../quick-start/transmitters/lua-howto/#packet-rate-and-telemetry-ratio). Setting higher telemetry ratios (like `1:8`, `1:4`, `1:2`) increases the frequency of updates.

    Image TK

=== "EdgeTX widget"

    !!! Note
        Requires a [connection to the transmitter](#link) and a custom Lua script, but does not require the receiver to be in WiFi mode.

    The receiver emits three telemetry sensors that reflect the IMU measurements: `Ptch`, `Roll`, and `Yaw`.

    Some community EdgeTX widgets allow to visualize the attitude of the aircraft based on those telemetry sensors.

    Example: https://github.com/qsiguy/EdgeTX-Widgets/tree/main/AttIndV2

    !!! Info
        If you find that the values are not updated often enough, you can increase the [Telemetry ratio](../../quick-start/transmitters/lua-howto/#packet-rate-and-telemetry-ratio). Setting higher telemetry ratios (like `1:8`, `1:4`, `1:2`) increases the frequency of updates.

## Output channels and limits

### Output channels



=== "WebUI"

    Start the WebUI on the receiver and go to the `Gyro` tab.

    TK

=== "Lua script"

    TK

### Endpoint calibration

Records the center value and maximum range of the incoming channels, so that the gyro commands don't risk damaging mechanical links.

=== "WebUI"

    Start the WebUI on the receiver and go to the `Gyro` tab. In the `Output Channels & Limits` panel press the `ENDPOINT CAL` button.

    First center the sticks and `CAPTURE CENTERS`. Then move the sticks across the totality of their range and `FINISH CALIBRATION`.

    Images TK

=== "Lua script"

    TK

## Flight mode tuning

=== "WebUI"

    Start the WebUI on the receiver and go to the `Gyro` tab. The `Flight Mode Tuning` panel displays the tuning parameters for each flight mode.

    Image TK

=== "Lua script"

    TK

### Rate Mode

_Also known as: wind rejection mode, stabilized mode_

The gyro corrects movements of the plane that are not the result of stick inputs.

#### Stick Priority

A variable gain that depends on the stick deflection. The value defines point of the stick travel the gyro gains reach zero.

By default, **stick priority** value is `100%`. At stick center, gyro gain is fully applied, and starts declining as the stick deflection increases. When the stick reaches 50% of its travel, the gyro gain has been reduced by half, and at full stick deflection (`100%` of travel) the gyro gain is zero.

When stick priority is set to `60%`, the gyro gain is still applied fully when the stick is centered. It is reduced by half when the stick reaches `30%` of its travel, and reaches zero when the stick reaches `60%` of its travel.

#### Gains

Define how much of the maxiumum travel the gyro should use. With higher gains, the gyro deflects the surfaces more, up to `100%` of their maximum travel.

### Envelope Mode

_Also known as: max angle envelope protection, horizon mode_

The gyro behaves like in **Rate mode**, but will keep the aircraft within the configured pitching and banking limits.

#### Use Rate

Combines Auto-Level with **Rate mode** behavior for wind rejection. When disabled, the gyro only activates when the **angle limits** are reached.

#### Trims

Only apply to Auto-Level mode, and ensure that the aircraft is flying level when the sticks are centered.

On the _pitch_ axis, positive(+) brings the nose up, negative (-) brings nose down. On the _roll_ axis, positive(+) causes banking to the left.

#### Limit Pitch/Roll

The maximum pitching and banking angles, in degrees.

#### Gains

Define how much of the maxiumum travel the gyro should use. With higher gains, the gyro will bring the aircraft back within the pitching and banking limits more agressively. A value of `35%` is a good starting point.

### Auto-level Mode

_Also know as: level mode, angle mode, angle demand_

The gyro keeps the aircraft flying level when the sticks are centered. It also prevents pitching or banking past the **angle limits***.

Move the stick 50% of the maximum travel, the aircraft will bank/pitch 50% of the **angle limit**.

Example: if **limit roll** is set to `70deg`, and the aileron stick is helf way out, the aircraft will fly at a `35deg` banking angle.

#### Use Rate

Combines Auto-Level with **Rate mode** behavior for wind rejection.

#### Trims

Only apply to Auto-Level mode, and ensure that the aircraft is flying level when the sticks are centered.

On the _pitch_ axis, positive(+) brings the nose up, negative (-) brings nose down. On the _roll_ axis, positive(+) causes banking to the left.

#### Limit Pitch/Roll

The maximum pitching and banking angles, in degrees.

#### Gains

Define how much of the maxiumum travel the gyro should use. With higher gains, the gyro will bring the aircraft to level more agressively when the sticks are released. A value of `35%` is a good starting point.
