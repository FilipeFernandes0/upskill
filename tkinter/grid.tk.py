from tkinter import *
from tkinter.ttk import *

master = Tk()
master.geometry("200x200")

b1 = Button(master,text = "Click me!")
b1.place(relx=1,x=-2,y=2, anchor = NE)