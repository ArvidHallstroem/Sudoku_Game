
def compute(ROW, WIDTH):
    cellsize = WIDTH / ROW
    X_CONST = - WIDTH / 2
    if ROW % 2 == 0:
        Y_CONST = 255
        y_pantry = -155
    else:
        Y_CONST = (248
                   - cellsize)
        y_pantry = -180

    pantry = []
    x,y = (X_CONST + cellsize / 2,y_pantry - cellsize / 2)
    for i in range(ROW):
        pantry.append((x,y))
        x += cellsize

    locs = []
    if ROW % 2 == 0:
        y = Y_CONST - cellsize / 2
    else:
        y = Y_CONST + cellsize
    for a in range(ROW):
        temp = []
        x = X_CONST + cellsize / 2
        for b in range(ROW):
            temp.append((x,y))
            x += cellsize
        y -= cellsize
        locs.append(temp)

    cell_occupied = []
    for y in range(ROW):
        temp_cell = []
        for x in range(ROW):
            temp_cell.append(0)
        cell_occupied.append(temp_cell)
    return pantry, locs, cell_occupied, cellsize