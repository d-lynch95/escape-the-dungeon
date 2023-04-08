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
        """
        This will restart the game if players arent ready to play
        """
        time.sleep(b)
        print()
        print("hmmmm")
        print("maybe this wasn't the place for you")
        time.sleep(a)
        print("another time perhaps...")   
        time.sleep(3)
        start()   

    else:
        start()  

def begin():
    """
    This function sets the scene for the players.
    """
    clearConsole()
    print("You wake up in a dark decrepid dungeon")
    time.sleep(a)
    print("Everything is shrouded in darkness")
    time.sleep(b)
    print("The dungeon is damp and slime covers the old stone walls")
    time.sleep(c)
    print("A small flame flickers across the dungeon")
    time.sleep(a)
    print("You try to move")
    time.sleep(b)
    print("Your feet have been shackled together")
    time.sleep(a)
    option1 = input("What will you do? Try to 'move' or 'stay' where you are?  ").lower().strip()
    print()

    if option1 == "move":
        #take player to firstMove()
        firstMove()
        

    elif option1 == "stay":
        #resets the game if the player opts to stay 
        time.sleep(a)
        print("Nothing happens")
        print()
        print("Your eyes start to close")
        print()
        time.sleep(b)
        print("Your body aches as you slowly drift into a slumber")
        time.sleep(c)
        begin()

    else:
        # if player hits the wrong button the game resets
        begin()

def firstMove():
    # This function allows the player to move across the room
    print("You try to move")
    print()
    time.sleep(a)
    print("Your body aches but you manage to stand")
    print()
    time.sleep(a)
    print("You shuffle across the floor towards the light")
    print()
    time.sleep(a)
    print("Your shackles clink as you make your way across the room")
    print()
    time.sleep(b)
    print("The light grows brighter")
    print()
    print()
    print("There is a torch on the wall")
    print()
    time.sleep(a)
    option2a = input("Do you 'take' it or 'stay' where you are?  ").lower().strip()

    if option2a == 'take':
        # take user to take function to progress the story line
        take()

    elif option2a == 'stay':
        # this function will take the player to the take function.
        print()
        print("You stand by the torch")
        print()
        time.sleep(a)
        print("The warmth of the torch is alluring")
        print()
        time.sleep(b)
        print("You reach out and take the torch")
        print()
        time.sleep(a)
        take()
    else:
        firstMove()

def take():
    # this function allows the user to take the torch and decide to stay or move
    print()
    time.sleep(a)
    print("You take the torch from it's sconce")
    print()
    print("You wave the torch and the room illuminates")
    print()
    time.sleep(b)
    print("The dungeon is grimy and damp")
    print("but you can only see half of it")
    time.sleep(b)
    print()
    option3 = input("Do you want to 'search' the dungeon or 'stay' where you are?  ").lower().strip()
    print()

    if option3 == 'search':
        # take user to the search function
        search()

    elif option3 == 'stay':
        # this function gives players a second chance to search or wait
        print("You stay where you are")
        print()
        time.sleep(a)
        print("The torch continues to burn")
        time.sleep(a)
        print()
        wait = input("Do you 'search' the room or 'wait' where you are?  ").lower().strip()

        if wait == 'search':
            #take the user to the search function
            search()
        
        elif wait == 'wait':
            # if the player chooses this option the game will end
            print()
            time.sleep(a)
            print("You wait where you are")
            time.sleep(a)
            print()
            print()
            print("Nothing happens")
            time.sleep(b)
            print()
            print("The torch slowly burns out")
            time.sleep(b)
            print()
            print("You are thrust into darkness")
            time.sleep(b)
            print()
            print("GAME OVER")
            print()
            time.sleep(c)
            start()

        else:
            take()

def search():
    # this function allows the player to search the room
    print("You shuffle across the room")
    print()
    time.sleep(a)
    print("The torch provides an ark of light in front of you")
    print()
    time.sleep(a)
    print("You reach the far wall and follow it around the near empty room")
    print()
    time.sleep(a)
    print("You come across a set of keys on the wall")
    print()
    keys = input("Do you 'take' them or 'leave' them?  ")

    if keys == 'take':
        #take users to the keyWest function to progress the storyline
        keyWest()

    elif keys == 'leave':
        print()
        time.sleep(a)
        print("You leave the keys on the wall")
        print()
        print()
        print()
        time.sleep(b)
        print("Are you sure you don't want to take those keys?")
        key2 = input("Do you take the keys?   Y/N ").lower().strip()
        if key2 == 'y':
            keyWest()
        elif key2 == 'n':
            print()
            print("You leave the keys where they are")
            time.sleep(a)
            print("Why would you do that?")
            time.sleep(b)
            print("GAME OVER")
            time.sleep(c)
            start()

        print()


    else:
        print("potato")

def keyWest(): 
    print()
    print("You take the keys and crouch down")
    print()
    time.sleep(a)
    print()
    print("There are three keys on the key chain")
    print()
    time.sleep(a)
    print()
    print("You try the first key")
    time.sleep(b)
    print()
    print("nothing")
    print()
    time.sleep(a)
    print("You try the second key")
    print()
    time.sleep(b)
    print("Nothing")
    print()
    time.sleep(b)
    print()
    print("You try the final key")
    print()
    time.sleep(c)
    print()
    print("SUCCESS")
    time.sleep(b)
    print("You hear the lock click and the shackles spring off your feet")
    print()
    time.sleep(b)
    print("It feels good to be partly free")

start()