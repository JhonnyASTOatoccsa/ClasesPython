#constantes para el tema oscuro
color_fondo_negro="#1a1b28"
color_texto_negro="white"
color_botones_especial_negro="#52c9dc"
color_botones_negro="#1e2435"
color_caja_texto_negro="#1a1b28"

#constante para el tema claro
color_fondo_light="#ffffff"
color_fondo_light="black"
color_botones_especial_light="#52c9dc"
color_botones_ligth="#f2f8fc"
color_caja_texto_light="#ffffff"

#funciones que nos permite centrar nuestra pantalla
def centrar_ventana(ventana,ancho_ventana,largo_ventana):
    pantalla_ancho=ventana.winfo_screenwidth()
    pantalla_largo=ventana.winfo_screenheight()
    x=int((pantalla_ancho/2)-(ancho_ventana/2))
    y=int((pantalla_largo/2)-(ancho_ventana/2))
    return ventana.geometry(f"{ancho_ventana}x{largo_ventana}+{x}+{y}")
