import customtkinter as ctk
import time
import psutil  # Import the psutil library
import telepot
from telepot.loop import MessageLoop
import os
import subprocess
from clean import cleann

ctk.set_default_color_theme("dark-blue.json")



API_TOKEN = '7160713391:AAG4xHih4ikau93Eek258CETx71W7SmmPCA'
bot = telepot.Bot(API_TOKEN)
chat_id = '5354793374' 

def set_brightness(level):
    # Make sure level is an integer from 0 to 100
    if 0 <= level <= 100:
        subprocess.run(f"powershell (Get-WmiObject -Namespace root/WMI -Class WmiMonitorBrightnessMethods).WmiSetBrightness(1,{level})", shell=True)
    else:
        print("Brightness level should be between 0 and 100.")

class DarkScreen(ctk.CTk):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        
        self.geometry("1920x1080")
        self.title("Dark Screen")
              
        self.wm_attributes("-fullscreen", True)
        self.wm_attributes("-transparentcolor", "black")
        self.wm_attributes("-topmost", True)
        self.state_active = True
        self.brightness = 255  # Track brightness level (0-255)
        self.cpu_stat = 0
        self.mem_stat = 0
        self.time = f"{time.strftime('%H:%M:%S')}"
        self.afk = False
        self.label_time = ctk.CTkLabel(self, text="hello", font=("space mono", 150)) 
        self.label_time.place(relx=0.5, rely=0.4, anchor="center") 

        self.text_label = ctk.CTkLabel(self, text="Sleeping", font=("space mono", 50))
        self.text_label.place(relx=0.5, rely=0.55, anchor="center")

        self.command_lable = ctk.CTkLabel(self, text="Command", font=("space mono", 20))
        self.command_lable.place(relx=0.5, rely=0.7, anchor="center")

        self.entry_command = ctk.CTkEntry(self, placeholder_text="Command")
        self.entry_command.place(relx=0.5, rely=0.8, anchor="center")

        self.bind("<Escape>", lambda event: self.destroy())
        self.bind("<Return>", lambda event: self.handle(self.entry_command.get()) )
        self.bind("p" , lambda event: self.wm_attributes("-topmost", False))
        MessageLoop(bot,self.handle).run_as_thread()
        set_brightness(0)
        self.update_time()
        self.update_stats()  # Call method to update CPU and RAM stats
    def update_time(self):
        self.time = f"{time.strftime('%H:%M')}"
        self.label_time.configure(text=self.time)
        self.after(1000, self.update_time)

    def update_stats(self):
        time_start = ""
        self.cpu_stat = psutil.cpu_percent()  # Get CPU usage
        self.mem_stat = psutil.virtual_memory().percent  # Get RAM usage         
        self.text_label.configure(text=f"CPU: {self.cpu_stat}% | RAM: {self.mem_stat}%")
        self.after(1000, self.update_stats)  # Update every secon
        

    def active_button(self):
        if self.state_active:
            self.state("minimized")
            self.state_active = False
        else:
            self.state("zoomed")
            self.state_active = True

    def handle(self,msg):
        # check if msg is string or not
        if isinstance(msg, str):
            msg = msg.lower()
        else:
            msg = msg['text'].lower()
        self.command_lable.configure(text=msg)
        # string lower
        
        if msg == "cpu":
            bot.sendMessage(chat_id, f"- CPU usage: {self.cpu_stat}% \n- RAM usage: {self.mem_stat}%")
        if msg == "afk":
            bot.sendMessage(chat_id, "Cleanning,Optimizing process")
            try:
                cleann()
            except Exception as e:
                print(e)
            bot.sendMessage(chat_id, "Start AFK")
            self.afk_process = subprocess.Popen("start cmd /c afk.bat", shell=True)
        if"shutdown" in msg:
            t = msg.split(" ")
            if len(t) > 1:
                bot.sendMessage(chat_id, f"Shutdowning in {t[1]} seconds")
                os.system(f"shutdown /s /t {t[1]}")
            else:
                bot.sendMessage(chat_id, "Shutdowning in 1 seconds")
                os.system("shutdown /s /t 1")
            # bot.sendMessage(chat_id, "Shutdowning in 1 seconds")
            # os.system("shutdown /s /t 1")
        if msg == "stop":
            bot.sendMessage(chat_id, "Stoping in 1 seconds")
            # stop afk
            os.system("taskkill /F /IM dnplayer.exe")
            os.system("taskkill /F /IM C:\Windows\System32\cmd.exe")
        if msg == "reset":
            bot.sendMessage(chat_id, "Reseting in 1 seconds")
            subprocess.run("shutdown /r /f /t 0", shell=True)


if __name__ == "__main__":
    bot.sendMessage(chat_id, "Bot started")
    app = DarkScreen()
    app.after(0, lambda: app.state("zoomed"))
    app.mainloop()
    bot.sendMessage(chat_id, "Bot stopped")
    set_brightness(80)
