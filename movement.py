#!/usr/bin/env python3

import sys
'''theseusX = 20 #sets the initial values of theseus and the minotaur
theseusY = 7
minotaurX = 22
minotaurY = 7'''

def displayMap(map): #displays the map and locations to the terminal
    for j in range(0,len(map)):
        sys.stdout.write(map[j])

def make_list(stream): #imports the stream and puts it into a list
    myMap = []
    for line in stream:
        for c in line:
            myMap.append(c)


    myMap.append('\n')
    return myMap

def wall_check(myMap, theseusX, theseusY): #checks if theseus hit a wall
    if myMap[(theseusX)+((theseusY)*41)] == '0':
        return 0  #if theseus has hit a wall return 0
    else :
        return 1

def map_list(myMap,theseusX, theseusY, theseusXprev, theseusYprev, minotaurX, minotaurY): #puts values into the map list
    if myMap[(theseusX)+((theseusY)*41)] == '0':
        theseusX = theseusXprev
        theseusY = theseusYprev
    else :
        myMap[(theseusX)+((theseusY)*41)] =  '?'
    if theseusX !=theseusXprev or theseusY != theseusYprev:
        myMap[(theseusXprev)+((theseusYprev)*41)] = ' '
    myMap[(minotaurX)+((minotaurY)*41)] = '$'
    return ''.join(myMap)
