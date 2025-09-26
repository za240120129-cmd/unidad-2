import tkinter as tk

def enviar():
    valor = entry.get()
    if valor.isdigit():
        label_estado.config(text=f"Valor almacenado: {valor}")
    else:
        label_estado.config(text="Solo números permitidos")

root = tk.Tk()
root.title("Entrada y validación de datos")

entry = tk.Entry(root)
entry.grid(row=0, column=0, padx=5, pady=5)
boton = tk.Button(root, text="Enviar", command=enviar)
boton.grid(row=0, column=1, padx=5, pady=5)

label_estado = tk.Label(root, text="Esperando datos...")
label_estado.grid(row=1, column=0, columnspan=2)

root.mainloop()
