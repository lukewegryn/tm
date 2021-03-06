#!/usr/bin/env python3

'''gameplay.py -- Responsible for main loop as well as initializing
all of the game data and acting as a Finite State Machine'''

import sys
import movement as M
import clearScreen as CS
import getChar as gC
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
levelNumber = 1 

Win_or_Unix = 0 #0 is unix 1 is windows
gameOver = 0 #when the game is over value set to 1
option = -1

while gameOver == 0:      #this is the game loop
    if option == -1:
        Win_or_Unix = CS.checkOs()
        option = 0

    if option == 0:
        CS.clearScreen(Win_or_Unix)
        print("Theseus and the Minotaur\nGet to the exit to win. \nHe gets 2 moves for every one of yours. \nUse w-a-s-d to navigate. Press q at anytime to quit \nand r at anytime to restart the level. \nPress b to begin. \n")
        selection = gC.getChar(Win_or_Unix)
        if selection == 'b':
            option = 1
            CS.clearScreen(Win_or_Unix)
        elif selection == 'q':
            gameOver =1
            break
        else:
            option = 0

    if option == 1:
        level, theseusX, theseusY, minotaurX, minotaurY = M.level_check(levelNumber)
        myMap = M.make_list(level)
        myString =M.map_list(myMap, theseusX, theseusY, theseusXprev, theseusYprev, minotaurX, minotaurY)
        CS.clearScreen(Win_or_Unix)
        M.displayMap(myMap)
        option = 2

    if option == 2:
        #direction =input("theseusX: ")
        direction = gC.getChar(Win_or_Unix)
        theseusXprev = theseusX
        theseusYprev = theseusY
        if direction == 'd':
            theseusX += 1
        if direction == 'a':
            theseusX -= 1
        if direction == 'w':
            theseusY -= 1
        if direction == 's':
            theseusY +=1
        if direction == 'q':
            gameOver = 1
            break
        if direction == 'n':
            levelNumber = 1
            option = 1
        if direction == 'r':
            option = 1
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
        CS.clearScreen(Win_or_Unix)
        myString = M.map_list(myMap, theseusX, theseusY, theseusXprev, theseusYprev, minotaurX, minotaurY)
        M.displayMap(myString)
        if(theseusX == minotaurX and theseusY == minotaurY):
            option = 3
        if(theseusX == 32 and theseusY == 8):
            option = 4

    if option == 3:
        CS.clearScreen(Win_or_Unix)
        print("Game Over \nPress n for a new game,\n      q to quit the game,\n    or r (to cheat) and restart the level")
        selection =  gC.getChar(Win_or_Unix)
        if selection == 'n':
            levelNumber = 1
            option = 0
        elif selection == 'r':
            option = 1
        elif selection == 'q':
            gameOver = 1
            break
        else:
            option = 3


    if option == 4:
        CS.clearScreen(Win_or_Unix)
        print("You Win!\n")
        if levelNumber == 6:
            print("You have beat all of our levels! \n")
            print("\nCONGRATULATIONS YOU ARE A \n")
            print("\nTHESEUS AND MINOTAUR MASTER \n")
            print("\nPress r to reset or q to quit the game \n")
        else:
            print("Press n to continue to the next level\n")
        selection = gC.getChar(Win_or_Unix)
        if selection == 'r':
            option = 0
            levelNumber=1
        elif selection == 'n' and levelNumber !=6:
            levelNumber += 1
            option = 1
        elif selection == 'q':
            gameOver = 1
            break
        else:
            option = 4
CS.clearScreen(Win_or_Unix)
