PTDC = float ( input ( "Inserte el precio total de la compra del cliente: "))
if PTDC > 2500:
    D = PTDC * 0.08
    NP = PTDC - D
    print(f"El nuevo precio del cliente es {NP}.")
else:
    print(f"El precio es {PTDC}.")
print(f"Fin del programa.")
