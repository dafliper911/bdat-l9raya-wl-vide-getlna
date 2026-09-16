# Git: status → add → commit → push
# edit logo.txt to change the logo
import platform
import psutil
import subprocess


version = "2.1.0" #  MAJOR.MINOR.PATCH
ram = psutil.virtual_memory().total
wos = platform.system() + " " +platform.release()

file = open("logo.txt", "r")

data = file.read()

print(data)

file.close()

cpu = subprocess.check_output(
    "wmic cpu get name",
    shell=True
).decode().split("\n")[1].strip()

print(cpu)
print(__import__("subprocess").check_output(["powershell", "-NoProfile", "-Command", "(Get-CimInstance Win32_VideoController).Name"]).decode().strip())
print(f"{ram / (1024 ** 3):.1f} GB")
print(wos)