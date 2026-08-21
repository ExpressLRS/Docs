---
template: main.html
description: Use an ExpressLRS receiver as a stabilizer for aircraft without a flight controller.
---

![Software Banner](https://raw.githubusercontent.com/ExpressLRS/ExpressLRS-Hardware/master/img/software.png)

## Overview

ExpressLRS receivers that are equipped with an _inertial measurement unit_ (IMU) / gyro can provide stabilization for aircraft without a flight controller. A <abbr title="Do It Yourself">DIY</abbr> gyro can also be added to some receivers, see [Gyro Receiver Mod](../hardware/gyro-receiver-mod.md) for details.

!!! Note
    Use the ExpressLRS Product Finder to list supported receivers with a gyro! https://www.expresslrs.org/product-finder/?search=gyro&classification=receiver

When a receiver acts as a gyro, it doesn't only output the channel values that it receives from the transmitter. Instead, the receiver _computes_ adequate output values based on:

- the channel values sent by the transmitter (i.e. the position of the sticks)
- the aircraft attitude, as measured by the <abbr title="Inertial Measuement Unit">IMU</abbr>
- the **gyro mode** currently active
- a **gyro gain** calculated for each axis and each _gyro mode_

How those parameters are balanced can be controlled by:

- the [**stick priority**](#stick-priority) setting
- the adjustable [**gyro gain**](#gyro-functions) value
- the [**rate gain multiplier**](#rate-gain-multiplier) setting
- the **gain** settings that are configurable for each axis in each _gyro mode_ (see [Gyro mode tuning](#gyro-mode-tuning))

This guide explains how to configure the receiver, and what to expect from each of the available _gyro modes_.

## Main setup

### Enable gyro

When the gyro is disabled, the receiver works normally without Gyro functionality.

=== "WebUI"

    Start the WebUI on the receiver and go to the `Gyro` tab. In the `Main Setup` panel, check `Enable Gyro`. Once enabled, the `Status` panel should indicate that the **gyro state** is OK.

    If the gyro state is not OK, see [Gyro state](#gyro-state) first, or [Troubleshooting](../../hardware/gyro-receiver-mod/#testing) if needed.

    Image TK

=== "Lua script"

    TK

### Rate gain multiplier

The **rate gain multiplier** adjusts the sensitivity of the gyro in **rate mode**, in order to allow the **gyro gain** to provide a meaningful adjusting range (see [Channel functions](#channel-functions)). A value of `1x` is usually a good starting point.

If your gyro is too sensitive even when the **gyro gain** is low, it could be useful to lower the sensitivity (`0.5x`). On the contrary, if you reach 100% of the **gyro gain**, it may be useful to increase the sensitivity (`1.5x`, `2x`).

=== "WebUI"

    Start the WebUI on the receiver and go to the `Gyro` tab. In the `Main Setup` panel, select the desired **rate gain multiplier**.

    Image TK

=== "Lua script"

    TK

!!! Note
    Always start testing with a low **gyro gain**.

    - <abbr title="Electric Ducted Fan">EDF</abbr> and fast aircraft can benefit from a low **rate gain multiplier**: `0.5x`
    - Slow aircraft, on the contrary, might require a higher multiplier: `1.5x` or `2x`
    - For testing on the bench, you might need to increase the **rate gain multiplier** in order to see the surfaces move! (`2x`)

### Gyro mode switch

Define which gyro [**modes**](#gyro-mode-tuning) are activated by the **gyro mode** channel.

The gyro mode switch can be defined as a 2, 3, 5 or 6-position switch in the **gyro mode** channel settings (see [Channel functions](#channel-functions)). A typical three-position switch will use `-100`,`0`,`+100` channel values.

??? tip "EdgeTX: Want a custom number of positions? (click/tap to expand)"
    Two, three and six positions are well covered by typical EdgeTX hardware.

    In addition, using EdgeTX _special functions_ allows to combine multiple switches to operate the **gyro mode** channel.

    Example with 4 positions: use the 5-position switch type, and set `-50=Off`, `0=Rate`, `+50=Envelope`, `+100=Auto-Level` in the gyro. On your transmitter, a 3-pos switch with a _weight_ of `50%` will take care of the first three. To activate `Auto-Level`, create a _special function_ on another switch (ex. `SH`) to override the **gyro mode** channel to `+100`.

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

Indicates when the sensor was detected and initialized correctly. Also indicates when the [**orientation settings**](#orientation-settings), and the [**level calibration**](#level-calibration) are missing.

### Link

Indicates whether the receiver is connected to the transmitter.

!!! Note
    The [**endpoint calibration**](#endpoint-calibration) wizard requires a connection to the transmitter.

!!! Info
    ExpressLRS versions that provide Gyro support allow the receiver to start the WiFi while connected to the transmitter.

    While the receiver is connected to the transmitter, open the ExpressLRS Lua script, in `Other devices` select your receiver. Then `Enable Web Config` to start the Wifi, and access the WebUI as you usually do.

### Orientation settings

In order to interpret the measurements from the <abbr title="Inertial Measuement Unit">IMU</abbr>, the gyro needs to know its orientation in the aircraft.

For best results, the **orientation settings** should be updated every time the receiver position in the aircraft has changed.

??? Warning "Only some gyro orientations are supported. (click/tap to expand)"
    Currently, the gyro **must be oriented along the axes of rotation of the aircraft**.

    Example: if the gyro is aligned with the receiver, the receiver can be installed upside-down or sideways, but _oblique_ positions are unsupported.

=== "WebUI"

    Start the WebUI on the receiver and go to the `Gyro` tab. In the `Status` panel, press `Orientation Wizard`.

    TK

=== "Lua script"

    TK

### Level calibration

In order to interpret the measurements from the <abbr title="Inertial Measuement Unit">IMU</abbr> accurately, the gyro needs to be calibrated in a level position.

=== "WebUI"

    Start the WebUI on the receiver and go to the `Gyro` tab. In the `Status` panel, press `Level Cal`.

    TK

=== "Lua script"

    TK

### Live attitude view

Allows to confirm that the gyro [**orientation**](#orientation) settings, and that the [**level calibration**](#level-calibration) are correct by rendering the measurements performed by the <abbr title="Inertial Measuement Unit">IMU</abbr>.

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

    The receiver emits three telemetry sensors that reflect the <abbr title="Inertial Measuement Unit">IMU</abbr> measurements: `Ptch`, `Roll`, and `Yaw`.

    Some community EdgeTX widgets allow to visualize the attitude of the aircraft based on those telemetry sensors.

    Example: https://github.com/qsiguy/EdgeTX-Widgets/tree/main/AttIndV2

    !!! Info
        If you find that the values are not updated often enough, you can increase the [Telemetry ratio](../../quick-start/transmitters/lua-howto/#packet-rate-and-telemetry-ratio). Setting higher telemetry ratios (like `1:8`, `1:4`, `1:2`) increases the frequency of updates.

## Channel functions and limits

### Channel functions

=== "WebUI"

    Start the WebUI on the receiver and go to the `Gyro` tab. The `Channel Functions & Limits` panel allow to define and configure channel functions.

    TK

=== "Lua script"

    TK

#### Settings

- **Channel**: both the incoming channel (from the transmitter) and the output channel (on the PWM receiver pins). _The transmitter setup and receiver setup must match. Mixing channels on the receiver is not possible._
- **Function**: the [**gyro function**](#gyro-functions) assigned to that channel output.
- **Master**: when multiple channels are assigned the same _function_, the value of the **master** channel will be taken into account by the gyro to calculate the output.
- **Invert**: whether the output of the channel should be inverted.
- **Min/Mid/Max**: center value and limits of the PWM output (in milliseconds).
- Gyro mode **switch type**: choose between a 2, 3, 5 or 6-position gyro mode switch.

#### Gyro functions

- **Aileron**, **Elevator**, **Rudder** outputs
- **Elevon** output (`Elevon`, `Elevon R`): Elevator + Aileron mix (left and right)
- **V-Tail** output (`V-Tail`, `V-Tail R`): Elevator + Rudder mix (left and right)
- **Gyro Mode**: incoming channel that commands the [**gyro mode** switch](#gyro-mode-switch).
- **Gyro Gain**: incoming channel that defines the **gyro gain** value.

??? Tip "Elevon/V-Tail configuration advice (click/tap to expand)"
    First assign the `V-Tail`/`Elevon` function and make sure that the gyro operates the _elevator_ in the correct direction for both surfaces. Use the **invert** setting if necessary.

    Then assign the `V-Tail R`/`Elevon R` function to correct the _rudder/aileron_ direction on the channel that needs it.


### Endpoint calibration

Records the center value and maximum range of the incoming channels, so that the gyro outputs don't risk damaging mechanical links.

=== "WebUI"

    Start the WebUI on the receiver and go to the `Gyro` tab. In the `Channel Functions & Limits` panel press the `ENDPOINT CAL` button.

    First center the sticks and `CAPTURE CENTERS`. Then move the sticks across the totality of their range and `FINISH CALIBRATION`.

    Images TK

=== "Lua script"

    TK

## Gyro mode tuning

=== "WebUI"

    Start the WebUI on the receiver and go to the `Gyro` tab. The `Gyro Mode Tuning` panel displays the tuning parameters for each gyro mode.

    Image TK

=== "Lua script"

    TK

### Rate Mode

_Also known as: wind rejection mode, stabilized mode_

The gyro corrects movements of the aircraft that are not the result of stick inputs.

#### Stick Priority

A variable gain that depends on the stick deflection. The gyro gain decreases as the stick deflection increases. The **stick priority** value defines at which point of the stick travel the gyro gain reaches zero.

By default, **stick priority** value is `100%`. At stick center, gyro gain is fully applied, and starts declining as the stick deflection increases. When the stick reaches 50% of its travel, the gyro gain has been reduced by half, and at full stick deflection (`100%` of travel) the gyro gain is zero.

When stick priority is set to `60%`, the gyro gain is still applied fully when the stick is centered. It is reduced by half when the stick reaches `30%` of its travel, and reaches zero when the stick reaches `60%` of its travel.

#### Gains

Define how much of the maximum output travel the gyro should use. With higher gains, the gyro deflects the surfaces more, up to `100%` of their maximum travel. A value of `35%` is a good starting point.

### Envelope Mode

_Also known as: max angle envelope protection, horizon mode_

The gyro behaves like in **Rate mode**, but will keep the aircraft within the configured pitching and banking limits.

#### Use Rate

Combines Envelope with **Rate mode** behavior for wind rejection. When disabled, the gyro only activates when the **angle limits** are reached.

#### Limit Pitch/Roll

The maximum pitching and banking angles, in degrees.

#### Gains

Define how much of the maximum output travel the gyro should use. With higher gains, the gyro will bring the aircraft back within the pitching and banking limits more aggressively. A value of `35%` is a good starting point.

### Auto-level Mode

_Also know as: level mode, angle mode, angle demand_

The gyro keeps the aircraft flying level when the sticks are centered. It also prevents pitching or banking past the **angle limits**.

Move the stick 50% of the maximum travel, the aircraft will bank/pitch 50% of the **angle limit**.

Example: if **limit roll** is set to `70deg`, and the aileron stick is half way out, the aircraft will fly at a `35deg` banking angle.

#### Use Rate

Combines Auto-Level with **Rate mode** behavior for wind rejection.

#### Trims

Ensure that the aircraft is flying level when the sticks are centered.

On the _pitch_ axis, positive(+) brings the nose up, negative (-) brings nose down. On the _roll_ axis, positive(+) causes banking to the left.

#### Limit Pitch/Roll

The maximum pitching and banking angles, in degrees.

#### Gains

Define how much of the maximum output travel the gyro should use. With higher gains, the gyro will bring the aircraft to level more aggressively when the sticks are released. A value of `35%` is a good starting point.

### Launch

The gyro keeps the aircraft climbing at a set pitching angle, and a level banking angle when the sticks are centered.

#### Use Rate

Combines Launch with **Rate mode** behavior for wind rejection.

#### Trims

Ensure that the aircraft is climbing at a set pitching angle, and a level banking angle when the sticks are centered.

On the _pitch_ axis, positive(+) brings the nose up, negative (-) brings nose down. On the _roll_ axis, positive(+) causes banking to the left.

#### Gains

Define how much of the maximum output travel the gyro should use. With higher gains, the gyro will bring the aircraft to a stable climb more aggressively when the sticks are released. A value of `35%` is a good starting point.

### Hover

The gyro keeps the aircraft flying in a vertical hover position when the sticks are centered.

#### Use Rate

Combines Hover with **Rate mode** behavior for wind rejection.

#### Gains

Define how much of the maximum output travel the gyro should use. With higher gains, the gyro will bring the aircraft to hover more aggressively when the sticks are released. A value of `35%` is a good starting point.