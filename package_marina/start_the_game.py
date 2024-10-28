
#Task1: a function that has as paramteres a matrix and point as a tuple
def task1_generate_the_neighbours(matrix, point):
    """

    :param matrix: the lenght of the matrix
    :param point: tuple
    :return: the list of neighbours
    """
    rows = cols = len(matrix)#generate the dimensions of the matrix
    i, j = point
    neighbours = [] #the list of neighbours
    if i + 1 < rows: #condition to verify the south point
        neighbours.append((i + 1, j))
    if j - 1 >= 0: #west point
        neighbours.append((i, j - 1))
    if j + 1 < cols:#east point
        neighbours.append((i, j + 1))
    if i - 1 >= 0: #nord
        neighbours.append((i - 1, j))
    return neighbours

# task 2: creating a function that has as parameters initial position and a value which is the key
# pressed by user
def task2_update_position(matrix, position, key):
    """

    :param matrix: the lenght of the matrix
    :param position: any position from matrix
    :param key:string
    :return: the positions
    """
    i , j = position #define the positions
    rows = cols = len(matrix)
    if key ==  "up" and int(i) - 1 >= 0:  # to the nord
        i -= 1
    elif key == "down" and i + 1 < rows:  # to the south
        i += 1
    elif key == "left" and j - 1 >= 0:  # to the west
        j -= 1
    elif key == "right" and j + 1 <= cols:  # to the east
        j += 1
    return (i, j)

# Task6: creating a def end of the game with parameters initial positions, cars life and final destination

def task6_end_game(init_pos, cars_life, final_destination):
    """

    :param init_pos: tuple
    :param cars_life: car's life below 10
    :param final_destination: verify if final_destination is equal to init_pos
    :return: 0
    """
    if cars_life <10:
        return -1
    elif init_pos == final_destination:
        return 1
    else: #verify if none of the conditions are accomplished
        return 0
