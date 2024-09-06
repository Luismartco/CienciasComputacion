#Este archivo perminira abrir otra ventana (VentanaX)
import subprocess 
import tkinter as tk

def abrir_ventanax():
    subprocess.Popen(['python','ventanaX.py'])



ventana = tk.Tk()
ventana.title("Ventana principal") 
ventana.minsize(600,600)
ventana.maxsize(600,600)

boton1 = tk.Button(ventana, text = "Abiri aplicacion ventanaX", command=abrir_ventanax)
boton1.grid(row=1, column=2, padx=5, pady=5) 
ventana.mainloop()