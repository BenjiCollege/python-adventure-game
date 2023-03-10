import os
from time import sleep

def prompt():
    print(bcolors.BG_WHITE)
    print("|-------------------------------------------------------------------------------------------|")
    print("|                             Welcome to the Dungeon of Azure!                              |")
    print("|-------------------------------------------------------------------------------------------|")
    sleep(1)
    print("|-------------------------------------------------------------------------------------------|")
    print("|               ____                                 ___    _____                           |")
    print("|              |    \ _ _ ___ ___ ___ ___ ___    ___|  _|  |  _  |___ _ _ ___ ___           |")
    print("|              |  |  | | |   | . | -_| . |   |  | . |  _|  |     |- _| | |  _| -_|          |")
    print("|              |____/|___|_|_|_  |___|___|_|_|  |___|_|    |__|__|___|___|_| |___|          |")
    print("|                            |___|                                                          |")
    print("|-------------------------------------------------------------------------------------------|")
    sleep(1)
    print("|-------------------------------------------------------------------------------------------|")
    print("|                _________________________________________________________                  |")
    print("|              /|     -_-                                             _-  |\                |")
    print("|             / |_-_- _                                         -_- _-   -| \               |")
    print("|               |                            _-  _--                      |  |              |")
    print("|               |                            ,                            | |               |")
    print("|               |      .-'````````'.        '(`        .-'```````'-.      | |               |")
    print("|               |    .` |           `.      `)'      .` |           `.    |                 |")
    print("|               |   /   |   ()        \      U      /   |    ()       \   |                 |")
    print("|               |  |    |    ;         | o   T   o |    |    ;         |  |                 |")
    print("|               |  |    |     ;        |  .  |  .  |    |    ;         |  |                 |")
    print("|               |  |    |     ;        |   . | .   |    |    ;         |  |                 |")
    print("|               |  |    |     ;        |    .|.    |    |    ;         |  |                 |")
    print("|               |  |    |____;_________|     |     |    |____;_________|  |                 |")
    print("|               |  |   /  __ ;   -     |     !     |   /     `'() _ -  |  |                 |")
    print("|               |  |  / __  ()        -|        -  |  /  __--      -   |  |                 |")
    print("|               |  | /        __-- _   |   _- _ -  | /        __--_    |  |                 |")
    print("|               |__|/__________________|___________|/__________________|__|                 |")
    print("|              /                                             _ -           \                |")
    print("|             /   -_- _ -             _- _---                       -_-  -_ \               |")
    print("|-------------------------------------------------------------------------------------------|")
    sleep(1)
    print("|-------------------------------------------------------------------------------------------|")
    print("|                           This is a text-based adventure game.                            |")
    print("|                   You will be presented with a series of choices.                         |")
    print("|                Choose wisely, as your choices will determine your fate.                   |")
    print("|   You can select either GO North, East, South, or West to proceed through the dungeon.    |")
    print("|-------------------------------------------------------------------------------------------|")
    sleep(1)
    print("|-------------------------------------------------------------------------------------------|")
    print("|                           You must collect all nine items before                          |")
    print("|                           fighting the final boss. Good luck!                             |")
    print("|-------------------------------------------------------------------------------------------|")
    sleep(1)
    print("|-------------------------------------------------------------------------------------------|")
    print("|                                   Moves:                                                  |")
    print("|                                   'go {direction}'                                        |")
    print("|                                   'get {item}'                                            |")
    print("|-------------------------------------------------------------------------------------------|")
    sleep(1)
    print("|-------------------------------------------------------------------------------------------|")
    input("|                                   Press the ENTER key to continue...                      |")
    print("|-------------------------------------------------------------------------------------------|")
    print(bcolors.ENDC)


# Clear screen
def clear():
    os.system('cls' if os.name == 'nt' else 'clear')


# Map
rooms = {
    'Dungeon of Azure': {'North': 'Catacombs', 'East': 'Mirror Maze', 'South':'Academy Gate', 'West': 'Empty Room 8'},
    'Mirror Maze': {'North': 'Academy of Sorcery', 'East': 'Mountain Tops', 'South':'Empty Room 11', 'West': 'Dungeon of Azure', 'Item': 'Crystal Orb'},
    'Academy of Sorcery': {'North': 'Altus Plateau', 'East': 'Empty Room 7', 'South':'Mirror Maze', 'West': 'Catacombs', 'Item': 'Dark Magic Staff'},
    'Bazaar' : {'North': 'Empty Room 2', 'East': 'Catacombs', 'South':'Empty Room 8', 'West': 'Empty Room 6', 'Item': 'Curved Greatsword'},
    'Meat Locker' : {'North': 'Empty Room 6', 'East': 'Swamp', 'South':'Crumbling Tower', 'West': 'Stormviel Castle', 'Item': 'Healing Potion'},
    'Quicksand Pit': {'North': 'Stormviel Castle', 'East': 'Crumbling Tower', 'South':'Empty Room 13', 'Item': 'Armor Set'},
    'Mountain Pass': {'North': 'Mountain Tops', 'East': 'Empty Room 12', 'South':'Forbidden Lands', 'West': 'Empty Room 11', 'Item': 'Crossbow'},
    'Bat Cavern': {'North': 'Empty Room 10', 'East': 'Empty Room 15', 'West': 'Empty Room 14', 'Item': 'Beast Shield'},
    'Sky Temple': {'North': 'Empty Room 5', 'South':'Empty Room 9', 'West': 'Empty Room 7', 'Item': 'Sacred Seal'},
    'Swamp': {'North': 'Empty Room 1', 'East': 'Empty Room 6', 'South':'Stormviel Castle', 'Item': 'Axe'},
    'Catacombs': {'North': 'Empty Room 3', 'East': 'Academy of Sorcery', 'South':'Dungeon of Azure', 'West': 'Bazaar', 'Boss 1': 'Spinal the Fell Omen'},
    'Academy Gate': {'North': 'Dungeon of Azure', 'East': 'Empty Room 11', 'South':'Empty Room 15', 'West': 'Empty Room 10', 'Boss 2': 'Regal Ancestor Loretta'},
    'Mountain Tops': {'North': 'Empty Room 7', 'East': 'Empty Room 9', 'South':'Mountain Pass', 'West': 'Mirror Maze', 'Boss 3': 'One Eyed Giant'},
    'Crumbling Tower': {'North': 'Meat Locker', 'East': 'Empty Room 10', 'South':'Empty Room 14', 'West': 'Quicksand Pit', 'Boss 4': 'Storm Hawk Smaug'},
    'Stormviel Castle': {'North': 'Swamp', 'East': 'Meat Locker', 'South':'Quicksand Pit', 'Boss 5': 'Elder Dragon Greyoll'},
    'Lurnia': {'East': 'Empty Room 2', 'South':'Empty Room 6', 'West': 'Empty Room 1', 'Boss 6': 'Supreme Sorcerer Azeroth'},
    'Altus Plateau': {'East': 'Empty Room 4', 'South':'Academy of Sorcery', 'West': 'Empty Room 3', 'Boss 7': 'Void Devourer Rykard'},
    'Limgrave': {'North': 'Empty Room 15', 'East': 'Forbidden Lands', 'West': 'Empty Room 11', 'Boss 8': 'Valiant Gargoyle'},
    'Forbidden Lands': {'North': 'Mountain Pass', 'East': 'Throne of Azure', 'West': 'Limgrave', 'Boss 9': 'Lord of Death, Mohg'},
    'Throne of Azure': {'North': 'Empty Room 12', 'West': 'Forbidden Lands', 'Boss 10': 'Dragonlord Placiduax'},
    'Empty Room 1': {'East': 'Lurnia', 'South':'Swamp'},
    'Empty Room 2': {'East': 'Empty Room 3', 'South':'Bazaar', 'West': 'Lurnia'},
    'Empty Room 3': {'East': 'Altus Plateau', 'South':'Catacombs', 'West': 'Empty Room 2'},
    'Empty Room 4': {'East': 'Empty Room 5', 'South':'Empty Room 7', 'West': 'Altus Plateau'},
    'Empty Room 5': {'South':'Sky Temple', 'West': 'Empty Room 4'},
    'Empty Room 6': {'North': 'Lurnia', 'East': 'Bazaar', 'South':'Meat Locker', 'West': 'Swamp'},
    'Empty Room 7': {'North': 'Empty Room 4', 'East': 'Sky Temple', 'South':'Mountain Tops', 'West': 'Academy of Sorcery'},
    'Empty Room 8': {'North': 'Bazaar', 'East': 'Dungeon of Azure', 'South':'Empty Room 10', 'West': 'Meat Locker'},
    'Empty Room 9': {'North': 'Sky Temple', 'South':'Empty Room 12', 'West': 'Mountain Tops'},
    'Empty Room 10': {'North': 'Empty Room 8', 'East': 'Academy Gate', 'South':'Empty Room 15', 'West': 'Crumbling Tower'},
    'Empty Room 11': {'North': 'Mirror Maze', 'East': 'Mountain Pass', 'South':'Limgrave', 'West': 'Academy Gate'},
    'Empty Room 12': {'North': 'Empty Room 9', 'South':'Throne of Azure', 'West': 'Mountain Pass'},
    'Empty Room 13': {'North': 'Quicksand Pit', 'East': 'Empty Room 14'},
    'Empty Room 14': {'North': 'Crumbling Tower', 'East': 'Bat Cavern', 'West': 'Empty Room 13'},
    'Empty Room 15': {'North': 'Academy Gate', 'East': 'Limgrave', 'West': 'Bat Cavern'},
    }

# Colors for text
class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKCYAN = '\033[96m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    BG_RED = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'
    BG_BLACK = '\033[40m'
    BG_RED = '\033[41m'
    BG_GREEN = '\033[42m'
    BG_YELLOW = '\033[43m'
    BG_BLUE = '\033[44m'
    BG_MAGENTA = '\033[45m'
    BG_CYAN = '\033[46m'
    BG_WHITE = '\033[47m'
    FG_BLACK = '\033[30m'
    FG_RED = '\033[31m'
    FG_GREEN = '\033[32m'
    FG_YELLOW = '\033[33m'
    FG_BLUE = '\033[34m'
    FG_MAGENTA = '\033[35m'
    FG_CYAN = '\033[36m'
    FG_WHITE = '\033[37m'
    # # Example of how to use colors
    # print(bcolors.OKGREEN + "OKGREEN: No active frommets remain. Continue?" + bcolors.ENDC)
    # print(bcolors.WARNING + "Warning: No active frommets remain. Continue?" + bcolors.ENDC)
    # print(bcolors.BG_RED + "BG_RED: No active frommets remain. Continue?" + bcolors.ENDC)
    # print(bcolors.HEADER + "HEADER: No active frommets remain. Continue?" + bcolors.ENDC)
    # print(bcolors.OKBLUE + "OKBLUE: No active frommets remain. Continue?" + bcolors.ENDC)
    # print(bcolors.OKCYAN + "OKCYAN: No active frommets remain. Continue?" + bcolors.ENDC)
    # print(bcolors.BOLD + "BOLD: No active frommets remain. Continue?" + bcolors.ENDC)
    # print(bcolors.UNDERLINE + "UNDERLINE: No active frommets remain. Continue?" + bcolors.ENDC)
    # print(bcolors.FG_BLACK + "FG_BLACK: No active frommets remain. Continue?" + bcolors.ENDC)
    # print(bcolors.FG_RED + "FG_RED: No active frommets remain. Continue?" + bcolors.ENDC)
    # print(bcolors.FG_GREEN + "FG_GREEN: No active frommets remain. Continue?" + bcolors.ENDC)
    # print(bcolors.FG_YELLOW + "FG_YELLOW: No active frommets remain. Continue?" + bcolors.ENDC)
    # print(bcolors.FG_BLUE + "FG_BLUE: No active frommets remain. Continue?" + bcolors.ENDC)
    # print(bcolors.FG_MAGENTA + "FG_MAGENTA: No active frommets remain. Continue?" + bcolors.ENDC)
    # print(bcolors.FG_CYAN + "FG_CYAN: No active frommets remain. Continue?" + bcolors.ENDC)
    # print(bcolors.FG_WHITE + "FG_WHITE: No active frommets remain. Continue?" + bcolors.ENDC)
    # print(bcolors.BG_BLACK + "BG_BLACK: No active frommets remain. Continue?" + bcolors.ENDC)
    # print(bcolors.BG_RED + "BG_RED: No active frommets remain. Continue?" + bcolors.ENDC)
    # print(bcolors.BG_GREEN + "BG_GREEN: No active frommets remain. Continue?" + bcolors.ENDC)
    # print(bcolors.BG_YELLOW + "BG_YELLOW: No active frommets remain. Continue?" + bcolors.ENDC)
    # print(bcolors.BG_BLUE + "BG_BLUE: No active frommets remain. Continue?" + bcolors.ENDC)
    # print(bcolors.BG_MAGENTA + "BG_MAGENTA: No active frommets remain. Continue?" + bcolors.ENDC)
    # print(bcolors.BG_CYAN + "BG_CYAN: No active frommets remain. Continue?" + bcolors.ENDC)
    # print(bcolors.BG_WHITE + "BG_WHITE: No active frommets remain. Continue?" + bcolors.ENDC)


# List of vowels
vowels = ['a', 'e', 'i', 'o', 'u']

# List to track inventory
inventory = []

# Tracks current room
current_room = "Dungeon of Azure"

# Tracks current boss
current_boss = ""

# Tracks last move
msg = ""

clear()
prompt()

# Gameplay loop
while True:

    clear()

    # Display player info
    print("|-------------------------------------------------------------------------------------------|")
    print(bcolors.BG_BLACK + bcolors.BOLD + f"You are in the {current_room}"+ bcolors.ENDC)
    print(bcolors.WARNING + f"Inventory : {inventory}" + bcolors.ENDC)
    print("|-------------------------------------------------------------------------------------------|")

    # Display msg
    print(msg)

    # Item indicator
    if "Item" in rooms[current_room].keys():

        nearby_item = rooms[current_room]["Item"]

        if nearby_item not in inventory:

            if nearby_item[-1] == 's':
                print(bcolors.WARNING + bcolors.UNDERLINE + f"You see {nearby_item}" + bcolors.ENDC)

            else:
                print(bcolors.WARNING + bcolors.UNDERLINE + f"You see a {nearby_item}" + bcolors.ENDC)
                print(bcolors.BG_GREEN + f"Do you want to GET the {nearby_item}?" + bcolors.ENDC)
    
    # Boss encounter
    if 'Boss 1' in rooms[current_room].keys():
        print(bcolors.BG_RED)
        print("|-------------------------------------------------------------------------------------------|")
        print("|        _____     _         _    _   _          _____     _ _    _____                     |")
        print("|       |   __|___|_|___ ___| |  | |_| |_ ___   |   __|___| | |  |     |_____ ___ ___       |")
        print("|       |__   | . | |   | .'| |  |  _|   | -_|  |   __| -_| | |  |  |  |     | -_|   |      |")
        print("|       |_____|  _|_|_|_|__,|_|  |_| |_|_|___|  |__|  |___|_|_|  |_____|_|_|_|___|_|_|      |")
        print("|             |_|                                                                           |")
        print("|-------------------------------------------------------------------------------------------|")
        sleep(1)
        print("|-------------------------------------------------------------------------------------------|")
        print("|                                                _.--""-._                                  |")
        print("|                   .                         ."         ".                                 |")
        print("|                  / \    ,^.         /(     Y             |      )\                        |")
        print("|                  /   `---. |--'\    (  \__..'--   -   -- -'""-.-'  )                      |")
        print("|                  |        :|    `>   '.     l_..-------.._l      .'                       |")
        print("|                  \      __l;__ .'        __.| |_.-'v'-._| |`   _.-'                       |")   
        print("|                  \  .-' | |  `              l._       _.'                                 |")
        print("|                   \/    | |                   l`^^'^^'j                                   |")
        print("|                         | |                _   \_____/     _                              |") 
        print("|                         | |               l `--__)-'(__.--' |                             |")
        print("|                         | |               | /`---``-----     |  ,-----.                   |")
        print("|                         | |               )/  `--' '---'   \ '-'  ___  `-.                |")
        print("|                         | |              //  `-'  '`----'  /  ,-'   I`.  \                |")
        print("|                       _ L |_            //  `-.-.'`-----' /  /  |   |  `. \               |")
        print("|                      '._' / \         _/(   `/   )- ---' ;  /__.J   L.__.\ :              |")
        print("|                       `._;/7(-.......'  /        ) (     |  |            | |              |")
        print("|                       `._;l _'--------_/        )-'/     :  |___.    _._./ ;              |")
        print("|                         | |                 .__ )-'\  __  \  \  I   1   / /               |")
        print("|                         `-'                /   `-\-(-'   \ \  `.|   | ,' /                |")
        print("|                                            \__  `-'    __/  `-. `---'',-'                 |")
        print("|                                               )-._.-- (        `-----'                    |")
        print("|                                              )(  l\ o ('..-.                              |")
        print("|                                        _..--' _'-' '--'.-. |                              |")
        print("|                                __,,-'' _,,-''            \ \                              |")
        print("|                                f'. _,,-'                   \ \                            |")
        print("|                               ()--  |                       \ \                           |")
        print("|                                 \.  |                       /  \                          |")
        print("|                                   \ \                      |._  |                         |")
        print("|                                    \ \                     |  ()|                         |")
        print("|                                     \ \                     \  /                          |")
        print("|                                      ) `-.                   | |                          |")
        print("|                                     // .__)                  | |                          |")
        print("|                                  _.//7'                      | |                          |")
        print("|                                '---'                         j_| `                        |")
        print("|                                                             (| | |                        |")
        print("|                                                             |  \ \                        |")
        print("|                                                              |lllj \                      |")
        print("|                                                              ||||| )                      |")
        print("|-------------------------------------------------------------------------------------------|")
        print(bcolors.ENDC)
        

        if len(inventory) < 1:
            print(f"You enter the room and {rooms[current_room]['Boss 1']} attacks you.")
            print(bcolors.UNDERLINE + f"You have {inventory} items to fight with." + bcolors.ENDC)
            print(bcolors.OKCYAN + "You need 1 item to fight with the Boss." + bcolors.ENDC)
            sleep(4)
            print(bcolors.BG_RED + f"You lost a fight with {rooms[current_room]['Boss 1']}." + bcolors.ENDC)
            print(bcolors.WARNING + "PRESS UP ARROW AND ENTER TO RESTART" + bcolors.ENDC)
            break

        else:
            print(f"You enter the room and {rooms[current_room]['Boss 1']} attacks you.")
            sleep(2)
            print(f"You attack {rooms[current_room]['Boss 1']}.")
            sleep(4)
            print(f"You beat {rooms[current_room]['Boss 1']}!")
            print(bcolors.OKGREEN)
            print("|-------------------------------------------------------------------------------------------|")
            print("|               Continue looking for more items then find the second Boss                   |")
            print("|-------------------------------------------------------------------------------------------|")
            print(bcolors.ENDC)
            
    
    if 'Boss 2' in rooms[current_room].keys():
        print(bcolors.BG_RED)
        print("|-------------------------------------------------------------------------------------------|")
        print("| _____             _    _____                 _             __                _   _        |")
        print("|| __  |___ ___ ___| |  |  _  |___ ___ ___ ___| |_ ___ ___  |  |   ___ ___ ___| |_| |_ ___  |")
        print("||    -| -_| . | .'| |  |     |   |  _| -_|_ -|  _| . |  _| |  |__| . |  _| -_|  _|  _| .'| |")
        print("||__|__|___|_  |__,|_|  |__|__|_|_|___|___|___|_| |___|_|   |_____|___|_| |___|_| |_| |__,| |")
        print("|          |___|                                                                            |")
        print("|-------------------------------------------------------------------------------------------|")
        sleep(1)
        print("|-------------------------------------------------------------------------------------------|")
        print("|                                          .      .                                         |")
        print("|                                          |\____/|                                         |")
        print("|                                         (\|----|/)                                        |")
        print("|                                          \ 0  0 /                                         |")
        print("|                                           |    |                                          |")
        print("|                                        ___/\../\____                                      |")
        print("|                                       /     --       \                                    |")
        print("|                                      /  \         /   \                                   |")
        print("|                                     |    \___/___/(   |                                   |")
        print("|                                     \   /|  }{   | \  )                                   |")
        print("|                                      \  ||__}{__|  |  |                                   |")
        print("|                                       \  |;;;;;;;\  \ / \_______                          |")
        print("|                                        \ /;;;;;;;;| [,,[|======'                          |")
        print("|                                          |;;;;;;/ |     /                                 |")
        print("|                                          ||;;|\   |                                       |")
        print("|                                          ||;;/|   /                                       |")  
        print("|                                          \_|:||__|                                        |")
        print("|                                           \ ;||  /                                        |")
        print("|                                           |= || =|                                        |")
        print("|                                           |= /\ =|                                        |")
        print("|                                           /_/  \_\                                        |")
        print("|-------------------------------------------------------------------------------------------|")
        print(bcolors.ENDC)

        if len(inventory) < 2:
            print(f"You enter the room and {rooms[current_room]['Boss 2']} attacks you.")
            print(bcolors.UNDERLINE + f"You have {inventory} items to fight with." + bcolors.ENDC)
            print(bcolors.OKCYAN + "You need 2 items to fight with the Boss." + bcolors.ENDC)
            sleep(4)
            print(bcolors.BG_RED + f"You lost a fight with {rooms[current_room]['Boss 2']}." + bcolors.ENDC)
            print(bcolors.WARNING + "PRESS UP ARROW AND ENTER TO RESTART" + bcolors.ENDC)
            break
            

        else:
            print(f"You enter the room and {rooms[current_room]['Boss 2']} attacks you.")
            sleep(2)
            print(f"You attack the {rooms[current_room]['Boss 2']}.")
            sleep(4)
            print(f"You beat {rooms[current_room]['Boss 2']}!")
            print(bcolors.OKGREEN)
            print("|-------------------------------------------------------------------------------------------|")
            print("|               Continue looking for more items then find the third Boss                    |")
            print("|-------------------------------------------------------------------------------------------|")
            print(bcolors.ENDC)
            

    if 'Boss 3' in rooms[current_room].keys():
        print(bcolors.BG_RED)
        print("|-------------------------------------------------------------------------------------------|")
        print("|                   _____            _____           _    _____ _         _                 |")
        print("|                  |     |___ ___   |   __|_ _ ___ _| |  |   __|_|___ ___| |_               |")
        print("|                  |  |  |   | -_|  |   __| | | -_| . |  |  |  | | .'|   |  _|              |")
        print("|                  |_____|_|_|___|  |_____|_  |___|___|  |_____|_|__,|_|_|_|                |")
        print("|                                         |___|                                             |")
        print("|-------------------------------------------------------------------------------------------|")
        sleep(1)
        print("|-------------------------------------------------------------------------------------------|")
        print("|                                               _......._                                   |")
        print("|                                           .-'.'.'.'.'.'.`-.                               |")
        print("|                                         .'.'.'.'.'.'.'.'.'.`.                             |")
        print("|                                        /.'.'               '.\                            |")
        print("|                                        |.'    _.--...--._     |                           |")
        print("|                                        \    `._.-.....-._.'   /                           |")
        print("|                                        |     _..- .-. -.._   |                            |")
        print("|                                     .-.'    `.   ((@))  .'   '.-.                         |")
        print("|                                    ( ^ \      `--.   .-'     / ^ )                        |")
        print("|                                     \  /         .   .       \  /                         |")
        print("|                                     /          .'     '.  .-    \                         |")
        print("|                                    ( _.\    \ (_`-._.-'_)    /._\)                        |")
        print("|                                     `-' \   ' .--.          / `-'                         |")
        print("|                                         |  / /|_| `-._.'\   |                             |")
        print("|                                         |   |       |_| |   /-.._                         |")
        print("|                                     _..-\   `.--.______.'  |                              |")
        print("|                                          \       .....     |                              |")
        print("|                                           `.  .'      `.  /                               |")
        print("|                                             \           .'                                |")
        print("|                                              `-..___..-`                                  |")
        print("|-------------------------------------------------------------------------------------------|")
        print(bcolors.ENDC)


        if len(inventory) < 3:
            print(f"You enter the room and {rooms[current_room]['Boss 3']} attacks you.")
            print(bcolors.UNDERLINE + f"You have {inventory} items to fight with." + bcolors.ENDC)
            print(bcolors.OKCYAN + "You need 3 items to fight with the Boss." + bcolors.ENDC)
            sleep(4)
            print(bcolors.BG_RED + f"You lost a fight with {rooms[current_room]['Boss 3']}." + bcolors.ENDC)
            print(bcolors.WARNING + "PRESS UP ARROW AND ENTER TO RESTART" + bcolors.ENDC)
            break
            

        else:
            print(f"You enter the room and {rooms[current_room]['Boss 3']} attacks you.")
            sleep(2)
            print(f"You attack {rooms[current_room]['Boss 3']}.")
            sleep(4)
            print(f"You beat {rooms[current_room]['Boss 3']}!")
            print(bcolors.OKGREEN)
            print("|-------------------------------------------------------------------------------------------|")
            print("|               Continue looking for more items then find the fourth Boss                   |")
            print("|-------------------------------------------------------------------------------------------|")
            print(bcolors.ENDC)
            

    if 'Boss 4' in rooms[current_room].keys():
        print(bcolors.BG_RED)
        print("|-------------------------------------------------------------------------------------------|")   
        print("|         _____ _                    _____           _      _____                           |")  
        print("|        |   __| |_ ___ ___ _____   |  |  |___ _ _ _| |_   |   __|_____ ___ _ _ ___         |")
        print("|        |__   |  _| . |  _|     |  |     | .'| | | | '_|  |__   |     | .'| | | . |        |")
        print("|        |_____|_| |___|_| |_|_|_|  |__|__|__,|_____|_,_|  |_____|_|_|_|__,|___|_  |        |")
        print("|                                                                              |___|        |")
        print("|-------------------------------------------------------------------------------------------|")
        sleep(1)
        print("|-------------------------------------------------------------------------------------------|")
        print("|                       /|                                           |\                     |")       
        print("|                      /||             ^               ^             ||\                    |")     
        print("|                     / \__           /                 \          __// \                   |")   
        print("|                    /  |_  \         | \   /     \   / |         /  _|  \                  |") 
        print("|                   /  /  \  \         \  \/ \---/ \/  /         /  /     \                 |")
        print("|                  /  /    |  \         \  \/\   /\/  /         /  |       \                |")
        print("|                 /  /     \   \__       \ ( 0\ /0 ) /       __/   /        \               |")
        print("|                /  /       \     \___    \ \_/|\_/ /    ___/     /\         \              |")
        print("|               /  /         \_)      \___ \/-\|/-\/ ___/      (_/\ \      `  \             |")
        print("|              /  /           /\__)       \/  oVo  \/       (__/   ` \      `  \            |")
        print("|             /  /           /,   \__)    (_/\ _ /\_)    (__/         `      \  \           |")
        print("|            /  '           //       \__)  (__V_V__)  (__/                    \  \          |")
        print("|           /  '  '        /'           \   |___|   /         .              \  \           |")
        print("|          /  '  /        /              \/ |___| \/\          `              \  \          |")
        print("|         /     /        '       .        \/_____\/  \          \    `         \  \         |")
        print("|              /                ,         /_______\   \          \    \         \           |")
        print("|                              /         /{___/_\___}\   `          \    `         \        |")
        print("|-------------------------------------------------------------------------------------------|")
        print(bcolors.ENDC)


        if len(inventory) < 4:
            print(f"You enter the room and {rooms[current_room]['Boss 4']} attacks you.")
            print(bcolors.UNDERLINE + f"You have {inventory} items to fight with." + bcolors.ENDC)
            print(bcolors.OKCYAN + "You need 4 items to fight with the Boss." + bcolors.ENDC)
            sleep(4)
            print(bcolors.BG_RED + f"You lost a fight with {rooms[current_room]['Boss 4']}." + bcolors.ENDC)
            print(bcolors.WARNING + "PRESS UP ARROW AND ENTER TO RESTART" + bcolors.ENDC)
            break
            

        else:
            print(f"You enter the room and {rooms[current_room]['Boss 4']} attacks you.")
            sleep(2)
            print(f"You attack {rooms[current_room]['Boss 4']}.")
            sleep(4)
            print(f"You beat {rooms[current_room]['Boss 4']}!")
            print(bcolors.OKGREEN)
            print("|-------------------------------------------------------------------------------------------|")
            print("|               Continue looking for more items then find the fifth Boss                    |")
            print("|-------------------------------------------------------------------------------------------|")
            print(bcolors.ENDC)
            

    if 'Boss 5' in rooms[current_room].keys():
        print(bcolors.BG_RED)
        print("|-------------------------------------------------------------------------------------------|")
        print("|       _____ _   _            ____                         _____                 _ _       |")
        print("|      |   __| |_| |___ ___   |    \ ___ ___ ___ ___ ___   |   __|___ ___ _ _ ___| | |      |")
        print("|      |   __| | . | -_|  _|  |  |  |  _| .'| . | . |   |  |  |  |  _| -_| | | . | | |      |")
        print("|      |_____|_|___|___|_|    |____/|_| |__,|_  |___|_|_|  |_____|_| |___|_  |___|_|_|      |")
        print("|                                           |___|                        |___|              |")
        print("|-------------------------------------------------------------------------------------------|")
        sleep(1)
        print("|-------------------------------------------------------------------------------------------|")
        print("|                           ___====-_  _-====___                                            |")
        print("|                     _--^^^#####/      \#####^^^--_                                        |")
        print("|                  _-^##########/ (    ) \##########^-_                                     |")
        print("|                 -############/  |\^^/|  \############-                                    |")
        print("|               _/############/   (@::@)   \############\_                                  |")
        print("|              /#############((      \/    ))#############                                  |")
        print("|             -###############\    (oo)    //###############-                               |")
        print("|            -#################\  / VV \  //#################-                              |")
        print("|           -###################\/      \//###################-                             |")
        print("|          _#/|##########/\######(   /\   )######/\##########|\#_                           |")
        print("|          |/ |#/\#/\#/\/  \#/\##\  |  |  /##/\#/  \/\#/\#/\#| \|                           |")
        print("|          `  |/  V  V  `   V  \#\| |  | |/#/  V   '  V  V  \|  '                           |")
        print("|             `   `  `      `   / | |  | | \   '      '  '   '                              |")
        print("|                              (  | |  | |  )                                               |")
        print("|                             __\ | |  | | /__                                              |")
        print("|                            (vvv(VVV)(VVV)vvv)                                             |")
        print("|-------------------------------------------------------------------------------------------|")
        print(bcolors.ENDC)

        if len(inventory) < 5:
            print(f"You enter the room and {rooms[current_room]['Boss 5']} attacks you.")
            print(bcolors.UNDERLINE + f"You have {inventory} items to fight with." + bcolors.ENDC)
            print(bcolors.OKCYAN + "You need 5 items to fight with the Boss." + bcolors.ENDC)
            sleep(4)
            print(bcolors.BG_RED + f"You lost a fight with {rooms[current_room]['Boss 5']}." + bcolors.ENDC)
            print(bcolors.WARNING + "PRESS UP ARROW AND ENTER TO RESTART" + bcolors.ENDC)
            break
            

        else:
            print(f"You enter the room and {rooms[current_room]['Boss 5']} attacks you.")
            sleep(2)
            print(f"You attack {rooms[current_room]['Boss 5']}.")
            sleep(4)
            print(f"You beat {rooms[current_room]['Boss 5']}!")
            print(bcolors.OKGREEN)
            print("|-------------------------------------------------------------------------------------------|")
            print("|               Continue looking for more items then find the sixth Boss                    |")
            print("|-------------------------------------------------------------------------------------------|")
            print(bcolors.ENDC)
            

    if 'Boss 6' in rooms[current_room].keys():
        print(bcolors.BG_RED)
        print("|-------------------------------------------------------------------------------------------|")
        print("|                                 _____                                                     |")
        print("|                                |   __|_ _  ___ ___ ___ _____ ___                          |")
        print("|                                |__   | | || . |  _| -_|     | -_|                         |")
        print("|                                |_____|___||  _|_| |___|_|_|_|___|                         |")
        print("|                                           |_|                                             |")
        print("|             _____                                _____                 _   _              |") 
        print("|            |   __|___ ___ ___ ___ ___ ___ ___   |  _  |___ ___ ___ ___| |_| |_            |")
        print("|            |__   | . |  _|  _| -_|  _| -_|  _|  |     |- _| -_|  _| . |  _|   |           |")
        print("|            |_____|___|_| |___|___|_| |___|_|    |__|__|___|___|_| |___|_| |_|_|           |")               
        print("|-------------------------------------------------------------------------------------------|")
        sleep(1)
        print("|-------------------------------------------------------------------------------------------|")
        print("|                                             ,-'._  |                                      |")
        print("|                                   .||,      |####\ |                                      |")
        print("|                                  \.`',/     \####| |                                      |")
        print("|                                  = ,. =      |###| |                                      |")
        print("|                                  / || \    ,-'\#/,'`.                                     |")
        print("|                                    ||     ,'   `,,. `.                                    |")
        print("|                                    ,|____,' , ,;' \| |                                    |")
        print("|                                   (3|\    _/|/'   _| |                                    |")
        print("|                                    ||/,-''  | >-''_,\ \                                   |")
        print("|                                    ||'      ==\ ,-'  ,'                                   |")
        print("|                                    ||       |  V \ ,|                                     |")
        print("|                                    ||       |    |` |                                     |")
        print("|                                    ||       |    |   \                                    |")
        print("|                                    ||       |    \    \                                   |")
        print("|                                    ||       |     |    \                                  |")
        print("|                                    ||       |      \_,-'                                  |")
        print("|                                    ||       |___,,--)  \_                                 |")
        print("|                                    ||         |_|   ccc/                                  |")
        print("|                                    ||        ccc/                                         |")
        print("|-------------------------------------------------------------------------------------------|")
        print(bcolors.ENDC)

        if len(inventory) < 6:
            print(f"You enter the room and {rooms[current_room]['Boss 6']} attacks you.")
            print(bcolors.UNDERLINE + f"You have {inventory} items to fight with." + bcolors.ENDC)
            print(bcolors.OKCYAN + "You need 6 items to fight with the Boss." + bcolors.ENDC)
            sleep(4)
            print(bcolors.BG_RED + f"You lost a fight with {rooms[current_room]['Boss 6']}." + bcolors.ENDC)
            print(bcolors.WARNING + "PRESS UP ARROW AND ENTER TO RESTART" + bcolors.ENDC)
            break
            

        else:
            print(f"You enter the room and {rooms[current_room]['Boss 6']} attacks you.")
            sleep(2)
            print(f"You attack {rooms[current_room]['Boss 6']}.")
            sleep(4)
            print(f"You beat {rooms[current_room]['Boss 6']}!")
            print(bcolors.OKGREEN)
            print("|-------------------------------------------------------------------------------------------|")
            print("|               Continue looking for more items then find the seventh Boss                  |")
            print("|-------------------------------------------------------------------------------------------|")
            print(bcolors.ENDC)
            

    if 'Boss 7' in rooms[current_room].keys():
        print(bcolors.BG_RED)
        print("|-------------------------------------------------------------------------------------------|")
        print("|      _____     _   _    ____                                 _____     _             _    |")
        print("|     |  |  |___|_|_| |  |    \ ___ _ _ ___ _ _ ___ ___ ___   | __  |_ _| |_ ___ ___ _| |   |")
        print("|     |  |  | . | | . |  |  |  | -_| | | . | | |  _| -_|  _|  |    -| | | '_| .'|  _| . |   |")
        print("|      \___/|___|_|___|  |____/|___|\_/|___|___|_| |___|_|    |__|__|_  |_,_|__,|_| |___|   |")
        print("|                                                                   |___|                   |")
        print("|-------------------------------------------------------------------------------------------|")                                                         
        sleep(1)
        print("|-------------------------------------------------------------------------------------------|")
        print("|                                          _____.-..-.                                      |")
        print("|                                       .-~@@/ / q  p \                                     |")
        print("|                                     .'@ _@/..\-.__.-/                                     |")
        print("|                                    /@.-~/|~~~`\|__|/                                      |")
        print("|                                    |'--<||     '~~'                                       |")
        print("|                                    |>--<\@\                                               |")
        print("|                                    \>---<\@`\.                                            |")
        print("|                                    `\>---<`\@`\.                                          |")
        print("|                                     `\>----<`\@`\.                                        |")
        print("|                                _     `\>-----<`\@`\.                                      |")
        print("|                              (_)      `\>-----<`\.@`\.                                    |")
        print("|                              (_)        `\>------<`\.@`\.                                 |")
        print("|~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~(__)~~~~~~~~~`\>-------<`\.@`\~~~~~~~~~~~~~                  |")
        print("|  \/..__..--  .  \/  .  ..____( _)@@@--..____\..--\@@@/~`\@@>-._   \/ . \/  .              |")
        print("|\/         \/ \/    \/     / - -\@@@@--@/- - \@@@/ - - \@/- -@@@@/- \.   --._              |") 
        print("|   .   \/    _..\/-...--.. |- - -\@@/ - -\@@@@/~~~~\@@@@/- - \@@/- - |   .\/               |")
        print("|        .  \/              | - - -@@ - - -\@@/- - - \@@/- - - @@- - -|      .              |")
        print("|. \/             .   \/     ~-.__ - - - - -@@- - - - @@- - - - -__.-~  . \/                |")
        print("|   __...--..__..__       .  \/   ~~~--..____- - - - -____..--~~~    \/_..--..              |")
        print("|\/  .   .    \/     \/    __..--... \/      ~~~~~~~~~     \/ . \/  .  .  \/                |")
        print("|-------------------------------------------------------------------------------------------|")
        print(bcolors.ENDC)
        if len(inventory) < 7:
            print(f"You enter the room and {rooms[current_room]['Boss 7']} attacks you.")
            print(bcolors.UNDERLINE + f"You have {inventory} items to fight with." + bcolors.ENDC)
            print(bcolors.OKCYAN + "You need 7 items to fight with the Boss." + bcolors.ENDC)
            sleep(4)
            print(bcolors.BG_RED + f"You lost a fight with {rooms[current_room]['Boss 7']}." + bcolors.ENDC)
            print(bcolors.WARNING + "PRESS UP ARROW AND ENTER TO RESTART" + bcolors.ENDC)
            break
            

        else:
            print(f"You enter the room and {rooms[current_room]['Boss 7']} attacks you.")
            sleep(2)
            print(f"You attack {rooms[current_room]['Boss 7']}.")
            sleep(4)
            print(f"You beat {rooms[current_room]['Boss 7']}!")
            print(bcolors.OKGREEN)
            print("|-------------------------------------------------------------------------------------------|")
            print("|               Continue looking for more items then find the eighth Boss                   |")
            print("|-------------------------------------------------------------------------------------------|")
            print(bcolors.ENDC)
            

    if 'Boss 8' in rooms[current_room].keys():
        print(bcolors.BG_RED)
        print("|-------------------------------------------------------------------------------------------|")
        print("|               _____     _ _         _      _____                     _                    |")
        print("|              |  |  |___| |_|___ ___| |_   |   __|___ ___ ___ ___ _ _| |___                |")
        print("|              |  |  | .'| | | .'|   |  _|  |  |  | .'|  _| . | . | | | | -_|               |")
        print("|               \___/|__,|_|_|__,|_|_|_|    |_____|__,|_| |_  |___|_  |_|___|               |")
        print("|                                                         |___|   |___|                     |")
        print("|-------------------------------------------------------------------------------------------|")
        sleep(1)
        print("|-------------------------------------------------------------------------------------------|")
        print("|                                                       _                                   |")
        print("|                                                     _)\.-.                                |")
        print("|                                    .-.__,___,_.-=-. )\`  a`\_                             |")
        print("|                                .-.__\__,__,__.-=-. `/  \     `                            |")
        print("|                                {~,-~-,-~.-~,-,;;;;\ |   '--;`)/                           |")
        print("|                                 \-,~_-~_-,~-,(_(_(;\/   ,;/                               |")
        print("|                                  ,- ~_,-~ -~(_)(_).      /                                |")
        print("|                                    `~-,_-~,-~(_(_(_(_\  `;                                |")
        print("|                              ,          ~--,)_)_)_)\_    ;                                |")
        print("|                              |\              (_(_/_(_,   \  ;                             |")
        print("|                              \ '-.       _.--'  /_/_/_)   | |                             |")
        print("|                               '--.\    .'          /_/    | |                             |")
        print("|                                   ))  /       \      |   /.'                              |")
        print("|                                  //  /,        | __.'|  ||                                |")
        print("|                                 //   ||        /`    (  ||                                |")
        print("|                                ||    ||      .'       \  \                                |")
        print("|                                ||    ||    .'_         \  \                               |")
        print("|                                 \   //   / _ `\        \  \__                             |")
        print("|                                  \ -'/(   _  `\,;        \ '--:,                          |")
        print("|                                   `"   "` `-,,;         `" ",,;                           |")
        print("|-------------------------------------------------------------------------------------------|")
        print(bcolors.ENDC)
        if len(inventory) < 7:
            print(f"You enter the room and {rooms[current_room]['Boss 8']} attacks you.")
            print(bcolors.UNDERLINE + f"You have {inventory} items to fight with." + bcolors.ENDC)
            print(bcolors.OKCYAN + "You need 7 items to fight with the Boss." + bcolors.ENDC)
            sleep(4)
            print(bcolors.BG_RED + f"You lost a fight with {rooms[current_room]['Boss 8']}." + bcolors.ENDC)
            print(bcolors.WARNING + "PRESS UP ARROW AND ENTER TO RESTART" + bcolors.ENDC)
            break
            

        else:
            print(f"You enter the room and {rooms[current_room]['Boss 8']} attacks you.")
            sleep(2)
            print(f"You attack {rooms[current_room]['Boss 8']}.")
            sleep(4)
            print(f"You beat {rooms[current_room]['Boss 8']}!")
            print(bcolors.OKGREEN)
            print("|-------------------------------------------------------------------------------------------|")
            print("|               Continue looking for more items then find the ninth Boss                    |")
            print("|-------------------------------------------------------------------------------------------|")
            print(bcolors.ENDC)
            
    
    if 'Boss 9' in rooms[current_room].keys():
        print(bcolors.BG_RED)
        print("|-------------------------------------------------------------------------------------------|")
        print("|         __              _        ___    ____          _   _      _____     _              |")
        print("|        |  |   ___ ___ _| |   ___|  _|  |    \ ___ ___| |_| |_   |     |___| |_ ___        |")
        print("|        |  |__| . |  _| . |  | . |  _|  |  |  | -_| .'|  _|   |  | | | | . |   | . |       |")
        print("|        |_____|___|_| |___|  |___|_|    |____/|___|__,|_| |_|_|  |_|_|_|___|_|_|_  |       |")
        print("|                                                                               |___|       |")
        print("|-------------------------------------------------------------------------------------------|")
        sleep(1)
        print("|-------------------------------------------------------------------------------------------|")
        print("|                                         ,-.                                               |")
        print("|                    ___,---.__          /'|`\          __,---,___                          |")
        print("|                 ,-'    \`    `-.____,-'  |  `-.____,-'    //    `-.                       |")
        print("|               ,'        |           ~'\     /`~           |        `.                     |")
        print("|              /      ___//              `. ,'          ,  , \___      \                    |")
        print("|             |    ,-'   `-.__   _         |        ,    __,-'   `-.    |                   |")
        print("|             |   /          /\_  `   .    |    ,      _/\          \   |                   |")
        print("|             \  |           \ \`-.___ \   |   / ___,-'/ /           |  /                   |")
        print("|              \  \           | `._   ` \  |  //'   _,' |           /  /                    |")
        print("|               `-.\         /'  _ `---'' , . ``---' _  `\         /,-'                     |")
        print("|                  ``       /     \    ,='/ \`=.    /     \       ''                        |")
        print("|                          |__   /|\_,--.,-.--,--._/|\   __|                                |")
        print("|                          /  `./   \`\ |  |  | /,//' \,'  \                                |")
        print("|                         /   /     ||--+--|--+-/-|     \   \                               |")
        print("|                        |   |     /'\_\_\ | /_/_/`\     |   |                              |")
        print("|                         \   \__, \_     `~'     _/ .__/   /                               |")
        print("|                          `-._,-'   `-._______,-'   `-._,-'                                |")
        print("|-------------------------------------------------------------------------------------------|")
        print(bcolors.ENDC)
        if len(inventory) < 8:
            print(f"You enter the room and {rooms[current_room]['Boss 9']} attacks you.")
            print(bcolors.UNDERLINE + f"You have {inventory} items to fight with." + bcolors.ENDC)
            print(bcolors.OKCYAN + "You need 8 items to fight with the Boss." + bcolors.ENDC)
            sleep(4)
            print(bcolors.BG_RED + f"You lost a fight with {rooms[current_room]['Boss 9']}." + bcolors.ENDC)
            print(bcolors.WARNING + "PRESS UP ARROW AND ENTER TO RESTART" + bcolors.ENDC)
            break
            

        else:
            print(f"You enter the room and {rooms[current_room]['Boss 9']} attacks you.")
            sleep(2)
            print(f"You attack {rooms[current_room]['Boss 9']}.")
            sleep(4)
            print(f"You beat {rooms[current_room]['Boss 9']}!")
            print(bcolors.OKGREEN)
            print("|-------------------------------------------------------------------------------------------|")
            print("|               Continue looking for more items then find the FINAL Boss                    |")
            print("|-------------------------------------------------------------------------------------------|")
            print(bcolors.ENDC)
            
    
    if 'Boss 10' in rooms[current_room].keys():
        print(bcolors.BG_RED)
        print("|-------------------------------------------------------------------------------------------|")
        print("|         ____                      _           _    _____ _         _   _                  |")
        print("|        |    \ ___ ___ ___ ___ ___| |___ ___ _| |  |  _  | |___ ___|_|_| |_ _ ___ _ _      |")
        print("|        |  |  |  _| .'| . | . |   | | . |  _| . |  |   __| | .'|  _| | . | | | .'|_'_|     |")
        print("|        |____/|_| |__,|_  |___|_|_|_|___|_| |___|  |__|  |_|__,|___|_|___|___|__,|_,_|     |")
        print("|                      |___|                                                                |")
        print("|-------------------------------------------------------------------------------------------|")
        sleep(1)
        print("|-------------------------------------------------------------------------------------------|")
        print("|                                                          ,--,  ,.-.                       |")
        print("|                            ,                   \,       '-,-`,'-.' | ._                   |")
        print("|                           /|           \    ,   |\         }  )/  / `-,',                 |")
        print("|                           [ ,          |\  /|   | |        /  \|  |/`  ,`                 |")
        print("|                           | |       ,.`  `,` `, | |  _,...(   (      .',                  |")
        print("|                           \  \  __ ,-` `  ,  , `/ |,'      Y     (   /_L\                 |")
        print("|                            \  \_\,``,   ` , ,  /  |         )         _,/                 |")
        print("|                             \  '  `  ,_ _`_,-,<._.<        /         /                    |")
        print("|                              ', `>.,`  `  `   ,., |_      |         /                     |")
        print("|                                \/`  `,   `   ,`  | /__,.-`    _,   `\                     |")
        print("|                            -,-..\  _  \  `  /  ,  / `._) _,-\`       \                    |")
        print("|                             \_,,.) /\    ` /  / ) (-,, ``    ,        |                   |")
        print("|                            ,` )  | \_\       '-`  |  `(               \                   |")
        print("|                           /  /```(   , --, ,' \   |`<`    ,            |                  |")
        print("|                          /  /_,--`\   <\  V /> ,` )<_/)  | \      _____)                  |")
        print("|                    ,-, ,`   `   (_,\ \    |   /) / __/  /   `----`   \                    |")
        print("|                   (-, \           ) \ ('_.-._)/ /,`    /             |                    |")
        print("|                   | /  `          `/ \ \ V   V, /`     /             |                    |")
        print("|                ,--\(        ,     <_/`\ \     ||      /             ,                     |")
        print("|               (   ,``-     \/|         \-A.A-`|     /            /                        |")
        print("|              ,>,_ )_,..(    )\          -,,_-`  _--`           (                          |")
        print("|             (_ \|`   _,/_  /  \_            ,--`             |                            |")
        print("|              \( `   <.,../`     `-.._   _,-`                |                             |")
        print("|-------------------------------------------------------------------------------------------|")
        print(bcolors.ENDC)
        if len(inventory) < 9:
            print(f"You enter the room and {rooms[current_room]['Boss 10']} attacks you.")
            print(bcolors.UNDERLINE + f"You have {inventory} items to fight with." + bcolors.ENDC)
            print(bcolors.OKCYAN + "You need 9 items to fight with the Boss." + bcolors.ENDC)
            sleep(4)
            print(bcolors.BG_RED + f"You lost a fight with {rooms[current_room]['Boss 10']}." + bcolors.ENDC)
            print(bcolors.WARNING + "PRESS UP ARROW AND ENTER TO RESTART" + bcolors.ENDC)
            break
            

        else:
            print(f"You enter the room and {rooms[current_room]['Boss 10']} attacks you.")
            sleep(2)
            print(f"You attack {rooms[current_room]['Boss 10']}.")
            sleep(4)
            print(f"You beat {rooms[current_room]['Boss 10']}!")
            print(bcolors.OKGREEN)
            print("|-------------------------------------------------------------------------------------------|")
            print("|                        CONGRATULATIONS! YOU HAVE BEATEN THE GAME!                         |")
            print("|-------------------------------------------------------------------------------------------|")
            print(bcolors.ENDC)
            break

    # Display available directions
    print("You can go:")
    for direction in rooms[current_room].keys():
        if direction != "Item" and direction != "Boss":
            print(bcolors.OKCYAN + direction + bcolors.ENDC)


    # Accepts player's move as input
    user_input = input(bcolors.WARNING + "Enter your move:\n" + bcolors.ENDC)

    # Splits move into words
    next_move = user_input.split(' ')

    # First word is action
    action = next_move[0].title()

    # Reset item and direction
    item = "Item"
    direction = "null"

    # Second word is object or direction
    if len(next_move) > 1:
        item = next_move[1:]
        direction = next_move[1].title()

        item = " ".join(item).title()

    # Moving between rooms
    if action == "Go":

        try:
            current_room = rooms[current_room][direction]
            msg = bcolors.OKGREEN + f"You traveled {direction}" + bcolors.ENDC

        except:
            msg = bcolors.BG_RED + "You can't go that way." + bcolors.ENDC


    
    # Picking up items
    elif action == "Get":
        try:
            if item == rooms[current_room]["Item"]:

                if item not in inventory:

                    inventory.append(rooms[current_room]["Item"])
                    msg = bcolors.FG_GREEN + f"{item} retrieved!" + bcolors.ENDC

                else:
                    msg = f"You already have the {item}"
            
            else:
                msg = f"Can't find {item}"
        except:
            msg = f"Can't find {item}"
    
    # Exit program
    elif action == "Exit":
        break

    # Inventory command
    elif action == "Inventory":
        msg = f"You have {inventory} in your inventory"

    # Help command
    elif action == "Help":
        msg = "Commands: Go, Get, Exit, Help, Inventory"

    # Any other commands invalid
    else:
        msg = "Invalid command"