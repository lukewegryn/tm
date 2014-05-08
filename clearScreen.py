#!/usr/bin/env python3

import os

def clearScreen(Win_Or_Unix):
	if Win_Or_Unix == 0:
		os.system("clear")
	else:
		os.system("cls")

