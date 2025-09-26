import tkinter as tk 
from tkinter import messagebox

def guardar():
    messagebox.showinfo("Guardar Configuración", "Configuración guardada exitosamente")

root = tk.Tk()
root.title("Guardar Configuración")
tk.Button(root, text="Guardar Configuración", command=guardar).pack(pady=20)

root.mainloop()
