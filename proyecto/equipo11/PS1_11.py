X1 = float(input("Inserte la coordenada X de el vertice 1 (P1):"))
Y1 = float(input("Inserte la coordenada Y de el vertice 1 (P1):"))
X2 = float(input("Inserte la coordenada X de el vertice 2 (P2):"))
Y2 = float(input("Inserte la coordenada Y de el vertice 2 (P2):"))
X3 = float(input("Inserte la coordenada X de el vertice 3 (P3):"))
Y3 = float(input("Inserte la coordenada Y de el vertice 3 (P3):"))

D1 = ((X1 - X2) * 2 + (Y1 - Y2) * 2) ** 0.5
D2 = ((X2 - X3) * 2 + (Y2 - Y3) * 2) ** 0.5
D3 = ((X3 - X1) * 2 + (Y3 - Y1) * 2) ** 0.5

print(f"El perimetro del triangulo con lados {D1, D2, D3} es: {D1 + D2 + D3}")
