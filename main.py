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
          "keyboards" + Fore.RESET + " to move to your home !\n Drive safe buddy !")

    difficulty = input("Choose the difficulty (1 : standard, 2 : medium , 3 : hard). Type down just the number:")
    dim_map = input("The map will be a square. Choose your size:")  # get the input from the user to generate the map
    car_life = 90
    matrix_map = gen_random_map(int(dim_map),int(difficulty))  # generate the map

    for row in range(len(matrix_map)):
        for column in range(len(matrix_map)):
            if matrix_map[row][column] == 'S':
                starting_point = (row, column)  # save the starting point
                path = add_step_to_queue(matrix_map[row][column])  # save the starting point in user's path
            elif matrix_map[row][column] == 'F':
                finish_point = (row, column)  # save the finish point
    end_game = task6_end_game(starting_point, car_life, finish_point)
    while end_game == 0:  # while the user didn't end the game by the rules
        break



