from rich import print
from rich.markdown import markdown
#titulo
edad=20
respuesta="es mayor de edad" if edad>17 else "es menor de edad"
texto="""
    # parrafo
    ```bash
    git comint -m "titulo" -m "cuerpo del commit"
    #comenatario
    ```
    * lista
    * lista
    > informacion valiosa
    {}
""".format(respuesta)
monstrar_mark=markdown(texto)
print(monstrar_mark)