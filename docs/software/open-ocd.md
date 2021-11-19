---
template: main.html
---

<img src="https://raw.githubusercontent.com/ExpressLRS/ExpressLRS-Hardware/master/img/software.png">

If you are using linux then you can't use the ST-LINK utility from st.com. But fortunately you can achieve the same effect with openocd on the linux command line. This tutorial assumes you have an STLink v2

1. install openocd from your distro's repository. for debian/ubuntu use: `sudo apt-get install openocd`
2. change directories to openocd script repository: `cd /usr/share/openocd`
3. issue the full command:

    a. For R9mm/mini `openocd -f ./scripts/interface/stlink-v2.cfg -f ./scripts/target/stm32f1x.cfg -c "init; reset halt; stm32f1x unlock 0; reset run; shutdown"`

    b. For Ghost atto/zepto `openocd -f interface/stlink-v2.cfg -f target/stm32f3x.cfg -c 'init; reset halt; stm32f3x unlock 0; flash protect 0 0 last off; stm32f3x mass_erase 0; reset halt; exit`

4. restart your device so the disabled readout protection can take effect.
5. Now you can proceed with flashing your R9m or R9MM. this may work on other frsky devices or it might not.