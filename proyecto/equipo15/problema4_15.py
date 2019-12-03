N=int(input("Ingrese el numero de sucursales:"))
M=int(input("Ingrese el numero de anos:"))
i = 1
j = 1
MONTO = []
if (N>=1) and (N<=35) and (M>=1) and (M<=10):
        for i in range(1,M,1):
                for j in range(1,N,1):
                        MONTO.append(float(input(f"Ingrese ventas de la sucursal: {j}, en el ano {i}:")))
                MONTO.sort()
        MAX = 0
        for j in range(1,N,1):
                SUM = 0
                for i in range(1,M,1):
                        SUM = SUM + MONTO[i,j]
                if SUM > MAX:
                        MAX = SUM
                        SUC = j
        print(f"La sucursal que mas vendio fue: {SUC}")
        MAX =0
        for i in range(1,M,1):
                SUM = 0
                for j in range(1,N,1):
                        SUM += MONTO[i,j]
                PROM = SUM/N
                print(f"El promedio de ventas del ano: {i}, es: {PROM}")
                if PROM > MAX:
                        MAX = PROM
                        ANO = i
                i+= 1
        print(f"El ano con mayor promedio es: {ANO}")
else:
        print("Error en los datos")
print("Fin del programa! :D")

