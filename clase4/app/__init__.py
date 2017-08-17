def imprimir_lista(x):
    print("\nMi lista de supermercado...")
    for a in x:
        print(str((int(x.index(a)+1))) +". " + a)

def imprimir_diccionario(w):

if  __name__ == '__main__':
    #lista = []#
    diccionario = {}

    while True:
        print("LISTA DE SUPERMERCADO")
        print('1. Agregar elemento')
        print('2. Quitar elemento')
        print('3. Ver lista')
        print('4. Salir')
        try:
            opc = int(input("OPCION: "))
        except ValueError:
             opc=0

        if opc == 1:
            print("\nVamos a ingresar un articulo a la lista..")
            artInsertar = input("Articulo: ")
            if artInsertar not in lista:
                lista.append(artInsertar)
            else:
                print("Articulo ya en la lista")

        elif opc == 2:
            print("\nvamos a quitar un articulo de la lista...")
            imprimir_lista(lista)
            artBorrar = input("Articulo: ")
            if artBorrar in lista:
                lista.remove(artBorrar)

            else:
                print("Lo siento... Articulo no encontrado")
        elif opc == 3:
            imprimir_lista(lista)
        elif opc == 4:
            print("OPCION 4")
            break
        else:
            print("ERROR: : Opcion no valida")
    print("Hasta luego")

