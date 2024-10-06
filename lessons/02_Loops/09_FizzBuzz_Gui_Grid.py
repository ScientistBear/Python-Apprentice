"""Fizzbuzz Grid

We're going to use a Windowing library, guizero, to create a 10x10 grid of
numbers, with each number in a separate cell, but we're also going to set the
color of the number based on the following rules:

* If the number is evenly divisible by 5, print '🦡'
* If the number is evenly divisible by 3, print '🍄'
* If the number is evenly divisible by 15, print '🐍'
* If it is divisible by neither, print the number.

Additionally, If you are displaying a number  color the numbers as follows:

* If the sum of the digits of the number is even, color the number blue
* If the sum of the digits of the number is odd, color the number red

Here is how you can display a number in your grid. Call this function in your loop
to display the number in the grid cell at the row and column you specify.

    Text(app, text=str(number), grid=[col, row], color=color)

Or to display a badger: 
    
    Text(app, text='🦡', grid=[col, row], color=color)

HINT: You can use % and // to get the first and last digit of a number, 
our you can convert the number to a string and iterate over the digits

"""
from guizero import App, Box, Text

app = App("Numbers Grid", layout="grid")
# Create a 10x10 grid using nested loops

# Or you can use a single loop and calculate the row and column

# In the loop, calculate or increment the number
# Use % determing the display, using fizzbuzz rules
r = 0
s = 0
f = 0


ae = [(0,0), (0,1), (0,2), (0,3), (0,4), (0,5), (0,6), (0,7), (0,8), (0,9), (1,0), (1,1), (1,2), (1,3), (1,4), (1,5), (1,6), (1,7), (1,8), (1,9), (2,0), (2,1), (2,2), (2,3), (2,4), (2,5), (2,6), (2,7), (2,8), (2,9), (3,0), (3,1), (3,2), (3,3), (3,4), (3,5), (3,6), (3,7), (3,8), (3,9), (4,0), (4,1), (4,2), (4,3), (4,4), (4,5), (4,6), (4,7), (4,8), (4,9), (5,0), (5,1), (5,2), (5,3), (5,4), (5,5), (5,6), (5,7), (5,8), (5,9), (6,0), (6,1), (6,2), (6,3), (6,4) ,(6,5), (6,6), (6,7), (6,8), (6,9), (7,0), (7,1), (7,2), (7,3), (7,4) ,(7,5) ,(7,6), (7,7), (7,8), (7,9), (8,0), (8,1), (8,2), (8,3), (8,4), (8,5), (8,6), (8,7), (8,8), (8,9), (9,0), (9,1), (9,2) ,(9,3), (9,4), (9,5), (9,6), (9,7), (9,8), (9,9)]
# If you are displaying a number, calculate the sum of the digits and determine the color
for e in range(100): # Change only this line
    
    if e % 15 == 0:
        r + 1
        Text(app, text=str(1), grid=ae[r], color='black')
    elif e % 5 == 0:
        s + 1
        Text(app, text=str(2), grid=ae[s], color='black')
    elif e % 3 == 0:
        f + 1
        Text(app, text=str(3), grid=ae[f], color='black')
    
    else:
        print(e)


app.display()
