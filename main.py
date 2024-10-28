from time import sleep
from colorama import Fore
from package_cristian.generate_map import *
from package_andreea.game_steps import *
from package_marina.start_the_game import *
if __name__ == '__main__':
    print("Hello there !")
    # sleep(1)
    print("You have been to mechanic and your car have only 90 % health\n"
          "Drive safe to your home. You can follow a clean way to your house or you can choose to follow a adventure "
          "way until there. ")
    # sleep(6)
    print("Depending on the obstacles you overcome, your car’s health will decrease. When your car is below "
          "10% health, you are no longer able to drive the car.\nYou can only use" + Fore.RED+ " up, down, left, right "
          "commands" + Fore.RESET + " to change the direction till home !\n F is your home destionation !\n Drive safe buddy !")

    difficulty = input("Choose the difficulty (1 : standard, 2 : medium , 3 : hard). Type down just the number:")
    dim_map = input("The map will be a square. Choose your size:")  # get the input from the user to generate the map
    car_life = 90  # how much life user's car gets from the beginning
    matrix_map = gen_random_map(int(dim_map),int(difficulty))  # generate the map

    if matrix_map == 666:  # when I generate a random map and get the code '666', the user get our 'Easter egg'
        print("It's your lucky day ! The mechanic it's your next-neighbour and you are already home !")
    else:  # else I got a correct map
        print("Aici este mapa :")
        for row in matrix_map:
            print(row)
        for row in range(len(matrix_map)):  # search the starting and finish points
            for column in range(len(matrix_map)):
                if matrix_map[row][column] == 'S':
                    starting_point = (row, column)  # save the starting point
                    # print("Punctul de start este ", starting_point)
                    path = add_step_to_queue(matrix_map[row][column])  # save the starting point in user's path
                elif matrix_map[row][column] == 'F':
                    finish_point = (row, column)  # save the finish point

        current_position = starting_point  # current position will be a tuple
        end_game = task6_end_game(current_position, car_life, finish_point)
        while end_game == 0:  # while the user didn't end the game by the rules
            # aici trebuie sa dau pozitia curenta si da iau input de la user pentru urmatoarea miscare
            #plus sa ii afisez vecinii pozitiei curente
            list_neighbours_current_position = task1_generate_the_neighbours(matrix_map,current_position)  # get the
            # neighbours for current location

            # print("lista de vecini sub forma de tuplu este : ", list_neighbours_current_position, "\n")
            print("\nChoose your next step :")
            for (row,column) in list_neighbours_current_position:
                neighbour = matrix_map[row][column]  # acel dictionar cu o singura keye din mapa
                if row+1 == current_position[0] and column == current_position[1]:  # this means this is in nord
                    if type(neighbour) == dict:  # in our map it's possible to have or a dict or just the S and F points
                        print(list(neighbour.keys())[0], " UP")
                    else:
                        print(neighbour, " UP")
                elif row-1 == current_position[0] and column == current_position[1]:  # this means this is in sud
                    if type(neighbour) == dict:
                        print(list(neighbour.keys())[0], " DOWN")
                    else:
                        print(neighbour, " DOWN")
                elif row == current_position[0] and column-1 == current_position[1]:  # this means this is in east
                    if type(neighbour) == dict:
                        print(list(neighbour.keys())[0], " RIGHT")
                    else:
                        print(neighbour, " RIGHT")
                elif row == current_position[0] and column+1 == current_position[1]:  # this means this is in west
                    if type(neighbour) == dict:
                        print(list(neighbour.keys())[0], " LEFT")
                    else:
                        print(neighbour, " LEFT")

            direction_input_from_user = input(f"\nType down the direction you wanna follow up :").lower()  # get the input
            # from user. Transform to lower because my colleague Marina chose to work with lower case letters
            # print(direction_input_from_user)
            current_position = task2_update_position(matrix_map, current_position, direction_input_from_user)  # update
            # the position based to user's input. This is a tuple with coords
            # print("urmatorul punct este ",current_position)


            coord_row, coord_column = current_position
            current_obstacle = matrix_map[coord_row][coord_column]

            if current_obstacle == 'F':
                end_game = 1
                break

            car_life = update_car_health(car_life,matrix_map[coord_row][coord_column])  # update the car's health
            print(f"\nNow your current life is : {car_life}")  # show the car's health to the user
            print(get_random_messages(list(current_obstacle.keys())[0]))  # print a message that have a bound to
            # the obstacle
            path = add_step_to_queue(list(current_obstacle.keys())[0])  # add the position to the queue
            end_game = task6_end_game(current_position, car_life, finish_point)

        if end_game == -1:  # that means the user lost, the car's life is below 10%
            print("Game over ! Your car is broken ! Your path was : ")  # show user's path
            print(display_user_path_from_queue())
        elif end_game == 1:  # that means the user gets home
            print("\n\nCongrats, you did it buddy ! Your path was : ")
            print(display_user_path_from_queue())
