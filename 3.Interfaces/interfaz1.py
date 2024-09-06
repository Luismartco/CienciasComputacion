import tkinter as tk

def ventana1():
    ventana1 = tk.Toplevel()
    ventana1.title("Ventana1")
    ventana1.minsize(400,400)
    salirv1 = tk.Button(ventana1,text="Salir",command=ventana1.destroy)
    salirv1.grid(row=1,column=1,padx=5,pady=5)

def ventana2():
    ventana2 = tk.Toplevel()
    ventana2.title("Ventana2")
    ventana2.minsize(400,400)
    salirv2 = tk.Button(ventana2,text="Salir",command=ventana2.destroy)
    salirv2.grid(row=1,column=1,padx=5,pady=5)

def salir():
    ventana.destroy()

ventana = tk.Tk()

ventana.title("Ventana 1")
ventana.minsize(600,600)
ventana.maxsize(720,1280)
ventana.iconbitmap('icono.ico')

ventana.configure(bg="blue")
#etiqueta1 = tk.Label(ventana,text="mi primera etiqueta")
#etiqueta1.grid(row=1,column=1,padx=5,pady=5)
#etiqueta2 = tk.Label(ventana,text="mi segunda etiqueta")
#etiqueta2.grid(row=2,column=1,padx=5,pady=5)

boton1 = tk.Button(ventana,text="Ventana 1",command=ventana1)
boton1.grid(row=1,column=1,padx=5,pady=5)
boton2 = tk.Button(ventana,text="Ventana 2",command=ventana2)
boton2.grid(row=2,column=1,padx=5,pady=5)
salir = tk.Button(ventana,text="Salir",command=salir)
salir.grid(row=3,column=1,padx=5,pady=5)

ventana.mainloop()