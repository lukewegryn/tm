#!/usr/bin/env python3

import GetInput

def getChar(Win_Or_Unix):
	if Win_Or_Unix == 1:
		char = (GetInput.getch.impl()).decode("utf-8")
	else:
		char = GetInput.getch.impl()
	return char

