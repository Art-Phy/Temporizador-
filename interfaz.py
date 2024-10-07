### Interfaz del Temporizador ###

import tkinter as tk
from tkinter import messagebox

# definimos la func que llamará al temporizador que hemos creado
def iniciar_temporizador(temporizador_func):
    horas = entry_horas.get() or 0
    minutos = entry_minutos.get() or 0
    segundos = entry_segundos.get() or 0
    total_segundos = int(horas * 3600 + int(minutos) * 60 + int(segundos))
    temporizador_func(total_segundos)

# definimos la func que crea la interfaz
def crear_interfaz(temporizador_func):
    global entry_horas, entry_minutos, entry_segundos, label_tiempo

    # ventana principal
    root = tk.Tk()
    root.title("Temporizador")

    # widget de la interfaz
    label_horas = tk.Label(root, text="Horas:")
    label_horas.grid(row=0, column=0)
    entry_horas = tk.Entry(root, width=5)
    entry_horas.grid(row=0, column=1)

    label_minutos = tk.Label(root, text="Minutos:")
    label_minutos.grid(row=0, column=0)
    entry_minutos = tk.Entry(root, width=5)
    entry_horas.grid(row=1, column=1)

    label_segundos = tk.Label(root, text="Segundos:")
    label_segundos.grid(row=2, column=0)
    entry_segundos = tk.Entry(root, width=5)
    entry_segundos.grid(row=2, column=1)

    button_inciar = tk.Button(root, text="Iniciar", command=lambda: iniciar_temporizador(temporizador_func))
    button_inciar.grid(row=3, column=0, columnspan=2)

    label_tiempo = tk.Label(root, text="00h:00m:00s", font=("Helvetica", 24))
    label_tiempo.grid(row=4, column=0, columnspan=2)

    # iniciamos el bucle de la interfaz
    root.mainloop()

# func para actualizar el tiempo de la interfaz
def actualizar_tiempo_restante(tiempo_restante):
    label_tiempo.config(text=tiempo_restante)


