N=int(input("Ingrese el numero de datos: "))
VEC=[]

if N>=1 and N<=50:
    I=0
    I+=1
    for I in range(1,N+1,1):
        VEC.append(int(input(f"Ingrese el dato {I}: ")))
        VEC.sort()
    print(VEC)
    X=int(input("Ingrese el dato a buscar: "))
    IZQ=1
    DER=N
    BAN=1
    while(IZQ<=DER and BAN==1):
        CEN= (IZQ+DER)//2
        if(VEC[CEN]==X):
           BAN=0
        else:
            if(X>(VEC[CEN])):
                IZQ=CEN+1
            else:
                DER=CEN-1
    if(BAN==1):
            print("El elemento no esta en el arreglo")
    else:
            print("El elemento si esta en el arreglo")
else:
    print("Error en los datos")
