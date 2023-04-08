from tkinter import *
from termcolor import *
import subprocess
import datetime
import requests
import getpass
import psutil
import ctypes
import shutil
import time
import sys
import os

os.system("title 짱짱 캐시 삭제 프로그램")
os.system("mode con: cols=45 lines=10")

# 관리자 권한 체크
if os.name == "nt":
    try:
        isAdmin = ctypes.windll.shell32.IsUserAnAdmin()
    except:
        isAdmin = False
else:
    isAdmin = os.getuid() == 0
if isAdmin:
    cprint("관리자 권한으로 실행 중 입니다.", "green")
else:
    cprint("관리자 권한으로 실행해 주세요.", "red")
    exit()

#프로그램 작동 시간 표시
now = datetime.datetime.now()
nowDatetime = now.strftime('%Y-%m-%d %H:%M:%S')

# HWID 확인
hwid = str(str(subprocess.check_output('wmic csproduct get uuid')).strip().replace(r"\r", "").split(r"\n")[1].strip())
r = requests.get("https://pastebin.com/jF58Tqxz")

def printSlow(text):
    for char in text:
        print(char, end="")
        sys.stdout.flush()
        time.sleep(.1)

def Main_Program():
    if hwid in r.text:
        cprint("접근을 허가합니다.", "green")
        cprint(f"프로그램 실행 시간 : {nowDatetime}", "blue")
        time.sleep(.1)
    else:
        cprint("확인 되지 않은 HWID 입니다.", "red")
        cprint("등록되어 있는지 HWID인지 확인 해주세요:" + hwid ,"blue")
        print()
        print()
        print()
        cprint("========================5초후 프로그램이 자동 종료 됩니다.========================","magenta",attrs=['blink'])
        time.sleep(5)
        exit()
      
if __name__ == "__main__":
    Main_Program()


username = getpass.getuser() # 사용자 이름을 확인하는 코드

discord_path = f"C:/Users/{username}/AppData/Roaming/discord/Cache/Cache_Data"
chrome_path = f"C:/Users/{username}/AppData/Local/Google/Chrome/User Data/Default/Cache/Cache_Data"
edge_path = os.path.join(os.getenv("LOCALAPPDATA"), "Microsoft", "Edge", "User Data", "Default", "Cache")

try:
    # 폴더 삭제
    shutil.rmtree(chrome_path)
    cprint("크롬 캐시를 삭제 했습니다.", "green")
except OSError as e:
    cprint("크롬 캐시를 찾을 수 없습니다.", "red")
except Exception as e:
    print(e)

try:
    # 엣지 브라우저 종료
    for proc in psutil.process_iter():
        if proc.name() == "msedge.exe":
            proc.kill()
    # 캐시 폴더 삭제
    shutil.rmtree(edge_path)
    cprint(f"엣지 캐시를 삭제 했습니다.", "green")
except OSError as e:
    cprint(f"엣지 캐시를 찾을 수 없습니다.", "red")
    
try:
    # 폴더 삭제
    shutil.rmtree(discord_path)
    cprint("디스코드 캐시를 삭제 했습니다.", "green")
except OSError as e:
    cprint("디스코드 캐시를 찾을 수 없습니다.", "red")
except Exception as e:
    print(e)

cprint("Developer By github.com/201580ag", "red", "on_yellow", attrs=["reverse", "blink"])
os.system("pause")