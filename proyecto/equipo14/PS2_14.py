import math
A=str(input("A:x^2  B:X/6   C:x^(1/2)   D:X^3+5\nIngrese la letre de la expresion que desea clacular(en mayuscula): "))
X=int(input("ingrese el valor de x (valor entero): "))
if A=="A":
    R=X**2
    print(f"el resultado es {R}")
elif A=="B":
    R=X/6
    print(f"el resultado es {R}")
elif A=="C":
    R=math.sqrt(X)
    print(f"el resultado es {R}")
elif A=="D":
    R=(X**3)+5
    print(f"el resultado es {R}")
else:
    print("error al selecionar")
