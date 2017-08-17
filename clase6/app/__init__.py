if  __name__ == '__main__':
    lista1 = []
    lista2 = []

    while True:
        print("\tCOMPAÑIA ABC")
        print('1. Agregar vendedor')
        print('2. Ver total')
        print('3. Salir')
        try:
            opc = int(input("OPCION: "))
        except ValueError:
            opc = 0

        if opc == 1:
           print("\nVamos a ingresar datos de un vendedor")
           vendInsertar = input("Nombre del vendedor: ")
        if vendInsertar not in lista1:
           lista1.append(vendInsertar)
           ventasInsertar = int(input("Cantidad vendida del vendededor: "))
        if ventasInsertar not in lista2:
           lista2.append(ventasInsertar)

        elif opc==2
         print("COMPAÑIA ABC")
         sumlista2 = 0
        for i in range(0, len(lista2)):
                sumlista2 = ventasInsertar + lista2[i]
        print(sumlista2)







