import datetime
color_fondo_primario="#004d4d"
color_fondo_secundario="#b3daff"
color_boton="#52c9dc"
titulo_app="app de contactos"
date=datetime.datetime.now()
hora_actual=f"fecha: {date.day}-{date.month}-{date.year},hora: {date.hour}:{date.minute}"

def centrar_ventana(ventana,ancho_ventana,largo_ventana):
    pantalla_ancho=ventana.winfo_screenwidth()
    pantalla_largo=ventana.winfo_screenheigth()
    x=int((pantalla_ancho/2)-(ancho_ventana/2))
    y=int((pantalla_largo/2)-(largo_ventana/2))
    return ventana.geometry(f"{ancho_ventana}x{largo_ventana}+{x}+{y}")

  