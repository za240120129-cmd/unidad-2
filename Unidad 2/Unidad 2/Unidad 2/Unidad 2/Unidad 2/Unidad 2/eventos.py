import tkinter as tk

def encender_led():
    label_estado.config(text="LED Encendido")

def apagar_led():
    label_estado.config(text="LED Apagado")

root = tk.Tk()
root.title("panel de control de LED")

label_estado = tk.Label(root, text="Estado del LED: Apagado", font=("Arial", 12))
label_estado.pack(pady=10)

btn_encender = tk.Button(root, text="Encender LED", command=encender_led)
btn_encender.pack(pady=5)


btn_encender = tk.Button(root, text="Apagar LED", command=apagar_led)
btn_encender.pack(pady=5)

root.mainloop()
