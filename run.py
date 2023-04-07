# Your code goes here.
# You can delete these comments, but do not change the name of this file
# Write your code to expect a terminal of 80 characters wide and 24 rows high

import time
import random
import os

a = 1
b = 2
c = 3

def clearConsole():
    """
    Clears the console.
    """
    os.system('cls' if os.name == 'nt' else 'clear')

def start():
    """
    This is the standard introduction for all players.
    Users will understand the purpose of the game and input their name.
    """
    clearConsole()
    print("Welcome to the dungeon")
    time.sleep(a)
    print("Can you escape in one piece?")
    time.sleep(a)
    print("What is your name?")
    time.sleep(a)
    print("We'll need to write something on your gravestone")
    time.sleep(a)
    name = input("Insert Username here: ")
    print("Best of luck " + name)
    print()
    time.sleep(a)
    print("...you'll need it")
    print()
    print()
    time.sleep(a)
    ready = input("Are you ready to begin? Y/N ").lower().strip()

    if ready == "y":
        """
        This will start the game for the player using begin() function
        """
        time.sleep(a)
        print()
        print()
        print("See you on the other side " + name)
        begin()

    elif ready == "n":
        time.sleep(b)
        print("hmmmm")
        print("maybe this wasn't the place for you")
        time.sleep(a)
        print("another time perhaps...")   
        time.sleep(3)
        start()     




start()