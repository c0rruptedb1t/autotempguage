import os
print("Installing lm-sensors")
os.system("sudo apt-get install lm-sensors -y")
wait = input("Press Enter To Continue")
os.system("sudo sensors-detect")
print("agree to everything")
wait = input("Press Enter To Continue")
