# PROGRAMACION ORIENTADA A OBJETOS (POO)- _OBJET ORIENT PROGRAMING(OOP)_
Es un paradigma (estilo, regla, patron, o ejemplo que se debe seguir) de programacion.

POO es un modelo de como programar

``OBJETIVO:`` El objetivo es organizar el codigo de manera que se asemeje a como pensamos en la vida real.
 
Se basa en objetos y en la POO es toda entidad que se puede describir a traves de **atributos** y las **funciones** que puede realizar la entidad.

 # Ejemplo
 Un animal: 🐶
  puede caminar, comer, saltar, correr, etc.

 - clase generales
 - instancia propios


## EJEMPLO CELULARES 📱
```python
class Celular:
    # atributos tipo clase
    #que son iguales para todos los objetos 
    # que se creen
    familia='Smart Fhone'
    # se sobre escribe cuando coincide el mismo nombre de variable


    # atributos de instancia
    # son atributos propios del objeto
    # creamos una funcion inicializadora
    def __init__(self, marca, modelo, imei, nrocelular):
        self.marca=marca
        self.modelo=modelo
        self.imei=imei
        self.nrocelular=nrocelular
    # funcionalidades
    def llamar(self, destino):
        return f'llamando a {destino}'

    #objeto cecular jory
llamandojory=Celular('poco','x5','723576456','67867867876')
#instanciando mi clase - creadon mi objeto celular
print(llamandojory.marca)
print(llamandojory.familia)
print(llamandojory.llamar('china'))

#objeto celular nadine
llamandonadine=Celular('alcatel','basic','715345646','6424564566')

print(llamandonadine.marca)
print(llamandonadine.familia)
print(llamandonadine.llamar('ollanta'))
```