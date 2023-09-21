# Solicita los dos números
numero_1 = int(input("Ingrese el primer número: "))
numero_2 = int(input("Ingrese el segundo número: "))

# Imprime el menú
print("Menú:")
print("1. Suma")
print("2. Resta")
print("3. Multiplicación")

# Solicita la opción del usuario
opcion = int(input("Ingrese la opción que desea realizar: "))

# Realiza la operación seleccionada
if opcion == 1:
    resultado = numero_1 + numero_2
    print("La suma de los dos números es:", resultado)
elif opcion == 2:
    resultado = numero_1 - numero_2
    print("La resta de los dos números es:", resultado)
elif opcion == 3:
    resultado = numero_1 * numero_2
    print("La multiplicación de los dos números es:", resultado)   
else:
    print("La opción ingresada no es válida.")