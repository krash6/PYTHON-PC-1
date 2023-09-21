# Solicita el consumo del usuario
consumo = float(input("Ingrese el costo de su consumo: "))

# Solicita el porcentaje de propina
propina = float(input("Ingrese el porcentaje de propina que desea dejar: "))

# Calcula la cantidad de propina
propina_total = consumo * propina / 100

# Muestra la cantidad de propina
print("La cantidad de propina a dejar es: $", propina_total)