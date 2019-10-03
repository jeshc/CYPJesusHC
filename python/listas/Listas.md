# Listas
###La estructura de datos lista tienen las siguientes caracteristicas:
- Puede contener 0 ó mas elementos,[]
- Son buenas para almacenar datos en orden.
- Los elementos pueden ser de diferentes tipos. ["Manzana", 12.9,"10"]
- Pueden ser anidados y crear estructuras de datos mas complejas. [manzana,["Melón chino","Melón valenciano ","Melón galia", ]]
- Estructura secuencial.
- Se puede crear usando [] y usando List().
- Son mutables. ¡Vaya que lo son!.

Ejemplo:
```
lista1=[]
datos=["pera","manzana",20, 2.30,True]
dias_semana=["lunes","martes","miercoles","jueves","viernes","sabado","domingo"]

```

### Otras formas de crear Listas
** A partir de una tupla **
```
mi_tupla=('servidor','disco duro','NAS')
activos=list(mi_tupla) # ['servidor', 'disco duro', 'NAS']
```

 ** A partir de strings**

 ```
 fecha='12/05/2019'
 fecha_separada=fecha.split('/') # ['12', '05', '2019']

 crudos="124,2323,-42,34,1025,34,134211"
 datos=crudos.split(',')  #  ['124', '2323', '-42', '34', '1025', '34', '134211']
 ```

 #### de lista de strings a string
 Es posible convertir un arreglo a un sólo string , pero éste debe ser tipo str.

 ```
 dias_semana=["lunes","martes","miercoles","jueves","viernes","sabado","domingo"]
 print(','.join(dias_semana))
 #lunes,martes,miercoles,jueves,viernes,sabado,domingo
 ```
**Las listas son mutables**. Puede cambiar un elemento de lugar, agregar nuevos elementos y eliminar o sobrescribir elementos existentes. El mismo valor puede ocurrir más de una vez en una lista.

```
#intercambio
dias_semana=["lunes","martes","miercoles","jueves","viernes","sabado","domingo"]
tmp=dias_semana[1]
dias_semana[1]=dias_semana[0]
dias_semana[0]=tmp
```
# Eliminar
dias_semana.remove("martes") # ['lunes', 'miercoles', 'jueves', 'viernes', 'sabado', 'domingo']


## Eliminar en una posición específica
```
# opcion 1 con remove()
dias_semana.remove("martes") # ['lunes', 'miercoles', 'jueves', 'viernes', 'sabado', 'domingo']
# Opcion 2 con del
del dias_semana[0] # elimina "lunes"
```



## vaciar una lista
```
dias_semana.clear()
print("Dias:" , dias_semana) # []
```

### Insertar en una posición específica
```
dias_semana.insert(1,"martes")

```
## Modificar un elemento usando []

```
dias_semana[0]="un dia"
print(dias_semana) # ['un dia', 'martes', 'miercoles', 'jueves', 'viernes', 'sabado', 'domingo']
```

## Ordenar

```
lista1=['Kiwi', 'Manzana', 'Naranja', 'Pera']
print(lista1.sort())
print("Lista:" , lista1) # Lista: ['Kiwi', 'Manzana', 'Naranja', 'Pera']
```

### Orden inverso
```
dias_semana.reverse()    # ['domingo', 'sabado', 'viernes', 'jueves', 'miercoles', 'lunes']
```
# Slicing
Las listas pueden ser rebanadas con el operador [::] de la forma:
```
[<inicio>:<fin>:<step>]

Valores por defecto:
<inicio> =0
<fin> = tamaño de la lista
<step> = 1
```
Ejemplos
```
numeros=[0,1,2,3,4,5,6,7,8,9]
print(numeros[::])        # [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
print(numeros[::-1])      # [9, 8, 7, 6, 5, 4, 3, 2, 1, 0]
print(numeros[::2])       # [0, 2, 4, 6, 8]
print(numeros[:6:])       # [0, 1, 2, 3, 4, 5]
print(numeros[-4:-9:-1])  # [6, 5, 4, 3, 2]
```
## Sustituir segmentos con Slicing

```
numeros=[0,1,2,3,4,5,6,7,8,9]
numeros[2:7]=[-4]
print(numeros) #[0, 1, -4, 7, 8, 9]
```


## Probar existencia de elemento

```
numeros=[0,1,2,3,4,5,6,7,8,9]
print(3 in numeros) # True
```

## Listas de Listas

```
autos=["Mazda","Honda","VW", "Akura","Ford"]
motocicletas=["Suzuki", "Vento","BMW", "Kawasaki", "Ducatti"]
bicicletas=["Benotto","Alubike"]
vehiculos=[autos,motocicletas,bicicletas]

```

resultado:

```
[['Mazda', 'Honda', 'VW', 'Akura', 'Ford'], ['Suzuki', 'Vento', 'BMW', 'Kawasaki', 'Ducatti'], ['Benotto', 'Alubike']]
```

Preguntas:¿Qué imprimirán las siguientes expresiones?

```
print(vehiculos[1])   # ['Suzuki', 'Vento', 'BMW', 'Kawasaki', 'Ducatti']

print(vehiculos[2][0]) # Benotto

print(vehiculos[2]) # ?

print(vehiculos[2][1]) # ?

print(vehiculos[0][3]) # ?

print(vehiculos[1][3]) # ?

print(vehiculos[0][0]) # ?

print(vehiculos[4][4]) # ?

print(vehiculos[0][4]) # ?
```

**Preguntas nivel ninja:**
```
print(vehiculos[1][1:4])   # ?

print(vehiculos[0:2])   # ?

print(vehiculos[2][0][2]) # ??
```

## Extender Listas

Con la funcion extends, el cual agrega a una lista existente otra lista.

```
numeros=[0,1,2,3,4,5,6,7,8,9]
dias_semana=["lunes","martes","miercoles","jueves","viernes","sabado","domingo"]
numeros.extend(dias_semana)
print(numeros) #[0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 'lunes', 'martes', 'miercoles', 'jueves', 'viernes', 'sabado', 'domingo']
```

## Extender con el operador +=
El mismo resultado que **extend**
```
numeros += dias_semana #[0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 'lunes', 'martes', 'miercoles', 'jueves', 'viernes', 'sabado', 'domingo']
```

# Multiplicar Listas
Al multiplicar las listas por un entero duplica los elementos internos.
```
numeros*2 # [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
```

# append() y pop()
En conbinación estos dos métodos nos permiten simular una estructura de datos pila.

```
alturas=list()
alturas.append(1.82) # [1.82]
alturas.append(1.76) # [1.82,1.76]
alturas.append(1.66) # [1.82,1.76,1.66]
alt=alturas.pop()    # [1.82,1.76]
```
## unpacking de lista
```
fecha= ['12', '05', '2019']
d,m,a=fecha
print(d)  # 12
print(m)  #5
print(a)  #2019
```

## Listas y la estructura de control for
```
dias_semana=["lunes","martes","miercoles","jueves","viernes","sabado","domingo"]
for dia in dias_semana:
    print(dia.upper())
```

Resultado:
```
LUNES
MARTES
MIERCOLES
JUEVES
VIERNES
SABADO
DOMINGO
```


# Resumen de métodos de las listas.
- append
- clear
- copy
- count
- extend
- index
- insert
- pop
- remove
- reverse
- sort
