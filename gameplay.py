#!/usr/bin/env python3
import sys
import movement as M
from movement import theseusX, theseusY
from movement import minotaurX, minotaurY
theseusXprev = theseusX
theseusYprev = theseusY
needUpdate = 1

level = open('level3.map', 'r')
myMap = M.make_list(level)
myString =M.map_list(myMap, theseusX, theseusY, theseusXprev, theseusYprev)
M.displayMap(myMap)

while(1):
    direction =input("theseusX: ")
    theseusXprev = theseusX
    theseusYprev = theseusY
    print(theseusX)
    if direction == 'd':
        theseusX += 1
    if direction == 'a':
        theseusX -= 1
    if direction == 'w':
        theseusY -= 1
    if direction == 's':
        theseusY += 1

    #myMap = make_list(level)
    myString = M.map_list(myMap, theseusX, theseusY, theseusXprev, theseusYprev)
    M.displayMap(myString)
