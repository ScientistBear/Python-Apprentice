"""
Write a Python program that asks the user for two numbers. The program should
display the sum of the two numbers.

In this program we will just give you the comments for what you need to do. Look
at the comments and the code snippets in the previous lessons, like
03_My_Ages.py, to figure out how to complete the program.


"""
from tkinter import messagebox, simpledialog, Tk # import required modules

window = Tk()     # Create a window object
window.withdraw() # Hide the window; we just want to see pop ups
# Import the required modules

# Create a window object

# Hide the window, hint: use the withdraw method

# Ask the user for the first number   
numb1 = simpledialog.askinteger("numb1", "enter number one")
numb2 = simpledialog.askinteger("numb2", "enter number two")
# Ask the user for the second number

# Display the sum of the two numbers 
messagebox.showinfo(title='+', message=(numb1 + numb2))
# Keep the window open

