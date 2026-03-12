reprobados = 0
aprobados = 0
excelentes = 0

cantidad_estudiantes = int(input("Ingrese la cantidad de estudiantes: "))

for i in range(cantidad_estudiantes):

    nombre = input("\nIngrese el nombre del estudiante: ")

    suma_notas = 0
    cantidad_notas = 0

    while True:

        nota = float(input("Ingrese una nota: "))
        suma_notas += nota
        cantidad_notas += 1

        otra = input("¿Desea agregar otra nota? (si/no): ")

        if otra.lower() != "si":
            break

    promedio = suma_notas / cantidad_notas

    if promedio < 3:
        estado = "Reprobado"
        reprobados += 1

    elif promedio < 4:
        estado = "Aprobado"
        aprobados += 1

    else:
        estado = "Excelente"
        excelentes += 1

    print("\nEstudiante:", nombre)
    print("Promedio:", round(promedio,2))
    print("Estado:", estado)

print("\nRESULTADOS FINALES")
print("Reprobados:", reprobados)
print("Aprobados:", aprobados)
print("Excelentes:", excelentes)                                                                                   