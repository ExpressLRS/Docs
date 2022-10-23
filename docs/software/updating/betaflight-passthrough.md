---
template: main.html
---

<img src="https://raw.githubusercontent.com/ExpressLRS/ExpressLRS-Hardware/master/img/software.png">

## General Instructions

Once you have Flashed ELRS onto your receivers they can be conveniently updated using the passthrough feature of Betaflight (and similar FC FW). This is a relatively simple process.
  
1. Open VS Code or the configurator and prepare to compile and upload.  
2. Plug in your FC to your computer, but do NOT connect to the betaflight configurator.  
3. Select `env:YOUR_RX_via_Betaflight_Passthrough` and hit upload.  
4. That's it!

## ESP-Specific Instructions

Since 1.0.0, ESP receivers can be updated via passthrough without using the boot button as long as the firmware is not corrupted. If you're unable to get it to work, your firmware might be corrupted, in which case you'll need to temporarily turn off the telemetry feature in betaflight. If it still doesn't work, the bootloader might be messed up and the following steps should work.

1. Open VS Code or the configurator and prepare to compile and upload.  
2. Plug in your FC to your computer, but do NOT connect to the betaflight configurator and do NOT power the RX. If your RX gets powered from USB, desolder the power wire so that you can manually power it up independently of the flight controller.  
3. Hold the boot button of the RX or jump the boot jumper.  
4. Select `env:YOUR_RX_via_Betaflight_Passthrough` and hit upload.  
5. Wait for the command line to show `.....-----`.  
6. Plug in a battery or otherwise power up the RX.

## Troubleshooting

- If it fails to flash (may display a success message but has errors show up above the final success output), check if it is flashing the correct COM. Sometimes an ethernet adapter on your motherboard will populate a COM port, which will confuse the script and it will attempt to flash to that COM. 
   
      - The solution that could work would be manually editing the `UARTUpload.py` and `BetaflightinitPassthrough.py` files in `src/python`.
      - Another possible solution could be [changing the COM to a higher number](http://www.co2meters.com/Documentation/AppNotes/AN134-Change-COM-Ports.pdf) for the unnecessary COMs 

- Sometimes the boot jumper or button must be used while powering up the receiver.

## Ardupilot Instructions (community contribution, untested)

- Connect the autopilot to a PC using a USB cable and connect with a Ground Station (i.e. Mission Planner, QGC, etc).
- Set SERIAL_PASSTIMO to a length of time (in seconds) that gives you enough time to connect with the sensor’s configuration software. 30 to 60 seconds is a good choice
- Set SERIAL_PASS2 to the number of the serial port connected to the sensor. I.e. “2” if the sensor is connected to Telem2/Serial2.
- Be sure to set each port’s baud rate appropriately using the SERIALx_BAUD parameter. The rates may be different for each port. ArduPilot will do the buffering.
- Press the “Disconnect” button on the ground station but leave the USB cable from the PC to the autopilot connected.
- Open the sensor’s configuration software and connect to the autopilot’s COM port. If all goes well the configuration software should work as it does when the PC is directly connected to the sensor
- If the configuration fails to connect there are some things to try:
- Some configuration software will not allow connecting to the autopilot’s COM port by default but may have an option to display all available COM ports
- If no serial messages are received from the PC the timeout will expire and SERIAL_PASS2 will revert to -1

   You can also refer to the [Ardupilot official docs](https://ardupilot.org/plane/docs/common-serial-passthrough.html) for serial passthrough.
