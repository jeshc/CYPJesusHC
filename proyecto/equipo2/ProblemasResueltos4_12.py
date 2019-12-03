A= []
N=int(input("Ingrese la dimension del arreglo"))
if 1<=N and N<=50:
    I =1
    for K in range(I,N,1):
        J = 1
        for H in range(J,N,1):
            I = int(input("Ingrese e indice del arreglo"))
            J= int(input("Ingrese el indice del arreglo"))
            A.append(I)
            A.append(J)
            J+=1
        else: I+=1
    else:
        BAND=1
        I=1
        while I <= N and BAND==1:
            J=1
            while J<=1 and BAND==1:
                if A[I,J] == A[J,I]:
                    J+=1
                else:
                    BAND=0
            else:
                if BAND==1:
                    print("Es simetrica")
                else:
                    print("No es simetrica")
else:
    print("La dimension de la matriz no es correcta")
print("Fin del programa")
