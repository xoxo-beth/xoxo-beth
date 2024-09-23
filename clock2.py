from tkinter import Tk
from tkinter import Label
import time
import sys

master = Tk()
master.title("Beth's clock")

def get_time ():
    timeVar = time.strftime("%I:%M:%S %p")
    clock.config(text=timeVar)
    clock.after(200, get_time)

    
clock = Label(master,font=('ds-digital',90),bg='purple', fg='pink')
clock.pack()

get_time()

master.mainloop()