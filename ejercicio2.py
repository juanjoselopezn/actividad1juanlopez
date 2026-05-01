import os

salida = "his/hce.txt"

while True:
    print("Menu:")
    print("1. Procesar archivos")
    print("2. Ver archivo generado")
    print("3. Salir")

    opcion = int(input("Ingrese opcion: "))

    if opcion == 1:
        if not os.path.exists("his"):
            os.makedirs("his")

        with open(salida, "w") as s:
            s.write("Nombre|Documento|EPS|Edad|Genero\n")

            listarch = os.listdir("patients")

            for a in listarch:
                with open("patients/" + a, "r") as f:
                    l = f.readlines()

                    nombre = l[3].split("|")[4].split("^")[1].strip()
                    documento = l[3].split("|")[5].strip()
                    eps = l[3].split("|")[6].strip()
                    edad = l[3].split("|")[7].strip()
                    genero = l[3].split("|")[-1].strip()

                    s.write(nombre + "|" + documento + "|" + eps + "|" + edad + "|" + genero + "\n")

        print("Procesado correctamente")

    elif opcion == 2:
        try:
            with open(salida, "r") as f:
                print("Contenido:\n" + f.read())
        except:
            print("No existe el archivo")

    elif opcion == 3:
        print("Fin del programa")
        break

    else:
        print("Opcion incorrecta")