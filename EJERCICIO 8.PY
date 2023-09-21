# Horas de inicio y fin de cada comida
hora_desayuno_inicio = 7.0
hora_desayuno_fin = 8.0
hora_almuerzo_inicio = 12.0
hora_almuerzo_fin = 13.0
hora_cena_inicio = 18.0
hora_cena_fin = 19.0

# Solicita la hora al usuario
hora = input("Ingrese la hora en formato 24 horas (hh:mm): ")

# Convierte la hora a float
hora_float = float(hora.split(":")[0]) + float(hora.split(":")[1]) / 60

# Determina la hora de la comida
if hora_float >= hora_desayuno_inicio and hora_float <= hora_desayuno_fin:
    print("Es hora de desayunar.")
elif hora_float >= hora_almuerzo_inicio and hora_float <= hora_almuerzo_fin:
    print("Es hora de almorzar.")
elif hora_float >= hora_cena_inicio and hora_float <= hora_cena_fin:
    print("Es hora de cenar.")
else:
    print("No es hora de comer.")