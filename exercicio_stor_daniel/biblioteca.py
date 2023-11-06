



# class Pessoa:
#     def __init__(self, nome,idade):
#         self.nome = nome
#         self.idade = idade

#     def alterar_nome(self,novo_nome):
#         self.nome = novo_nome




# class ContaBancaria:
#     def __init__(self,nome, saldo=0):
#         self.nome = nome
#         self.saldo = saldo

#     def depositar(self, montante):
#         if montante > 0:
#             self.saldo += montante
#             print(f'deposito de {montante} realizado, saldo atual e de {self.saldo}')
#         else:
#             print('o montante do deposito deve ser maior do que 0')

#     def levantar(self, montante):
#         if montante > 0:
#             if self.saldo >= montante:
#                 self.saldo -= montante
#                 print(f'levantamento do montante {montante} realizado o seu saldo e de {self.saldo}')
#             else:
#                 print("Saldo insuficiente para efetuar o levantamento.")
#         else:
#             print("O valor do levantamento deve ser maior que zero.")


# class Pessoa:
#     def __init__(self, nome,idade):
#         self.nome = nome
#         self.idade = idade
#         self.contas_bancarias = []

#     def adicionar_contas_bancarias(self,conta):
#         if isinstance(conta,ContaBancaria):
#             self.contas_bancarias.append(conta)
#             print(f'conta bancaria adicionada ao nome {self.nome} idade de {self.idade}')
#         else:
#             print('o objeto nao foi encontrado')
# pessoa1 = Pessoa("Joao",12)
# pessoa2 = Pessoa("Maria",20)

# conta1 = ContaBancaria('Joao',0)
# conta2 = ContaBancaria('Maria',0)

# pessoa1.adicionar_contas_bancarias(conta1)
# pessoa2.adicionar_contas_bancarias(conta2)

# conta1.depositar(1000)
# conta2.depositar(500)
   

import sqlite3

class Livros:
    def __init__(self, titulo, autor, isbn):
        self.titulo = titulo
        self.autor = autor
        self.isbn = isbn

    def guardar_no_sqlite(self):

       conn = sqlite3.connect('biblioteca.db')

       conn.execute('''CREATE TABLE IF NOT EXISTS livros
                    (id INTEGER PRIMARY KEY AUTOINCREMENT,
                    titulo TEXT NOT NULL,
                    autor TEXT NOT NULL,
                    isbn TEXT NOT NULL)''') 
       
       conn.execute('INSERT INTO livros (titulo, autor, isbn) VALUES (?,?,?)',(self.titulo, self.autor, self.isbn))

       conn.commit()
       conn.close()

    @staticmethod
    def recuperar_do_sqlite(isbn):

        conn = sqlite3.connect('biblioteca.db')

        cursor = conn.execute("SELECT titulo, autor, isbn FROM livros WHERE isbn = ?", (isbn,))
        livro_info = cursor.fetchone()

        conn.close()

        if livro_info:
            titulo, autor, isbn = livro_info
            livro = Livros(titulo,autor,isbn)

            return livro
        else:
            print('livro nao encontrado')
            return None
        
    @staticmethod
    def remover_do_sqlite(isbn):
        conn = sqlite3.connect('biblioteca.db')
        conn.execute('DELETE FROM livros WHERE isbn = ?',(isbn,))
        conn.commit()
        conn.close()

class Biblioteca:
    def __init__(self):
        self.livros = []
        self.vendas = []

    def adicionar_livros(self, livro):
        if isinstance(livro, Livros):
            self.livros.append(livro)
            livro.guardar_no_sqlite()
            print(f'Livro {livro.titulo} adicionado a biblioteca')

        else:
            print('o objeto nao e uma instancia da classe livros')

    def remover_livros(self, isbn):
        for livro in self.livros:
            if livro.isbn == isbn:
                self.livros.remove(livro)
                Livros.remover_do_sqlite(isbn)
                print(f'livro {livro.titulo} foi removido da biblioteca')
                return
        print('livro nao foi encontrado')
    
    def consultar_por_isbn(self, isbn):
        for livro in self.livros:
            if livro.isbn == isbn:
                return  livro
        return None

    def adicionar_venda(self, venda):
        if isinstance(venda, Venda):
            self.vendas.append(venda)
            print(f'venda concluida')
        
        else:
            print(f'o objeto nao e uma instancia de vendas')
    def relatorio_de_vendas(self):
        if not self.vendas:
            return "Nenhuma venda registrada."
        
        report = "Relatório de Vendas:\n"
        for venda in self.vendas:
            report += f"Comprador: {venda.comprador}\n"
            report += f"Livro: {venda.livro.titulo}\n"
            report += f"Preco: {venda.preco:.2f}€\n\n"

        return report
    
    def busca_avancada(self, titulo=None, autor=None):
        resultados = []

        for livro in self.livros:
            if (not titulo or titulo.lower() in livro.titulo.lower() ) and (not autor or autor.lower() in livro.autor.lower()):
                resultados.append(livro)
        return resultados
            

    

class Venda:
    def __init__(self, livro, preco, comprador):
        self.livro = livro
        self.preco = preco
        self.comprador = comprador
    def registrar_venda(self):
        print(f"Venda registrada: {self.comprador} comprou '{self.livro.titulo}' por {self.preco:.2f}€")



biblioteca = Biblioteca()

livro1 = Livros("Python for Beginners", "John Smith", "978-1234567890")
livro2 = Livros("Data Science Essentials", "Jane Doe", "978-0987654321")


biblioteca.adicionar_livros(livro1)
biblioteca.adicionar_livros(livro2)



venda1 = Venda(livro1, 50.0, "Joao")
venda2 = Venda(livro2, 75.0, "Maria")

venda1.registrar_venda()
venda2.registrar_venda()
biblioteca.adicionar_venda(venda1)
biblioteca.adicionar_venda(venda2)
sales_report = biblioteca.relatorio_de_vendas()
print(sales_report)

resultados = biblioteca.busca_avancada(titulo='Python', autor='John Smith')

if resultados:
    print('resultados da pesquisa')
    for livro in resultados:
        print(f'titulo:{livro.titulo}, autor: {livro.autor}')

else:
    print('nenhum resultado encontrado')
