num1 = float(input("x: "))
num2 = float(input("y: "))

print("Sum of two numbers:", num1 + num2)
print("Difference of two numbers:", num1 - num2)
print("Mutliplication of two numbers:", num1*num2)
print("Average of two numbers:", (num1 + num2)/2)
if num1 != num2:
    print("Bigger number:", max(num1, num2))
    print("Smaller number:", min(num1, num2))
else:
    print("Both numbers are equal to each other.")
