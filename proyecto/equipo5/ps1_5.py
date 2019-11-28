interesGanado = 0

cantidadDinero = float(input("Ingrese la cantidad de dinero que desea invertir: "))
tasaInteres = float(input("Ingrese la Tasa de Interés: "))

interesGanado = cantidadDinero*(tasaInteres/100)

print("Al final del mes usted recibira $%.2f" %(cantidadDinero+interesGanado))
print("Su ganancia fue de $%.2f" %(interesGanado))
