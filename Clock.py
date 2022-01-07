# Lets make a clock!

# import the essential libraires
from tkinter import *  
from tkinter.ttk import *  
from time import strftime  

# create an UI for the clock. Create root window. Root window is the main application window in programs containing title bar and borders
root = Tk()
root.title("Clock")


def clock_time():
    time = strftime('%H: %M: %S %p')  # setting the clock format
    clock_label.config(text=time)
    clock_label.after(1000, clock_time)


# store the clock. Label a widget that is used to implement display boxes where you can place text or images
clock_label = Label(root, font=("ds-digital", 80), foreground="blue", background="green")
clock_label.pack(anchor='center')

clock_time()

mainloop()
