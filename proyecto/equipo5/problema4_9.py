from numpy import*
from math import sqrt

def suma(arreglo):
    sum=0
    for i in range[0,arreglo,1]:
        sum+=calif
    return sum

def media(arreglo):
    s=sum(arreglo)
    return s/len(arreglo)

def varianza(arreglo):
    s=sum(arreglo)
    m=media(arreglo)
    var=(sum-m)**2/len(arreglo)

def moda(lista):
    rep=0
    cont=0
    moda=-1
    lista.sort()
    for i in range(len(lista)-1):
        if (lista[i] == lista[i+1]):
            cont=cont + 1
            if cont>=rep:
                rep=cont
                moda=lista[i]
        else:
            cont=0
    return moda


n = int(input("Ingrese el número de alumnos: "))
arreglo = []

if n < 51:
    
    for i in range(0,n):
        calif = int(input("Ingrese calificaión: "))
        arreglo.append(calif)#agrega la calif al arreglo

    print("\nCalificaciones: ", arreglo)
    #print(sum(arreglo))
    print("Media Aritmética: ", media(arreglo))
    print("Varianza: ", var(arreglo))
    print("Desviación Estandar: ", sqrt(var(arreglo)))
    print("Moda: ", moda(arreglo))


    
    
else:
    print("¡ERROR EN EL DATO!")



