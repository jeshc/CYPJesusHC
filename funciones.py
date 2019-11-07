def sumar( x  ,  y ):
    z = x + y
    return z

def restar ( x , y ):
    return x - y

def mi_print( texto ):
    print(f"Este es mi print: {texto} ")

def multiplica( valor , veces ):
    if veces == None :
        print("Debes enviar el segundo argumeno de la funcion")
    else :
        print( valor * veces )

def comanda( mesa , comensal , entrada , medio , fuerte , postre="Gela de limon"):
    print(f"Mesa: {mesa}  comensal:{comensal}")
    print(f"\t Entrada: { entrada }")
    print(f"\t Segundo tiempo: { medio } ")
    print(f"\t Plato fuerte: { fuerte } ")
    print(f"\t Postre: { postre }")

def comanda2( **comida ):
    llaves = comida.keys()
    for elem in llaves:
        print(elem, "->", comida[elem])

def imprime_argumentos( *argumentos):
    for index in range( len(argumentos) ):
        print(argumentos[index])
    
a = 10
b = 5
c = sumar(a,b)
print(f"La suma de {a} y {b} es {c}")
c = restar(a,b)
print(f"La resta de {a} y {b} es {c}")
mi_print("Hola!!!")
multiplica( 10 , 3 )
multiplica( 10 , None )
multiplica ('hola' , 3)
comanda(2, 1 ,"Ensalada","sopa de rana","Filete de pompi de sirena", "Flan" )
comanda("Ensalada","sopa de rana","Filete de pompi de sirena", "Flan",2,1 )
comanda(entrada="Ensalada",medio="sopa de rana",fuerte="Filete de pompi de sirena", postre="Flan",mesa=2,comensal=1 )
comanda(entrada="Ensalada",medio="sopa de rana",fuerte="Filete de pompi de sirena",mesa=2,comensal=1 )
imprime_argumentos('Hola',True, 3.1416, 1000, {'id':'sc01', 'nombre':'juan'} )
imprime_argumentos()
comanda2(entrada="Ensalada",medio="sopa de rana",fuerte="Filete de pompi de sirena",mesa=2,comensal=1 , postre="Strudel de manzana" , bebida='coca ligth')










