import tkinter as tk 

def validar_numero(*args):
    valor = v_numero.get()
    if not valor.isdigit():
        estado.set("Entrada inválida: solo números permitidos")
    else:
        estado.set("Entrada válida")

root = tk.Tk()
root.title("Validación de Entrada")

v_numero = tk.StringVar()
v_numero.trace_add('write', validar_numero)

tk.Entry(root, textvariable=v_numero).pack(pady=5)
estado = tk.StringVar(value="Esperando entrada...")
tk.Label(root, textvariable=estado, font=("Arial", 12)).pack(pady=5)

root.mainloop()
