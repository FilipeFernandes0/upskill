'''

tabuleiro = [[" "," "," "," "," "," "," "," "," "," "],
             [" "," "," "," "," "," "," "," "," "," "],
             [" "," "," "," "," "," "," "," "," "," "],
             [" "," "," "," "," "," "," "," "," "," "],
             [" "," "," "," "," "," "," "," "," "," "],
             [" "," "," "," "," "," "," "," "," "," "],
             [" "," "," "," "," "," "," "," "," "," "],
             [" "," "," "," "," "," "," "," "," "," "],
             [" "," "," "," "," "," "," "," "," "," "],
             [" "," "," "," "," "," "," "," "," "," "]]

#letters_to_numbers = {"A": 0, "B":1, "C":2,"D":3,"E": 4, "F":5, "G":6,"H":7,"I": 9}


#print(tabuleiro)

def print_tabuleiro(tabuleiro):
    print("  A B C D E F G H I J")
    print("  -------------------")

    row_number = 1
    for row in tabuleiro:
        print(row_number, " ".join(row))
        row_number += 1

def definir_navios(tabuleiro):
    tipos_navios = {"porta aviões": 5,
                    "couraçado": 4,
                    "cruzador": 3,
                    "submarino":3,
                    "destruidor":2
                    }
    for navio,tamanho in tipos_navios.items():
        print("defina a posição e orientação para cada navio", navio)
        while True:
           posicao = input("Posição(exemplo: A1): ").upper()
           orientacao = input("Orientaçao(H - horizontal V - vertical): ").upper()
           
           coluna = ord(posicao[0]) - 65 
           linha = int(posicao[1:]) -1 
           if (coluna < 0 or coluna >= 10) or (linha < 0 or linha >= 10):
               print("posição invalida tenta novamente")
               continue
           if orientacao not in ["H", "V"]:
               print("orientaçao inválida. Tenta novamente")
           if orientacao == "H":
               if coluna + tamanho > 10:
                   print("O navio nao cabe nessa posiçao. Tenta novamente")
                   continue
               for i in range(tamanho):
                   if tabuleiro[linha][coluna + i] != " ":
                       print("espaço ocupado por outro navio, tenta novamente")
                       break
               else:
                   for i in range(tamanho):
                       tabuleiro[linha][coluna + i] = "O"
                   break
           else:
               if linha + tamanho > 10:
                   print("O navio nao cabe nessa posição, tenta novamente")
                   continue
               for i in range(tamanho):
                   for i in range(tamanho):
                    if tabuleiro[linha + i][coluna] != " ":
                        print("Espaço ocupado por outro navio. Tente novamente.")
                        break
               else:
                    for i in range(tamanho):
                        tabuleiro[linha + i][coluna] = "O"
                    break 
               
        print_tabuleiro(tabuleiro)



definir_navios(tabuleiro)


def jogada_utilizador(tabuleiro):
    while True:
        posicao = input("escolhe uma posiçao para atacar (exemplo A1): ")
        coluna = ord(posicao[0]) - 65

        linha = int(posicao[1:]) -1

        if (coluna < 0 or coluna >= 10) or (linha < 0 or linha >= 10):
            print("posição inválida, tenta novamente")
            continue
        if tabuleiro[linha][coluna] == "X" or tabuleiro[linha][coluna] == "*":
            print("já atacou essa posiçao tenta novamente")
            continue
        if tabuleiro[linha][coluna] == "O":
            print("voce acertou um navio")
            tabuleiro[linha][coluna] = "X"
        else:
            print("Não acertou nenhum navio")
            tabuleiro[linha][coluna] == "*"

        print_tabuleiro(tabuleiro)
        

jogada_utilizador(tabuleiro)'''







           




