# print tiene 4 formas de uso
"""
1.- con comas
2.- con signo '+'
3.- Con la función format()
4.- Es con una variante de format()
"""
# Con comas , concatenar agregando
#un espacio y haciendo casting de tipo
edad = 10
nombre = "Juan"
estatura = 1.67
print(edad , estatura , nombre )
# con '+' hace lo mismo pero no
# realiza el casting automático
# no agrega espacio
print( str(edad) + str(estatura) + nombre )

# 3.- funcion format()

print("Nombre: {1} Edad: {0} ".format(nombre, edad, estatura))

# 4.- con una variante de format() simplificada

print(f"Nombre: \"{nombre}\" \nEdad:\t{edad} ")

# print y el argumento end
print("Solo hay 10 tipos de personas, las que saben binario y las que no",end="---")
print("otra linea")







