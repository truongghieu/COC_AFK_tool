from time import sleep
from adb_ldplayer import tap
import json
data = json.load(open('data.json'))
buttons = data['buttons']
def change_account(n):
    print("Change Account")
    tap(buttons['setting'])
    sleep(2)
    tap(buttons['change_account'])
    sleep(2)
    if n == 1:
        tap(buttons['account_1'])
    elif n == 2:
        tap(buttons['account_2'])
    elif n == 3:
        tap(buttons['account_3'])
    elif n == 4:
        tap(buttons['account_4'])
    elif n == 5:
        tap(buttons['account_5'])
    sleep(2)

    

    
