from Zebsential import Debug

"""
From 1 to 20, try to divide them by numbers starting from 2
to the largest number in the list A.
If any number can be divided:
   add that divider to a list B
   then divide the ones that can be divided.
   Leave the numbers that can't be divided the way they are.

"""
list_a = [num for num in range(1, 21)]

for num in list_a:
    for divider in range(2, 21):
        product = num % divider
