import subprocess
import pygetwindow as gw
import os
from time import sleep

from PIL import Image


# Provide full path to ADB
adb_path = f"C:\\LDPlayer\\LDPlayer9\\adb.exe"
ldplayer_path = f"C:\\LDPlayer\\LDPlayer9\\dnplayer.exe"  # Adjust this path if necessary

ldplayer_window = gw.getWindowsWithTitle('LDPlayer')


import telepot

API_TOKEN = '7160713391:AAG4xHih4ikau93Eek258CETx71W7SmmPCA'
bot = telepot.Bot(API_TOKEN)
chat_id = '5354793374' 

def tap(cord):
    subprocess.call(f"{adb_path} shell input tap {cord[0] } {cord[1]}", shell=True)
    

def start_ldplayer():
    # subprocess.Popen(ldplayer_path)
    os.startfile(ldplayer_path)
    # minimize
    


def close_ldplayer():
    # subprocess.call("taskkill /F /IM dnplayer.exe", shell=True)
    os.system("taskkill /F /IM dnplayer.exe")

# screenshot
def screenshot(path=None):
    if path is None:
        subprocess.call(f"{adb_path} exec-out screencap -p > screenshot.png", shell=True)
    else:
        subprocess.call(f"{adb_path} exec-out screencap -p > {path}", shell=True)
    with Image.open('screenshot.png') as im:
        crop_area = (666, 19, 754, 133)
        im = im.crop(crop_area)
        im.save('screenshot.png')

def minimize():
    print(ldplayer_window)
    if ldplayer_window:
        ldplayer_window[1].minimize()



def send_photo():
    with open('screenshot.png', 'rb') as photo:
        bot.sendPhoto(chat_id, photo)

def send_text(text):
    bot.sendMessage(chat_id, text)

if __name__ == "__main__":
    # start_ldplayer()
    # close_ldplayer()
    # minimize()
    screenshot()
    # send_photo()
    # send_text("hello")
    print("hello")