#!/usr/bin/env python3

import sys

theseusX = 20
theseusY = 7
minotaurX = 22
minotaurY = 7

theseusXprev = theseusX
theseusYprev = theseusY
needUpdate = 1

def displayMap(map):
    for j in range(0,len(map)):
        sys.stdout.write(map[j])

def make_list(stream):
    myMap = []
    for line in stream:
        for c in line:
            myMap.append(c)


    myMap.append('\n')
    return myMap

def map_list(myMap,theseusX, theseusY, theseusXprev, theseusYprev):
    if myMap[(theseusX)+((theseusY)*41)] == '0':
        theseusX = theseusXprev
        theseusY = theseusYprev
    myMap[(theseusX)+((theseusY)*41)] =  '?'
    #else:
     #   myMap[(theseusX)+((theseusY)*41)] == '?'
      #  myMap[(theseusXprev)+((theseusYprev)*41)] == ' '
    myMap[(minotaurX)+((minotaurY)*41)] = '$'
    return ''.join(myMap)

level = open('level2.map', 'r')
myMap = make_list(level)
myString = map_list(myMap, theseusX, theseusY, theseusXprev, theseusYprev)
displayMap(myMap)

while(1):
    direction = input("theseusX: ")
    theseusXprev = theseusX
    theseusYprev = theseusY
    if direction == 'd':
        theseusX += 1
    if direction == 'a':
        theseusX -= 1
    if direction == 'w':
        theseusY -= 1
    if direction == 's':
        theseusY += 1

    #myMap = make_list(level)
    myString = map_list(myMap, theseusX, theseusY, theseusXprev, theseusYprev)
    displayMap(myString)
