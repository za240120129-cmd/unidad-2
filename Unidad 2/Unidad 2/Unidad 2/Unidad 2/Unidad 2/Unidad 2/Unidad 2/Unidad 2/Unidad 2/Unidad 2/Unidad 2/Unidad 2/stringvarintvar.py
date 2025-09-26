import tkinter as tk

def actualizar_temperatura():
    valor = entrada_temp.get()
    etiqueta_temp.config(text=f"Temperatura: {valor} °C")

root = tk.Tk()
root.title("monitor de temperatura")

etiqueta_temp = tk.StringVar()
etiqueta_temp.set("Temperatura: -- °C")

tk.Label(root, textvariable=etiqueta_temp, font=("Arial", 14)).pack(pady=10)
entrada_temp = tk.Entry(root, width=10)
entrada_temp.pack(pady=5)
btn_actualizar = tk.Button(root, text="Actualizar Temperatura", command=actualizar_temperatura)
btn_actualizar.pack(pady=5)

root.mainloop()
