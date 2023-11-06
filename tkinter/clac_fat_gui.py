import tkinter as tk
from tkinter import messagebox



def calculate_fatorial():
    try:
        number = int(entry.get())
        if number <= 0:
            raise ValueError
        
        factorial = 1
        for i in range(1,number+1):
            factorial *= i
        messagebox.showinfo("Resultado do fatorial", f"O fatorial de {number} e {factorial}")
        #print(f"o factorial de {number} é {factorial}")

    except ValueError:
       #print(f"por favor introduza um inteiro positivo")
       messagebox.showerror("ERRO!!","Por favor introduza um inteiro positivo")



#criar janela tkinter
janela = tk.Tk()
janela.title("calculadora fatorial")



#criar elementos gui

label = tk.Label(janela,text="introduza um numero: ")
label.pack()


entry = tk.Entry(janela)
entry.pack()

button = tk.Button(janela,text="calcular fatorial",command=calculate_fatorial)
button.pack()


#correr evento mainloop

janela.mainloop()


