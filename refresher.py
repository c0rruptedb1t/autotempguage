#if this doesnt work try 'sudo apt-get install lm-sensors -y' then type 'sudo sensors-detect' and say yes to everything
#this is meant to be run in python3
import os
import time
on = "1"
timer = input("How many seconds between updates? ")
timer = int(timer)
while on == ("1"):
	time.sleep(timer)
	os.system("clear; sensors")
	print("Ctrl + C to stop")

#ver 1.0
#c0rruptedb1t
#Built in Kali Linux
