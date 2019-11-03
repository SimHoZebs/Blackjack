import turtle
t = turtle.Turtle()
t.shape("arrow")

import math

x1 = float(input("x1: "))
y1 = float(input("y1: "))
x2 = float(input("x2: "))
y2 = float(input("y2: "))

l = math.sqrt((x2 - x1)**2 + (y2 - y1)**2)
angle = ((math.acos((x2 - x1)/l))/math.pi)*180
print(angle)
print(l)

t.left(angle)
t.fd(l)
