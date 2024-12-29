from tkinter import messagebox, simpledialog, Tk
import math, random
db = [
]
taken_rooms = [
]
names = [
]
code_passes = [
]




def user(db):
    in_out = simpledialog.askstring(title='', prompt='Are you going to your room, checking in, or checking out')
    if in_out == 'checking in':
        code = random.randint(1000,9999)
        name = simpledialog.askstring(title='Name', prompt='whats your name')
        r = simpledialog.askstring(title='Room number', prompt='What room would you like to have')
        messagebox.showinfo(title='Code', message='your code is '+ str(code))
        if r not in taken_rooms:
            z = name+':'+r+':'+str(code)
            db.append(z)
            taken_rooms.append(r)
            print(db)
            return db
        else:
            messagebox.showerror(title='taken room', message='your room choice is taken')
    elif in_out == 'going to room':
        namee = simpledialog.askstring(title='Name', prompt='Whats your name')
        room = simpledialog.askstring(title='room numb', prompt='what is your room number')
        code_pass = simpledialog.askstring(title='Passcode', prompt='Whats your passcode')
        if namee+':'+room+':'+code_pass in db:
            messagebox.showinfo(title='Correct', message='You may enter your room')
    elif in_out == 'checking out':
        namee = simpledialog.askstring(title='Name', prompt='Whats your name')
        room = simpledialog.askstring(title='room numb', prompt='what is your room number')
        code_pass = simpledialog.askstring(title='Passcode', prompt='Whats your passcode')
        if namee+':'+room+':'+code_pass in db:
            db.remove(namee+':'+room+':'+code_pass)
        else:
            messagebox.showerror(title='Incorect', message='one of the fields you entered was incorrect')
    else:
        messagebox.showerror(message='enter checking in, checking out, or going to room')
        
            
        
                

while True:
    x = user(db)
    


    
    