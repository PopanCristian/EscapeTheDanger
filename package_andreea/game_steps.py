import random
import queue
import pandas as pd

def get_random_messages(road_choice):
    """
    This function will take a random message associated with a chosen obstacle from a csv file
    :param road_choice: The name of the obstacle
    :return: A random message associated with the obstacle or an error message
    """
    df = pd.read_csv("obstacles.csv") #Read the csv file
    row = df[df['Nume posibilitate'] == road_choice] #Search for the row that corresponds to the user's choice

    #Check if the row is not empty
    if not row.empty:
        messages = eval(row['Mesaje'].values[0]) #Use eval to obtain the list of messages
        return random.choice(messages) #Choose a random message from the list
    else:
        return "Unknown road, please try another option"


def update_car_health(health, obstacle_dict):
    """
    This function will update the health of the car
    :param health: The current health of the car
    :param obstacle_dict: A dictionary containing a single key and a single value
    :return: The updated health of the car
    """
    updated_health = health #Initialize updated_health with the current health
    #Iterate over the key-value pairs in the obstacle dictionary
    if obstacle_dict == 'S':
        return updated_health
    for key, value in obstacle_dict.items():
        obstacle_value = value #Get the value of the obstacle

        updated_health = health + obstacle_value #Update the car's health
        #Check if the updated health exceeds the maximum limit of 100
        if updated_health > 100:
            updated_health = 100

    return updated_health


user_path_queue = queue.Queue() #Create an empty queue to record the user's steps
#Function to add each user's step to the queue
def add_step_to_queue(road_choice):
    """
    This function adds the user's chosen road step to the path queue
    :param road_choice: The road chosen
    """
    user_path_queue.put(road_choice) #Add the step to the queue

def display_user_path_from_queue():
    """
    This function will display the user path from the queue
    """
    while not user_path_queue.empty():
        print("\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t"+user_path_queue.get()) #Display each step the user has taken

        if user_path_queue.empty():  # when our queue is empty we will get None
            return ""   # so we cheat a little bit :d