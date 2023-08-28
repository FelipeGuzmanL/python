def clientes():
    clientes = {}
    
    continuar = True
    
    while continuar:
        opcion = int(input("1)Añadir Cliente 2)Eliminar Cliente 3)Mostrar Cliente 4)Listar todos los clientes 5)Clientes Preferentes 6)Terminar: "))
        if opcion == 1:
            rut = input("Ingrese rut: ")
            nombre = str(input("Nombre: "))
            direccion = str(input("Direccion: "))
            telefono = int(input("Telefono: "))
            correo = str(input("Correo: "))
            preferente = str(input("Preferente: "))
            if preferente == "si":
                preferente = True
            else:
                preferente = ''
            cliente = {'nombre':nombre, 'direccion':direccion,'telefono':telefono,'correo':correo,'preferente':preferente}
            clientes[rut] = cliente

        elif opcion == 2:
            rut = input("Ingrese rut: ")
            if rut in clientes:
                clientes.pop(rut)
            else:
                print("El rut no existe")
        elif opcion == 3:
            rut = input("Ingrese rut: ")
            if rut in clientes:
                for clave, valor in clientes[rut].items():
                    print(clave, ': ', valor)
        elif opcion == 4:
            for clave, valor in clientes.items():
                print(clave, valor['nombre'])
        elif opcion == 5:
            for clave, valor in clientes.items():
                if valor['preferente']:
                    print(clave, valor["nombre"])
        elif opcion == 6:
            print("Adios")
            break
        else:
            print("Ingrese una opcion correcta")

clientes()