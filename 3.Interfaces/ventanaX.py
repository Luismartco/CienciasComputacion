import tkinter as tk
ventana = tk.Tk()

    #Se crea la funcion para sumar
def sumar():
    n1 = float (caja1.get())
    n2 = float (caja2.get())
    res = n1 + n2
    resultado.config(text= f"{res}")

    #Se define las dimenciones de la ventana
ventana.title("Cajas de texto") 
ventana.minsize(600,600)
ventana.maxsize(600,600)

    #Se crea label1 y label2
etiqueta1 = tk.Label(ventana, text="Digite un valor", font=("Arial", 14))
etiqueta1.grid(row=1, column=1, padx=5, pady=5) 
caja1 = tk.Entry(ventana)
caja1.grid(row=1, column=2, padx=5, pady=5) 
etiqueta2 = tk.Label(ventana, text="Otro valor", font=("Arial", 14))
etiqueta2.grid(row=2, column=1, padx=5, pady=5) 
caja2 = tk.Entry(ventana)
caja2.grid(row=2, column=2, padx=5, pady=5) 

    #Se crea el boton
boton1 = tk.Button(ventana, text = "Sumar", command=sumar)
boton1.grid(row=3, column=2, padx=5, pady=5) 

    #Se muestra el resultado
resultado = tk.Label(ventana, text="Resultado")
resultado.grid(row=4, column=1, padx=5, pady=5) 

ventana.mainloop()