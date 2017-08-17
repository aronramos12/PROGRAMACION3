#Programa para aprende sintaxis basicas de Python

while (True):
    nombre = input("NOMBRE:")
    edad = int(input("EDAD"))


print("\nBienvenido, " + nombre + ". Tienes "+ str(edad)+ " años.")

if(edad < 18):
    print("\nEstas castigado")
elif(edad==18):
    print("\nPuedes salir\t...\tPero ven temprano")
else:
    print("\nLarga a trabajar")

    salida = input("desea continuar(S/N): ")
    if salida.upper() !="S" or salida != "s":
     break
    print (!Ciao!)