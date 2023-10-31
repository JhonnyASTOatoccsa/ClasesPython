import tkinter as tk

def sumar():
    num1 = float(numero1_entry.get())
    num2 = float(numero2_entry.get())
    resultado_var.set(num1 + num2)

def restar():
    num1 = float(numero1_entry.get())
    num2 = float(numero2_entry.get())
    resultado_var.set(num1 - num2)

def multiplicar():
    num1 = float(numero1_entry.get())
    num2 = float(numero2_entry.get())
    resultado_var.set(num1 * num2)

def dividir():
    num1 = float(numero1_entry.get())
    num2 = float(numero2_entry.get())
    if num2 == 0:
        resultado_var.set("No se puede dividir por cero")
    else:
        resultado_var.set(num1 / num2)

def limpiar():
    numero1_entry.delete(0, tk.END)
    numero2_entry.delete(0, tk.END)
    resultado_var.set("")

ventana = tk.Tk()
ventana.title("Calculadora")
ventana.geometry("300x250")

numero1_label = tk.Label(ventana, text="Ingrese número:")
numero1_label.pack(pady=10)

numero1_entry = tk.Entry(ventana)
numero1_entry.pack()

numero2_label = tk.Label(ventana, text="Ingrese número:")
numero2_label.pack(pady=10)

numero2_entry = tk.Entry(ventana)
numero2_entry.pack()

# Botones de operaciones
frame_operaciones = tk.Frame(ventana)
frame_operaciones.pack(pady=10)
boton_sumar = tk.Button(frame_operaciones, text=" +  ", command=sumar)
boton_sumar.grid(row=0, column=0, padx=5)

boton_restar = tk.Button(frame_operaciones, text="  -  ", command=restar)
boton_restar.grid(row=0, column=1, padx=5)

boton_multiplicar = tk.Button(frame_operaciones, text="  *  ", command=multiplicar)
boton_multiplicar.grid(row=0, column=2, padx=5)

boton_dividir = tk.Button(frame_operaciones, text="  /  ", command=dividir)
boton_dividir.grid(row=0, column=3, padx=5)


# Botón para limpiar
boton_borrar = tk.Button(ventana, text="Borrar", command=limpiar)
boton_borrar.pack(pady=10)

resultado_var = tk.StringVar()
resultado_label = tk.Label(ventana, textvariable=resultado_var)
resultado_label.pack(pady=10)

ventana.mainloop()