# Función para invertir una lista
def invertir_lista(lista):
    lista_invertida = []
    for i in range(len(lista) - 1, -1, -1):
        lista_invertida.append(lista[i])
    return lista_invertida

# Lista original
lista = ["Di", "buen", "día", "a", "papa"]

# Invierte la lista
lista_invertida = invertir_lista(lista)

# Imprime la lista invertida
print(lista_invertida)