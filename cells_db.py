#cell_db.py

def leer_datos( path ):
    file = open(path, 'rt')
    lista_final=[]
    dic_cel={}
    datos = file.readlines()
    #print(datos)
    for ren in range(len(datos)):
        datos[ren]=datos[ren].strip().split(',')
    #print(datos)
    for ren in range(1 , len(datos), 1):
        dic_cel={}
        for col in range( len(datos[ren])):
            dic_cel[datos[0][col].strip()]= datos[ren][col]
        lista_final.append(dic_cel)
    #print(lista_final)
    return lista_final

def salida_formato( celular ):
    print(f"Celular marca { celular['marca'] } ")
    print(f"\t Modelo: { celular['modelo'] }")
    print(f"\t Alm.: { celular['almacenamiento'] }")
    print(f"\t Vel.: { celular['velocidad'] }")
    print(f"\t Memoria interna: { celular['ram'] }")
    print(f"\t Color: { celular['color'] }")
    
def main():
    archivo = "celulares.txt"
    bd = leer_datos(archivo)
    print(f"DB = {bd}")
    salida_formato(bd[6])
main()
