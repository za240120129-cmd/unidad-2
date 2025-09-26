import tkinter as tk

def solo_numeros(P):
    return P.isdigit()

root = tk.Tk()
root.title("Validación en Tiempo Real")

vcmd = (root.register(solo_numeros), '%P')
entry = tk.Entry(root, validate='key', validatecommand=vcmd)
entry.pack(pady=10)

root.mainloop()
