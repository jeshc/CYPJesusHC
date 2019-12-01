distancia=float(input("Ingrese distancia de ida en KM: "))
distancia2=float(input("Ingrese distancia de vuelta en KM: "))
dias=int(input("¿Cuantos dias duro su estancia?: "))
distotal= distancia+distancia2
preciob=(distancia*0.23)
if distotal>800 or dias>7:
    print(f"El precio original es de: ${preciob}")
    descuento=preciob*0.30
    costov=preciob-descuento
else:
    costov=preciob
print(f"El Billete Costara: ${costov}")    
