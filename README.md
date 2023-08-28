# About

An undetectable autoclicker for Windows made in Python.
<br />
<br />
I've been banned several times for using autoclickers, so I decided to find out how to bypass the anti-cheats,
then I created a program to log the time of every single click and release of a legitimate human click, and
with the collected data, I developed this program that simulates legitimate clicking by using randomized timeouts.
It was already tested against a lot of server anti-cheats, and none of them could detect it.
<br />
<br />

**Warning**: This program can be detected if the anti-cheat runs on your computer or if you need to share your screen.
You may also get banned if you exceed the maximum clicking speed of the server anti-cheat or if you keep it enabled for a while without taking a break.

# Download

Download it here: [Ghost_Autoclicker.exe](https://github.com/kelio-mv/python-autoclicker/releases/download/v1.0/Ghost_Autoclicker.exe)

# Usage

By default, for security reasons, the click speed is 10 clicks per second and the checkbox "hold to click" is enabled.

- To use the autoclicker, hold any of the mouse hotkeys: **Scroll, x1 or x2**.
- Move the slider to change the speed of the autoclicker.
- Uncheck "hold to click" if you don't want to hold the hotkey. In this case, you'll need to press the hotkey again to stop the autoclicker.

# Build

Before starting the build process, make sure you have [Python 3](https://www.python.org/) installed on your computer.

1. Download this repository as a zip file and extract it.
2. In extracted folder, open the terminal and run:

```sh
pip install -r requirements.txt
pyinstaller main.pyw --onefile --name=Ghost_Autoclicker --icon=icon.ico
```

3. After executing the commands, you'll find the generated executable file in the folder **dist**.
