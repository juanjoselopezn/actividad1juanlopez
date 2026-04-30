import os

salida = "his/hce.txt"

while True:
    print("Menu")
    print("1. Procesar archivos")
    print("2. Ver archivo generado")
    print("3. Salir")

    opcion = int(input("Ingrese opcion: "))

    if opcion == 1:
        if not os.path.exists("his"):
            os.makedirs("his")

        with open(salida, "w") as s:
            s.write("Id|Nombre|Apellido|Edad|Genero|FechaNacimiento|EPS\n")

            listarch = os.listdir("patients")

            for a in listarch:
                with open("patients/" + a, "r") as f:
                    i = f.readlines()[0].split("^")[1].strip()
                    n = f.readlines()[1].split("^")[1].strip()
                    ap = f.readlines()[2].split("^")[1].strip()
                    ed = f.readlines()[3].split("^")[1].strip()
                    g = f.readlines()[4].split("^")[1].strip()
                    fn = f.readlines()[5].split("^")[1].strip()
                    eps = f.readlines()[6].split("^")[1].strip()

                s.write(i + "|" + n + "|" + ap + "|" + ed + "|" + g + "|" + fn + "|" + eps + "\n")

        print("Procesado")

    elif opcion == 2:
        try:
            with open(salida, "r") as f:
                print("\nContenido:\n" + f.read())
        except:
            print("No existe el archivo")

    elif opcion == 3:
        print("Fin del programa")
        break

    else:
        print("Opcion incorrecta")