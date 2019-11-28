"""
Una persona compró una estancia en un país sudamericano. La extensión de la estancia está especificada
en "acres". Calcule e imprima la extensión del mismo en hectareas
"""
acres = float(input("Escribe el número de acres del terreno en metros cuadrados: "))
met=acres*4047
hectarea = met/10000
print("El número de acres en hectáreas es de: ",hectarea, "metros cuadrados" )
