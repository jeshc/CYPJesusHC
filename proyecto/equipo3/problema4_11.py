"""
El programa, dados tres arreglos unidimensionales sur, centro y norte,
que contienen los paises del sur,centro y norteamerica, respectivamente,
forma un cuarto arreglo en el cual aparecen todos los paises de
america ordenados alfabeticamente.
"""
print ("Ingrese el total de paises de Sur (tps), centro (tpc) y norteamerica (tpn).")
tps = int(input("tps: "))
tpc = int(input("tpc: "))
tpn = int(input("tpn: "))
if (1 <= tps <= 30) and (1 <= tpc <= 30) and (1 <= tpn <= 30):
    print("Ingrese los nobres de los paises de Sudamerica.")
    i = 1
    sur= []
    while (i <= tps):
        nue = input("Ingrese el nombre del pais: ")
        sur.append(nue)
        i += 1
        sur.sort()
    print("Ingrese los nobres de los paises de Centroamerica.")
    i = 1
    centro= []
    while (i <= tpc):
        nue = input("Ingrese el nombre del pais: ")
        centro.append(nue)
        i += 1
        centro.sort()
    print("Ingrese los nobres de los paises de Norteamerica.")
    i = 1
    norte= []
    while (i <= tpn):
        nue = input("Ingrese el nombre del pais: ")
        norte.append(nue)
        i += 1
        norte.sort()
    #print(sur)
    #print(centro)
    #print(norte)
    i = 1
    america = []
    for  i in sur:
        america.append(i)
    for  i in centro:
        america.append(i)
    for  i in norte:
        america.append(i)
    america.sort()
    print(america)
else:
    print("Verifique el numero de paises ingresados")
