---
template: main.html
---

<img src="https://raw.githubusercontent.com/ExpressLRS/ExpressLRS-Hardware/master/img/software.png">

## Model Configuration

The ExpressLRS stores unique configurations based on the Recevier number configured in OpenTX/EdgeTX.

The parameters that are unique to a configuration are as follows:
| Setting | Description |
|---|---|
| P.Rate | The RC update frequency in Hz |
| T.Rate | Telemetry rate, (off, 1/128, 1/64, 1/32, 1/16, 1/8, 1/4, 1/2) |
| Power | Transmitter output power level in dBm |
| Switch | Either 1-bit or Hybrid8 mode |
| Model Match | A flag that tells the transmitter to tenable model matching |

## Model Match

If the *Model Match* flag in the LUA script is enabled, then the receiver number configured in the external module configuration must match the model number stored on the receiver module for the receiver and transmitter to connect.

If the *Model Match* flag is disabled, then receivers with a model number of 0 are matched irrespective of the receiver number configure in the transmitter model configuration screen. In this mode you can have different settings for the transmitter module e.g. different switch mode, power settings for different situations.

### Setting the Receiver's Model ID

To set a model id on a receiver, there are multiple methods.
1. On the web interface on wifi-enabled RX modules there is a section that allows you to enter or change the model number.
2. Once you are connected to a receiver, you can change the model number from the LUA script by changing the model number in the `Set RX Model` field and pressing enter. The RX will save the model number and reboot. You will then need to enable model match above with the tx module receiver number configured to match.
3. Flash the RX module with a default model id using `-DMODEL_MATCH_ID=x`, where x in the model number you wish to use.
