---
template: main.html
description: A short guide on how to add an IMU / gyro to an ExpressLRS receiver.
---

![Hardware-Banner](https://raw.githubusercontent.com/ExpressLRS/ExpressLRS-Hardware/master/img/hardware.png)

## Overview

ExpressLRS receivers that are equipped with an _inertial measurement unit_ (IMU) / gyro can provide stabilization for aircraft without a flight controller. See [Gyro](../software/gyro.md) for details.

This guide explains how to attach a DIY board to an existing receiver.

## Supported hardware

### IMU / gyro boards:

- MPU6050: very common, supports 5V.
- LSM6Dxx: not that common. Only supports 3.3V and will need a voltage regulator.

### Receivers

Any supported receiver based on the ESP32 chip, with an accessible I2C or SPI bus. Example: BetaFPV Super-P, RadioMaster ER6, ER8, even ER6GV (via PWM pins).

??? Info "Finding supported ESP32 receivers. (click/tap to expand)"
    In the [official targets list](https://github.com/ExpressLRS/Targets/blob/master/targets.json), the field `"platform": "esp32"` indicates that the receiver is based on an ESP32 chip.

    If the receiver has PWM pins or multiple UART pads, those may be remapped as I2C or SPI pins.

## Receiver configuration

=== "WebUI"

    TK

=== "Target file"

    TK

## Wiring


=== "I2C"

    - The `SCL` pad on the <abbr title="Inertial Measurement Unit">IMU</abbr> board must be connected to the `SCL` pin on the receiver.
    - The `SDA` pad on the <abbr title="Inertial Measurement Unit">IMU</abbr> board must be connected to the `SDA` pin on the receiver.
    - The `VCC` pad on the <abbr title="Inertial Measurement Unit">IMU</abbr> board must be connected to a `+` pin on the receiver.
    - The `GND` pad on the <abbr title="Inertial Measurement Unit">IMU</abbr> board must be connected to a `-` pin on the receiver.

=== "SPI"

    TK

### Wiring examples

<figure markdown>
  ![TX Binding Tab](../assets/images/gyro/BetaFPV-Super-P-MPU6050.jpg)
  <figcaption>BetaFPV Super-P with MPU6050 over I2C</figcaption>
</figure>

<figure markdown>
  ![TX Binding Tab](../assets/images/gyro/RadioMaster-ER6GV-MPU6050.png)
  <figcaption>RadioMaster ER6GV with MPU6050 over I2C via PWM pins</figcaption>
</figure>

## Testing

=== "WebUI"

    TK

=== "Lua script"

    TK

=== "Serial console"

    TK

## Troubleshooting

TK

??? faq "If the gyro is enabled, why is status not OK?"
    TK
