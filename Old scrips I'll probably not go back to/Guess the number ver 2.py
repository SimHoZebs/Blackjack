# -*- coding: utf-8 -*-
"""
Created on Sat Feb  9 16:41:35 2019

@author: Zebs
"""

import random

num = random.randint(1, 100)
list1 = []
list1_counter = 0
num_detector = "0123456789"
is_string = 0

guess = input("Guess a number from 1 to 100 until you get it right.\nYour input: ")

def error_prevention():
    global difference
    global is_string
    global guess
    
    while type(guess) != int:
        for alphabet in guess:
            if alphabet not in num_detector:
                is_string += 1
                
        if is_string > 0:
            guess = input("A number, dipshit.\nTry again: ")
            
        elif int(guess) > 100 or int(guess) < 1:
            guess = input("From 1 to 100, dipshit.\nTry again:")            
        else:
            guess = int(guess)
            difference = abs(num - guess)
            break
        is_string = 0

#First guess        
error_prevention()

if guess != num:
    list1.append(guess)
    if difference < 50:
        if difference <= 10:
            print("HOT!")
        else:
            print("Warm...")
    else:
        print("Cold...")
else:
    print("Jesus christ, you got it in one go.")
  
#Consecutive guesses
while guess != num:
    guess = input("Guess again: ")
    error_prevention()
    list1.append(guess)

    """
    #Debugging prints
    print("\nRandom number:", num)
    print("Difference:", difference)
    print("Last number:", list1[list1_counter])
    print("Previous difference:", abs(num - list1[list1_counter]))
    """
    
    if guess == num:
        print(f"You got it! In {len(list1)} attempts!")
        
    elif num == list1[list1_counter]:
        print("You already said that number.")
        
    elif difference < abs(num - list1[list1_counter]):
        if difference <= 10:
            print("Hotter...")
        elif difference >= 50:
            print("Warmer but still cold...")
        else:
            print("Warmer...")
            
    else:
        if difference >= 50:
            print("Chilly af boi")
        elif difference <= 10:
            print("Colder but still hot...")
        else:
            print("Colder...")
    list1_counter += 1