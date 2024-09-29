"""

Create a program that will draw a crazy pattern using the turtle.

Create lists for the path that Tina will take, the angles 
she will turn, and the colors she will use. The access those
lists to draw the pattern.

hint: all of your lists should have the same number of elements.
Review the ' Using Lists' section of the previous lesson if you need 
more help

"""


import turtle, random                           # Tell Python we want to work with the turtle
turtle.setup (width=600, height=600)    # Set the size of the window

tina = turtle.Turtle()                  # Create a turtle named tina

tina.shape('turtle')                    # Set the shape of the turtle to a turtle
tina.speed(0)                           # Make the turtle move as fast, but not too fast. 

tina.goto(0,0)

colors = [ 'red', 'orange', 'yellow', 'green', 'blue', 'purple' ]

for  i in range(100000):

    forward = random.randint(-100, 100)
    left = random.randint(-100, 100)
    color = colors[random.randint(0,5)]


    tina.color(color)
    tina.goto(forward, left)
    if i == 100:
        tina.goto(0,0)
    elif i == 200:
        tina.goto(0,0)
    elif i == 300:
        tina.goto(0,0)
    elif i == 400:
        tina.goto(0,0)
    elif i == 500:
        tina.goto(0,0)
    elif i == 600:
        tina.goto(0,0)
    elif i == 700:
        tina.goto(0,0)
    elif i == 800:
        tina.goto(0,0)
    elif i == 900:
        tina.goto(0,0)
    elif i == 1000:
        tina.goto(0,0)
turtle.exitonclick()  

