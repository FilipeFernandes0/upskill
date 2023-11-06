import tkinter as tk

#importar modulo tkinter como tk, que é uma instancia (objeto)
root = tk.Tk() #instancia que representa uma janela principal(main window)

#prioridade - 
# 1- TOP,BOTTOM,LEFT,RIGHT da janela
#dentro do "side" 
#1.1- TOP,BOTTOM,LEFT,RIGHT
#relativo aos buttoes anteriormente instaciados e independente do side atribuido
#1.1.1 
# 
'''
>>>>>>>>>>> FRAME <<<<<<<<<<<

            TOP1|
            TOP2|
                V
------->                 <-------
lEFT1 LEFT2        ^   RIGHT2 RIGHT1
            BOTTOM2|
            BOTTOM1|


'''



#botoes

def button_click():
    print("botao clicado")

button = tk.Button(root, text="clica-me", command= button_click)
button.pack()



root.mainloop()