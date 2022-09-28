
#############################################################################################################################
#   filename:printTudo.py                                                       
#   created: 2022-09-28                                                              
#   import your librarys below                                                    
#############################################################################################################################

import pyautogui 
import time
import datetime
from datetime import datetime, timezone, timedelta
import getpass
import platform
import subprocess
from pathlib import Path

#variaveis
datatime = datetime.now()
times = str(datatime)
data = times.replace('-','_').replace(' ', '_').replace(':','_')[:19]



def printTudo():
    path = Path(f"print")
    path.mkdir(parents=True, exist_ok=True)
    for i in range(10):
        foto = pyautogui.screenshot()
        time.sleep(4)
        foto.save(f"print/print_{i}_{data}.png")
    
    print("worked")


