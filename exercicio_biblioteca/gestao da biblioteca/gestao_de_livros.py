biblioteca = []
livros = {"titulo":"anjos e demonios",
          "preco": 15.0,
          "disponivel" : True
          }
biblioteca.append(livros)

def ordem_alfabetica(biblioteca):
    ordenados = []
    for livro in biblioteca:
        ordenados.append(livro["titulo"])
        ordenados.sort()
    
    print(ordenados)

    

def criar_livros(titulo_novo_livro, preco):
    for livro in biblioteca:
        if livro['titulo'] == titulo_novo_livro: 
            return "Livro já existente"
    livros = {'titulo': titulo_novo_livro, 'preco' : preco, 'disponivel': True}
    biblioteca.append(livros)
    print(biblioteca)


def atualizar_livros(titulo_novo_livro,atualizar_titulo,atualizar_preco):
    for livro in biblioteca:
        if livro["titulo"] == titulo_novo_livro:
            livro["titulo"] = atualizar_titulo
            livro["preco"] = atualizar_preco
            print("este livro foi atualizado")
            print(biblioteca)
            return
    print("livro nao encontrado")


def eliminar_livros(eliminar_titulo):
        for livro in biblioteca:
            if eliminar_titulo == livro['titulo']:
                biblioteca.remove(livro)
                print("eliminado com sucesso")
                return biblioteca
        print("esse livro nao foi encontrado")
        #return biblioteca
    

# print(f"O primeiro livro criado é {livros}\n")
# print(f"Atualmente a biblioteca tem os livros -> {biblioteca}\n")
# print(f"Adicionar um novo livro -> {criar_livros(biblioteca, 'caim', 20.0)}\n")
# print(f"Atualizar um novo livro -> {atualizar_livros('caim', 'crime e castigo', 30.0)}\n")
# print(f"Ordem alfabetica -> {ordem_alfabetica(biblioteca)}\n")
# print(f"Atualmente a biblioteca tem os livros -> {biblioteca}\n")
# print(f"Eliminar -> {eliminar_livros('anjos e demónios')}")




