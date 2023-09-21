# Precios de las entradas
precio_gratis = 0
precio_ninos = 5
precio_adultos = 10

# Solicita la edad del cliente
edad = int(input("Ingrese la edad del cliente: "))

# Calcula el precio de la entrada
if edad < 4:
    precio = precio_gratis
elif edad <= 18:
    precio = precio_ninos
else:
    precio = precio_adultos

# Muestra el precio de la entrada
print("El precio de la entrada es de: $", precio)