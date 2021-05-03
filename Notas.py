## Reto N° 1

# Ingresar 5 notas y obtener el promedio, la mayor nota y la menor

notas = []
i = 0

print("----- INGRESO DE NOTAS -----")
print("----------------------------")

while True:

    try:
        n = int(input(f"Ingresa la nota N° {i+1}: "))
        notas.append(n)
        i += 1
        if (i == 5):
            break
    except ValueError:       
        print("Debe ingresar un número entero\n")

print("\n------- Resultado -------")
print(f"Lista de Notas: {notas}")
print(f"Nota Mayor: {max(notas)}")
print(f"Nota Menor: {min(notas)}")
print(f"Nota Promedio: {sum(notas)/int(len(notas))}")
print("---------------------------")
    

















