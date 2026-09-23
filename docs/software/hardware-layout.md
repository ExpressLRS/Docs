---
template: main.html
description: Field reference for the ExpressLRS Hardware Layout page, covering every option in hardware.json.
---

![Software Banner](https://raw.githubusercontent.com/ExpressLRS/ExpressLRS-Hardware/master/img/software.png)

## Description

The Hardware Layout page in the [Web UI](../quick-start/webui.md) holds the hardware definition for your device. It records which pin does what, how the radio is wired, how power is controlled, and which peripherals are fitted. The device stores it as a file called `hardware.json`.

Every target already ships with a correct layout. You only need this page if you are bringing up a new board, or if you have been asked to change a specific field.

!!! danger "Danger"
    A wrong value here can stop the device from starting, and can damage the hardware. Setting a power table that the amplifier cannot deliver, or pointing a pin at the wrong function, is not protected against. Export your settings from the Import/Export tab before you change anything, and change one field at a time.

!!! note "Note"
    Changing the Hardware Layout does not change what the hardware is. Raising `Max Power` on a receiver without a power amplifier makes the device report a higher number. It does not make the device transmit at that power.

## How to Read This Reference

`Field` is the key as it appears in `hardware.json`. `Name` is the label shown in the Web UI.

`Type` is one of:

| Type | Meaning |
|---|---|
| `uint` | Whole number with no sign. Pin fields use the GPIO number. |
| `int` | Whole number that may be negative. |
| `float` | Decimal number. |
| `checkbox` | Enabled or disabled. |
| `array` | Comma separated list of values. |
| `select` | One value from a fixed list. |

Leave a pin field empty, or set it to a negative number, when the device does not have that pin. The firmware treats both as not fitted.

Some fields only apply to certain hardware. Where that is the case, the restriction is stated on the section or in the description.

## Field Reference

### CRSF Serial Pins

| Field | Name | Type | Description |
|---|---|---|---|
| `serial_rx` | RX pin | `uint` | Pin used to receive CRSF signal from the handset |
| `serial_tx` | TX pin | `uint` | Pin used to transmit CRSF telemetry to the handset (may be the same as the RX PIN) |

### Serial2 Pins

*ESP32 only.*

| Field | Name | Type | Description |
|---|---|---|---|
| `serial1_rx` | RX pin | `uint` | Serial2 RX - ESP32 targets only |
| `serial1_tx` | TX pin | `uint` | Serial2 TX - ESP32 targets only |

### Radio Chip Pins & Options

| Field | Name | Type | Description |
|---|---|---|---|
| `radio_busy` | BUSY pin | `uint` | GPIO Input connected to SX128x busy pin (Not on SX127x radios.) |
| `radio_dio0` | DIO0 pin | `uint` | Interrupt pin for SX127x (SX127x radios only.) |
| `radio_dio1` | DIO1 pin | `uint` | Interrupt pin for SX128x/LR1121 (Not on SX127x radios.) |
| `radio_miso` | MISO pin | `uint` | MISO connected to (possibly) multiple SX1280/127x |
| `radio_mosi` | MOSI pin | `uint` | MOSI connected to (possibly) multiple SX1280/127x |
| `radio_nss` | NSS pin | `uint` | Chip select pin for first SX1280/127x |
| `radio_rst` | RST pin | `uint` | Reset pin connected to (possibly) multiple SX1280/127x |
| `radio_sck` | SCK pin | `uint` | Clock pin connected to (possibly) multiple SX1280/127x |
| `radio_busy_2` | BUSY_2 pin | `uint` | Busy pin for second SX1280 (ESP32 only. Not on SX127x radios.) |
| `radio_dio0_2` | DIO0_2 pin | `uint` | Interrupt pin for second SX127x (ESP32 only. SX127x radios only.) |
| `radio_dio1_2` | DIO1_2 pin | `uint` | Interrupt pin for second SX1280 (ESP32 only. Not on SX127x radios.) |
| `radio_nss_2` | NSS_2 pin | `uint` | Chip select pin for second SX1280 (ESP32 only.) |
| `radio_rst_2` | RST_2 pin | `uint` | Reset pin connected to second SX1280/127x (ESP32 only.) |
| `radio_dcdc` | DCDC enabled | `checkbox` | Use the SX1280 DC-DC converter rather than LDO voltage regulator (15uH inductor must be present) (Not on SX127x radios.) |
| `radio_rfo_hf` | RFO_HF enabled | `checkbox` | SX127x PA to use, either the RFO_HF or PA_BOOST (depends on circuit design) (Not on SX128x radios.) |
| `radio_rfsw_ctrl` | LR1121 RF Switch Controls | `array` | Comma-separated list of 8 values used for setting the LR1121 RF switch controls (LR1121 radios only.) |

### Radio Antenna

| Field | Name | Type | Description |
|---|---|---|---|
| `ant_ctrl` | Antenna select pin | `uint` | Pin connected to Antenna select pin on power amplifier or switch |
| `ant_group` | Antenna group pin | `uint` | Secondary pin connected to an antenna switch, used to select from internal/external antenna port(s) via Lua (Receivers only.) |

### Radio Power

| Field | Name | Type | Description |
|---|---|---|---|
| `power_enable` | PA enable pin | `uint` | Enable the power amplifier (active high) |
| `power_apc2` | APC2 pin | `uint` | Power amplifier control voltage |
| `power_rxen` | RXEN pin | `uint` | Enable RX mode LNA (active high) |
| `power_txen` | TXEN pin | `uint` | Enable TX mode PA (active high) |
| `power_rxen_2` | RXEN_2 pin | `uint` | Enable RX mode LNA on second SX1280 (active high) (ESP32 only.) |
| `power_txen_2` | TXEN_2 pin | `uint` | Enable TX mode PA on second SX1280 (active high) (ESP32 only.) |
| `power_min` | Min Power | `select` | Minimum selectable power output Options: 10mW, 25mW, 50mW, 100mW, 250mW, 500mW, 1000mW, 2000mW |
| `power_max` | Max Power | `select` | Maximum selectable power output Options: 10mW, 25mW, 50mW, 100mW, 250mW, 500mW, 1000mW, 2000mW |
| `power_default` | Default Power | `select` | Default power output when resetting or first flashing a module Options: 10mW, 25mW, 50mW, 100mW, 250mW, 500mW, 1000mW, 2000mW |
| `power_control` | Power Level control | `select` | How the power level is set Options: via SEMTECH, via ESP DACWRITE |
| `power_values` | Power Value(s) | `array` | Comma-separated list of values that set the power output (if using a DAC these are the DAC values) |
| `power_values2` | Secondary Power Value(s) | `array` | Comma-separated list of values that set the power output (if using a DAC then these set the Semtech power output) |
| `power_values_dual` | Dual Power Value(s) | `array` | Comma-separated list of values that set the higher frequency power output of a dual band Tx/Rx (LR1121 radios only.) |
| `power_lna_gain` | PA LNA Gain | `uint` | The amount of dB gain provided by the LNA |

### Radio Power Detection

*Transmitters only.*

| Field | Name | Type | Description |
|---|---|---|---|
| `power_pdet` | PDET pin | `uint` | Analog input (up to 1.1V) connected to 'power detect' pin on PA for adjustment of the power output |
| `power_pdet_intercept` | Intercept | `float` | Intercept and Slope are used together to calculate the dBm from the measured mV on the PDET pin |
| `power_pdet_slope` | Slope | `float` | dBm = mV * slope + intercept, this is then used to adjust the actual output power accordingly |

### Analog Joystick

*Transmitters only.*

| Field | Name | Type | Description |
|---|---|---|---|
| `joystick` | ADC pin | `uint` | Analog Input (3.3V max) use to read joystick direction using a resistor network |
| `joystick_values` | Values | `array` | Comma-separated list of ADC values (12-bit) for UP, DOWN, LEFT, RIGHT, ENTER, IDLE |

### Digital Joystick

*Transmitters only.*

| Field | Name | Type | Description |
|---|---|---|---|
| `five_way1` | Pin 1 | `uint` | These 3 pins create a binary value for the joystick direction |
| `five_way2` | Pin 2 | `uint` | 7 = IDLE, 6 = OK, 5 = DOWN |
| `five_way3` | Pin 3 | `uint` | 4 = RIGHT, 3 = UP, 2 = LEFT |

### Mood Lighting

| Field | Name | Type | Description |
|---|---|---|---|
| `led_rgb` | RGB LED pin | `uint` | Signal pin for WS2812 RGB LED or LED strip |
| `led_rgb_isgrb` | RGB LED is GRB | `checkbox` | Most WS2812 RGB LEDs are actually GRB |
| `ledidx_rgb_status` | RGB indexes for Status | `array` | Indexes into the "string" of RGB LEDs (if empty then only LED at 0 is used) |
| `ledidx_rgb_vtx` | RGB indexes for VTX Status | `array` | Indexes into the "string" of RGB LEDs (if empty then no VTX status) (Receivers only.) |
| `ledidx_rgb_boot` | RGB indexes for Boot animation | `array` | Indexes into the "string" of RGB LEDs (if empty status indexes are used) |
| `led` | LED pin | `uint` | Pin used for single color LED (Receivers only.) |
| `led_red_invert` | LED inverted | `checkbox` | LEDs are active LOW unless this is checked (Receivers only.) |
| `led_red` | Red LED pin | `uint` | If there are multiple LEDs, then this is the pin for the RED LED (Transmitters only.) |
| `led_red_invert` | Red LED inverted | `checkbox` | LEDs are active LOW unless this is checked (Transmitters only.) |
| `led_green` | Green LED pin | `uint` | If there is a GREEN LED as well as RED above (Transmitters only.) |
| `led_green_invert` | Green LED inverted | `checkbox` | Check if the LED is active HIGH (Transmitters only.) |
| `led_blue` | Blue LED pin | `uint` | Pin for a 3rd, BLUE, LED! (Transmitters only.) |
| `led_blue_invert` | Blue LED inverted | `checkbox` | Check if the LED is active HIGH (Transmitters only.) |

### Button(s)

| Field | Name | Type | Description |
|---|---|---|---|
| `button` | Button 1 pin | `uint` | Single/first (active low) button |
| `button_led_index` | Button 1 RGB Index | `uint` | Index of button LED in RGB string, leave empty for no RGB LED (Transmitters only.) |
| `button2` | Button 2 pin | `uint` | Second (active low) button (Transmitters only.) |
| `button2_led_index` | Button 2 RGB Index | `uint` | Index of button LED in RGB string, leave empty for no RGB LED (Transmitters only.) |

### OLED/TFT (Crotch TV)

*Transmitters only.*

| Field | Name | Type | Description |
|---|---|---|---|
| `screen_type` | Screen type | `select` | Options: None, I2C OLED (SSD1306 128x64), SPI OLED (SSD1306 128x64), SPI TFT (ST7735 160x80) |
| `screen_reversed` | 180 rotation | `checkbox` | Select to rotate the display 180 degrees |
| `screen_mirror` | Screen mirror | `checkbox` | Mirror the display horizontally. Combine with "180 rotation" for vertical mirror. OLED only; no effect on SPI TFT screens. |
| `screen_cs` | CS pin | `uint` | Chip Select (if using SPI) |
| `screen_dc` | DC pin | `uint` | Data/Command Select (if using SPI) |
| `screen_mosi` | MOSI pin | `uint` | Data (if using SPI) |
| `screen_rst` | RST pin | `uint` | Reset |
| `screen_sck` | SCK pin | `uint` | Clock (either SPI or I2C) |
| `screen_sda` | SDA pin | `uint` | Data (I2C) |
| `screen_bl` | BL pin | `uint` | Backlight |

### Backpack / Logging

*Transmitters only.*

| Field | Name | Type | Description |
|---|---|---|---|
| `use_backpack` | Enable Backpack | `checkbox` | If a TX backpack is connected |
| `debug_backpack_baud` | Baud Rate | `uint` | Baud rate used to communicate to the backpack (normally 460800) |
| `debug_backpack_rx` | RX pin | `uint` | Connected to TX pin on backpack |
| `debug_backpack_tx` | TX pin | `uint` | Connected to RX pin on backpack |
| `backpack_boot` | BOOT pin | `uint` | Pin connected to GPIO0 pin on backpack ESP8285, allows passthrough flashing |
| `backpack_en` | EN pin | `uint` | Pin connected to EN pin on backpack ESP8285, allows passthrough flashing |
| `passthrough_baud` | Passthrough baud | `uint` | Baud rate to flash the backpack ESP8285 (default is to use the baud rate above) |

### I2C & Misc Devices

*Transmitters only.*

| Field | Name | Type | Description |
|---|---|---|---|
| `i2c_scl` | SCL pin | `uint` | I2C clock pin used to communicate with I2C devices (may be the same as OLED I2C) |
| `i2c_sda` | SDA pin | `uint` | I2C data pin used to communicate with I2C devices (may be the same as OLED I2C) |
| `misc_fan_en` | Fan enable pin | `uint` | Pin used to enable a cooling FAN (active HIGH) |
| `misc_fan_pwm` | Fan PWM pin | `uint` | If the fan is controlled by PWM |
| `misc_fan_speeds` | Fan PWM output values | `array` | If the fan is PWM controlled, then this is the list of values for the PWM output for the matching power output levels |
| `misc_fan_tacho` | Fan TACHO pin | `uint` | If the fan has a "tachometer" interrupt pin |
| `gsensor_stk8xxx` | Has STK8xxx G-sensor | `checkbox` | Checked if there is a STK8xxx g-sensor on the I2C bus |
| `misc_gsensor_int` | G-sensor interrupt pin | `uint` | Pin connected the STK8xxx g-sensor for interrupts |
| `thermal_lm75a` | Has LM75A Thermal sensor | `checkbox` | Checked if there is a LM75A thermal sensor on the I2C bus |

### PWM

*Receivers only.*

| Field | Name | Type | Description |
|---|---|---|---|
| `pwm_outputs` | PWM pins | `array` | Comma-separated list of pins used for PWM (and other I/O features) |
| `pwm_out_only` | PWM pins are output-only | `checkbox` | Enable this when the PWM pins are behind output-only buffers such as Schmitt triggers. Input or bidirectional functions like Serial and I2C will be disabled on PWM pins. |

### Voltage Sensors

*Receivers only.*

| Field | Name | Type | Description |
|---|---|---|---|
| `vbat` | VBat pin | `uint` | Primary analog input pin for battery voltage (1V max on 8285, 3.3V max on ESP32) |
| `vbat_offset` | VBat offset | `int` | Offset and scale are used together with the analog pin to calculate the voltage |
| `vbat_scale` | VBat scale | `uint` | voltage = (analog - offset) / scale |
| `vbat_atten` | VBat attenuation | `select` | ADC pin attenuation (ESP32) and optional efuse-based calibration adjustment Options: Default, 0 dB, 2.5 dB, 6 dB, 11 dB, 0 dB + calibration, 2.5 dB + calibration, 6 dB + calibration, 11 dB + calibration (ESP32 only.) |
| `vbat_noreading` | VBat no-reading threshold | `uint` | Raw ADC values at or below this are treated as not connected (0mV in cell telemetry) |
| `vbat_cal_min` | VBat calibration min | `uint` | Manufacturer-defined minimum supported source voltage in mV used by the calibration wizard |
| `vbat_cal_max` | VBat calibration max | `uint` | Manufacturer-defined maximum supported source voltage in mV used by the calibration wizard |
| `vsrc1` | VSrc1 pin | `uint` | Voltage source input pin for source 2 (ESP32 only.) |
| `vsrc1_offset` | VSrc1 offset | `int` | Offset used with the VSrc1 analog pin to calculate the voltage (ESP32 only.) |
| `vsrc1_scale` | VSrc1 scale | `uint` | voltage = (analog - offset) / scale (ESP32 only.) |
| `vsrc1_atten` | VSrc1 attenuation | `select` | ADC pin attenuation (ESP32) and optional efuse-based calibration adjustment Options: Default, 0 dB, 2.5 dB, 6 dB, 11 dB, 0 dB + calibration, 2.5 dB + calibration, 6 dB + calibration, 11 dB + calibration (ESP32 only.) |
| `vsrc1_noreading` | VSrc1 no-reading threshold | `uint` | Raw ADC values at or below this are treated as not connected (0mV in cell telemetry) (ESP32 only.) |
| `vsrc1_cal_min` | VSrc1 calibration min | `uint` | Manufacturer-defined minimum supported source voltage in mV used by the calibration wizard (ESP32 only.) |
| `vsrc1_cal_max` | VSrc1 calibration max | `uint` | Manufacturer-defined maximum supported source voltage in mV used by the calibration wizard (ESP32 only.) |
| `vsrc2` | VSrc2 pin | `uint` | Voltage source input pin for source 3 (ESP32 only.) |
| `vsrc2_offset` | VSrc2 offset | `int` | Offset used with the VSrc2 analog pin to calculate the voltage (ESP32 only.) |
| `vsrc2_scale` | VSrc2 scale | `uint` | voltage = (analog - offset) / scale (ESP32 only.) |
| `vsrc2_atten` | VSrc2 attenuation | `select` | ADC pin attenuation (ESP32) and optional efuse-based calibration adjustment Options: Default, 0 dB, 2.5 dB, 6 dB, 11 dB, 0 dB + calibration, 2.5 dB + calibration, 6 dB + calibration, 11 dB + calibration (ESP32 only.) |
| `vsrc2_noreading` | VSrc2 no-reading threshold | `uint` | Raw ADC values at or below this are treated as not connected (0mV in cell telemetry) (ESP32 only.) |
| `vsrc2_cal_min` | VSrc2 calibration min | `uint` | Manufacturer-defined minimum supported source voltage in mV used by the calibration wizard (ESP32 only.) |
| `vsrc2_cal_max` | VSrc2 calibration max | `uint` | Manufacturer-defined maximum supported source voltage in mV used by the calibration wizard (ESP32 only.) |
| `vsrc3` | VSrc3 pin | `uint` | Voltage source input pin for source 4 (ESP32 only.) |
| `vsrc3_offset` | VSrc3 offset | `int` | Offset used with the VSrc3 analog pin to calculate the voltage (ESP32 only.) |
| `vsrc3_scale` | VSrc3 scale | `uint` | voltage = (analog - offset) / scale (ESP32 only.) |
| `vsrc3_atten` | VSrc3 attenuation | `select` | ADC pin attenuation (ESP32) and optional efuse-based calibration adjustment Options: Default, 0 dB, 2.5 dB, 6 dB, 11 dB, 0 dB + calibration, 2.5 dB + calibration, 6 dB + calibration, 11 dB + calibration (ESP32 only.) |
| `vsrc3_noreading` | VSrc3 no-reading threshold | `uint` | Raw ADC values at or below this are treated as not connected (0mV in cell telemetry) (ESP32 only.) |
| `vsrc3_cal_min` | VSrc3 calibration min | `uint` | Manufacturer-defined minimum supported source voltage in mV used by the calibration wizard (ESP32 only.) |
| `vsrc3_cal_max` | VSrc3 calibration max | `uint` | Manufacturer-defined maximum supported source voltage in mV used by the calibration wizard (ESP32 only.) |

### SPI VTX

*Receivers only. ESP32 only.*

| Field | Name | Type | Description |
|---|---|---|---|
| `vtx_amp_pwm` | RF amp PWM pin | `uint` | Set the power output level of the VTX PA (value is calculated based on power and frequency using VPD interpolation values) |
| `vtx_amp_vpd` | RF amp VPD pin | `uint` | Analog input for VPD (power detect) from VTX PA |
| `vtx_amp_vref` | RF amp VREF pin | `uint` | Active high enable pin the the VTX PA VREF (voltage reference) |
| `vtx_nss` | SPI NSS pin | `uint` | Chip select for RTC6705 VTx (leave undefined if sharing Radio SPI bus) |
| `vtx_sck` | SPI SCK pin | `uint` | Clock pin on RTC6705 VTx (leave undefined if sharing Radio SPI bus) |
| `vtx_miso` | SPI MISO pin | `uint` | MISO pin on RTC6705 VTx (leave undefined if sharing Radio SPI bus) |
| `vtx_mosi` | SPI MOSI pin | `uint` | MOSI pin on RTC6705 VTx (leave undefined if sharing Radio SPI bus) |
| `vtx_amp_vpd_25mW` | 25mW VPD interpolation values | `array` | 4 values for 5650, 5750, 5850, 5950 frequencies at 25mW |
| `vtx_amp_vpd_100mW` | 100mW VPD interpolation values | `array` | 4 values for 5650, 5750, 5850, 5950 frequencies at 100mW |
| `vtx_amp_pwm_25mW` | 25mW PWM interpolation values | `array` | 4 values for 5650, 5750, 5850, 5950 frequencies at 25mW |
| `vtx_amp_pwm_100mW` | 100mW PWM interpolation values | `array` | 4 values for 5650, 5750, 5850, 5950 frequencies at 100mW |

### I2C

*Receivers only. ESP32 only.*

| Field | Name | Type | Description |
|---|---|---|---|
| `i2c_scl` | SCL pin | `uint` | I2C clock pin used to communicate with I2C devices |
| `i2c_sda` | SDA pin | `uint` | I2C data pin used to communicate with I2C devices |

