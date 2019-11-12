archivo = open("numeros.txt","rt")
print(dir(archivo))

numeros1 = archivo.read()
print(numeros1)
print(numeros1.split('\n'))
lista_num =[]
for linea in numeros1.split('\n'):
    for numero in linea.split(','):
        lista_num.append( int(numero) )
print(lista_num)
lista_num.sort()
print(f"\n Lista ordenada:{lista_num} \n")

print(f"El mayor es :{lista_num[-1]} y el menor es: {lista_num[0]}")
archivo.close()

archivo=open("numeros.txt","rt")
numeros2 = archivo.readlines()
print(numeros2)
archivo.close()

archivo=open("numeros.txt","rt")
numeros2 = archivo.readline()
print(numeros2)
archivo.close()


