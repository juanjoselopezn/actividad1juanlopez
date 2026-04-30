opcion = 0

while True:
    print("Menu")
    print("1. Ingresar paciente")
    print("2. Ver archivo")
    print("3. Salir")

    opcion = int(input("Ingrese opcion: "))

    if opcion == 1:
        archivo = "salida.txt"

        try:
            with open(archivo, "r") as f:
                l = f.readlines()
                i = len(l) + 1
        except:
            i = 1

        h = input("Nombre: ")
        a = input("Apellido: ")
        e = input("Edad: ")

        with open(archivo, "a") as f:
            f.write(str(i) + "|" + h + "|" + a + "|" + e + "|\n")

        print("Guardado")

    elif opcion == 2:
        archivo = "salida.txt"

        try:
            with open(archivo, "r") as f:
                print("\nContenido:\n" + f.read())
        except:
            print("No existe el archivo")

    elif opcion == 3:
        print("Fin del programa")
        break

    else:
        print("Opcion incorrecta")