print("Ejercicio 10. Cosecha.")


MESES = ['Enero', 'Febrero', 'Marzo', 'Abril', 'Mayo', 'Junio', 'Julio', 'Agosto', 'Septiembre', 'Octubre', 'Noviembre', 'Diciembre']
COSECHA = []

print("Por favor introduzca las toneladas que se cosecharon en cada mes.")
for i in range (0, 12, 1) :
    ASSIGN = float(input(f"Cosecha de {MESES[i]}: "))
    COSECHA.append(ASSIGN)

PROM = COSECHA[0]
MAYOR = COSECHA[0]
MES = 0
for i in range (1, 12, 1):
    PROM += COSECHA[i]
    if COSECHA[i] > MAYOR :
        MAYOR = COSECHA[i]
        MES = i
PROM /= 12

SUP = 0
INF = 0
for i in range (0, 12, 1):
    if COSECHA[i] > PROM :
        SUP += 1
    elif COSECHA[i] < PROM :
        INF += 1


print("Promedio Anual: ", PROM)
print("Cantidad de meses por encima del promedio: ", SUP)
print("Cantidad de meses por debajo del promedio: ", INF)
print(f"El mes en que la cosecha fue mayor es {MESES[MES]}, con {MAYOR} toneladas. ")
