from model.Participante import Participante
import re
if __name__ == "__main__":
    listaParticipantes = []
    while (True):
        print("\n\nASISTENCIA EVENTO")
        print("1. Ingresar participante")
        print("2. ver estadisticas")
        print("3. Ver todos los participantes")
        print("4. Salir")
        try:
            opc = int(input("OPCION> "))
        except:
            opc = 0

        if opc == 1:
            print("\nINGRESAR PARTICIPANTE")
            while(True):
                 nombre = input("nombrey apellido: ")
                 if re.search("^[A-Z][a-z]*(\s[A-Z][a-z]*)$", nombre):
                     break
                 else:
                    print("ERROR :: Nombre no valido")
            while(True):
                try:
                   edad = int(input("Edad: "))
                except:
                    edad = 0
                if edad > 0:
                    break
                else:
                  print("ERROR :: Edad no valida")
            while(True):
                sexo = input("Sexo(M/F): ").upper()
                if sexo == "M" or sexo == "F":
                    break
                else:
                    print("ERROR:: sexo no valido")
                    participante = Participante(nombre, edad, sexo)
                    listaParticipantes.append(Participante)
        elif opc == 2:
            masculino = 0
            femenino = 0
            mayoredad = 0
            print("\nVER ESTADISTICAS")
            print("total de Participantes: " + str(len(listaParticipantes)))
            for p in listaParticipantes:
                if p.get_sexo()=="M":
                    masculino += 1
                else:
                    femenino += 1
                if p.get_edad() >= 18:
                    mayoredad += 1
            print("Total de hombres: " + str(masculino))
            print("Total de mujeres: " + str(femenino))
            print("total de mayores de edad:" + str(mayoredad))

        elif opc == 3:
            print("\nVER TODOS")
            for p in listaParticipantes:
                p.mostrar()
                print("\nVER TODOS")

        elif opc == 4:
             break

        else:
            print("ERROR")
