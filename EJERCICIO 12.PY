# Diccionario que mapea sufijos de archivo a tipos MIME
tipos_mime = {
    ".gif": "image/gif",
    ".jpg": "image/jpeg",
    ".jpeg": "image/jpeg",
    ".png": "image/png",
    ".pdf": "application/pdf",
    ".txt": "text/plain",
    ".zip": "application/zip"
}

# Solicita al usuario el nombre de un archivo
nombre_archivo = input("Ingrese el nombre de un archivo: ")

# Obtiene el sufijo del archivo
archivo, extension = nombre_archivo.split(".")
sufijo_archivo = extension.casefold()

# Verifica si el nombre del archivo termina en un sufijo permitido
if sufijo_archivo in tipos_mime:
    # Obtiene el tipo de archivo MIME
    tipo_mime = tipos_mime[sufijo_archivo]
else:
    # El nombre del archivo no termina en un sufijo permitido
    tipo_mime = "application/octet-stream"

# Imprime el tipo de archivo MIME
print(tipo_mime)