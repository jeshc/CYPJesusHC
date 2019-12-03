Modelo = int(input("--Modelos de autos-- \n1. Blazer-Trail \n2. Cavalier \n3. Chevy \n4. Opel-Astra \n"
    "Escoga el modelo que desee, '1, 2, 3, 4':"))
if Modelo == 1:
    PB = float(input("Ingrese el precio del Blazer-Trail:"))
    NPB = PB - (PB * 0.8)
    print(f"El precio original del Blazer-Trail era de {PB}, El nuevo precio aplicando el descuento es {NPB}.")
elif Modelo == 2:
    PC = float(input("Ingrese el precio del Cavalier:"))
    NPC = PC - (PC * 0.5)
    print(f"El precio original del Cavalier era de {PC}, El nuevo precio aplicando el descuento es {NPC}.")
elif Modelo == 3:
    PCH = float(input("Ingrese el precio del Chevy:"))
    NPCH = PCH - ( PCH * 0.6)
    print(f"El precio original del Chevy era de {PCH}, El nuevo precio aplicando el descuento es {NPCH}")
elif Modelo == 4:
    POA = float(input("Ingrese el precio del Opel-Astra:"))
    NPOA = POA - (POA * 0.9)
    print(f"EL precio original del Opel-Astra era de {POA}, El nuevo precio aplicando el decueto es {NPOA}")

print("Fin del programa! :D")

