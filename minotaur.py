#!/usr/bin/env python3
def minotaurNextLocation(map,theseusX, theseusY, minotaurX, minotaurY):
    if minotaurX < theseusX and map[(minotaurX + 1)+ minotaurY*41] != '0':
        map[(minotaurX)+minotaurY*41] = ' '
        minotaurX += 1
    elif minotaurX > theseusX and map[(minotaurX - 1) + minotaurY*41] !='0':
        map[(minotaurX)+minotaurY*41] = ' '
        minotaurX -= 1
    elif minotaurY < theseusY and map[minotaurX + (minotaurY+1)*41] !='0':
        map[(minotaurX)+minotaurY*41] = ' '
        minotaurY += 1
    elif minotaurY > theseusY and map[minotaurX + (minotaurY-1)*41] !='0':
        map[(minotaurX)+minotaurY*41] = ' '
        minotaurY -= 1

    return minotaurX, minotaurY
