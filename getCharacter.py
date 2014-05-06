#!/usr/bin/env python3

import sys
import curses

def getCharacter(stdscr):
	def main(stdscr):
		c = stdscr.getch()
		direction = chr(c)
		return direction	
#stdscr.addstr(chr(c)+ ": "+ str(c) + "\n)
	direction = curses.wrapper(main)
	#stdscr.refresh()
	#print(direction)
	return direction
	

