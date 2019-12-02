SUE = float(input("Introduce tu sueldo:"))
if SUE >= 1000:
    NSUE = SUE * 0.12
    SUE += NSUE
    print(f"El nuevo sueldo es de: ${SUE}")
else:
    NSUE = SUE * 0.15
    SUE += NSUE 
    print(f"El nuevo sueldo es de: ${SUE}")
print("Fin del programa")

