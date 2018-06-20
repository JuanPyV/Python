park = [[1, 0, 1, 0, 1, 1, 1, 1, 0, 1, 0, 1, 1, 0, 1],
        [0, 1, 0, 0, 0, 1, 1, 1, 0, 1, 0, 1, 0, 1, 1],
        [0, 1, 1, 1, 1, 1, 1, 1, 1, 0, 1, 0, 1, 1, 1],
        [1, 0, 1, 0, 1, 1, 1, 1, 0, 1, 0, 1, 1, 0, 1],
        [0, 1, 0, 0, 0, 1, 1, 1, 0, 1, 0, 1, 0, 1, 1],
        [0, 1, 1, 1, 1, 1, 1, 1, 1, 0, 1, 0, 1, 1, 1],
        [0, 1, 1, 1, 1, 1, 1, 1, 1, 0, 1, 0, 1, 1, 1],
        [1, 0, 1, 0, 1, 1, 1, 1, 0, 1, 0, 1, 1, 0, 1],
        [0, 1, 0, 0, 0, 1, 1, 1, 0, 1, 0, 1, 0, 1, 1],
        [0, 1, 1, 1, 1, 1, 1, 1, 1, 0, 1, 0, 1, 1, 1]]


def vacios(sensors):
    free_spaces = []
    positions = ['a','b','c','d','e','f','g','h','i','j',]
    for pos,row in enumerate(sensors):
        for pos2,status in enumerate(row):
            if(int(status)==0):
                for pos3,row3 in enumerate(positions):
                    current = positions[pos]
                    current +=str(pos2)
                free_spaces.append(current)
    return(free_spaces)

print(vacios(park))