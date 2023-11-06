import tkinter as tk
from tkinter import messagebox




class QuizApp:
    def __init__(self,master):
        #janela principal

        self.master = master
        self.master.title("Quizz")
        self.num_question = 0
        self.resultado = 0

        self.questoes = [
        {
                "questao": "qual é a capital da Franca?",
                "opcoes": ["Paris", "Londres", "Berlim", "Roma"],
                "resposta": "Paris"
        },
        {       "questao": "quem pintou a Mona Lisa?",
                "opcoes": ["vincent van gogh", "leonardo da vinci", "Pablo Picasso", "michelangelo"],
                "resposta": "leonardo da vinci"
        },
        {       "questao": "qual a montanha mais alta do mundo",
                "opcoes": ["Kilimanjaro", "serra da estrela", "Fuji", "Evereste"],
                "resposta": "Evereste"
        }
        
    ]
        
    #construir etiquetas de questoes
        self.questao_label = tk.Label(self.master,text="")
        self.questao_label.pack()
        #construir etiquetas de opcoes
        self.opcoes_var = tk.StringVar()
        self.opcoes_var.set("")
    
        self.opcoes_label = tk.Label(self.master,textvariable=self.opcoes_var)
        self.opcoes_label.pack()
    #construir etiquetas de respostas
        self.resposta_var = tk.StringVar()
        self.resposta_var.set("")
        self.resposta_label = tk.Label(self.master, textvariable=self.resposta_var)
        self.resposta_label.pack()
        self.botao_seguinte = tk.Button(self.master,text = "Proximo",command=self.questao_seguinte)
        self.botao_seguinte.pack()

    def questao_seguinte(self):
        if self.num_question < len(self.questoes):
            questao = self.questoes[self.num_question]
            self.questao_label.configure(text=questao["questao"])
            self.opcoes_var.set("\n".join(questao["opcoes"]))
            self.resposta_var.set("")
            self.botao_seguinte.configure(text="proximo")
        else:
            messagebox.showinfo("o quizz terminou ", f"terminou o quizz o seu resultado foi de {round(self.resultado/len(self.questoes)*100)}%")
            self.master.destroy()

    def verificar_resposta(self,opcao_selecionada):
        questao = self.questoes[self.num_question]
        if opcao_selecionada == questao["resposta"]:
            self.resultado +=1
            self.resposta_var.set("correto")
        else:
        
            self.resposta_var.set("errado")

        self.num_question +=1
        self.botao_seguinte.configure(text="Proxima")
        self.botao_seguinte.focus_set()

   
root = tk.Tk()

app = QuizApp(root)
root.mainloop()

