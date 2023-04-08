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
    print()
    name = input("Insert Username here: ")
    print()
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
        print()
        time.sleep(a)
        begin()

    elif ready == "n":
        time.sleep(b)
        print()
        print("hmmmm")
        print("maybe this wasn't the place for you")
        time.sleep(a)
        print("another time perhaps...")   
        time.sleep(3)
        start()     

def begin():
    clearConsole()
    print("You wake up in a dark decrepid dungeon")
    time.sleep(a)
    print("Everything is shrouded in darkness")
    time.sleep(b)
    print("The dungeon is damp and slime covers the old stone walls")
    time.sleep(c)
    print("a small flame flickers across the dungeon")
    time.sleep(a)
    print("You try to move")
    time.sleep(b)
    print("your feet have been shackled together")
    time.sleep(a)
    option1 = input("What will you do? Try to 'move' or 'stay' where you are?  ")



start()