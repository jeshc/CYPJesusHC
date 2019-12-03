X1 = float(input("Ingrese la coordenada en 'x' del punto 1: "))
Y1 = float(input("Ingrese la coordenada en 'y' del punto 1: "))
X2 = float(input("Ingrese la coordenada en 'x' del punto 2: "))
Y2 = float(input("Ingrese la coordenada en 'y' del punto 2: "))
X3 = float(input("Ingrese la coordenada en 'x' del punto 3: "))
Y3 = float(input("Ingrese la coordenada en 'y' del punto 3: "))

area_triangulo = 1/2 * abs(X1 * (Y2-Y3) + X2 * (Y3-Y1) + X3 * (Y1-Y2))

print("El area del triangulo es: ",area_triangulo)
