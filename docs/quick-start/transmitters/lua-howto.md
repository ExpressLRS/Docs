---
template: main.html
description: Here is a simple ExpressLRS Lua Script guide explaining the different options.
---

![Setup-Banner](https://github.com/ExpressLRS/ExpressLRS-Hardware/raw/master/img/quick-start.png)

Now that you have flashed your TX it is time to learn how to use the ELRS Lua script!

## Installing the Lua Script

Download the [ELRSv3 Lua Script](https://github.com/ExpressLRS/ExpressLRS/blob/3.x.x-maintenance/src/lua/elrsV3.lua?raw=true) (you can simply right-click, save-as) into your radio's SD Card under the `Scripts/Tools` folder and Long Press the "SYS" button (for T16 or similar Radios) or the "Menu" button (for Taranis X9D or similar Radios) to access the Tools Menu where you can find the ExpressLRS script ready to run with only one click.

Here's how it looks in the Tools menu (X9D+ and T16 Shown):

<figure markdown>
![Lua Script](../../assets/images/lua1.jpg)
</figure>

<figure markdown>
![Lua Script T16](../../assets/images/lua2.jpg)
</figure>

## Check if your TX is Connected

Enter the Lua script by selecting "ExpressLRS" in the Tools menu and pressing ENTER.

If the parameter list does not populate after a few seconds, and it's stuck at `Loading...`, first verify the ExpressLRS module has power by checking its LED. If there is no LED lit up, it is possible the Protocol set for the External Module is incorrect (should be set to CRSF) or that the module is not properly connected to the pins of the JR bay of the radio. Another possible reason is that you haven't updated the firmware of the module to version 2.x.

If parameters do show up, but the Bad/Good section on the right side of the header is showing an unstable value, have a look at your model settings and make sure the Internal RF module is set to Off. If the Bad/Good indicates something other than `0/<your selected packet rate>` this means `CRSFshot` is not working-- verify that you properly followed the [Radio Preparation](tx-prep.md) Guide.

<figure markdown>
![Lua3](../../assets/images/lua3.jpg)
</figure>

<figure markdown>
![Lua Script Config BW](../../assets/images/lua/config-bw.png)
</figure>

The `master 942c40` from the photo above is the git branch and commit hash of the firmware version that the module has. You can reference this hash from [Releases](https://github.com/ExpressLRS/ExpressLRS/releases). In the first photo above, `master` means the module is flashed with the `Master Branch` with the git commit `942c40`. If you're on a Released version or a Release Candidate, this will read something like `3.0` or `3.0-RC1` plus the commit hash of the release.

!!! note "Note"
    Colors may differ from Handset to Handset, depending on the current theme in use.

## Understanding and using the Lua Script
Now, we can explore the complexities of the Lua script, and how to interpret each of its many sections. ExpressLRS supports multiple configuration profiles, and the configuration profile is selected by setting the "Receiver" property in handset Model Setup -> External Module -> Receiver (number).

<figure markdown>
![Model CFG](../../assets/images/modelcfg.jpg)
</figure>

!!! warning "WARNING"
	Do not change parameters while ARMED. When a parameter is changed, the module goes into Parameter Commit mode, interrupting the normal loop. This could result in a desync on some hardware combination which would result in a FAILSAFE.

### The Header

The first line, "Header", will show you some information about your ExpressLRS link. 

The first part will show you the current ExpressLRS TX Module ID, followed by the current status of the link.

The `0/nnn` is your Packet Counter. The second set of numbers should match your currently selected Packet Rate. e.g. If you've set your Packet Rate to 500Hz, the Packet Counter should show 0/500, which means you're not getting any Bad Packets ( 0 Bad Packets ) and only getting Good Packets ( 500 Good Packets ). Any small fluctuation is normal and often goes back to 100% Good Packets, especially when you change a setting and it's committed into memory. 

Should the indicator starts showing Bad Packets, and Good Packets goes down, it isn't a good situation. Make sure your module is not overheating and it's still getting a good connection with the radio. This is most dangerous when you're armed and flying several kilometers/miles out, as this could mean a sudden Failsafe.

The `Connection Status` indicator shows your current RC link status. When not connected to any receiver, it will show a dash (`-`); while a `C` shows up when bound and connected.

The `Model Mismatched` message will also show up to indicate you are connected to a receiver, but the model selected on your radio is incorrect. See the [Model Match](../../software/model-config-match.md) page for more info about Model Matching.

### Folder Titles

Items with `>` before the name is a folder that when selected shows another level of customization. `TX Power`, `VTX Administrator`, `Wifi Connectivity` are examples of these items.

:new: These items will now show what is currently set for the items within. An example would be on `TX Power`, which will show the current Power set, and if Dynamic Power is enabled, it will show the current set Max Power, followed by the indicator `Dyn`.

### Packet Rate and Telemetry Ratio

These are shown as `Packet Rate` and `Telem Ratio` in the Lua script, which allows you to change your performance parameters. 

* `Packet Rate` sets how fast data packets are sent, higher rates send packets more frequently and have lower latency.

	The following options are available for `2.4GHz`:

	- `50Hz, 150Hz, 250Hz & 500Hz`: Lora-based options. Higher means lower latency at the expense of sensitivity. Since v1.0.
	- `F500 & F1000` :new: : Pure FLRC for lowest latency, reduced range compared to LoRa, 500Hz and 1000Hz. [Details](https://github.com/ExpressLRS/ExpressLRS/pull/1277)
	- `D250 & D500` :new: : Redundant transmit FLRC modes.  `D` stands for `Déjà Vu`, 250Hz and 500Hz. Higher latency, reduced packet jitter and higher LQ. Same range as other FLRC modes. [Details](https://github.com/ExpressLRS/ExpressLRS/pull/1527)
	- `100Hz Full & 333Hz Full` :new: : Lora-based 10-bit Full Resolution with 8ch/12ch/16 Switch Mode options. [Details](https://github.com/ExpressLRS/ExpressLRS/pull/1572)
	
	The following options are available for `900MHz`:

	- `25Hz, 50Hz, 100Hz & 200Hz`: LoRa-based options. Higher means lower latency at the expense of sensitivity. Since v1.0.
	- `100Hz Full` :new: : Lora-based 10-bit Full Resolution with 8ch/12ch/16 Switch Mode options. [Details](https://github.com/ExpressLRS/ExpressLRS/pull/1572)

	The number following the rate in parentheses (e.g. -105dBm for 500Hz) is the Sensitivity Limit for the rate, the lowest RSSI where packets will still be received. See [Signal Health](../../info/signal-health.md) for more information about the sensitivity limit.

!!! warning "WARNING"
	Never change the packet rate while flying as this **FORCES A DISCONNECT** between the TX and RX. 

* `Telem Ratio` sets the telemetry ratio or how much of the packet rate is used to send telemetry. The options, in order of increasing telemetry rate, are: `Off, 1:128, 1:64, 1:32, 1:16, 1:8, 1:4, 1:2`. A Telem Ratio of 1:64 means one out of every 64 packets are used for telemetry data.
	- :new: v3.0 comes with `Std` and `Race` options. `Std` changes ratio depending on the Packet Rate, and `Race` is the same as Std, but will disable telemetry and sync while Armed.

	For information on telemetry setup, see [First Flight: Telemetry](../pre-1stflight.md#telemetry) and [Telemetry Bandwidth](../../info/telem-bandwidth.md).

### Switch Mode

The Switch Mode setting controls how channels AUX1-AUX8 are sent to the receiver (the 4 main channels are always 10-bit). The options are `Hybrid & Wide`. **Hybrid** mode is 6x 2, 3 or 6-position + 1x 16-position, and **Wide** is 7x 64 or 128-position. For detail about the differences, see the [Switch Configs](../../software/switch-config.md) documentation.

:new: In full resolution modes, the Switch Mode parameter selects the number of channels to be used. [Full Resolution Switch Modes](../../software/switch-config.md#full-resolution-switch-configuration-modes) 

!!! hint "Hot Tip"
	The Switch Mode can only be changed when not connected to a receiver. The top right corner of the Lua script will show a `-` if you're not connected.

### Model Match

Model Match is used to prevent accidentally selecting the wrong model in the handset and flying with an unexpected handset or ELRS configuration. Setting this to `On` while a receiver is connected will make that receiver only connect with the current Receiver ID. Setting it to `Off` will allow a connection with any bound receiver (including those using a Bind Phrase). Both sides of the connection must agree on their Model Match setting. For a detailed explanation of how this restricts connections see [Model Match](../../software/model-config-match.md). The current Receiver ID is shown after the option value.

### TX Power

<figure markdown>
![Power Settings](../../assets/images/lua/pwrrm.png)
</figure>

<figure markdown>
![Power Settings BW](../../assets/images/lua/power-bw.png)
</figure>

TX Power is a folder, press ENTER to enter the TX Power settings and use RTN/EXIT to exit the folder.

* `Max Power` sets the maximum power level your TX will transmit at. Selecting a power level higher or lower than your TX supports will revert to the closest supported level. The options are `10, 25, 50, 100, 250, 500, 1000 & 2000` mW. If Dynamic Power is set to `Off` this is the power level your TX always uses. 

* `Dynamic` enables the Dynamic Power feature. `Off` means that the TX will transmit at Max Power at all times. `Dyn` means the TX will dynamically _lower_ power to save energy when maximum power is not needed. The options `AUX9, AUX10, AUX11, AUX12` indicate that the TX can be changed from max power to dynamic power by changing the position of a switch. where switch HIGH (>1500us) = dynamic power, switch LOW (<1500us) = max power. For more information, [Dynamic Transmit Power](../../software/dynamic-transmit-power.md) provides a deeper dive into the algorithm and usage.

* `Fan Thresh` sets the power level the Fan should activate, e.g. if set to 100mW, then the fan should spin up if you set `Max Power` to 100mW with `Dynamic` set to OFF after a short delay. The fan will continue running for some time even after the power level goes below the threshold. Not all modules have a Fan header that benefits from the setting. . Default fan threshold is 250mW.

### VTX Administrator

<figure markdown>
![VTX Settings](../../assets/images/lua/vtxrm.png)
</figure>

<figure markdown>
![VTX Settings BW](../../assets/images/lua/vtx-bw.png)
</figure>

VTX Administrator allows you to change your VTX settings directly from your radio, and have those VTX settings be applied to any receiver you connect to. The VTX settings are sent every time a new connection is acquired, or when `[Send VTX]` is pressed.

!!! hint "Hot Tip"
    VTX Administrator will send the current VTX settings to the flight controller whenever the TX module detects a connection to the RX. This means that it will resend them after telemetry lost/recovered. So if you have used any other method to change the VTX power level (i.e. OSD), then that will be overridden if you lose/regain telemetry in flight.

* `Band` sets the VTX band, the options are `Off, A, B, E, F, R & L`, the standard analog FPV bands. `Off` means that VTX Administrator will not adjust any VTX settings.

* `Channel` sets the VTX channel, the options are `1, 2, 3, 4, 5, 6, 7 & 8` which are the standard channels in the above bands.

* `Pwr Lvl` sets the VTX power by index, the options are `-, 1, 2, 3, 4, 5, 6, 7, & 8` which are the power levels that your VTX can do. Refer to your VTX table settings on the flight controller for the exact power levels. For example a VTX may have 1 = 25mW, 2 = 100mwW, 3 = 200mW, 4 = 500mW.

* `Pitmode` the options are `On & Off` which allow you to quickly switch into or out of pitmode

* Finally pressing the `[Send VTX]` button sends the configured settings to the receiver and on to the VTX. These settings are also sent every time a connection is established.

### WiFi Connectivity

<figure markdown>
![WiFi Connectivity Settings](../../assets/images/lua/wifirm.png)
</figure>

<figure markdown>
![WiFi Connectivity Settings BW](../../assets/images/lua/wifi-bw.png)
</figure>

This section contains all the WiFi-related functions.

* `Enable WiFi` will activate the Tx module WiFi mode for updating via WiFi (if the Tx Module has WiFi Capabilities). Visit [this page](../../software/updating/wifi-updating.md) for instructions on how the updating process works.

* `Enable Rx WiFi` will put the bound and connected receiver into WiFi mode to facilitate updating via WiFi (if the receiver has WiFi capabilities).

* `Enable Backpack WiFi` will put the Tx Backpack into WiFi mode (available only to TX modules with backpacks connected and updated to the new [Backpack](https://github.com/ExpressLRS/Backpack) firmwares).

* `Enable VRx WiFi` will put the VRx [Backpack](https://github.com/ExpressLRS/Backpack) that is bound and connected to the onboard TX Backpack into WiFi mode to facilitate updating via WiFi.

### Bind
<figure markdown>
![Binding](../../assets/images/lua/bindrm.jpg)
</figure>

<figure markdown>
![Binding BW](./../../assets/images/lua/bind-bw.png)
</figure>

Pressing the `[Bind]` button activates the binding mode for traditional binding. This does nothing for users who have configured a bind phrase and is not needed. For more information check out this page on [binding](../binding.md).

### BLE Joystick (ESP32 TXes Only)
<figure markdown>
![BLE Joystick](../../assets/images/lua/blerm.jpg)
</figure>

<figure markdown>
![BLE Joystick BW](../../assets/images/lua/blejoystick-bw.png)
</figure>

Pressing the `[BLE Joystick]` selection activates BluetoothLE Joystick mode which allows connection to simulators through the bluetooth of your computer. Reboot or change models to exit this mode.

### Other Devices

The Other Devices folder, if present, allows changing the configuration of other connected devices, such as the current receiver. Within this folder there are options such as Init Rate, Telemetry Power, Diversity Mode & the [Loan Model](../../software/loan-model.md) features. The `Init Rate` setting lets you set which packet rate it starts from when cycling through rates looking for a TX, this is particularly helpful when using lower packet rates where it might take some time for the receiver to get around to your chosen rate. 
## Recommendations

* For racing where maximum performance is a must, the `500Hz` modes or faster, with the `Race` Telemetry mode, is ideal. `Hybrid` Switch Mode is also good here.

* For freestyle and general everyday flying, you may use the `250Hz` modes or faster, with the `Std` Telemetry mode. Switch Mode doesn't matter as much here. Select what's appropriate for your Flight Mode settings.

* For fixed wings, we recommend using `100Hz Full Res`, together with either `Std` or your choice of Telemetry Ratio. Switch Mode will depend greatly on how many full resolution channels you intend to use.

## Troubleshooting the Lua Script

### <span class="custom-heading" data-id="1">ExpressLRS Lua Script is stuck at `Loading...`</span>

??? Note "ExpressLRS Lua Script is stuck at `Loading...`"
    Go back to the [Radio Setup Guide](tx-prep.md) and make sure your radio is prepped up for ExpressLRS. Check that the ExpressLRS Tx module is enabled - otherwise the script cannot be loaded.

    Also, make sure your module has been flashed with v3.0 firmware. V3 Lua for V3.0-flashed modules, V2 Lua for v2.x-flashed modules (including some modules fresh from the factory).

    For newly-acquired ExpressLRS modules, flashing via USB is the recommended update method.

### <span class="custom-heading" data-id="2">I cannot change the Switch Mode!</span>

??? Note "I cannot change the Switch Mode!"
    Changing switch modes requires that the TX module and Receiver aren't connected to each other (no C in the top right corner of the Lua Script). Power off the receiver first, change the Switch Mode from the Lua script, then power up the receiver. The Switch Mode should then apply.

### <span class="custom-heading" data-id="3">I cannot change my Packet Rate to F1000!</span>

??? Note "I cannot change my Packet Rate to F1000!"
    F1000 requires higher than 400K baud rates. First update your baud rate setting either in the Model Setup menu or in the System Menu -> Hardware, reboot your radio to ensure that the baud rate setting got applied and then change the Packet Rate.

    Do note that not every handset is capable of higher than 400K baud rates. See the [Radio Setup Guide](tx-prep.md) for the details.

### <span class="custom-heading" data-id="4">I cannot change to Full Resolution Rates!</span>

??? Note "I cannot change to Full Resolution Rates!"
    As Full Resolution Rates call for an entirely different Switch Modes, you need to first disconnect the Receiver and the TX module from each other, like how you would change Switch Modes. Power down the receiver, change the Packet Rate to the Full Resolution modes, select your Switch Mode scheme and then power up the receiver or the aircraft.

### <span class="custom-heading" data-id="5">VTX Admin is not working but I can change VTX channels via OSD Menu.</span>

??? Note "VTX Admin is not working but I can change VTX channels via OSD Menu."
    As VTX Admin depends on MSP which then depends on Telemetry, ensure that you have Telemetry enabled on your FC Configuration and that you are getting more than 10 Telemetry Sensors on your Radio (Model Setup -> Telemetry page; Delete and Discover New sensors to refresh the sensor list.)
    Also, make sure Telem Ratio is not Off.

### <span class="custom-heading" data-id="6">There is no C on the top right corner, and I'm not getting Telemetry in my radio!</span>

??? Note "There is no C on the top right corner, and I'm not getting Telemetry in my radio!"

    Make sure Telem Ratio is not set to `Off`.
    Set it to `Std`, or any other value other than `Off`.

### <span class="custom-heading" data-id="7">On v1.x, I can choose 2W on the Lua, but I cannot do that anymore. What gives?</span>

??? Note "On v1.x, I can choose 2W on the Lua, but I cannot do that anymore. What gives?"
    This means your module cannot go that high or that low. The power levels you can select on the new Lua script are based on the power levels your module supports.
    This also applies to other options like `Enable Backpack WiFi` or `BLE Joystick`. If your module doesn't support any of these features, it won't show up on the Lua Script.

<script src="../../../assets/javascripts/admonition-enhancement.js"></script>
