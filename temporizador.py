### Temporizador ###

import time

def temporizador(segundos): #minutos, horas):
    while segundos:
        min = segundos // 60
        seg = segundos % 60
        hor = segundos // 3600
        tiempo_restante = f"{min:02d}:{seg:02d}:{hor:02d}"
        print(tiempo_restante, end="\r")
        time.sleep(1)
    print("Tiempo finalizado")

tiempo_ingresado = int(input("Ingresa el tiempo: "))

temporizador(tiempo_ingresado)
        