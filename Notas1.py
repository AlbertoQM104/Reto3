## Reto N° 2

# Ingresar el nombre de un alumno, pedir las notas que va a tener dicho alumno, 
# obtener el promedio, la nota mayor y la menor (range(5)--> [0:4] | while )

# import os       ## importado para el clear

print("      --- INGRESO DE NOTAS ---")
print("-------------------------------------")

notas = []
i = 0
u = 0        

while True:
        nombre = input("Ingresa el nombre del Alumno: ")

        if nombre.isalpha():        # verifica si el str ingresado no es int

            while True:
                try:
                    cant = int(input(f"Ingrese cuantas notas va a tener el alumno {nombre}: "))
                    while True:    
                        try:
                            nota = int(input(f"Ingresa la nota número {i+1}: "))
                            if nota<=20 and nota>=0:
                                notas.append(nota)
                                i +=1
                                print("--------------------------------")
                            else:
                                print("La Nota ingresa no está en el rango [0-20]\n")
                                
                            if i == cant:
                                break
                        except Exception:
                            print("La nota ingresada es incorrecta\n")
                    break
                except Exception:
                    print("El valor ingresado es incorrecto!\n")
            break
        else:
            print("El valor ingresado no es un Nombre!\n")
            # clear = lambda: os.system('clear')   ## para poder realizar el limpiado 
            # clear()


print("==================")
print(f"      {nombre}")
print("==================")
for i in notas:
    u += 1
    print(f"La nota {u} es: {i}")
print("---------------------------------")
print(f"El Promedio de las notas es: {sum(notas)/len(notas)}")
print(f"La nota Mayor es: {max(notas)}")
print(f"La nota Menor es: {min(notas)}")
print("=================================")
























