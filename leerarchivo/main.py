def leer_archivo(nombre_archivo):
    try:
        with open(nombre_archivo, 'r') as archivo:
            contenido = archivo.read()
        return contenido
    except FileNotFoundError:
        print("El archivo no se encontró.")
    except Exception as e:
        print("Ocurrió un error:", e)
