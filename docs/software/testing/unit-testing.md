---
template: main.html
---

<img src="https://raw.githubusercontent.com/ExpressLRS/ExpressLRS-Hardware/master/img/software.png">

## Tools

Assuming you have Visual Studio Code and platformIO installed

## Windows Prerequisite

* Install mingw-w64 from [sourceforge.net](https://sourceforge.net/projects/mingw-w64/files/Toolchains%20targetting%20Win32/Personal%20Builds/mingw-builds/installer/mingw-w64-install.exe/download)
* In the windows search bar type `env` and select __Edit the system environment variables__
* Click the `Environment Variables...` button and in the `System variables` section double-click `Path` and click `New` then paste `C:\Program Files (x86)\mingw-w64\i686-8.1.0-posix-dwarf-rt_v6-rev0\mingw32\bin`. This path may be different on your system, but it is the path that mingw-w64 was installed previously.

## Running the tests

* In VSCode with the ExpressLRS project open, click on the `New Terminal` button in the status bar
* Ensure the native platform is installed by entering `pio platform install native` in the terminal window.
* Now you can enter `pio test -e native` to run the tests.
* It is also possible to use the pio module and select native/Advanced/Test in the target selection list.