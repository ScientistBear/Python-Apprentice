"""
Infuriating Calculator

Let's write a calculator that's really hard to use, not because we want it to be
hard, but just because we haven't learned how to make it easy yet.

Ask the user for three things: 

1. A number
2. A second number
3. A math operation (add, subtract, multiply, divide)
4. Use if-elif-else statements to provide the desired math operation on the
   numbers and display the result.

If the user enters an unknown operation, display an error message. ( use
messagebox.showerror() 

For the number, you can ask for a float or an integer with
simpledialog.askfloat() or simpledialog.askinteger(), and for the math operation
you can ask for a string with simpledialog.askstring()

"""

# Import the required modules
from tkinter import messagebox, simpledialog, Tk, sys # import required modules

window = Tk()     # Create a window object
window.withdraw() # Hide the window; we just want to see pop ups
# Import the required modules
# Create a window object

# Hide the window, hint: use the withdraw method5857
numb1 = simpledialog.askinteger("numb1", "enter number one")
numb2 = simpledialog.askinteger("numb2", "enter number two")
numb3 = simpledialog.askinteger("numb2", "enter number three")
# Ask the user for the first number   32984759

# Ask the user for the second number
sys.set_int_max_str_digits(999999)
# Ask the user for the math operation
operation = simpledialog.askstring("operation", "ex. + - ** / *")
# Use if-elif-else statements to provide the desired math operation on the numbers and display the result.
if operation == '+':
   messagebox.showinfo(title='calculation',message=(numb1 + numb2))
elif operation == '-':
   messagebox.showinfo(title='calculation',message=(numb1 - numb2))
elif operation == '/':
   messagebox.showinfo(title='calculation',message=(numb1 / numb2))
elif operation == '*':
   messagebox.showinfo(title='calculation',message=(numb1 * numb2))
elif operation == '**':
   print(numb1 ** numb2)
   messagebox.showinfo(title='calculation',message=(numb1 ** numb2 ** numb3))
   
# If the user enters an unknown operation, display an error message. ( use messagebox.showerror()3728975897
# Keep the window ope