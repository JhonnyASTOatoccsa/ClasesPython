from tkinter import *
from tkinter import font
import confign as cons
class InterfazCalculadora(Tk):
    def __init__(self):
        super().__init__()
        self.configura_ventana()

    def configura_ventana(self):
        self.title("calculadora avanzada")
            #color
        self.configure(bg=cons.color_fondo_negro)
            #que no se pueda escalar
        self.resizable(0,0)
            #propiedad para darle transparencia
        self.attributes("-alpha",0.96)
            #llamar a la funcion centrar_ventana
        w,h=370,570
            #w=370
            #h=570
        cons.centrar_ventana(self,w,h)
        
    def construir_widget(self):
        #etiqueta para mostrar la operacion 
        self.operacion_label=Label(self,text="hola",font=("Arial",16)),
        fg=cons.COLOR_TEXTO_NEGRO,BG=cons.COLOR_FONDO_NEGRO,justify='ringht'
        self.operacion_label.grid(row=0,column=3,padx=10,pady=10)  

        #caja de texto donde se muestra los numeros ingresado
        self.caja_operaciones=Entry(self,width=12,font=("Arial",40),
        bd=0,fg=cons.COLOR_TEXTO_NEGRO,bg=cons.COLOR_FONDO_NEGRO,justify='right')
        self.caja_operaciones.grid(row=1,column=1,columnspan=4,padx=10,pady=10)

        #creando botones
        botones=[
            "c","%","<","/",
            "7","8","9","*",
            "4","5","6","+",
            "0",".","=",
        ]
        row_ini=2
        col_ini=0
        robot_font=font.Font(family="Roboto",size=16)

        for boton in botones:
            if boton in ["=","*","/","-"+","C","<","%",]:
                color_fondo=cons.color_botones_especial_negro
                boton_font=font.Font(size=16,Widght="bold")
            else:
            color_fondo=cons.color_botones_negro
            boton_font=robot_font
            if boto == "=":
            Button(self,text=boton,width=11,heigth=2,
            bg=color_fondo,fg=cons.color_texto_negro,relief=FLAT,
            highlightthickness=0,overrelief="flat").grid 
            (row=row_ini,column=col_ini,pady=5)
            col_ini+= 1
            if col_ini>3:
                col_ini=0
                row_ini


