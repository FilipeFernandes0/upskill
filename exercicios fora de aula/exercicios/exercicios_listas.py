# # Exemplo com erro de lógica na verificação de números primos
# def is_prime(n):
#     for i in range(2, n):
#         if n % i == 0:
#             return False
#     return True

# ola = is_prime(12)

# print(ola)


# Exemplo com erro de lógica no cálculo da média
# def calcular_media(lista):
#     soma = 0
#     for num in lista:
#         soma += num
#     media = soma / len(lista) + 1
#     return media


# def teste(s):
#     char_count = {}

#     for char in s:
#         if not char in s:
#             char_count[char] = 0
#         else:
#             char_count[char] += 1
        
#         if char_count[char] >= 1:
#             return char
#     return None


# def contar_elementos(lista):
#     elementos_contados = {}
#     for elemento in lista:
#         if not elemento in elementos_contados:
#             elementos_contados[elemento] = 1
#         else:
#             elementos_contados[elemento] += 1
#     return elementos_contados


# def verificar_palindromos(lista_de_strings):
#     for string in lista_de_strings:
#         reversed_string = string[::-1]
#         if string == reversed_string:
#             return True
#         else:
#             return False
        
def media_ponderada(valores, pesos):
    if len(valores) != len(pesos):
        return None
    soma_pesos = sum(pesos)
    soma_ponderada = sum([valores[i] * pesos[i] for i in range(len(valores))])
    return soma_ponderada / soma_pesos