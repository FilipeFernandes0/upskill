'''
Ex. 1

Criar uma janela pricipal com um campo de introdução de texto com um botão a dizer mostrar mensagem, 
quando clicado aparece uma messagebox com o título mensagem e conteúdo :Olá, _texto introduzido_'''

import tkinter as tk
from tkinter.messagebox import showinfo
from tkinter.simpledialog import askstring
from tkinter.scrolledtext import ScrolledText

# main_window = tk.Tk()
# main_window.geometry("700x300")
# entry = askstring("name" ,"what is your name")
# showinfo('Hello!', 'Hi, {}'.format(entry))

# main_window.mainloop()

'''
Ex. 2

Write a program that asks the user to type  a word and return him its reverse without using any predefined function . 
Example if the user enters the word python, the program returns nohtyp to him as shown in the figure below:'''


# win = tk.Tk()
# win.geometry("700x300")
# entry = askstring("name" ,"what is your name")
# showinfo('Hello!', 'Hi, {}'.format(entry[::-1]))

# label = tk.Label()
# win.mainloop()

'''
Ex 3

Write a Python GUI program to create a ScrolledText widgets using tkinter module.'''


root = tk.Tk()
root.title("scrolled text widget")

st = ScrolledText(root,width = 50,height = 10)
st.pack(fill = tk.BOTH, side = tk.LEFT, expand=True)

root.mainloop()