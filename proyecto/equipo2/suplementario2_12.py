print("Ingrese la temperatura en grados Fahrenheit: ")
TEMP=input()
TEMP=int(TEMP)
if TEMP > 85:
    print("Se puede practicar Natacion")
elif 70<TEMP and TEMP<=85:
    print("Se puede practicar Tenis")
elif 32<TEMP and TEMP<=70:
    print("Se puede practicar Golf")
elif 10<TEMP and TEMP<=32:
    print("Se puede practicar Esqui")
elif TEMP<=10:
    print("Se puede practicar Marcha")
