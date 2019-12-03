def Suma(a,b):
    return a+b
def Resta(a,b):
    return a-b
def Multiplicacion(a,b):
    return a*b
def divicion(a,b):
    return a/b
C=str(input("ingrese el simbolo de la opearacion que desea realizar\n(Suma:+     Resta:-       Multiplicacion:*        Divicion:/): "))
A=float(input("ingrese el primer valor a operar: "))
B=float(input("ingrese el segundo valor a operar: "))
if C == "+":
    D = Suma(A,B)
elif C == "-":
    D = Resta(A,B)
elif C == "*":
    D = Multiplicacion(A,B)
elif C == "/":
    D = divicion(A,B)
else:
    D = "error al ingresar el signo de la operacion"
print(f"el resultado es: {D}")
