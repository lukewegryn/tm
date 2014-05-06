#!/usr/bin/env python3
import sys
import movement as M
#from movement import theseusX, theseusY
#from movement import minotaurX, minotaurY
import os
import minotaur as mino
import GetInput
theseusX = 20
theseusY = 7
minotaurX = 1
minotaurY = 1
minotaurXprev = minotaurX
minotaurYprev = minotaurY
theseusXprev = theseusX
theseusYprev = theseusY

os.system("clear")

option = 0

while(1):
    if option == 0:
        os.system("clear")
        sys.stdout.write("Theseus and the Minotar\n Get to the exit to win. \n He gets 2 moves for every one of yours. \n Use W-A-S-D and Enter to navigate \n")
        selection = GetInput.getch.impl()
        theseusX = 20
        theseusY = 7
        minotaurX = 1
        minotaurY = 1
        level = open('level3.map', 'r')
        myMap = M.make_list(level)
        myString =M.map_list(myMap, theseusX, theseusY, theseusXprev, theseusYprev, minotaurX, minotaurY)

        if selection == 's':
            option = 1
            os.system("clear")
            M.displayMap(myMap)
        else:
            option = 0


    if option == 1:
        #direction =input("theseusX: ")
        direction = GetInput.getch.impl()
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
        minotaurX, minotaurY = mino.minotaurNextLocation(myMap, theseusX, theseusY, minotaurX, minotaurY)
        os.system("clear")
        myString = M.map_list(myMap, theseusX, theseusY, theseusXprev, theseusYprev, minotaurX, minotaurY)
        M.displayMap(myString)
        if(theseusX == minotaurX and theseusY == minotaurY):
            option = 2
        if(theseusX == 32 and theseusY == 8):
            option = 3

    if option == 2:
        os.system("clear")
        sys.stdout.write("Game Over \n")
        selection = input("Enter: ")
        if selection == 'r':
            option = 0
        else:
            option = 2


    if option == 3:
        os.system("clear")
        sys.stdout.write("You Win!\n")
        selection = input("Enter: ")
        if selection == 'r':
            option = 0
        else:
            option = 3

