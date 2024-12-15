from tkinter import messagebox, simpledialog, Tk
from guizero import App, Box, Text, TextBox, PushButton, ListBox, error
db = [
]
taken_rooms = [
]
def update(db):
    name = simpledialog.askstring(title='Name', prompt='whats your name')
    r = simpledialog.askstring(title='Room number', prompt='What room would you like to have')
    if r not in taken_rooms:
        z = name+' : '+r
        db.append(z)
        taken_rooms.append(r)
        return db
    else:
        messagebox.showerror(title='taken room', message='your room choice is taken')

while True:
    x = update(db)
    print(db)
    


    
    