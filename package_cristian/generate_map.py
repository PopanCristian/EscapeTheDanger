import random
import pandas as pd

def generate_start_point(size_map):
    """
    This function will generate a random start point for the game. The start point will be somewhere on the edges
    :param size_map: the size of the map
    :return:  a tuple that contains coordinates for start point
    """
    coord_x = random.randint(0, size_map-1)  # for X coordinate I can randomize from 0 -> size_map-1

    if coord_x == 0 or coord_x == size_map-1:  # for Y coordinate in function of X coordinate, so :
        # if X == 0 | X == size_map means first and last line Y can ba random from 1-size_map
        coord_y = random.randint(0, size_map-1)
    else:
        # if X have a value from (0,size_map) interval, Y will be a random value between 0 and size_map-1 values.
        coord_y = random.choice([0, size_map-1])

    return (coord_x, coord_y)

def get_obstacles_from_csv(file_path):
    """
    :param file_path: path to csv file
    :return: dataframe just with names
    """

    df = pd.read_csv(file_path)

    return [
        {obstacle_name: dmg_obstacle}
            for obstacle_name, dmg_obstacle in zip(df['Nume posibilitate'], df['Valoare posibilitate'])
    ]

def fill_map_function(size_map, matrix_map, start_point_tuple, finish_point_tuple, list_with_obstacles,difficulty):
    """
    Description : fill our empty map with elements
    :param size_map: dimension got from user
    :param matrix_map: the empty map
    :param start_point_tuple: starting point
    :param finish_point_tuple: finish point
    :param list_with_obstacles: list with multiple dictionaries with obstacle names and dmg
    :param difficulty: difficulty got from user
    :return: a filled map with obstacles
    """
    for row in range(size_map):
        for column in range(size_map):
            if (row, column) == start_point_tuple:  # if we get the starting point will mark in our map
                matrix_map[row][column] = 'S'
            elif (row, column) == finish_point_tuple:  # if we get the finish point will mark in our map
                matrix_map[row][column] = 'F'
            else:  # else we put a random obstacle with a value depending on user difficulty request
                random_obstacle = random.choice(list_with_obstacles)
                (obstacle_name, obstacle_value), = random_obstacle.items()
                matrix_map[row][column] = {obstacle_name: obstacle_value * difficulty}
    return matrix_map

def gen_random_map(size_map, difficulty):
    """
    This function will generate a random map with size and difficulty given by user with start and finish points and obstacles
    :param size_map: size of the map
    :return: A list that represent the map
    """
    matrix_map = [[{} for _ in range(size_map)] for _ in range(size_map)] # create an empty map
    # Each element represent a dictionary "key_name_obstacle" : value_obstacle
    # print(matrix_map)

    start_point_tuple = generate_start_point(size_map)  # starting point
    finish_point_tuple = (random.randint(0, size_map-1), random.randint(0, size_map-1))  # The finish point(home) will
    # be a random point from the map

    obstacles = get_obstacles_from_csv("obstacles.csv")  # list with dictionaries
    # that contains names of obstacles with dmg
    # print(obstacles)

    matrix_map = fill_map_function(size_map, matrix_map, start_point_tuple, finish_point_tuple, obstacles,difficulty)

    for row in matrix_map:
        print(row)

    # print(get_diff_from_csv("obstacles.csv",difficulty))

