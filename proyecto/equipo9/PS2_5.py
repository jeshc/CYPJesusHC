a = int(input("Dame el numero entero A:"))
b = int(input("Dame el numero entero B:"))
c = int(input("Dame el numero entero C:"))
d = int(input("Dame el numero entero D:"))
while d == 0:
    print("La división entre cero no está definida")
    d = int(input("Dame el numero entero D:"))
res = (a-c)**2/d
res2 = (a-b)**3/d
print(f"El resultado es:{res} y {res2}")
print("Fin del programa")
