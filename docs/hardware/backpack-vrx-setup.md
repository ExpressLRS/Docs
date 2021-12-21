---
template: main.html
---
# VRx Backpack Setup
![Hardware-Banner](https://raw.githubusercontent.com/ExpressLRS/ExpressLRS-Hardware/master/img/hardware.png)

## Flashing your VRx Backpack Device

Before wiring up your VRx Backpack, you NEED to first flash the VRx Backpack firmware into it either via WiFi or UART/FTDI.

Good VRx Backpack candidates are the EP1 or EP2 receivers from Happymodel as these have Boot pads, instead of Boot buttons. The Boot pads will be repurposed for the SPI communication with the VRx module.

### Flashing via WiFi (ESP-based ExpressLRS Receivers)

Power up your selected VRx Backpack device. Let it go into WiFi Update mode (fast blinking LED) and load up the WiFi Update page. In the Address bar of your browser, add `?force=true` to ensure it will accept the VRx Backpack firmware. The resulting URL should read `http://10.0.0.1/?force=true` (if you connected via Access Point) or `http://elrs_rx.local/?force=true` (if your device has connected to your local WiFi network).

!!! note ""
    The `?force=true` is not needed for these ESP-based receivers with factory-firmware. It will only be needed if you have flashed the receiver into ExpressLRS v2.0 and wanted to repurpose it for VRx Backpack.

On the Assets section of the [Backpack Release](https://github.com/ExpressLRS/Backpack/releases) on Git Hub, `Download` the binary suited for your VRx module. Upload this binary into the VRx device using the Web Update page. Wait (~30s) until the LED on the VRx device has turned on again.

Alternatively, you can use the ExpressLRS Configurator to create your binaries for you. **Build** your binary, with the set `binding phrase` (Optional) as well as Home Network SSID and Password (Optional; available starting 0.2.0). Upload the resulting binary into the WiFi Update page as outlined above.

### Flashing via FTDI/UART

Connect your FTDI Rx pin into the Tx pad of your VRx Device, and the FTDI Tx pin into the Rx pad of the VRx Device; then the 5v and Gnd pads. The Boot pad needs to be bridged with the Ground pad. Connect your FTDI, with the connected VRx device, into a free USB port (VRx Device's LED should light up SOLID). Using the ExpressLRS Configurator, select your VRx module, select the `via UART` method and set your `binding phrase` (Optional) and the Home Network SSID and Password (Optional; Available starting 0.2.0). Click **Build and Flash** and the compiling and flashing should commence. If done right, the Success bar should appear and your VRx Backpack should now be ready for wiring into your selected VRx Module.

