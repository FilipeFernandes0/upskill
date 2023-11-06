import tkinter as tk
from tkinter import messagebox
def Click():
    replay = messagebox.askquestion("Quit?","Are you sure")
    if replay == "yes":
        messagebox.showinfo("info","i will close the app")
        my_app.destroy()
my_app = tk.Tk()
my_app.title("my app")
button = tk.Button(my_app, text="hello",command =Click)
button.pack()
button.place(x=100,y=100)
my_app.mainloop()
