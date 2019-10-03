CyP 2020
# Métodos String
String al ser un objeto, contiene métodos muy útiles a los cuales se les saca provecho en programas de cualquier nivel.


s= "programacion con python 3"

#### Una cadena es tratada como una lista(un arreglo en programación c)
```
s[0] #p
s[3] #g
s[-1] #3
s[-3] #n

```

#### Buscar cadena
find() regresa el indice de la primer coincidencia.
```
s.find( 'a')  # 5
```

#### Remplazar cadena

```
>>> s.replace('con','KoN')
'programacion KoN python 3'
>>> s
'programacion con python 3'
>>>
```


#### Formato capitalizado.
**capitalizado**
  Cambia a mayúsculas la primer letra.
**Título**
  Primera de cada palabra.
```
s.capitalize()
s.title()
```

### Mayúsculas
```
s.upper()
```



### Minúsculas



```
s.lower()
```



### Contar palabras en la cadena


```
 s.count('p')         #2
 s.count('python')    #1
```


### Formato centrado
center(40), Se cambia el tamaño del string y los elementos faltantes se llenan con el caracter espacio en blanco;

center(40,'f') se llenan con el caracter enviado como argumento.

```
s.center(40)     #        programacion con python 3        <- Aqui termina
s.center(40,'f') # fffffffprogramacion con python 3ffffffff
```



# Métodos de verificación - ¡Muy usados!

### Verificar si la cadena es alfanumérica o si contiene solo caracteres.

```
s.isalnum()  #False por los espacios
s.isalpha()  #False por los espacios
```



### Verificar si la cadena es un espacio

```
s.isspace() # true
```





### Verifica que tiene una mayúscula tipo titulo
```
s.istitle()                   # False
(s.capitalize()).istitle()    #True
```



### ¿Esta en mayúsculas o Minúsculas?
```
s.isupper()
s.islower()
```




### Termina en una caracter en especial
```
s.endswith('k')  #false
```





###  Eliminar espacios al inicio y al final
```
s= "     programacion con python 3       "
print(s)
print(s.strip())
#Por defecto usa espacio y lo mete en una lista


s.rstrip()  # trim a la derecha
s.lstrip()  # trima a la izquierda
```





###  Dividir Split ¡IMPORTANTE!
por defecto divide por espacios.
```
l=s.split()
print(l)
```
#Por defecto usa espacios y lo deja en su cadena

###  Dividir Split  con caracter específico.
```
l=s.plit('c')
print(l)        # ['   programa', 'ion ', 'on python 3       ']
```
