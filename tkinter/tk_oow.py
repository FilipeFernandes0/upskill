




#criacao de janela atraves de class

# class App(tk.Tk):
#     def __init__(self):
#         super().__init__()

    



# if __name__ == "__main__":
#     app = App()



#     app.mainloop()


import tkinter as tk
from tkinter import ttk
from tkinter.messagebox import showinfo

class App(tk.Tk):
    def __init__(self):
        super().__init__()
    
        self.title("A minha aplicacao")
        self.geometry("300x50")

        self.label = ttk.Label(self, text = "Hello, is it me you are looking for")
        self.label.pack()

        self.button = ttk.Button(self,text = "Clica-me")
        self.button["command"] = self.button_clicked
        self.button.pack()

    def button_clicked(self):
        showinfo(title="Informacao", message="YES IT IS ME!")



if __name__ == "__main__":
    app = App()
    app.mainloop()