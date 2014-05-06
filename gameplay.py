#!/usr/bin/env python3
import sys
import movement as M
#from movement import theseusX, theseusY
#from movement import minotaurX, minotaurY
import os
import minotaur as mino
theseusX = 20
theseusY = 7
minotaurX = 1
minotaurY = 1

minotaurXprev = minotaurX
minotaurYprev = minotaurY
theseusXprev = theseusX
theseusYprev = theseusY
needUpdate = 1

os.system("clear")

level = open('level3.map', 'r')
myMap = M.make_list(level)
myString =M.map_list(myMap, theseusX, theseusY, theseusXprev, theseusYprev, minotaurX, minotaurY)
M.displayMap(myMap)

while(1):
    direction =input("theseusX: ")
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
        theseusY += 1

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

    minotaurPrevX = minotaurX
    minotaurPrevY = minotaurY
    minotaurX, minotaurY = mino.minotaurNextLocation(myMap, theseusX, theseusY,minotaurX, minotaurY)
    #mino.minotaurRemoveLast(myMap, theseusX, theseusY, minotaurX, minotaurY, dirChange)
    minotaurX, minotaurY = mino.minotaurNextLocation(myMap, theseusX, theseusY, minotaurX, minotaurY)
    #mino.minotaurRemoveLast(myMap, dirChange)
    os.system("clear")
    myString = M.map_list(myMap, theseusX, theseusY, theseusXprev, theseusYprev, minotaurX, minotaurY)
    M.displayMap(myString)
