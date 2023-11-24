from tkinter import *
from tkinter import ttk
from config import*
class InterfazApp(Tk):
    def __init__(self):
        super().__init__()
        self.configurar_ventana()
        self.construir_widget()
    def configurar_ventana(self):
        self.title(f"{TITULO_APP}, {HORA_ACTUAL}")
        self.configure(bg=COLOR_FONDO_PRIMARIO)
        self.resizable(0,0)
        self.attributes("-alpha", 0.70)
        w,h=870,470
        centrar_ventana(self,w,h)
    
    def construir_widget(self):

    #cajitas de textos
        self.cajas_texto=LabelFrame(self,text="Cajitas de textos",width=150,height=430,
        relief=FLAT,pady=10,bg=COLOR_FONDO_PRIMARIO,fg="white",font=("Arial",12))
        # Caja de texto para los nombres
        self.cajas_texto.grid(row=0,column=0,padx=20,pady=20)
        self.Label_nombre=Label(self.cajas_texto,text="Nombres",
        bg=COLOR_FONDO_PRIMARIO,fg="white",font=("Roboto",10)).pack(pady=10)
        self.nombre_texto=Entry(self.cajas_texto,bd=0,width=12,font=("Arial",14))
        self.nombre_texto.pack()

        # Caja de textos para los apellidos 
        self.cajas_texto.grid(row=0,column=0,padx=20,pady=20)
        self.Label_Apellidos=Label(self.cajas_texto,text="Apellidos",
        bg=COLOR_FONDO_PRIMARIO,fg="white",font=("Roboto",10)).pack(pady=10)
        self.Apellidos_texto=Entry(self.cajas_texto,bd=0,width=12,font=("Arial",14))
        self.Apellidos_texto.pack()

        # Caja para celular
        self.cajas_texto.grid(row=0,column=0,padx=20,pady=20)
        self.Label_celular=Label(self.cajas_texto,text="Celular",
        bg=COLOR_FONDO_PRIMARIO,fg="white",font=("Roboto",10)).pack(pady=10)
        self.Celular_texto=Entry(self.cajas_texto,bd=0,width=12,font=("Arial",14))
        self.Celular_texto.pack()
        # Fin cajita de textos

    # Cajita de botones
        self.cajas_botones=LabelFrame(self,text="Cajita de botones",width=150,height=430,
        bg=COLOR_FONDO_PRIMARIO,fg="white",font=("Arial",12),relief=FLAT,pady=20)
        self.cajas_botones.grid(row=0,column=1,padx=20,pady=20)

        # Boton de nuevo
        self.nuevo=Button(self.cajas_botones,text="Nuevo",bg=COLOR_BOTONES,fg="white",
        relief=FLAT,bd=0,width=20,height=2,font=("Arial",10)).pack(pady=10)

        # Boton de Actualizar
        self.actualizarctualizar=Button(self.cajas_botones,text="Actulizar",bg=COLOR_BOTONES,fg="white",
        relief=FLAT,bd=0,width=20,height=2,font=("Arial",10)).pack(pady=10)

        # Boton de Eliminar
        self.eliminar=Button(self.cajas_botones,text="Eliminar",bg=COLOR_BOTONES,fg="white",
        relief=FLAT,bd=0,width=20,height=2,font=("Arial",10)).pack(pady=10)

        # Boton de Cancelar
        self.cancelar=Button(self.cajas_botones,text="Cancelar",bg=COLOR_BOTONES,fg="white",
        relief=FLAT,bd=0,width=20,height=2,font=("Arial",10)).pack(pady=10)
        # Fin cajita de botones
        
        #Caja dedatos
        self.cajas_datos=LabelFrame(self,text="Caja de datos",width=630,height=400,
        bg=COLOR_FONDO_PRIMARIO,fg="white",font=("Arial",12),relief=FLAT,pady=20)
        self.cajas_datos.grid(row=0,column=2,padx=20,pady=20)

        #Caja de tabla
        self.tabla_datos=ttk.Treeview(self.cajas_datos,columns=("#1","#2"))
        self.tabla_datos.column("#0",width=100)
        self.tabla_datos.column("#1",width=120)
        self.tabla_datos.column("#2",width=100)

        self.tabla_datos.heading("#0",text="Nombres")
        self.tabla_datos.heading("#1",text="Apellidos")
        self.tabla_datos.heading("#2",text="Celular")

        alumnitos=[
            ("moises","Peñadira","937463642"),
            ("yadira","medafiel","9475747543"),
            ("maria","de jory", "938746533"),
            ("nadinne","guadalupe","974365754")
        ]
        for nom,ape,cel in alumnitos:
            self.tabla_datos.insert("",END,text=nom,values=(ape,cel))

        self.tabla_datos.place(x=0,y=0,width=430,height=520)





# Mostrar la tabla de datos


# altura es pady en cada self  despues d3e pack
