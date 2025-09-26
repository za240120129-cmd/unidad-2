import tkinter as tk

root = tk.Tk()
root.title("selector de modo operación")

frame = tk.Frame(root, padx=10, pady=10)
frame.pack(pady=10)

tk.Label(frame, text="Selecciona el modo de operación:", font=("Arial", 12)).pack(pady=5)

btn_manual = tk.Button(frame, text="Modo Manual", width=15)
btn_manual.pack(side="left", padx=5)
btn_auto = tk.Button(frame, text="Modo Automático", width=15)
btn_auto.pack(side="left", padx=5)

root.mainloop()
