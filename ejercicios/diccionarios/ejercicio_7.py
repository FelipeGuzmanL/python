def cesta_compra():
    lista = {}
    continuar = True
    
    while continuar:
        articulo = input("Que articulo desea comprar?: ")
        precio = int(input(articulo + ": "))
        lista[articulo] = precio
        print(lista)
        continuar = input("¿Quiere agregar otro producto? (SI/NO): ") == "si"
        
    print("Articulo Precio")
    total = 0
    for articulo, precio in lista.items():
        print(articulo, precio)
        total = total + precio
    print("Total: ", total)
cesta_compra()
