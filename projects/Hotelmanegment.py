from tkinter import messagebox, simpledialog, Tk
import math
db = [
]
taken_rooms = [
]
names = [
]
code_passes = [
]




def user(db):
    in_out = simpledialog.askstring(title='', prompt='are you going to your room or checking in')
    if in_out == 'checking in':
        name = simpledialog.askstring(title='Name', prompt='whats your name')
        r = simpledialog.askstring(title='Room number', prompt='What room would you like to have')
        code = simpledialog.askstring(title='Room code', prompt='Pick a sucure pascode')
        if r not in taken_rooms:
            code_passes.append(code)
            taken_rooms.append(r)
            names.append(name)

            print(taken_rooms, names, code_passes)
            return db
        else:
            messagebox.showerror(title='taken room', message='your room choice is taken')
    elif in_out == 'going to room':
        namee = simpledialog.askstring(title='Name', prompt='Whats your name')
        room = simpledialog.askstring(title='room numb', prompt='what is your room number')
        code_pass = simpledialog.askstring(title='Passcode', prompt='Whats your passcode')
        if room in taken_rooms:
            if namee in names:
                if code_pass in code_passes:
                    messagebox.showinfo(title='Correct', message='You may enter your room')
    else:
        messagebox.showerror(message='enter checking in or going to room')
        
            
        
                

while True:
    x = user(db)
    


    
    