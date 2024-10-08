### Interfaz del Temporizador ###

import tkinter as tk
from temporizador import iniciar_temporizador

# definimos func que inicia temporizador y actualiza la interfaz
def iniciar_desde_interfaz():
    tiempo_ingresado = int(entrada_tiempo.get())
    iniciar_temporizador(tiempo_ingresado, actualizar_tiempo_restante)

# func que actualiza el tiempo en la interfaz
def actualizar_tiempo_restante(tiempo_restante):
    etiqueta_tiempo.config(text=tiempo_restante)

# ventana principal
root = tk.Tk()
root.title("Temporizador")

# widget de la interfaz
etiqueta_tiempo = tk.Label(root, text="00:00:00", font=("Helvetica", 24))
etiqueta_tiempo.grid(row=0, column=0, columnspan=2)
entrada_tiempo = tk.Entry(root)
entrada_tiempo.grid(row=1, column=0, columnspan=2)
boton_iniciar = tk.Button(root, text="Inicar", command=iniciar_desde_interfaz)
boton_iniciar.grid(row=2, column=0, columnspan=2)

# iniciamos el bucle de la interfaz
root.mainloop()



