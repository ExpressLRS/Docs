---
template: main.html
---

<img src="https://raw.githubusercontent.com/ExpressLRS/ExpressLRS-Hardware/master/img/software.png">

## Overview

If you are using Linux then you can't use the ST-LINK utility from st.com. But fortunately, you can achieve the same effect with openocd on the Linux command line. This tutorial assumes you have an STLink v2.

1. Install openocd from your distro's repository. For Debian/Ubuntu use: `sudo apt-get install openocd`
2. Issue the full command:

    a. For R9mm/Mini `openocd -f interface/stlink-v2.cfg -f target/stm32f1x.cfg -c 'init; reset halt; stm32f1x unlock 0; reset run; shutdown'`

    b. For Ghost Átto/Zepto `openocd -f interface/stlink-v2.cfg -f target/stm32f3x.cfg -c 'init; reset halt; stm32f3x unlock 0; flash protect 0 0 last off; reset halt; exit'`

3. Restart your device so the disabled readout protection can take effect.
4. Now you can proceed with flashing your receiver. This may work on other devices or it might not.
