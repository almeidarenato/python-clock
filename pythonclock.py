from tkinter import *
from tkinter.ttk import *
from time import strftime
root = Tk()
root.title('Relógio')
def time():
    string = strftime('%H:%M:%S %p')
    label.config(text = string)
    label.after(1000,time)
label = Label(root, font=('Century Ghotic',40,'bold'),
            background = 'black',
            foreground = 'white'
            )
label.pack(anchor = 'center')
time()
mainloop()