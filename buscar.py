def buscar_palabra(contenido):
    palabra_buscada = input('Buscar: ')

    for x in contenido:
        if palabra_buscada.upper() == x.upper():
            print(x)
            break
