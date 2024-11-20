from time import sleep
from adb_ldplayer import tap
import json

data = json.load(open('data.json'))
buttons = data['buttons']

def train_troops():
    print("Training......")
    tap(buttons['troop_window'])
    sleep(2)
    tap(buttons['fast_train'])
    sleep(2)
    tap(buttons['training'])
    sleep(2)
    tap(buttons['exit_train'])
    sleep(2)

