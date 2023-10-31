# REPASO PYTHON
## 1.TIPOS DE DATOS
 * *TIPOS DE DATOS PRIMITIVOS* 
 * *'a' -->string cadena de texto*
 * *'hola' -->esto tambien es un string*
 * *'hola' --> soy un strig y te saludo' # cadena larga*
>#### OBSERVACIÓN: todo lo que este entre comillas es un string 
>* *'100'*,
>*'false'*,
>*'hola'*.
>### Un string puede estar entre comillas simples o dobles 
>
>* *100 -->etse es un tipo de dato númerico entero* 
>* *2.1 --> este es un tipo de dato numerioc flotante*
>* *False --> este es un tipo de dato boleano falso* 
>* *true -->tipo de dato boleano verdadero*
## 2. VARIABLES
* *Es donde almacenamos nuestros tipos de datos.*
* *Esos datos pueden mutar o ccambiar o modificarse.*
* *Como creamos una variable para almacenar nuestros datos.*
* *1.Darle un nombre significante o realacionado al dato que estamos almacenando.*
* *2. Indicarle a que dato esta relacionado -> asignacion*
* *3. indicar el tipo de dato que va a almcenar -> darle el dato a guardar*
* *primero el dato voy a pedir la edad de nadine* 
```python
edad_nadine=18 
```
## 3.OPERADORES
###  *Operadores aritmetricos*
*suma*,*resta*,
*multiplicacion*,*division*.
#### *suma=45+12* 
#### *resta=45-12*
#### *multiplicacion=45 * 2*
#### *division=45/5*
```python
operacion=(45+12+23)/4
op=15+12+14/4
```
### Operadores de Presedencia
* suma=45+42   *operador suma resulatado 87*
* suma='45'+12 *operador concatenacion resultado 4512*
* saludo ='hola'+'+mundo' *concatenacion holamundo*
* saludo2='hola'+''+'mundo' *concatenar hola mundo*
* saludos='hola'* 2  *holahola*
## 5. funciones
### Controles de flujo
* *solo se ejecuta si cumple o si las condiciones es verdadera podemos hacer que su condiciones es false se ejecute otro codigo*
### Decisiones
* *expecifica el codigo que se ejecutara si se cumple una decision*
```python
if <condicion:
´´´´
* el codigo que deseamos ejecutar si la condicxion es verdad 
print ("ejecuta esto")
* aqui estamos fuera del if o del si este codigo siempre se ejecutara no depende.
print("esto siempre ejecutara ")
* si queremos que se ejecute un codigo en caso sea falsa 
if <condicion falsa >:
print("solo imprime si es verdad 
else :
print("solo imprime  si es falso")
# ejemplo 
if 15>18
print("si es verdad imprime esto ")
else:
print(" si es verdad falso imprime esto ")
if 15*2==30
print(si es verdad imprime esto" )
else:
print(" si es falso imprime esto")
condicion 
```
# Ciclos
* *existen dos tipos*
* *cuando sabes la cantidad de veces que vamos a repetir*
* *para este caso existe el for*
* *sintaxis despues de la palabra reservada for debemos crear una variable que almacene el numero que iremos iterando*
* *luego tendremos que indicar el rango a iterar a los elemntos a iterar*
 ```python
 vocales=('a','e','i','o','u')
 for i in vocales:
print (i)
 ```
* *iterar cuando sabes la cantidad  de veces*


# falta algo




* *en esta funcion nos muestra el numero de una lista*
```python
lista=[45,12,78,9,6,12]
numero_menor=main(lista)
print(numero_menor)
```
* *funcion para convertir de un strig a un numero entero*
```python
numero_strig=`100`
print(type(numero_strig))
numero_entero=int(numero_strig)
print(type(numero_entero))
```
* *funcion para converir de un strig a un numero entero*
```python
int('100') -> 100 -> entero
```
* *funcion para convertir un entero a un strig* 
```python
str(100) ->'100' -> strig
```
* *funcion de python que noos permite agregar elemntos al final de una lista*           
* *Esta funcion nos muestra el numero mayor de una lista.*
```python
lista=[45,12,78,3,24,50]
numero_mayor=max(lista)
print(numero_mayor)
```
### MIN
* **sta funcion nos muestra el numero menor de una lista.*
```python
Ejemplo:
lista=[45,12,78,9,6,12]
numero_menor=min(lista)
print(numero_menor)
```
### Funcion para convertir de un string a un numero entero
```python
numero_string='100'
print(type(numero_string))
numero_entero=int(numero_string)
int('100') # ->>   100  ->> entero
python
str(100) #  ->>  '100'  ->>  string
```
### APPEND
* *Funcion de python quenos permite agregar elementos al final de una lista*
```python
lista=[15,12,78]
elemento=10
lista.append(elemento)
print(lista)
```
### POP
* *Funcion de pythom que nos permite eliminar los elementos que se encuentran al final de una lista. Pop elimna y almacena lo eliminado(temporalmente).*
```python
lista=[15,12,78]
eliminado=lista.pop()
print(lista)
print(eliminado)
```
### INSERT
* *Funcion de python  que nos permite agregar elementos en cualquier posicion de una lista es se le tiene que pasar dos parametro, primero indiacarle el indice y segundo el dato que se va agregar.*
```python
lista_nombres=['jory','nadine','bichota']
lista_nombre.insert(1,'satan')
print(lista_nombres)
```
### Remove
* *uncion de python que nos permite eliminar  elementos de cualquier posicion de una lista, esta funcion recibe solo el elemento que deseamos eliminar.*
```python
lista=[4,5,6,7,8,]
lista.remove(6)
print(lista)
```
  * *Funcion que nos permite dividir en una lista una cadena.*
```python
cadena='Hola como estan'
lista=cadena.split()
print(lista)
url='wwww.google.com/id=70133573
id=url.split('=').pop()
print(id)
```
### funciones creadas

 * *funciones propias*
 * *pasos para crear una funcion propia* 
 * *hacer uso de la palabra reservada def*
 * *definir un nombre de funcion que describa que tarea va a realizar*
 * *establecer los parametros que resivira la funcion entre*
*parentesis ().*
 * *establecer que valor o dato va retornar mi funcion con la*
*palabra reservada return*
 * *Observacion =>> tambien podemos hacer uso de la funcion print () para retornar un mensaje en nuestra funcion*
 * *existen dos tipos de funciones los que no resiven ningun parametro y los que resiven parametros*
```python
def saludo():
print('hola este es un saludo'
```
* *como hacemos uso de la funcion??*
* *nombre de la funcion y parentesis*
#### funciones de parametros
```python
def mi_print(texto):
    print(texto)
     
     print('hola este es print de  python')
     mi_print('hola este es mi print creado')


def suma(a+b)
 total=a+b
 return total
 mi_print(suma(45,12))  -->57
 ```  
 * *ejemplo*
 * *para que se usa esta funcion para monstrar el valor maximo de una lista*
 ```python
 lista=^[12,4,45,78,3,1]  
 mi_print(max(lista)) ---->
 def mi_max(lista):
    numero_mayor=lsita[0]
    for numero in lsita:
        if numero > numero_mayor:
            numero_mayor=numero
            return numero_mayor
            mi_print(mi_max(lista))
``` 
* *funciones con muchos paramatros*
 ```python
 def funciones()