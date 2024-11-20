import pyautogui
from time import sleep
import random
import json
from adb_ldplayer import tap,screenshot

TIME_ENDGAME = 30

file = open('data.json')
data = json.load(file)
file.close()

buttons = data['buttons']

def pregame():
    print("Pregame......")
    tap(buttons['def_oke'])
    sleep(1)
    tap([0,0])
    sleep(1)


def start_new_game():
    pregame()
    print("Starting......")
    tap(buttons['enter_find_game'])
    sleep(1)
    tap(buttons['find_game'])

    # wait for game to start
    sleep(5)
  
  
  
    
 


def select_troops(s):
    print("Selecting troops......")
    trop_name = "troop_" + s
    
    tap(buttons[trop_name])
    
    
def implement():
    pos = random.choice(buttons['troop_cord'])
    tap([pos[0] + random.randint(0,5), pos[1] + random.randint(0,5)]) 

def end_game():
    tap(buttons["surrender"])
    sleep(1)
    tap(buttons["surrender_oke"])
    print("Ending......")
    tap(buttons['exit_game'])
    sleep(5)
    tap(buttons['award_oke'])
    sleep(2)
    tap([0,0])


TROOPS = [['1',40],['2',15],['3',15],['4',15],['5',15],['6',15],['7',30]]

def start_pvp_game():
   
    start_new_game()
    sleep(random.randint(1,2))
    for i in TROOPS:
        select_troops(i[0])  
        print("Implementing...")
        for j in range(i[1]):  
            implement()

    sleep(TIME_ENDGAME)
    end_game()


