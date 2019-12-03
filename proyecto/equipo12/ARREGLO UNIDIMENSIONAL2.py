vec=(1,3,5,8,9,12,23,16,15,24,1,0,1,3,5,8,9,12,23,16,15,24,1,0,1,3,5,8,9,12,23,16,15,24,1,0,1,3,5,8,9,12,23,16,15,24,1,0,1,3,5,8,9,12,23,16,15,24,1,0,1,3,5,8,9,12,23,16,15,24,1,0,1,3,5,8,9,12,23,16,15,24,1,0,1,3,5,8,9,12,23,16,15,24,1,0)
n=int(input("Ingresa el numero de elementos del arreglo menor o igual a 500 elementos:"))
if (n>=1) and (n<=500):
 i=int(input("Ingresa el  valor:"))
for i in range(0,n,):
    print(vec[i])
i<=n
while True:
    j=i+1
    if j<=n:
        while True:
            vec[j]= vec[i]
            k=j
            while True:
                 vec[k]=vec[k+1]
                 k=k+1
                 break
                 n=n-1
print(f"Arreglo sin repeticiones {k}")
print("Fin del programa")
     
 
