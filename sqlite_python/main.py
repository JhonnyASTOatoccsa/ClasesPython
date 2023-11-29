import orm
from tablas.Productos import Productos
from tablas.Clientes import Clientes

db=orm.SQLiteORM("tienditas")
db.crear_tabla(Productos)
db.crear_tabla(Clientes)


#data={
#    "nombre":"detergente",
#    "precio":"2.5",
#    "descripcion":"el que limpia todo",
#    "cantidad":"10"
#}
#db.insertarUno("Productos",data)
data=[
     {
    "nombre":"chinita",
    "dni":"54512334",
    "celular":"9876543243",
    "f_nacimiento":"10/12/2000"
     },
     {
    "nombre":"mochucha",
    "dni":"45646334",
    "celular":"9285643",
    "f_nacimiento":"20/10/2010"
     }
]
#db.insertarVarios("Clientes",data)
data={"nombre":"maria"}
db.actualizar("Clientes",data,"dni=54512334")
db.eliminar("Clientes","dni=12345678")

print(db.mostrar("Clientes"))
db.cerrar()



