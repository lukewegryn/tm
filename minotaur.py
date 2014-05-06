def minotaurNextLocation(map,theseusX, theseusY, minotaurX, minotaurY):
    if minotaurX < theseusX and map[minotaurX + 1, minotaurY] != '0':
        minotaurX += 1
    elif minotaurX > theseusX and map[minotaurX - 1, minotaurY] !='0':
        minotaurX -= 1
    elif minotaurY < theseusY and map[minotaurX, minotaurY+1] !='0':
        minotaurY += 1
    elif minotaurY > theseusY and map[minotaurX, minotaurY-1] !='0':
        minotaurY -= 1
