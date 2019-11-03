x = int(input("Enter an integer: "))

num1 = x%10             #Get first place. (1234, gets 4)
print(num1)
final = num1            #Got first place. (4)
print(final)
num1 = x//10            #Get second place. (123)
print(num1)
while num1 >=10:    #While second and other places are mixed, (true)
    num2 = num1%10     #Got the second place. (123%10 = 3)
    print("Next place:", num2)
    final += num2       #First + second (4 + 3)
    print(final)
    num1 //= 10         #Get third place. (123//10 = 12)
    print(num1, "end of loop")

print("Last place:", num1)
final += num1

print(final)
