---
template: main.html
---

![Software Banner](https://raw.githubusercontent.com/ExpressLRS/ExpressLRS-Hardware/master/img/software.png)


!!! note "Note" 
    These instructions are meant as a quick start quide for those who develop on Linux.
    Typically developers on Linux don't need much of an explanation and just look for the right commands for the toolchain.
    That's what this guide will provide, without any nudging to use Microsoft VSCode IDE.

## Toolchain Setup (Advanced) for Linux Users

`ExpressLRS` is written in C++ using the Arduino framework and the [PlatformIO](https://platformio.org/) toolchain.
PlatformIO is based on Python and following best practices in Python we will create a virtual environment in the project
after cloning the repo.

### Cloning the Repo
Open a Shell (Bash) in your regular workspace and clone the repo recursively like always and change into that directory.
It is assumed that Linux users know how to use git. You also want to add the user_defines.txt to your local .gitignore .

```
git clone --recursive https://github.com/ExpressLRS/ExpressLRS.git
cd ExpressLRS
echo "src/user_defines.txt" >> .gitignore
```

### PlatformIO
PlatformIO is available as a Python package and can be installed via Pip.
Following best practices we will create a virtual environment in the repo directory first.

1. Install virtual-env (just in case it's not installed by default)

```
pip install virtual-env
```

2. Setup a virtual environment to not taint your system's python installation.
It does not matter where you create this but it makes sense to create it in the project directory, because best practice is to have a separate venv for each python project.

```
python -m venv .venv
source .venv/bin/activate
```

3. Install the required python packages. Empy and pexpect are listed because modules like `dronecan` fail to correctly specify
their dependencies for pip to install them automatically.

```
pip install platformio dronecan setuptools empy==3.3.4 pexpect
```

### Building Targets using PlatformIO

The platformio package comes with the [pio](https://docs.platformio.org/en/latest/core/userguide/cmd_run.html) executable.
It is the build command of the toolchain.
Pio expects a platformio.ini file in the directory where it is invoked, so change into src directory first.

There find and open the `user_defines.txt` file in your favorite editor.
This file contains the build flags that you know from ELRS Configurator.
At least uncomment the line for your regulatory domain. That's the minimum requirement for the build to work.
You may also want to set everything you would normally set in the ELRS Configurator.

To verify your build environment does work, start building firmware for a common 900Mhz target. It obviously needs a corresponding regulatory domain setting.

```
pio run --environment Unified_ESP32_900_RX_via_BetaflightPassthrough
```

At some point at the end of the build you will be asked to select some configuration between different manufacturers and products.
This sets parameters to provision a unified software binary with information about the device hardware, e.g. if the device has a power amplifier, diversity, etc. .

When you reach that point, this indicates that everything did work.

### Finding the right configuration for your target

This is the most tricky and obscure part of the ELRS project.
Browsing through the `platformio.ini` file already gives hints about the correct environment, but typically you need to look into the [targets](https://github.com/ExpressLRS/targets) and into the [devices](https://github.com/ExpressLRS/ExpressLRS-Configurator/tree/master/devices) to back-track what the configurator would select for your device.
Another option is to look into the logs of the ELRS Configurator after it flashed your device. You should find the call to pio together with the arguments there.

### Flashing

When you select `--target upload` and provide an `--upload-port`, pio will flash the device as the final step of the build, again asking you about manufacturer / device. Under the hood pio then invokes [esptool](https://github.com/espressif/esptool).

```
pio run --target upload --environment Unified_ESP32_900_RX_via_BetaflightPassthrough --upload-port /dev/ttyUSB0
```

