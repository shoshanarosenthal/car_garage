import os
import platform
import json
from colorama import Fore, Back, Style
from enum import Enum

class Action (Enum):
    ADD = 1
    PRINT = 2
    DELETE = 3
    EXIT = 4
    SEARCH = 5
Cars=[]
FILE_NAME = "car_list.txt"
def clear_screen():
    if platform.system() == "Windows":
        os.system('cls')
    else:
        os.system('clear')

def save_cars_to_file ():    
    with open(FILE_NAME, "w") as f:
            # f.write(str((Cars)) )
          json.dump(Cars, f, indent=4)    
print( Fore. YELLOW + "car added successfully" + Style.RESET_ALL)

def load_cars_from_file(FILE_NAME):
    global Cars
    try:
        with open(FILE_NAME, "r") as f:
            Cars = json.load(f)
    except FileNotFoundError:
            Cars = []

def menu():
    for act in Action: print ( Fore.BLUE + f"{act.value}-{act.name}" + Style.RESET_ALL)
    return input( Back.WHITE+ "what do you want to do?" + Style.RESET_ALL)

def add_car_to_list():
    Cars.append({"model": input("model?"),"brand": input("brand?"),"color": input("color?")})
    save_cars_to_file ()



def show_all_cars ():
    if not Cars:
        print(Fore.RED + "No cars found!" + Style.RESET_ALL)
    else:
        for i, car in enumerate(Cars, start=1):
            print(Fore.GREEN + f"{i}. Model: {car['model']}, Brand: {car['brand']}, Color: {car['color']}" + Style.RESET_ALL)



if __name__ == "__main__":
    user_selection=""
    load_cars_from_file()

    while True:
        user_selection = Action(int(menu()))
        clear_screen()

        if user_selection == Action.EXIT : exit()
        elif user_selection == Action.ADD: add_car_to_list()
        elif user_selection == Action.DELETE: pass
        elif user_selection == Action.PRINT: show_all_cars ()
        elif user_selection == Action.SEARCH: pass
