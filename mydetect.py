import os
import subprocess
import time
from typing import Optional


def detectOS() -> Optional[str]:
    osname: Optional[str] = None

    if osname is not None:
        return osname

    # Linuxの判定
    if os.path.sep == "/":
        osname: Optional[str] = "Linux"

    # Windowsの判定
    if "windir" in os.environ:
        osname: Optional[str] = "Windows"

    return osname


def executeCommand(command: str) -> None:
    currentOS: Optional[str] = detectOS()
    if currentOS == "Windows":
        subprocess.call(["powershell", "-Command", command])
    else:
        os.system(command)


def sleepTime(seconds: float) -> None:
    currentOS: Optional[str] = detectOS()
    if currentOS == "Windows":
        executeCommand("Start-Sleep -Milliseconds " + str(seconds * 1000))
    else:
        time.sleep(seconds)


def clearScreen() -> None:
    currentOS: Optional[str] = detectOS()
    if currentOS == "Windows":
        executeCommand("cls")
    else:
        executeCommand("clear")
