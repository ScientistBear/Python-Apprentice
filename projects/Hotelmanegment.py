from tkinter import messagebox, simpledialog, Tk
from guizero import App, Box, Text, TextBox, PushButton, ListBox, error

def add_hotel_person_thingy(db, key, value):
    db[key]=value
    pass
def update(db):
    e = simpledialog.askinteger(title='', prompt='')
    l= [

    ]
    for i in db.keys():
        d = db[i]
        z = i+' : '+d
        l.append(z)
    pass
db = {}
y = add_hotel_person_thingy()
x = update