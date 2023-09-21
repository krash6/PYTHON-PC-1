# Peso de un payaso
peso_payaso = 112

# Peso de una muñeca
peso_muñeca = 75

# Número de payasos vendidos
payasos_vendidos = int(input("Ingrese el número de payasos vendidos: "))

# Número de muñecas vendidas
muñecas_vendidas = int(input("Ingrese el número de muñecas vendidas: "))

# Peso total del paquete
peso_total = payasos_vendidos * peso_payaso + muñecas_vendidas * peso_muñeca

# Muestra el peso total del paquete
print("El peso total del paquete es de:", peso_total, "g")