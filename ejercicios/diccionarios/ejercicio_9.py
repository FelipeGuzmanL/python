def factura():
    factura = {'252602':25000,'12520':80000}
    continuar = True
    total_pagado = 0
    total_deuda = 0
    
    while continuar:
        opcion = int(input("Qué opcion desea realizar? 1)Añadir factura 2)Pagar Factura 3)Terminar: "))
        if opcion == 1:
            clave = str(input("Numero de la factura: "))
            factura[clave] = int(input(clave + ": "))
            #print(factura)
        elif opcion == 2:
            numero = str(input("Numero de la factura?: "))
            if numero in factura:
                total_pagado = total_pagado + factura[numero]
                #print(total_pagado)
                factura.pop(numero)
                #print(factura)
            else:
                print("Factura no existe")
        elif opcion == 3:
            print("Adios")
            break
        else:
            print("El valor ingresado no es correcto")
            
    for precio in factura:
        total_deuda = total_deuda + factura[precio]
    
    print("Deuda Total: ", total_deuda, "Total Pagado: ", total_pagado)
            
factura()