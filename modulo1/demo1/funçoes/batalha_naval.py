

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



def definir_tabuleiro(tabuleiro):
    print("  A B C D E F G H I J")
    print("  -------------------")

    row_number = 1
    for row in tabuleiro:
        print(row_number, " ".join(row))
        row_number += 1

def definir_navios(tabuleiro):

    tipos_de_navios = {"porta aviões": 5,
                       "Couraçado": 4,
                       "cruzador": 3,
                       "submarino":3,
                       "destruidor": 2,
                       }
    for navio,tamanho in tipos_de_navios.items():
        print("defina no tabuleiro cada navio", navio)
        while True:
            #for navio,tamanho in tipos_de_navios.items():
                #print("defina no tabuleiro cada navio", navio)
                posicao = input("defina a posição (por exemplo A1): ").upper()
                orientacao = input("defina a orientaçao H - horizontal e V - vertical: ").upper()

                coluna = ord(posicao[0]) - 65
                linha = int(posicao[1:]) -1

                if (coluna < 0 or coluna >= 10) or (linha < 0 or linha >= 10):
                    print("O número é inválido, tenta novamente")
                    break
                if orientacao not in ["H","V"]:
                    print("letra incorreta, tenta novamente")
                    break
                if orientacao == "H":
                    if coluna + tamanho > 10:
                        print("numero invalido, tenta novamente")
                        break
                    for i in range(tamanho):
                        if tabuleiro[linha][coluna + i] != " ":
                            print("espaço ocupado por outro navio")
                            break
                    else:
                        for i in range(tamanho):
                            tabuleiro[linha][coluna + i] = "O"
                    break
                if orientacao == "V":
                    if linha + tamanho > 10:
                        print("espaço invalido, tenta novamente")
                        break
                    for i in range(tamanho):
                        if tabuleiro[linha+i][coluna] != " ":
                            print("este espaço ja esta ocupado, tenta novamente")
                            break
                    else:
                        for i in range(tamanho):
                            tabuleiro[linha + i][coluna] = "O"
                    break
        definir_tabuleiro(tabuleiro)


def definir_jogada(tabuleiro):
    turno = 30
    while turno != 0:
        print("=====turno=====", turno)
        jogada = input("qual é a jogada que queres fazer(por exemplo A1): ")
        coluna = ord(jogada[0]) - 65
        linha = int(jogada[1:]) - 1 

        if (coluna < 0 or coluna >= 10) or (linha < 0 or linha >= 10):
            print("Não está no alcance do jogo")
            turno -= 1
            continue
        if tabuleiro[linha][coluna] == "X" or tabuleiro[linha][coluna] == "*":
            print("ja acertas-te nessa posição")
            turno -=1
            continue
        if turno == 0:
            print("====GAMEOVER!!=====")
        if tabuleiro[linha][coluna] == "O":
            print("=======HIT=======")
            turno -= 1
            tabuleiro[linha][coluna] = "X"
        else:
            print("========SPLASH======")
            turno -= 1
            tabuleiro[linha][coluna] = "*"
        
            
        definir_tabuleiro(tabuleiro)

definir_navios(tabuleiro)

definir_jogada(tabuleiro)





