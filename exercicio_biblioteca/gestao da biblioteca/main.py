from gestao_de_livros import *
from emprestimos import *



while True:
    decidir= int(input("1-gestao de livros \n 2-gestao de emprestimos "))
    if decidir == 1:
        gestao = int(input("qual a opcao\n1-criar livro\n2-atualizar livro\n3-eliminar livro\n4-ordenar livros\n"))
    if decidir == 2:
        emprestimos = int(input("qual a opcao\n1-criar emprestimo\n2-atualizar emprestimo\n3-eliminar emprestimo\n4-entregar livro\n5-livros emprestados\n"))

    if gestao == 1:
       criar_livros(input("qual é o titulo do novo livro: "),float(input("qual é o preco do novo titulo: ")))
    if gestao == 2:
        atualizar_livros(input("qual é o titulo do livro que queres atualizar: "),input("qual é o titulo do novo livro: "),float(input("qual é o preco do novo titulo: ")))
    if gestao == 3:
        eliminar_livros(input("qual é o titulo do livro que queres eliminar: "))
    if gestao == 4:
        ordem_alfabetica(biblioteca)


    if emprestimos == 1:
        criar_emprestimos(biblioteca,input("qual é o livro que quer: "),input("data do emprestimo: "), input("data da devolucao: "))
    if emprestimos == 2:
        atualizar_emprestimos(input("titulo do livro emprestado: "),input("nova data de devolucao: "))
    if emprestimos == 3:
        eliminar_emprestimos(input("titulo do livro emprestado que quer eliminar: "))
    if emprestimos == 4:
        entregar_livros(input("titulo do livro emprestado que quer devolver: "), biblioteca)
    if emprestimos == 5:
        livros_emprestados()























