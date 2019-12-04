votos=[]
votos.append(None)
for i in range (0,12,1):
    votos.append(0)
candidato=int(input("Ingrese el primer voto \n(recuerde que los candidatos estan asignados del 1 al 12,\ningrese -1 para dejar de votar): "))
while candidato<-1 or candidato>-1:
    votos[candidato]+=1
    candidato=int(input("Siguiente voto?: "))
print("Total de votos por candidato: ")
for i in range(1,13,1):
    print(f" Candidato {i}: {votos[i]}")
ganador=1
maxvot=votos[1]
totalvot=votos[1]
for i in range (2,12,1):
    if votos[i]>maxvot:
        ganador=i
        maxvot=votos[i]
    totalvot+=votos[i]
print("Total de votos: ",totalvot)
print(f"Candidato ganador: {ganador}\nTotal de votos obtenidos: {maxvot}\nPorcentaje de votos obtenidos: {maxvot/totalvot}")
print("fin del programa")
