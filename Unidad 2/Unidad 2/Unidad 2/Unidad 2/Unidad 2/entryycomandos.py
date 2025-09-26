import tkinter as tk

def send_command():
    comand = entry.get()
    label_status.config(text=f"Comando enviado: {comand}")

root = tk.Tk()
root.title("Entrada de Comandos")

entry = tk.Entry(root, width=20)
entry.grid(row=0, column=0, padx=5, pady=5)

btn_send = tk.Button(root, text="Enviar Comando", command=send_command)
btn_send.grid(row=0, column=1, padx=5, pady=5)

label_status = tk.Label(root, text="Estado: Esperando comando", font=("Arial", 12))
label_status.grid(row=1, column=0, columnspan=2, pady=10)

root.mainloop()
