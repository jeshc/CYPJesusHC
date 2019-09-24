a = int(input("Dame el primer número: "))
b = int(input("Dame el segundo número: "))
c = int(input("Dame el tercer número: "))
if a > b and a > c:
    print(f"{a} es el número más grande")
if b > a and b > c:
    print(f"{b} es el número más grande")
if c > a and c > b:
    print(f"{c} es el número más grande")

print("Otra solucion")
if a != b and a != c and b != c:
    if a > b and a > c:
        print(a, "es el mayor")
    else:
        if b > a and b > c:
            print(b , "es el mayor")
        else:
            print(c , "es el mayor")


print("La misma pero simplificada:")
if a != b and a != c and b != c:
    if a > b and a >c:
        print(a, "es el mayor")
    elif b > a and b > c :
        print(b , "es el mayor")
    if:
        print(c,"es el mayor")
