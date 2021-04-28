## Reto N° 1

# Ingresar 5 notas y obtener el promedio, la mayor nota y la menor

notas = []
i = 0

print("----- INGRESO DE NOTAS -----")

while True:

    n = int(input(f"Ingresa la nota N° {i+1}: "))

    try:
        n = int(n)
        notas.append(n)
        i += 1
    except ValueError:       ## en observación
        print("Debe ingresar un número entero")

    if (i == 5):
        break

print("\n------- Resultado -------")
print(f"Lista de Notas: {notas}")
print(f"Nota Mayor: {max(notas)}")
print(f"Nota Menor: {min(notas)}")
print(f"Nota Mayor: {sum(notas)/int(len(notas))}")
print("---------------------------")
    

















