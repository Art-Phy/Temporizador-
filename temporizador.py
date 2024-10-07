### Temporizador ###

import time

def temporizador(segundos):
    while segundos:
        min =segundos // 60
        seg = segundos % 60
        hor = segundos // 3600
        tiempo_restante = f"{hor:02d}:{min:02d}:{seg:02d}" # ese formato indica el número de dígitos
        print(tiempo_restante, end="\r")
        time.sleep(1)
        segundos-= 1
    print("Tiempo finalizado")

tiempo_ingresado = int(input("Ingresa el tiempo: "))

temporizador(tiempo_ingresado)
        