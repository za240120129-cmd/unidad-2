import tkinter as tk

root = tk.Tk()
root.title("monitor de sensor embebido")
#simula lectura del sensor
valor_sensor = 36.8 #valor ficticio
#crea etiqueta para mostrar el valor del sensor
etiqueta = tk.Label(root, text=f"Valor del sensor: {valor_sensor } °C", font=("Arial", 14))
etiqueta.pack(pady=10)  

root.mainloop()
