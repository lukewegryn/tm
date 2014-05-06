#!/usr/bin/env python3

import sys

theseusX = 0
theseusY = 0
minotaurX = 1
minotaurY = 1
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

def map_list(list, theseusX, theseusY, minotaurX, minotaurY):
    myMap[((theseusX)+((theseusY)*80))] =  '?'
    myMap[(minotaurX)+((minotaurY)*80)] = '$'
    return ''.join(myMap)

level = open('level1.map', 'r')
myMap = make_list(level)
myString = map_list(myMap, theseusX, theseusY, minotaurX, minotaurY)
displayMap(myMap)

while(1):
    direction = input("theseusX: ")

    if direction == 's':
        theseusX += 1
        needUpdate = 1

        myMap = make_list(level)
        myString = map_list(level, theseusX, theseusY, minotaurX, minotaurY)
        displayMap(myString)
