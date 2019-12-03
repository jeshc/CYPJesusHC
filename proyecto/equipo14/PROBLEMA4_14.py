for i in range(1,13,1):
    for j in range(1,4,1):
        PROD=float(input(f"ingrese costos de produccion en el mes {i}, de departamento {j}: "))
        if i==1:
            if j==1:
                PROD1_1=PROD
            elif j==2:
                PROD1_2=PROD
            elif j==3:
                PROD1_3=PROD
        elif i==2:
            if j==1:
                PROD2_1=PROD
            elif j==2:
                PROD2_2=PROD
            elif j==3:
                PROD2_3=PROD
        elif i==3:
            if j==1:
                PROD3_1=PROD
            elif j==2:
                PROD3_2=PROD
            elif j==3:
                PROD3_3=PROD
        elif i==4:
            if j==1:
                PROD4_1=PROD
            elif j==2:
                PROD4_2=PROD
            elif j==3:
                PROD4_3=PROD
        elif i==5:
            if j==1:
                PROD5_1=PROD
            elif j==2:
                PROD5_2=PROD
            elif j==3:
                PROD5_3=PROD
        elif i==6:
            if j==1:
                PROD6_1=PROD
            elif j==2:
                PROD6_2=PROD
            elif j==3:
                PROD6_3=PROD
        elif i==7:
            if j==1:
                PROD7_1=PROD
            elif j==2:
                PROD7_2=PROD
            elif j==3:
                PROD7_3=PROD
        elif i==8:
            if j==1:
                PROD8_1=PROD
            elif j==2:
                PROD8_2=PROD
            elif j==3:
                PROD8_3=PROD
        elif i==9:
            if j==1:
                PROD9_1=PROD
            elif j==2:
                PROD9_2=PROD
            elif j==3:
                PROD9_3=PROD
        elif i==10:
            if j==1:
                PROD10_1=PROD
            elif j==2:
                PROD10_2=PROD
            elif j==3:
                PROD10_3=PROD
        elif i==11:
            if j==1:
                PROD11_1=PROD
            elif j==2:
                PROD11_2=PROD
            elif j==3:
                PROD11_3=PROD
        elif i==12:
            if j==1:
                PROD12_1=PROD
            elif j==2:
                PROD12_2=PROD
            elif j==3:
                PROD12_3=PROD
for i in range(1,13,1):
    if i==1:
        PRODM=PROD1_1
    elif i==2:
        PRODM=PROD2_1
    elif i==3:
        PRODM=PROD3_1
    elif i==4:
        PRODM=PROD4_1
    elif i==5:
        PRODM=PROD5_1
    elif i==6:
        PRODM=PROD6_1
    elif i==7:
        PRODM=PROD7_1
    elif i==8:
        PRODM=PROD8_1
    elif i==9:
        PRODM=PROD9_1
    elif i==10:
        PRODM=PROD10_1
    elif i==11:
        PRODM=PROD11_1
    elif i==12:
        PRODM=PROD12_1
    MAYDUL=PRODM
    if MAYDUL<PROD:
        MES=i
print(f"En el mes {MES} se registro el mayor costo de produccion de dulces")
SUM=0
for i in range(1,13,1):
    if i==1:
        PRODS=PROD1_2
    elif i==2:
        PRODS=PROD2_2
    elif i==3:
        PRODS=PROD3_2
    elif i==4:
        PRODS=PROD4_2
    elif i==5:
        PRODS=PROD5_2
    elif i==6:
        PRODS=PROD6_2
    elif i==7:
        PRODS=PROD7_2
    elif i==8:
        PRODS=PROD8_2
    elif i==9:
        PRODS=PROD9_2
    elif i==10:
        PRODS=PROD10_2
    elif i==11:
        PRODS=PROD11_2
    elif i==12:
        PRODS=PROD12_2
    SUM=SUM+PRODS
    P=SUM/12
print(f"Promedio anual de costo de produccion de bebidas: {P}")
MESMAY=1
MESMEN=1
for i in range(1,13,1):
    if i==1:
        PRODC=PROD1_2
        MAYBEB=PRODC
        MENBEB=PRODC
    elif i==2:
        PRODC=PROD2_2
    elif i==3:
        PRODC=PROD3_2
    elif i==4:
        PRODC=PROD4_2
    elif i==5:
        PRODC=PROD5_2
    elif i==6:
        PRODC=PROD6_2
    elif i==7:
        PRODC=PROD7_2
    elif i==8:
        PRODC=PROD8_2
    elif i==9:
        PRODC=PROD9_2
    elif i==10:
        PRODC=PROD10_2
    elif i==11:
        PRODC=PROD11_2
    elif i==12:
        PRODC=PROD12_2
    if MAYBEB<PRODC:
        MAYBEB=PRODC
        MESMAY=i
    elif MENBEB > PRODC:
        MENBEB=PRODC
        MESMEN=i
print(f"En el mes {MESMAY} se registro el mayor costo de produccion de bebidas, y en el mes {MESMEN} el menor")
for j in range(1,4,1):
    if j==1:
        DM=PROD12_1
        MENOR=DM
        DEP=1
    elif j==2:
        DM=PROD12_2
    elif j==3:
        DM=PROD12_3
    
    if MENOR > DM:
        MENOR=DM
        DEP=i
print(f"El departamento {DEP} tuvo el menor costo en diciembre")

