"""Compruebe la igualdad de la siguiente expresión
(A/B)**N = (A**N)/(B**N)
"""
A = int(input("Escribe el valor de A: "))
B = int(input("Escribe el valor de B: "))
N = int(input("Escribe el valor de la potencia: "))
OP1 = (A/B)**N
OP2 = (A**N)/(B**N)
print("El valor de(A/B)**N es: ", OP1)
print("El valor de(A**N)/(B**N)es: ", OP2)

