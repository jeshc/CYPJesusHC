"""
Dado un numero 'y' calcula el resultado de una funcion seccionada.
   3= y + 36           si 0 < y <= 11
   y**2 -10            si 11 < y <= 33
x= y**3 + y**2 -1      si 33 < y <= 64
   0                   para cualquier otro valor de y
"""
y = float(input("Ingrese el valor de 'y' = "))
if (0 < y <= 11):
    x = y + 33
    # x = 3
    print(f"El valor de 'x' es: {x} y el valor de 'y' fue: {y}")
elif (11 < y <= 33):
    print(f" El valor de 'x' es: {y**2 -10} y el valor de 'y' fue: {y}.")
elif (33 <y <= 64):
    print(f" El valor de 'x' es: {y**3 + y**2 -1} y el valor de 'y' fue: {y}.")
else:
    print(f" El valor de 'x' es: 0 y el valor de 'y' fue: {y}.")
