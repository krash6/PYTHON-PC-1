# Lista original
lista = ['Rojo', 'Verde', 'Blanco', 'Negro', 'Rosa', 'Amarillo']

# Solicita las posiciones a eliminar
posiciones_a_eliminar = input("Ingrese las posiciones a eliminar, separadas por comas: ").split(",")

# Elimina los elementos en las posiciones indicadas
for posicion in posiciones_a_eliminar:
    posicion = int(posicion)
    lista.pop(posicion)

# Imprime la lista resultante
print(lista)