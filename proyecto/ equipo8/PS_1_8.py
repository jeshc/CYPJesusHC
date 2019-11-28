import math
RadioCono=float(input("Ingrese El Radio Del Cono: "))
AlturaCono=float(input("Ingrese La Altura Del Cono: "))
GeneratrizCono=float(input("Ingrese La Generatriz Del Cono: "))

area_base = math.pi * RadioCono **2
area_lateral = math.pi * RadioCono * GeneratrizCono
area_total = area_base + area_lateral
volumen = (area_base * AlturaCono)/3

print("")
print("El Area De La Base Del Cono Es De: ",area_base)
print("El Area Lateral Del Cono Es De: ",area_lateral)
print("El Area Total Del Cono Es De: ",area_total)
print("El Volumen Del Cono Es De: ",volumen)
