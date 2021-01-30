# homeiot-ui

This python script is an interface to my [homeiot-system](https://github.com/CommanderRedYT/esp32homeIoT-V2.0). The script can control the ledstrip, my live-sign (custom PCB with the word "LIVE" written with LEDs) and IR-Devices like my av-receiver. <br><br> It also has the ability to read out the DHT sensor (Temperature, Humidity) and start my workstation from the esp32.
___

## Installation

The installation script only checks for the two packages needed (***colorama*** for terminal-color and ***requests*** to make the web-requests to the API) and if they are not installed, you will be prompted with an y/n. <br><br>When you type in ***y*** it will run `pip3 install <package>`. <br><br>If you don't have pip3 or a custom python3 installation, please use your preferred way to install both packages!
___

## Config files
First, login into [Thinger.io](https://console.thinger.io/) and get your Username and api-key. <br>
You need to create 3 config files in the project directory.
 1. *.username* (Your thinger.io username)
 2. *.key* (Used with .username to control the esp32)
 3. *.system* (In **`main.py`, Line 96**, you have to specify the project folder path. I maybe let the program read it out in a future version, but at the moment you have to configure it for yourself! - Used by the pull command)


___
If all packages are installed and the config files are created, you can execute the program with `python3 main.py`.
___
## Usage

There are a few hidden commands like 
- `pull` (only main screen; executes git pull)
- `max` or `min` (only ledstrip menu; will send the brighter/darker event 10 times, so the ledstrip will be at max/min brightness)

All commands for the current (sub-)menu are displayed at load.

The python script also supports "direct command mode". That means, you can use for example `python3 main.py l t`. The `l` stands for the submenu *l (ledstrip)*. The `t` stands for the sub-function *t (toggle)*. So the command would toggle the ledstrip.

<br>
If there are any errors, feel free to create an issue!