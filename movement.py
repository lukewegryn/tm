#!/usr/bin/env python3
'''movement.py -- Responsible for generating and updating the list
that controls the map layout and the thesis and minotaur positions'''
import sys

wall = '0' #this is the char that makes up the walls
thesChar = '*' #this represents the theseus
minoChar = '#' #this represents the minotaur (mino"char" get it?)

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
    if myMap[(theseusX)+((theseusY)*41)] == wall:
        return 0  #if theseus has hit a wall return 0
    else :
        return 1

def level_check(levelNumber): #returns the current positions and level
    if levelNumber == 1:
        theseusX = 13
        theseusY = 6
        minotaurX = 13
        minotaurY = 3
        level = open('level1.map', 'r')
    elif levelNumber == 2:
        theseusX = 11
        theseusY = 4
        minotaurX = 4
        minotaurY = 2
        level = open('level2.map', 'r')
    elif levelNumber == 3:
        theseusX = 9
        theseusY = 1
        minotaurX = 37
        minotaurY = 5
        level = open('level3.map', 'r')
    elif levelNumber == 4:
        theseusX = 1
        theseusY = 1
        minotaurX = 37
        minotaurY = 5
        level = open('level4.map', 'r')
    elif levelNumber == 5:
        theseusX = 1
        theseusY = 7
        minotaurX = 19
        minotaurY = 3
        level = open('level5.map', 'r')
    elif levelNumber == 6:
        theseusX = 1
        theseusY = 1
        minotaurX = 37
        minotaurY = 1
        level = open('level6.map', 'r')
    return level, theseusX, theseusY, minotaurX, minotaurY

def map_list(myMap,theseusX, theseusY, theseusXprev, theseusYprev, minotaurX, minotaurY): #puts values into the map list
    if myMap[(theseusX)+((theseusY)*41)] == wall:
        theseusX = theseusXprev
        theseusY = theseusYprev
    else:
        myMap[(theseusX)+((theseusY)*41)] =  thesChar
    if theseusX !=theseusXprev or theseusY != theseusYprev:
        myMap[(theseusXprev)+((theseusYprev)*41)] = ' '
    myMap[(minotaurX)+((minotaurY)*41)] = minoChar
    return ''.join(myMap)
