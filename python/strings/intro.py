nombre = "José Sosa"
print(nombre)
print(nombre[0])
print(nombre[8])
print(nombre[-1])
print(nombre[-4])
#slicing
print(nombre[1:3:1])
# valores por defecto de slicing
print(nombre[5::1])
print(nombre[:4:2])

# slicing negativo
print(nombre[-1:-5:-1])
print(nombre[::-1])
print(nombre[-6::-1])
frase = "Solo existen 10 tipos de personas, las que saben binario y las que no"
# ghacer un slicing para imprimir la palabra existen

# hacer otro para impimir la palabra personas en orden inverso: sanosrep

# hacer un slicin que imprima toda la frase en orden inverso.


print(dir(nombre))
print("Funciones de string (str)")
print(nombre.upper())
print(f"la palabra 'existen' esta en la pos. {frase.find('existen')} ")



