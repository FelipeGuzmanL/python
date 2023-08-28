def diccionario():
    diccionario = {}
    palabras = input("Introducir palabras con traduccion y separadas por comas: ")

    for i in palabras.split(","):
        clave, valor = i.split(":")
        diccionario[clave] = valor
        
    frase = input("Introduce la palabra en español: ")
    for i in frase.split():
        if i in diccionario:
            print(diccionario[i], end=' ')
        else:
            print(i, end=' ')
    
    
diccionario()