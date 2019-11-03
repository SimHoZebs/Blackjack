import turtle
colors = ["red", "purple", "blue", "green", "yellow", "orange"]
#^ Creating a list
t = turtle.Turtle()

turtle.bgcolor("black")
t.speed(0.1)
t.width(3)
length = 10

while length < 10000:
    print(length)
    t.forward(length)
    t.pencolor(colors[length%6])
    #^ The combination of length += 1 and length%6 allows
    # a continous loop of 6 variables. Pretty smart.
    t.right(91)
    length += 100


