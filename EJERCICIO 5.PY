# Solicita al usuario que ingrese el número de shows musicales vistos
numero_shows = int(input("¿Cuántos shows musicales has visto en el último año? "))

# Determina si el usuario ha visto más de 3 shows
if numero_shows > 3:
    mas_de_tres = True
else:
    mas_de_tres = False

# Muestra el resultado
print("¿Has visto más de 3 shows musicales en el último año?:", mas_de_tres)