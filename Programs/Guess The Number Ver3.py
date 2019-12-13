# -*- coding: utf-8 -*-
"""
Created on Sat Feb  9 16:41:35 2019

@author: Zebs
"""

import random



def error_prevention():
    global guess
    global is_string
    is_string = True
    
    while is_string:
        try:
            guess = int(guess)
        except ValueError:
            guess = input('A number, dipshit.\nTry again:')
            continue
        
        if int(guess) > 100 or int(guess) < 1:
            guess = input("From 1 to 100, dipshit. \nTry again:")
            continue
        else:
            guess = int(guess)
            is_string = False

num = 40
list1 = []
list1_counter = 0

#First guess
guess = input("Guess a number from 1 to 100 until you get it right.\nYour input: ")
        
error_prevention()

difference = abs(num - guess)

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

    
    #Debugging prints
    print("\nRandom number:", num)
    print("Difference:", difference)
    print("Last number:", list1[list1_counter])
    print("Previous difference:", abs(num - list1[list1_counter]))
    
    
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