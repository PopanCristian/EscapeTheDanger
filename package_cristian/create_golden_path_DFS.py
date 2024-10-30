def depth_first_search(matrix_map, row_coord_x, column_coord_y, visited_set, path_list, finish):
    """
    Description : God knows what the f I did here
    :param matrix_map: the filled map
    :param row_coord_x: starting row
    :param column_coord_y: starting column
    :param visited_set: contains the visited location
    :param path_list: " golden path "
    :param finish: finish point
    :return: true or false, true if we found a golden path, false if we not found
    """
    if not (0 <= row_coord_x < len(matrix_map) and 0 <= column_coord_y < len(matrix_map[0])):  # when I'm out of map's
        # limits or when I try to visit a location that is outside of map
        return False

    if (row_coord_x,column_coord_y) == finish:
        path_list.append((row_coord_x,column_coord_y))
        return True  # if we got to the finish point return 1 for making there

    visited_set.add((row_coord_x, column_coord_y))  # marked the position where we are

    directions = [(-1,0),(1,0),(0,-1),(0,1)]  # the neighbours for the current position

    for direction_row,direction_column in directions:  # for each new location

        new_direction_row,new_direction_column = row_coord_x+direction_row, column_coord_y + direction_column

        if( 0 <= new_direction_row <= len(matrix_map) and 0 <= new_direction_column <= len(matrix_map)
        and (new_direction_row, new_direction_column) not in visited_set):  # verify if you are in map limits and you
            # have not been here

            path_list.append((row_coord_x,column_coord_y))  # add the new location to our "golden path " to finish point

            if matrix_map[row_coord_x][column_coord_y] != 'S' and matrix_map[row_coord_x][column_coord_y] != 'F':
                matrix_map[row_coord_x][column_coord_y] = {"free road": 0}  # change the obstacle with free way

            if depth_first_search(matrix_map, new_direction_row, new_direction_column, visited_set, path_list, finish):
                return True

            path_list.pop()

    return False  # impossible here but to catch any possible error

def find_path(matrix_map, start, finish):
    """
    Description: This function find a golden path using depth first searching algorithm from depth_first_search funct
    :param matrix_map: the filled map with obstacles
    :param start: starting point
    :param finish: finish point
    :return: the same map just with a "golden path". Each obstacle was replaces with "free way"
    """
    visited_set = set()
    path = []
    depth_first_search(matrix_map, start[0], start[1], visited_set, path, finish)

    return matrix_map

