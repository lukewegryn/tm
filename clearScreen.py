#!/usr/bin/env python3

import os
from sys import platform as _platform

def clearScreen(Win_Or_Unix):
	if Win_Or_Unix == 0:
		os.system("clear")
	else:
		os.system("cls")

def checkOs():
	if _platform == "linux" or _platform == "linux2" or _platform == "darwin":
		return 0
	elif _platform == "win32":
		return 1


