from tkinter import *
from config import *


class InterfazApp(Tk):
    def __init__(self):
        super().__init__()
        self.configurar_ventana()
        self.construit_widget()
    #metood propio vamos a darle las configuraciones basicas para
    #monstrar nuestra ventana
    def configurar_ventana(self):
        self.title(f"{titulo_app} {hora_actual}")
        self.configure(bg=color_fondo_primario)
        self.resizable(0,0)
        self.attributes("-alpha",0.96)
        w,h=870,470
        centrar_ventana(self,w,h)

    def contruir_widget(self):
        self.cajas_texto=LabelFrame(self,text="cajas de texto",width=150,height=430,bg=color_fondo_primario,fg="white",font=("arial",12),relief=FLAT)
        self.cajas_texto.grid(row=0,column=0,pady=20,padx=20)
#fin cajita  nombre
        self.label_nombre=Label(self.cajas_texto,text="nombres",bg=color_fondo_primario,fg="white",font=("Roboto",10)).pack(pady=10)
        self.nombre_texto=Entry(self.cajas_texto,bd=0,width=12,font=("arial",14))
        self.nombre_texto.pack()
 #fin cajita  apellido
        self.label_apellido=Label(self.cajas_texto,text="nombres",bg=color_fondo_primario,fg="white",font=("Roboto",10)).pack(pady=10)
        self.apellido_texto=Entry(self.cajas_texto,bd=0,width=12,font=("arial",14))
        self.apellido_texto.pack()
#fin cajita  celular
        self.label_celular=Label(self.cajas_texto,text="nombres",bg=color_fondo_primario,fg="white",font=("Roboto",10)).pack(pady=10)
        self.celular_texto=Entry(self.cajas_texto,bd=0,width=12,font=("arial",14))
        self.celular_texto.pack()
      

#cajitas boton
        self.cajas_botones=LabelFrame(self,text="caja de botones",width=150,height=430,bg=color_fondo_primario,fg="white",font=("arial",12),relief=FLAT)
        self.cajas_botones.grid(row=0,column=1,pady=20,padx=20)
        #boton nuevo
        self.nuevo=Button(self.cajas_botones,text="nuevo",bg=color_boton,fg="white",relief=FLAT,bd=0,width=20,height=2,font=("Arial",10)).pack()
#fin de cajits btonon cancelar
        self.cancelar=Button(self.cajas_botones,text="cancelar",bg=color_boton,fg="white",relief=FLAT,bd=0,width=20,height=2,font=("arial",10)).pack(pady=8)
        #fin cajitas de botones

