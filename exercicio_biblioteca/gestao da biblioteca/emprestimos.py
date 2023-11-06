

emprestimos = []

def livros_emprestados():
    print(emprestimos)
def criar_emprestimos(biblioteca,titulo_emprestado ,data_de_emprestimo,data_de_devolucao):
    for livro in biblioteca:
        if livro["titulo"] == titulo_emprestado and livro["disponivel"]:
           livro["disponivel"] == False
           novo_emprestimo = {"titulo":titulo_emprestado,"data de emprestimo": data_de_emprestimo,"data de devolucao": data_de_devolucao}
           emprestimos.append(novo_emprestimo)
           print("emprestimo bem sucedido")
           return
    print("livro nao disponivel para emprestimo")
def atualizar_emprestimos(titulo_emprestado,nova_data_de_devolucao):
    for emprestimo in emprestimos:
        if emprestimo["titulo"] == titulo_emprestado:
            emprestimo["data de devolucao"] = nova_data_de_devolucao
            
            print("emprestimo atualizado")
            return 
    print("emprestimo nao encontrado")
def entregar_livros(titulo_emprestado,biblioteca):
    for emprestimo in emprestimos:
        if emprestimo["titulo"] == titulo_emprestado:
            emprestimos.remove(emprestimo)
            for livro in biblioteca:
                if livro["titulo"] == titulo_emprestado:
                    livro["disponivel"] = True
                    print("livro devolvido com sucesso")
                    return
    print("emprestimo nao encontrado")
def eliminar_emprestimos(titulo_emprestado):
    for emprestimo in emprestimos:
        if emprestimo["titulo"] == titulo_emprestado:
            emprestimos.remove(emprestimo)
            print("emprestimo eliminado")
            return
    print("emprestimo nao encontrado")




# criar_emprestimos("anjos e demonios", "2023-06-15", "2023-06-30")
# livros_emprestados()
# print(biblioteca)
# atualizar_emprestimos("anjos e demonios","2023-05-09")
# livros_emprestados()
# entregar_livros("anjos e demonios")
# livros_emprestados()
# print(biblioteca)
# eliminar_emprestimos("anjos e demonios")