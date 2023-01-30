---
template: main.html
description: Get your Radio Handset prepared for ExpressLRS with this setup guide.
---

![Setup-Banner](https://raw.githubusercontent.com/ExpressLRS/ExpressLRS-hardware/master/img/quick-start.png)

## Compatibility Requirements for ExpressLRS

### Requirements for High Packet Rate Support

To ensure full support for high packet rates, ExpressLRS requires either `CRSFShot` or Mixer Sync. If you are using OpenTX, make sure to update to [OpenTX-2.3.12](https://www.open-tx.org/2021/06/14/opentx-2.3.12) or later, as CRSFShot has been fully integrated into these [newer](https://www.open-tx.org/downloads.html#Releases23-ref) versions.

### Recommendation for Best Experience

The ExpressLRS development team highly recommends using [EdgeTX](https://github.com/EdgeTX/edgetx/releases) for the best experience and compatibility. EdgeTX offers options that will benefit both old and new radio handsets, including the One Bit sample mode for older Frsky radios (X9D, QX7) and support for Mega Bauds (baud rates higher than 400K). 

## Radio Setup

### Serial Baud Rate

The Baud Rate determines the communication speed between the Transmitter module and the Radio Handset, expressed in bits per second. Common baud rates are 115200bps and 400000bps.

A higher baud rate reduces the end-to-end latency of the system, but not all hardware supports higher rates. The baud rate setting can be found in the System Menu -> Hardware page, and can be changed to match your setup. On EdgeTX 2.7.0 and later, the Baudrate setting for external RF modules is located in the Model Setup section, while internal CRSF modules use the Baudrate setting in the System Menu -> Hardware page.

<figure markdown>
![Baudrate](../../assets/images/txprep-clr-hardware.jpg)
<figcaption>Baudrate setting on Colored Screen Radios</figcaption>
</figure>

<figure markdown>
![Baud Rate](https://fpvfrenzy.com/wp-content/uploads/2017/11/baud-rate.jpg)
<figcaption>Baudrate setting on Older Radios</figcaption>
</figure>

### Radio Packet Rate and Baud Rate Requirements

#### 500Hz Packet Rate

- A minimum of 400K Baud Rate setting is required on the radio handset.

#### F1000 Packet Rate

- Requires a Baud Rate setting of more than 400K on the radio handset.

#### Radio Handset Compatibility

- Frsky QX7, X10/S, and X12: [Crossfire Mod](https://blog.seidel-philipp.de/fixed-inverter-mod-for-tbs-crossfire-and-frsky-qx7/) or OneBit Sample mode (found in EdgeTX System Menu -> Hardware page) may be required for 400K or higher Baud Rate setting.
- Taranis X9D(+): Default 400K Baud Rate setting may not be sufficient and OneBit Sample Mode may be needed. (Refer to [Troubleshooting the X9D](../../hardware/x9d-troubleshooting.md) for more information)

!!! info "Note"
    When Radio Baud Rate is set at 115200, 250Hz will be the maximum Packet Rate you can use.

#### Module Compatibility

When adjusting the Baud Rate setting on your radio handset, it's important to take into account the type of module you are using. For example, the R9M 2018 may not be able to run at a Baud Rate of 400K, and may require a [Resistor Mod](../../hardware/inverter-mod.md) before it can be used. If you can run your radio handset at a lower Baud Rate of 115200, then the mod may not be necessary.

STM-based modules, such as the R9M 2019, Ghost, Happymodel ES915TX, and the Gen1 No OLED NamimnoRC Flash and Voyager modules, can run at a Baud Rate of 1.87M. On the other hand, ESP-based modules, such as the Happymodel ES24TX, BetaFPV Nano & Micro, and the Axisflying Thor, can run up to 3.75M or even 5.25M.

It's important to note that just because a higher Baud Rate is possible, it doesn't mean it's always the best option. If you're experiencing constant Telemetry Lost/Recovered even when in close proximity, or if Lua scripts are failing to load properly, this could be a sign that the selected Baud Rate is not compatible with your radio and/or module. In such cases, it may be necessary to lower the Baud Rate down a notch or settle with 400K.

### ADC Filter

The ADC filter is enabled by default in OpenTX, but it can cause problems with RC Command data. It can result in "jagged" RC command responses in black box logs because the filter smooths sequential RC packets with the same command value. We recommend turning off the ADC filter in [OpenTX/EdgeTX](https://www.youtube.com/watch?v=ESr2H_EZ89Q).

In EdgeTX 2.7 or newer, you can set this per-model (Global, On, Off), which is useful for Fixed Wing models equipped with PWM receivers connected to slower servos.

## Model Setup

### RF Protocol

!!! Note
    If you're using an External ExpressLRS Module, make sure the Internal RF Module is **OFF**.

    If your Radio has an Internal ExpressLRS Module, and you want to use it instead of an external module, then set External RF Module to **OFF**, and then set the Internal RF Module to **CRSF** Protocol.

ExpressLRS uses the CRSF serial protocol to communicate between the transmitter and the TX module. To set this up, enter into your model settings, and on the **Model Setup** tab, enable your **External RF** and select **CRSF** as the protocol:

<figure markdown>
![ExternalRF BW](../../assets/images/txprep-bw-externalRF.jpg)
</figure>

<figure markdown>
![ExternalRF Color](../../assets/images/txprep-clr-externalRF.jpg)
</figure>

### Internal ExpressLRS Module Configuration

For radios equipped with an Internal ExpressLRS module, such as the RadioMaster Zorro, RadioMaster TX16S MK2, RadioMaster TX12 MK2, Jumper T-lite V2, Jumper T-pro, or BetaFPV Lite Radio 3 Pro, set the Internal RF Module to CRSF Protocol and turn the External RF Module off if you want to use the internal ExpressLRS module instead of an external one. If the CRSF Protocol option is not available under the Internal RF Modes, set the `Internal Module Type` to CRSF through the `System Menu -> Hardware page`.

<figure markdown>
![InternalRF BW](../../assets/images/txprep-bw-internalRF.jpg)
</figure>

<figure markdown>
![InternalRF Color](../../assets/images/txprep-clr-internalRF.jpg)
</figure>

!!! Note
    The iFlight Commando 8 is NOT using an internal RF module for its ExpressLRS units, unlike the RadioMaster Zorro, RadioMaster TX16S MK2, RadioMaster TX12 MK2, Jumper T-lite V2, Jumper T-pro or the BetaFPV Lite Radio 3 Pro.

    Set the Internal RF module to Off, and set the External RF module to CRSF protocol, as any External RF module requires.

### Switches and Aux Channels

By default, a fresh model does not have any Aux Channels configured (Aux channels start from Ch5, with the first 4 Channels assigned to your joysticks). If moving any of the switches in your radio doesn't affect your Modes in Betaflight or INAV, this is one of the main reasons. So let's get this sorted out!

On the current model, navigate to the Mixes Page (Model Menu-> Mixes). You will need to assign switches to the remaining channels, as shown in the following images.

<figure markdown>
![mixes BW](../../assets/images/txprep-bw-mixes.jpg)
</figure>

<figure markdown>
![mixes Color](../../assets/images/txprep-clr-mixes.jpg)
</figure>

Select the Channel, long press Enter and select Edit. You can name this channel however you want to remind you of its purpose. Then under Source, set it to the Switch you'd want to use for this channel. An example would be for CH5, which will be your Arming switch, you'd want to choose a 2-position switch.

<figure markdown>
![mixesAux BW](../../assets/images/txprep-bw-mixAux.jpg)
</figure>

<figure markdown>
![mixesAux Color](../../assets/images/txprep-clr-mixAux.jpg)
</figure>

Once you're done, press the RTN key to go back to the Mixes page. Do the same to the rest of the Channels you need.

**Now that your radio is set, you can now proceed with flashing ExpressLRS!**