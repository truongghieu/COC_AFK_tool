from macro.pvp import start_pvp_game
from macro.train import train_troops
from macro.change_account import change_account
from macro.check import get_data_from_image 
from adb_ldplayer import start_ldplayer, close_ldplayer,screenshot,send_photo,send_text
from time import sleep
from clean import close_unwanted_processes
import time
import random
import pyautogui


ACCOUNT_NAME = ["chipp","Newstar","Fish","chipp1","chipp2"]
ACCOUNT_TAG = ["#YPCL0G0GY","#QJJCVYPJ9","#QRLY8R2JJ","#G8PUCYYVP","#GRJY2CJPQ"]

def AFK_pvp_1_account(n=1):
    
    start_ldplayer()
    sleep(10)
        # crt + q
    pyautogui.hotkey('ctrl', 'q')
    sleep(10)
    # ACCOUNT 1
    start_time = time.time()
    change_account(n)
    start_pvp_game()
    sleep(2)
    train_troops()
    sleep(2)    
    screenshot()
    sleep(1)
    # send_photo()
    data = get_data_from_image()
    elapsed_time = time.time() - start_time
    send_text(f"⏰ Time: {elapsed_time / 60:.2f} mins ✅\n➡ {ACCOUNT_NAME[1-1]}\n➡ {ACCOUNT_TAG[1-1]}\n{data}")

    try:
        close_ldplayer()
    except Exception as e:
        send_text(e)
    try:
        close_unwanted_processes(process_names="dnplayer.exe")
    except Exception as e:
        send_text(e)
    

while True:
    AFK_pvp_1_account(1)
    sleep(60*15)
