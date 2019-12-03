opcion = int(input("--Opciones-- \n1. Pulgadas a milimetros \n2. Yardas a metros \n3. Millas a kilometros \n"
    "Ingrese la opcion que necesite:"))
if opcion == 1:
    pulgadas = float(input("Ingrese las pulgadas:"))
    milimetros = pulgadas * 25.40
    print(f"{pulgadas} pulgadas equivalen a {milimetros} milimetros.")
elif opcion == 2:
    yardas = float(input("Ingrese las yardas:"))
    metros = yardas * 0.9144
    print(f" {yardas} yardas es igual a {metros} metros ")
elif opcion == 3:
    millas = float(input("Ingrese las millas:"))
    kilometros = millas * 1.6093
    print(f" {millas} millas es igual a {kilometros} kilometros")
print("Fin del programa! :D")


