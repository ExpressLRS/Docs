---
template: main.html
description: A guide on how to add an IMU / gyro to an ExpressLRS receiver.
---

![Hardware-Banner](https://raw.githubusercontent.com/ExpressLRS/ExpressLRS-Hardware/master/img/hardware.png)

## Overview

ExpressLRS receivers that are equipped with an _inertial measurement unit_ (IMU) / gyro can provide stabilization for aircraft without a flight controller. See [Gyro](../software/gyro.md) for details.

This guide explains how to attach a <abbr title="Do It Yourself">DIY</abbr> board to an existing receiver.

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

    Start the WebUI on the receiver and go to the `Gyro` tab.

    Image TK

=== "Lua script"

    TK

=== "Serial console"

    The IMU detection and gyro initialization is logged to the serial monitor.

    1. Connect the receiver equipped with the IMU board to a computer, using an FTDI adapter (USB/Serial converter).
    2. Open a serial monitor at 115200 baud.
       Example: `sudo minicom --device /dev/ttyUSB0 --baudrate 115200`
    3. Restart the receiver to capture the gyro initialization.
       Example output:
       ```
         [...]
         Starting wire on SCL 18, SDA 23
         SPI: gpio_sck :-1, gpio_miso: -1, gpio_mosi: -1, gpio_nss: -1, gpio_int -1
         Initializing PWM output: ch: 0, pin: 14
         Initializing PWM output: ch: 0, pin: 1
         Initializing PWM output: ch: 0, pin: 3
         Initializing PWM output: ch: 3, pin: 15
       > Starting I2C Gyro on SCL 2, SDA 4
       > Detecting MPU6050 (Address 0x68)
       > Gyro Id returned = 0x38
       > Gyro Init
       > Gyro Config Load
       > Gyro Config: version 9
         Detected baro: SPL06
         UID=(11, 22, 33, 44, 55, 66) ModelId=255
         Primary Domain ISM2G4, 80 channels, sync=40
         Hal Init
         SX1280 Reset
         SX1280 Ready!
         SX1280 Begin
         RFAMP_hal Init
         Use TX pin: 26
         Read Vers sx1280 #1: 43447
         Enabling DCDC regulator
         SetPower: 21
         Config LoRa hwTimer Init
       > RxPratameters.registerParameters(): Setting up GYRO LUA
       > RxPratameters.registerParameters(): GYRO LUA Done
       > Gyro Start
       > Gyro AHRS Start
         [...]
       ```

    TK

## Troubleshooting

??? faq "If the gyro is enabled, why is status not OK?"
    - Check the gyro [**orientation settings**](../software/gyro.md#orientation-settings), and [**level calibration**](../software/gyro.md#level-calibration).
    - Check the [**endpoint calibration**](../software/gyro.md#endpoint-calibration).
    - If using a <abbr title="Do It Yourself">DIY</abbr> board, check that it is connected to the correct I2C or SPI port. (Example: <abbr title="Do It Yourself">DIY</abbr> receivers with an integrated vario may use a distinct I2C bus for the vario and the gyro.)

??? faq "Why do Aileron and Elevator functions seem coupled?"
    In **Auto-Level** mode, assuming that sticks are centered, if the elevator moves when the aircraft banks, or the ailerons move when the aircraft pitches up or down, the physical **orientation** of the IMU might not be aligned on the aircraft axes of rotation. See known limitations in [Orientation settings](../software/gyro.md#orientation-settings).

??? faq "Two PWM channels are not working!"
    When the debugging options are used, the pins used by the debug UART are disconnected. Build the firmware again without the `-DDEBUG_LOG` or `-DDEBUG_RCVR_LINKSTATS` options.
