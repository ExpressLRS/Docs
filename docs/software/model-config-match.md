---
template: main.html
---

<img src="https://raw.githubusercontent.com/ExpressLRS/ExpressLRS-Hardware/master/img/software.png">

## Model Configuration

ExpressLRS stores unique configurations based on the CRSF Recevier number configured in OpenTX/EdgeTX. This can be used with or without model matching - for example a single drone being used for longrange and freestyle can have it's RF params switched quickly by changing the model on the radio. The value is shown highlighted below on a TX16s.

<img src="../../assets/images/modelcfg.jpg" width="50%">

The parameters that are unique to a configuration are as follows:

| Setting | Description |
|---|---|
| P.Rate | The RC update frequency in Hz |
| T.Rate | Telemetry rate, (off, 1/128, 1/64, 1/32, 1/16, 1/8, 1/4, 1/2) |
| Power | Transmitter output power level in dBm |
| Model Match | A flag that tells the transmitter to enable model matching |

## Model Match

If the `Model Match` flag is **disabled**, then recievers with model number 0 can be bound (any other number can not connect due to how the code functions). In this mode you can have different settings for the transmitter module regardless of RX e.g. different switch mode, power settings for different situations.

If the `Model Match` flag **is enabled**, then the receiver number configured in the external module configuration (as shown in the image above) must match the model number stored on the receiver module for the receiver and transmitter to connect.

There are multiple methods to set the model number of the reciever:

- On the web interface on wifi-enabled RX modules there is a section that allows you to enter or change the model number.
- Once you are connected to a receiver, you can change the model number from the LUA script by changing the model number in the `Set RX Model` field and pressing enter. The RX will save the model number and reboot. You will then need to insure that the TXes model number matches this set number and turn model match **on**
- Flash the RX module with a default model id using `-DMODEL_MATCH_ID=x`, where x in the model number you wish to use.
