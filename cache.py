from tkinter import *
from termcolor import *
import datetime
import getpass
import psutil
import ctypes
import shutil
import os

os.system("title Cache Delete Program")
os.system("mode con: cols=45 lines=10")

if os.name == "nt":
    try:
        isAdmin = ctypes.windll.shell32.IsUserAnAdmin()
    except:
        isAdmin = False
else:
    isAdmin = os.getuid() == 0
if isAdmin:
    cprint("Running with administrator privileges.", "green")
else:
    cprint("Please run it with administrator privileges.", "red")
    exit()

now = datetime.datetime.now()
nowDatetime = now.strftime('%Y-%m-%d %H:%M:%S')

username = getpass.getuser()

discord_path = f"C:/Users/{username}/AppData/Roaming/discord/Cache/Cache_Data"
chrome_path = f"C:/Users/{username}/AppData/Local/Google/Chrome/User Data/Default/Cache/Cache_Data"
edge_path = os.path.join(os.getenv("LOCALAPPDATA"), "Microsoft", "Edge", "User Data", "Default", "Cache")

try:
    shutil.rmtree(chrome_path)
    cprint("Chrome cache has been deleted.", "green")
except OSError as e:
    cprint("No Chrome cache found.", "red")
except Exception as e:
    print(e)

try:
    for proc in psutil.process_iter():
        if proc.name() == "msedge.exe":
            proc.kill()
    shutil.rmtree(edge_path)
    cprint(f"Edge cache deleted successfully.", "green")
except OSError as e:
    cprint(f"Edge cache not found.", "red")

try:
    shutil.rmtree(discord_path)
    cprint("Discord cache deleted.", "green")
except OSError as e:
    cprint("Discord cache not found.", "red")
except Exception as e:
    print(e)

cprint("Developer By github.com/201580ag", "red", "on_yellow", attrs=["reverse", "blink"])
os.system("pause")
