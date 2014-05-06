#!/usr/bin/env python3

import sys
theseusX = 20
theseusY = 7
minotaurX = 22
minotaurY = 7

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
    if theseusX !=theseusXprev or theseusY != theseusYprev:
        myMap[(theseusXprev)+((theseusYprev)*41)] = ' '
    #else:
     #   myMap[(theseusX)+((theseusY)*41)] == '?'
      #  myMap[(theseusXprev)+((theseusYprev)*41)] == ' '
    myMap[(minotaurX)+((minotaurY)*41)] = '$'
    return ''.join(myMap)


