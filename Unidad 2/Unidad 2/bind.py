import tkinter as tk

def mostrar_cordenadas(event):
    mensaje.set(f"Cordenadas: x={event.x}, y={event.y}")

root = tk.Tk()
root.title("detectar cordenadas del mouse")

mensaje = tk.StringVar()
tk.Label(root, textvariable=mensaje, font=("Arial", 12)).pack(pady=10)

panel = tk.Frame(root, width=200, height=100, bg="#e0f2f1")
panel.pack(pady=10)
panel.bind("<Button-1>", mostrar_cordenadas)

root.mainloop()
