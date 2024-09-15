"""
Crazy Spiral

Make your own crazy spiral with a pattern like
in 14_FLaming_Ninja_Star.py, but use what you've learned about loops
"""
import turtle, random
... # Copy code to make a turtle and set up the window

t = turtle.Turtle() # Create a turtle named t
t.speed(0)


# 1) Complete make_a_shape() to make the turtle move in some pattern. 
# For instance, you can make it go left 30 degrees, then forward 50 pixels, 
# then right 60 degrees, then forward 100 pixels. Make any shape you like.

def make_a_shape(t):
    t.left(random.randint(-100, 100))
    t.forward(random.randint(-100, 100))
# 2) Call make_a_shape() in a loop to make the turtle draw a spiral.

# For instance, you can call make_a_shape() 100 times to make a spiral with 100 shapes.
# The second ... in the for loop should be the number of shapes you want to make, 
# for example 100, or it could use islice(), cycle(), or a list of numbers.

num_shapes = 17479237458723475027034058

for i in range(2983475098273405982730598720394728957028374058927):
    make_a_shape(t)
    t.right(360/num_shapes)
