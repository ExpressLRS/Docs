---
template: main.html
---

![Setup-Banner](https://raw.githubusercontent.com/ExpressLRS/ExpressLRS-hardware/master/img/quick-start.png)

## Radio Firmware with CRSFShot/Mixer Sync

ExpressLRS **requires** CRSFShot or Mixer Sync to ensure full support for high packet rates. Starting with [OpenTX-2.3.12](https://www.open-tx.org/2021/06/14/opentx-2.3.12), `CRSFshot` has been fully implemented, and thus you will have to update your OpenTX radio to these [newer](https://www.open-tx.org/downloads.html#Releases23-ref) versions.

Another alternative is [EdgeTX](https://github.com/EdgeTX/edgetx/releases), the bleeding edge fork of OpenTX.

These firmwares allow flashing of `.elrs` files too.

## CRSF Protocol

!!! Note
    If you're using an External ExpressLRS Module, make sure the Internal RF Module is **OFF**.

    If your Radio has an Internal ExpressLRS Module, and you want to use it instead of an external module, then set External RF Module to **OFF**, and then set the Internal RF Module to **CRSF** Protocol.

ExpressLRS uses the CRSF serial protocol to communicate between the transmitter and the TX module. To set this up, enter into your model settings, and on the "Model Setup" tab, enable your "External RF" and select "CRSF" as the protocol:

![CRSF](https://oscarliang.com/ctt/uploads/2018/03/setup-tbs-crossfire-tx-rx-micro-nano-taranis-betaflight-fc-internal-external-rf-mode.jpg)
![CRSF](https://oscarliang.com/ctt/uploads/2019/12/JUMPER-T16-EXTERNAL-RF-MODE-PROTOCOL-TBS-CROSSFIRE-CRSF.jpg)

For Radios equipped with Internal ExpressLRS modules, like the RadioMaster Zorro, set the Internal RF Module to **CRSF** Protocol and the External RF Module to OFF if you want to use the Internal ExpressLRS module instead of an external one. If for some reason, you cannot find the CRSF Protocol under the Internal RF Modes, activate the CRSF Internal module via your Radio's `System Menu -> Hardware`, `Internal Module Type`.

## Serial Baud Rate

On some transmitters, the baud rate for comms between the opentx and the ExpressLRS module can be changed. The two rates available are 115200 and 400000. ExpressLRS supports both rates (auto switches to the correct rate on power-up), however, we have found that on the R9M 2018 modules, the inverter IC's that are used are not capable of reliably handling 400k baud. If you're using an R9M 2018 module, select 115200 baud in OpenTX, or do the resistor mod described on the [R9M 2018 Resistor Mod](../../hardware/inverter-mod.md) page.

The QX7, X10/S, X12 will also going to require the [Crossfire Mod](https://blog.seidel-philipp.de/fixed-inverter-mod-for-tbs-crossfire-and-frsky-qx7/) if you're going to use 400k baud rates for use with higher packet rates, particularly with the 2.4G ExpressLRS Modules. Alternatively, EdgeTX can be flashed into these Radios and have OneBit enabled.

The X9D(plus) can't change its Max Bauds settings, but it has been found to be finicky, causing unstable packet transfers, and constant Telemetry Lost/Recovered messages from OpenTX. One fix for this is the use of the OneBit firmware or EdgeTX. Click [here](../../hardware/x9d-troubleshooting.md) for more info.

![Baud Rate](https://fpvfrenzy.com/wp-content/uploads/2017/11/baud-rate.jpg)

If your radio is on EdgeTX, you can use higher Baud Rates than initially available. Max Baud Rate currently supported is 5.25M (EdgeTX 2.6.0) but not every ExpressLRS modules will be able to run at such speeds. If you're experiencing Telemetry Lost/Recovered notification from your Radio, set the Baud Rate to a much lower setting. Higher Baud Rate means faster transfer of data between radio and module, and faster load times of the Lua Script.

## ADC Filter

The ADC filter is enabled by default in OpenTX and is known to cause issues with RC Command data. This can result in "jagged" RC command responses in black box logs, caused by sequential RC packets that have the same command value (which were "smoothed" by the ADC filter). We recommend turning the ADC filter OFF in [OpenTX](https://www.youtube.com/watch?v=ESr2H_EZ89Q).

**Now that your radio is set, you can now proceed with flashing ExpressLRS!**