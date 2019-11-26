n = int(input("Ingrese el número de alumnos: "))
alumno = []
if 1 <= n <= 100:
    for i in range (n):
        alumno.append(float(input("Ingrese la calificación del alumno: ")))
    prom = 0
    taluma = 0
    talumr = 0
    cal8 = 0
    for i in range (n):
        if alumno[i] >= 6:
            taluma = taluma + 1
            if alumno[i] > 8:
                cal8 = cal8 + 1
        else:
            talumr = talumr + 1
        prom = prom + alumno[i]
    prom = prom / n
    print(f"El promedio del grupo es de: {prom}")
    print(f"El total de alumnos aprobados es de: {taluma}")
    print(f"El total de alumnos reprobados es de: {talumr}")
    porca = (taluma * 100) / n
    porcr = (talumr * 100) / n
    print(f"El porcentaje de alumnos aprobados es de: {porca}%")
    print(f"El porcentaje de alumnos reprobados es de: {porcr}%")
    print(f"El total de alumnos con calificación mayor a 8 es de: {cal8}")
else:
    print("El número de alumnos ingresados es incorrecto")
