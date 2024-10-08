### Interfaz del Temporizador ###

import tkinter as tk
from temporizador import iniciar_temporizador

# definimos func que inicia temporizador y actualiza la interfaz
def iniciar_desde_interfaz():
    tiempo_ingresado = entrada_tiempo.get()
    tiempo_en_segundos = convertir_a_segundos(tiempo_ingresado)
    iniciar_temporizador(tiempo_en_segundos, actualizar_tiempo_restante, root)

# func que convierte el tiempo en s
def convertir_a_segundos(tiempo):
    partes = tiempo.split(":")
    if len(partes) == 3:
        horas = int(partes[0])
        minutos = int(partes[1])
        segundos = int(partes[2])
    elif len(partes) ==2:
        horas = 0
        minutos = int(partes[0])
        segundos = int(partes[1])
    else:
        horas = 0
        minutos = 0
        segundos = int(partes[1])
    return horas * 3600 + minutos * 60 + segundos
    

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
entrada_tiempo.insert(0, "00:00:00")
boton_iniciar = tk.Button(root, text="Inicar", command=iniciar_desde_interfaz)
boton_iniciar.grid(row=2, column=0, columnspan=2)

# iniciamos el bucle de la interfaz
root.mainloop()



