print("Asigne un valor de tipo entero a las siguientes variables: ")
A = int(input("A = "))
B = int(input("B = "))

if A == B:
    print("A es divisor de B y viceversa")
elif A % B == 0:
    print(f"B = {B} es divisor de A = {A}:")
    print(f"Cociente: {A/B}")
    print(f"Residuo: {A%B}")
elif B % A == 0:
     print(f"A = {A} es divisor de B = {B}:")
     print(f"Cociente: {B/A}")
     print(f"Residuo: {B%A}")    
else:
    print("Ninguno de los numeros dados es divisor del otro")
