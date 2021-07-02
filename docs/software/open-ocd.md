---
template: main.html
---

<img src="https://raw.githubusercontent.com/ExpressLRS/ExpressLRS-Hardware/master/img/software.png">

If you are using linux then you can't use the ST-LINK utility from st.com. But fortunately you can achieve the same effect with openocd on the linux command line. This tutorial assumes you have an STLink v2

1. install openocd from your distro's repository. for debian/ubuntu use: `sudo apt-get install openocd`
2. change directories to openocd script repository: `cd /usr/share/openocd`
3. issue the full command: `openocd -f ./scripts/interface/stlink-v2.cfg -f ./scripts/target/stm32f1x.cfg -c "init; reset halt; stm32f1x unlock 0; reset run; shutdown"`
4. restart your device so the disabled readout protection can take effect.
5. Now you can proceed with flashing your R9m or R9MM. this may work on other frsky devices or it might not.