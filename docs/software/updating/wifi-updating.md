---
template: main.html
---

<img src="https://raw.githubusercontent.com/ExpressLRS/ExpressLRS-Hardware/master/img/software.png">


1. Build your fimware and locate your `firmware.bin` file (this may be named something else if someone built it for you but that's fine)  
2. Put your device in Wi-Fi updating mode 📶  
   a. For TX, open LUA script on the handset and select "Wi-Fi Update"  
   b. For RX, power the receiver by plugging in a battery or USB and wait for LED to be blinking fast 🙈  
3. Connect to the Wi-Fi network from your computer with the password `expresslrs`  
   Note 1: Some receivers have very weak Wi-Fi antennas so they will have to be extremely close to the computer's Wi-Fi antenna.  
   Note 2: If a window pops up automatically when you connect to the Wi-Fi , close it and use a regular browser window instead.  
4. Open a browser tab and navigate to `http://10.0.0.1`  
5. Click "Choose File"  
6. Select `firmware.bin` from your latest build(eg: ...ExpressLRS\src\.pio\build\\[target]\firmware.bin)  
7. Click "Update"  
8. Wait for the page to refresh and your URL bar to say 10.0.0.1/update (it'll look like the page is frozen for a bit)
9. **WAIT AT LEAST 10 SECONDS** after the page refreshes indicating the upload is complete. It takes time for the firmware to flash *after* the upload, so do not pull the power until you see activity on the LED of the device or you will soft brick your device due to pulling power mid-flash.

Done! You now have the latest version of ELRS on your hardware. Go Fly! 🚁