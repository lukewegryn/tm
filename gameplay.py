#!/usr/bin/env python3
import sys
import movement as M
from movement import theseusX, theseusY
from movement import minotaurX, minotaurY
import os
import curses
import getCharacter as GC 

theseusXprev = theseusX
theseusYprev = theseusY
needUpdate = 1

level = open('level3.map', 'r')
myMap = M.make_list(level)
myString =M.map_list(myMap, theseusX, theseusY, theseusXprev, theseusYprev)
M.displayMap(myMap)
stdscr = curses.initscr()
while(1):
    print("theseusX: ")
    #c=curses.wrapper(curses.initscr().getch())
    direction = stdscr.getch()
    direction = chr(direction)
   # curses.nocbreak#()
    #stdscr.keypad(False)
   # curses.echo()
#    curses.endwin()
    #direction = curses.wrapper(getCharacter)
    #print(direction+'\r')
 #   stdscr.refresh()
    if direction == 'd' or direction == 's' or direction == 'a' or direction == 'w' :
        theseusXprev = theseusX
        theseusYprev = theseusY
        # print(theseusX)
        if direction == 'd':
            theseusX += 1
        if direction == 'a':
            theseusX -= 1
        if direction == 'w':
            theseusY -= 1
        if direction == 's':
            theseusY +=1
        atWall = M.wall_check(myMap, theseusX, theseusY)
        if atWall == 0:
            if direction == 'd':
                theseusX -=1
            if direction == 'a':
                theseusX +=1
            if direction == 'w':
                theseusY +=1
            if direction == 's':
                theseusY -=1

        #os.system("clear")
        myString = M.map_list(myMap, theseusX, theseusY, theseusXprev, theseusYprev)
        M.displayMap(myString)
