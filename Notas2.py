## Reto N° 3

# Ingrese la cantidad de alumnos a colocar notas, por cada alumno se ingresara 
# la cantidad de notas por alumno, obtener el promedio, la nota mayor y la menor.

        # [{
        #     "nombre" : "",
        #     "notas" : [],
        #     "promedio" : "",
        #     "nota_max" : "",
        #     "nota_min" : ""
        # }]

alumnos = []

## Ingreso de cantidad de alumnos
while True:
        try:
                print("=====================================")
                print(" -------------- NOTAS -------------- ")
                print("=====================================")
                cant_alum = int(input("Ingrese la cantidad de Alumnos: "))
                print("------------------------------------------")
                if cant_alum<=10:
                        break
                else:
                        print("El valor ingresado es mayor a 10.")
                        print("INTENTA OTRA VEZ!\n\n")
        except Exception:
                print("Dato Ingresado Incorrecto!\n\n")

## Ingreso de los nombres de los alumnos
for i in range(cant_alum):
        alumnos.append({})     ## Añade data a la lista
        alumno = alumnos[i]

        while True:
                alumno["Nombre"] = input(f"Ingresa el nombre del alumno N° {i+1}: ")
                print("------------------------------------------")
                if alumno["Nombre"].isalpha():  ## Verifica si ingresa una cadena
                        break
                else:
                        print("El valor ingresado no es String")
                        print("Intentelo otra vez...\n")

        alumno["Notas"] = []

        while True:
                try:
                        cant_notas = int(input("Ingresa la cantidad de Notas: "))  ## Ingresa la cantidad de notas
                        print("------------------------------------------")
                        if cant_notas<=10:
                                break
                        else:
                                print("El valor ingresado es mayor a 10.")
                                print("INTENTA OTRA VEZ!\n\n")
                except Exception:
                        print("El valor ingresado es errado!\n")

        j = 0

        while j<cant_notas :
                try:
                        nota = int(input(f"Ingresa nota {j+1}: "))
                        alumno["Notas"].append(nota)   ## Añade dato a la lista 
                        j += 1

                        if j == cant_notas:
                                print("------------------------------------------")
                                print("\n")

                except Exception:
                        print("El valor ingresado es incorrecto!")
                        print("Intenta otra vez...\n")
        
        prom = 0

        for n in alumno["Notas"]:
                prom += nota 

        alumno["Nota Promedio"] = prom / cant_notas
        alumno["Nota Maxima"] = min(alumno["Notas"])
        alumno["Nota Minimo"] = max(alumno["Notas"])

print("============================================================")
print(alumnos)