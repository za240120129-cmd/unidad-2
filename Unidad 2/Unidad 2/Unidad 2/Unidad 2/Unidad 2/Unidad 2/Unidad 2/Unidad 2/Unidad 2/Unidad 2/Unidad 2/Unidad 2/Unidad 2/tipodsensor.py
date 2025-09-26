import tkinter as tk
from tkinter import ttk

def elegir_sensor(event=None):
    seleccion = combo_sensores.get()
    etiqueta.set(f"Sensor seleccionado: {seleccion}")

root = tk.Tk()
root.title("Selección de Tipo de Sensor")

lista = ["Temperatura", "Humedad", "Presión", "Luz", "Movimiento"]
combo_sensores = ttk.Combobox(root, values=lista, state="readonly")
combo_sensores.pack(pady=5)
combo_sensores.bind("<<ComboboxSelected>>", elegir_sensor)
etiqueta = tk.StringVar(value="Seleccione un tipo de sensor")
ttk.Label(root, textvariable=etiqueta, font=("Arial", 12)).pack(pady=5)

root.mainloop()
    
