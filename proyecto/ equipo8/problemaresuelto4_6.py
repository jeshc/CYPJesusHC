N=int(input("Ingrese el numero de elementos: "))
vector=[]
if N>=1 and N<=50:
    for i in range (0,N,1):
        vector.append(int(input("Ingrese dato: ")))
    for i in range (0,N-1,1):
        menor=vector[i]
        K=i
        for j in range (i+1,N,1):
            if vector[j]<menor:
                menor=vector[j]
                k=j
        vector[k]=vector[i]
        vector[i]=menor
    print("Arreglo ordenado")
    for i in range (0,N,):
        print(f"Posicion {i+1}",vector[i])
else:
    print("Error en los datos")
print("fin del programa")
