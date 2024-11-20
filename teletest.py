import telepot

API_TOKEN = '7160713391:AAG4xHih4ikau93Eek258CETx71W7SmmPCA'
bot = telepot.Bot(API_TOKEN)
chat_id = '5354793374' 

with open('screenshot.png', 'rb') as photo:
    bot.sendPhoto(chat_id, photo)