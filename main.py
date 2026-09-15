# Git: status → add → commit → push
import platform
import psutil
import subprocess


version = "2.0.0" #  MAJOR.MINOR.PATCH
ram = psutil.virtual_memory().total
wos = platform.system() + " " +platform.release()




cpu = subprocess.check_output(
    "wmic cpu get name",
    shell=True
).decode().split("\n")[1].strip()

print(cpu)
print(__import__("subprocess").check_output(["powershell", "-NoProfile", "-Command", "(Get-CimInstance Win32_VideoController).Name"]).decode().strip())
print(f"{ram / (1024 ** 3):.1f} GB")
print(wos)