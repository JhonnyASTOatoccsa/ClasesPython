#1.
#crear un programa que me pida la edad de una persona
# si la edad es mayor o igual a 18 que me muestre un mensaje 'eres mayor de edad' 
#caso contrario que me muestre un mensaje 'eres menor de edad
#edad = int(input("Ingresa tu edad: "))
#if edad >= 18:
 #   print("Eres mayor de edad.")
#else:
 #   print("Eres menor de edad.")    

#Una tienda comercial desea hacer un descueto del 20%, crear un programa que me determine si el cliente se 
#hace acreedor del descueto teniendo encuenta los siguiente, si el cliente realiza una compra de igual o mayor a 
#1000 soles mostrar un mensaje que diga 'ganaste el descuento del 20% ahora pagaras <mostrar el total de la compra 
#menos el descuento en caso la compra no supere los 1000 soles entonces mostrar un mensaje que diga  
#'no aplicas al descuento <mostrar el monto de la compra>

#monto_compra = float(input("Ingrese el monto de la compra en soles: "))
#if monto_compra >= 1000:
   # descuento = monto_compra * 0.2
  #  total_con_descuento = monto_compra - descuento
 #   print("¡Ganaste el descuento del 20%! Ahora pagarás:", total_con_descuento, "soles.")
#else:
#    print("No aplicas al descuento. El monto de tu compra es:", monto_compra, "soles.")


    #crea una funcion por cada operador artmetrico
    #  y que revida 2 paramatros y retorna el resultado de la operacion, ojo 
    # . crease un funcion que nos permite imprimir el resultado
    
    
#suma
#def suma(a, b):
  #  imprimir_resultado = a + b
 #   return resultado
#def imprimir_resultado(resultado):
 #   print("El resultado es:", resultado)


#resta
#ef suma(a, b):
 #   imprimir_resultado = a - b
   # return resultado
#def imprimir_resultado(resultado):
   # print("El resultado es:", resultado)
   

    #multiplicacion
  #  ef suma(a, b):
 #   imprimir_resultado = a * b
  #  return resultado
#def imprimir_resultado(resultado):
    #print("El resultado es:", resultado)
   
   
    #diviison
   # ef suma(a, b):
  #  imprimir_resultado = a / b
 #   return resultado
#def imprimir_resultado(resultado):
  #  print("El resultado es:", resultado)
    
#escribe una funcion que reciba un numero entero positivo y devuelva sus factoriales

def factorial(n):
    if n ==0:
        retutn 1
        else:
            return *n factorial (n-1)

#escribe una funcion que revise como parametros una lista ed nuestros y retorne una nueva lista con 
#el cuadro de cada numero de la lista ingresada
 
 def calcular_cuadrados(lista):
    cuadrados = []
    for num in lista:
        cuadrados.append(num ** 2)
    return cuadrados