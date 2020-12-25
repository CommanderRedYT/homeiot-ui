import os
import colorama
import requests
from colorama import Fore, Style
version = "1.0 "
running = True
valid = []

def printMenu(selected):
    global menu
    menu = selected

    global valid
    print(Fore.RED)
    if menu == 1:

        valid = ['l', 'r', 'a', 'o']
        print(Fore.LIGHTGREEN_EX)

    elif menu == 2:

        valid = ['back', 'b', 'd', 't', 'c', 'max', 'min']
        print(Fore.GREEN)

    elif menu == 3:

        valid = ['back', 'on', 'off', '1', '0']
        print(Fore.YELLOW)

    elif menu == 4:

        valid = ['back', 'T' , 't', '+', '-', 'M', 'm', 'DVD', 'dvd', 'Aux', 'aux', 'Tuner', 'tuner', 'u', 'up', 'd', 'down', 'mov', 'ent', '10', '-10']
        print(Fore.CYAN)

    elif menu == 5:
        
        valid = ['back', 'wol', 'lamp']
        print(Fore.LIGHTYELLOW_EX)

    elif menu == "error":

        valid = ['l', 'r', 'a', 'o']
        print(Fore.LIGHTGREEN_EX)

    print(" ================")
    print(" | HomeIoT V" + version + "|")
    print(" ================\n" + Fore.RESET)
    if menu == "error":
        print(Fore.RED + " Error: I didn't recognized that command!\n" + Fore.RESET)
        menu = 1

    if menu == 1:
        print("=========================================\n What menu would you like to open?\n")
    else:
        print("=========================================\n What function would you like to use?")   
    printOptions()
    print('  Use "exit" to exit the program\n=========================================')

def handleInput(key):
    #main menu
    if menu == 1:
        if key == "l": #ledstrip
            key = "" 
            return 2
        elif key == "r": #rec-sign
            key = ""
            return 3
        elif key == "a": #av-receiver
            key = ""
            return 4
        elif key == "o": #other stuff
            key = ""
            return 5

    #ledstrip
    elif menu == 2:
        if key == "b": #ledstrip brighter
            key = ""
            getThingerMsg("esp32", "webledstripBrighter")
            return 2
        elif key == "d": #ledstrip darker
            key = ""
            getThingerMsg("esp32", "webledstripDarker")
            return 2
        elif key == "t": #ledstrip on/off
            key = ""
            getThingerMsg("esp32", "webledstripToggle")
            return 2
        elif key == "c": #correct status
            key = ""
            ledstatus = getThingerMsg("esp32", "stripStatus")
            getThingerMsg("esp32", "webledstripToggle")
            if ledstatus == "1":
                r = sendThingerMsg("esp32", "stripSetStatus", "true")
            else:
                r = sendThingerMsg("esp32", "stripSetStatus", "false")
            return 2
        elif key == "max":
            key = ""
            tries = 10
            while tries > 0:
                tries = tries - 1
                getThingerMsg("esp32", "webledstripBrighter")
                pass
            return 2

        elif key == "min":
            key = ""
            tries = 10
            while tries > 0:
                tries = tries - 1
                getThingerMsg("esp32", "webledstripDarker")
                pass
            return 2

    #rec sign
    elif menu == 3:
        if key == "on" or key == "1":
            key = ""
            sendThingerMsg("esp32", "led", "true")
            return 3
        elif key == "off" or key == "0":
            key = ""
            sendThingerMsg("esp32", "led", "false")
            return 3

    #av receiver
    elif menu == 4:
        if key == "t" or key == "T":
            key = ""
            sendThingerMsg("esp32", "webavPower", "true")
            return 4

        elif key == "+":
            key = ""
            sendThingerMsg("esp32", "webavVolup", "true")
            sendThingerMsg("esp32", "webavVolup", "true")
            return 4

        elif key == "-":
            key = ""
            sendThingerMsg("esp32", "webavVoldown", "true")
            sendThingerMsg("esp32", "webavVoldown", "true")
            return 4

        elif key == "10":
            key = ""
            tries = 10
            while tries > 0:
                tries = tries - 1
                sendThingerMsg("esp32", "webavVolup", "true")
                pass
            return 4

        elif key == "-10":
            key = ""
            tries = 10
            while tries > 0:
                tries = tries - 1
                sendThingerMsg("esp32", "webavVoldown", "true")
                pass
            return 4

        elif key == "m" or key == "M":
            key = ""
            sendThingerMsg("esp32", "webavMute", "true")
            return 4

        elif key == "DVD" or key == "dvd":
            key = ""
            sendThingerMsg("esp32", "webavDVD", "true")
            return 4

        elif key == "Aux" or key == "aux":
            key = ""
            sendThingerMsg("esp32", "webavAux", "true")
            return 4

        elif key == "Tuner" or key == "tuner":
            key = ""
            sendThingerMsg("esp32", "webavTuner", "true")
            return 4
        
        elif key == "u" or key == "up":
            key = ""
            sendThingerMsg("esp32", "webavPresetUp", "true")
            return 4
        
        elif key == "d" or key == "down":
            key = ""
            sendThingerMsg("esp32", "webavPresetDown", "true")
            return 4

        elif key == "mov":
            key = ""
            sendThingerMsg("esp32", "webavMov", "true")
            return 4
            
        elif key == "ent":
            key = ""
            sendThingerMsg("esp32", "webavEnt", "true")
            return 4

    elif menu == 5:
        if key == "wol":
            key = ""
            sendThingerMsg("esp32", "wol", "true")
            return 5
        elif key == "lamp":
            key = ""
            sendThingerMsg("esp32", "webLamp", "true")
            return 5

    #no menu
    else:
        key = ""
        return 1
    #want to go back?
    if key == "back":
        key = ""
        return 1

def printOptions():
    if menu == 1:
        print('  - (l)edstrip')
        print('  - (r)ec-Sign')
        print('  - (a)v-receiver')
        print('  - (o)ther\n')
    elif menu == 2:
        print('  - (b)righter')
        print('  - (d)arker')
        print('  - (t)oggle')
        print('  - (c)orrect status\n')

        ledstatus = getThingerMsg("esp32", "stripStatus")
        if ledstatus == "1":
            print(Fore.LIGHTGREEN_EX + " --[Ledstrip is on" + Fore.RESET)
        else:
            print(Fore.LIGHTRED_EX + " --[Ledstrip is off" + Fore.RESET)
    elif menu == 3:
        print('  - on')
        print('  - off')
    elif menu == 4:
        print(Fore.CYAN + '  - (T)' + Fore.RESET + 'oggle power')
        print('  - Volume up' + Fore.CYAN + '    (Use "+")' + Fore.RESET)
        print('  - Volume down' + Fore.CYAN + '  (Use "-")' + Fore.RESET)
        print(Fore.CYAN + '  - (M)' + Fore.RESET + 'ute')
        print(Fore.CYAN + '  - DVD' + Fore.RESET)
        print(Fore.CYAN + '  - Aux' + Fore.RESET)
        print(Fore.CYAN + '  - Tuner' + Fore.RESET)
        print('  - Preset ' + Fore.CYAN + '(u)' + Fore.RESET +'p')
        print('  - Preset ' + Fore.CYAN + '(d)' + Fore.RESET +'own')
        print(Fore.CYAN + '  - (mov)' + Fore.RESET + 'ie theatre 2')
        print(Fore.CYAN + '  - (ent)'+ Fore.RESET + 'ertainment')
    
    elif menu == 5:
        print('\n  - wol')
        print('  - lamp')
        dht = getThingerMsg("esp32", "dht")
        dht = dht.replace("}", "")
        dht = dht.replace("tmp", "")
        dht = dht.replace("hum", "")
        dht = dht.replace("{", "")
        dht = dht.replace(":", "")
        dht = dht.replace('"', "")
        dht = dht.replace("'", "")
        dht = dht.split(",")
        temp = dht[1]
        print("\n =======[Stats]=======")
        temp = " | Temperature: " + temp + "°C"
        hum = dht[0]
        hum = " | Humidity: " + hum + "%"
        print(temp)
        print(hum)
        print(" =====================")

    if menu != 1: print('\n Type "back" to go back to main! Press ENTER to reload!')

def sendThingerMsg(device, thing, value):
    host = "https://backend.thinger.io/v3/users/"
    url = host + usr + "/devices/" + device + "/resources/" + thing + "?authorization=" + cryptkey
    msg = '{"in": ' + value + '}'
    headers = {'Content-type': 'application/json'}
    response = requests.post(url, data=msg, headers=headers)
    return response.text

def getThingerMsg(device, thing):
    host = "https://backend.thinger.io/v3/users/"
    url = host + usr + "/devices/" + device + "/resources/" + thing + "?authorization=" + cryptkey
    response = requests.get(url)
    return response.text

os.system('cls' if os.name == 'nt' else 'clear')

with open('.key', 'r') as file:
    global cryptkey
    cryptkey = file.read().replace('\n', '')
with open('.username', 'r') as file:
    global usr
    usr = file.read().replace('\n', '')


printMenu(1)

while True:
    try:
        keyboard = input()
    except:
        os.system('cls' if os.name == 'nt' else 'clear')
        printMenu("error")
    if keyboard == "exit":
        os.system('cls' if os.name == 'nt' else 'clear')
        break
    elif keyboard == "clear":
        os.system('cls' if os.name == 'nt' else 'clear')
        printMenu(menu)
    elif keyboard in valid:
        os.system('cls' if os.name == 'nt' else 'clear')
        menu = handleInput(keyboard)
        printMenu(menu)
    elif keyboard == "":
        os.system('cls' if os.name == 'nt' else 'clear')
        printMenu(menu)
    else:
        os.system('cls' if os.name == 'nt' else 'clear')
        printMenu("error")