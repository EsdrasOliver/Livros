# PAGINA: 101

# PERGUNTAS
""" 
4.1 Escreva o código para a função soma, vista anteriormente.
4.2 Escreva uma função recursiva que conte o número de itens em uma lista.
4.3 Encontre o valor mais alto em uma lista.
4.4 Você se lembra da pesquisa binária do Capítulo 1? Ela também é um
algoritmo do tipo dividir para conquistar. Você consegue determinar o
caso-base e o caso recursivo para a pesquisa binária? 
"""


def soma_recursiva(lista):
    if not lista:
        return 0
    else:
        return lista[0] + soma_recursiva(lista[1:])


lista = [1, 2, 3, 4, 5]
print(soma_recursiva(lista))


def contar_itens(lista):
    if not lista:
        return 0
    else:
        return 1 + contar_itens(lista[1:])


def encontrar_maximo(lista):
    if len(lista) == 1:
        return lista[0]
    else:
        maximo_resto = encontrar_maximo(lista[1:])
        return lista[0] if lista[0] > maximo_resto else maximo_resto


def pesquisa_binaria(lista, item, inicio=0, fim=None):
    if fim is None:
        fim = len(lista) - 1
    if inicio > fim:
        return False
    meio = (inicio + fim) // 2
    if lista[meio] == item:
        return True
    elif lista[meio] > item:
        return pesquisa_binaria(lista, item, inicio, meio - 1)
    else:
        return pesquisa_binaria(lista, item, meio + 1, fim)


print(contar_itens(lista))
print(encontrar_maximo(lista))
print(pesquisa_binaria(lista, 5))
