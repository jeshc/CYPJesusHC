N = int(input("Ingrese el número de datos: "))
VECTOR = []
if N >= 1 and N <= 50:
    
    for I in range (0,N,1):
        
        VECTOR.append(int(input(f"Ingrese el dato {I}: ")))
              
        
    for I in range (1,len(VECTOR)):
        AUX= VECTOR[I]
        K = I-1
        while K >=0 and AUX <= VECTOR[K]:
            VECTOR[K+1]= VECTOR[K]
            K=K-1
            I+=1
        
            
        VECTOR[K+1]= AUX
  
    print("ARREGLO ORDENADO")
    
    for I in range (N):
        print(f"{VECTOR[I]}")
        
else:
    print("ERROR DE DATOS")
print("FIN DEL PROGRAMA")
