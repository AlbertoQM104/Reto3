## Reto N° 2

#Ingresar el nombre de un alumno, pedir las notas que va a tener dicho alumno, 
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
                    nota = int(input(f"Ingresa la nota número {i+1}: "))
                    notas.append(nota)
                    i +=1
                    print("--------------------------------")
                    
                    if i == 5:
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
























