class QuizApp:
    def __init__(self):
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
        
    def start_quiz(self):
        for questao in self.questoes:
            print(questao["questao"])

            for index,opcao in enumerate(questao["opcoes"]):
                print(f"{index + 1}.{opcao}")

            opcao_escolhida = int(input("A sua resposta (introduza um numero da resposta): "))
            
            if questao["opcoes"][opcao_escolhida-1] == questao["resposta"]:
                print("certo")
                self.resultado +=1
            
            else:
                print("errado")

            
        print(f"terminou o quizz o seu resulatdo foi de {round(self.resultado/len(self.questoes)*100)}%")


quizzapp = QuizApp()

quizzapp.start_quiz()