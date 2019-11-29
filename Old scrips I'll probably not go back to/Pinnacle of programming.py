import turtle
t = turtle.Turtle()
turtle.speed(1)

s = 0

def yeet():
    re = int(input("Type 1 to repeat & 2 to end: "))
    global s
    if re == 1:
        t.right(180)
        t.fd((11/2)*x)
        t.right(90)
        t.fd(x)
        t.clear()
        t.right(180)
        s = 0
    elif re == 2:
        s = 1

y = turtle.textinput("", "What's your name?: ")
t.write("A " + str(len(y)) + " character long name, how stupid. Whatever though.")

while 1:
    if s == 0:
        t.right(180)
        a = turtle.textinput("", "How big: ")
        t.clear()
        x = int(a)
        t.circle(x)
        t.left(180)
        t.circle(-x, 90)
        t.right(180)
        t.fd(5*x)
        t.circle(-x, 180)
        t.fd(5*x)
        t.circle(x)
        t.right(90)
        t.fd(2*x)
        t.right(90)
        t.fd(5*x)
        t.circle(-x,90)
        t.right(90)
        t.fd((1/2)*x)
        t.write("This is your dick, %s." %y)
        yeet()
        #Weirdly, the code above runs the function yeet() in order to
        #find the value of it without me directly asking it to find the value.
        #What if yeet() doesn't produce a value?
    else:
        break
