ARSU = 0
ARNO = 0
MERSU = 50000
MES = 0
ARCE = 0
for i in range(1 , 13 , 1):
    print(f" Mes { i }:")
    RNO = int(input("Promedio de lluvias del mes Zona Norte:"))
    RCE = int(input("Promedio de lluvias del mes Zona Centro:"))
    RSU = int(input("Promedio de lluvias del mes Zona Sur:"))
    
    ARNO = ARNO + RNO   # ARNO += RNO
    ARCE  = ARCE + RCE
    ARSU = ARSU + RSU

    if RSU < MERSU:
        MERSU = RSU
        MES = i
PRORCE = ARCE / 12
print(f"Promedio region centro:{ PROCE }")
print(f"Mes con menor lluvia en reg. sur:{ MES } ")
print(f"Registro del mes con menor lluvia es:{ MERSU }")

if ARNO > ARCE :
    if ARNO > ARSU:
        print("La region con mayor lluvia en la region norte")
    else:
        print("La region con mayor lluvia es la region sur")
elif ARCE > ARSU  :
    print("LA region con mayores lluvias es la region centro")
else:
    print("La region con mayores lluvias es la region sur")

print("Fin del programa!!!")
    









    
    
