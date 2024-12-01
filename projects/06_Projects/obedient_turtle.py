"""
Make an obedient turtle that will obey commands to draw shapes.
"""

import turtle
from tkinter import messagebox, simpledialog, Tk

window = Tk()
window.withdraw()
# TODO)
#   1. Create a turtle.

turtle.setup(width=600, height=600)
t = turtle.Turtle()


#   2. Write 3 function definitions for drawing a square, triangle, and
#      circle.
def square():
    for i in range(4):
        t.forward(100)
        t.right(90)

def circle():
    t.circle(radius=100)

def triangle():
    for i in range(3):
        t.forward(100)
        t.left(120)

#   3. Ask the user for the for a shape to draw.

Shaaapeee = simpledialog.askstring(title='Shape', prompt='Would you like a square, triangle, or a circle')
if Shaaapeee == 'square':
    y = square()
if Shaaapeee == 'triangle':
    y = triangle()
if Shaaapeee == 'circle':
    y = circle()

#   4. Draw the appropriate shape depending on their answer (call the right
#      function)
turtle.exitonclick() 
pass
