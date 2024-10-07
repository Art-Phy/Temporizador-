### Temporizador ###

import time
from interfaz import crear_interfaz, actualizar_tiempo_restante

# func del temporizador
def temporizador(segundos):
    while segundos > 0:
        hor = segundos // 3600
        min = (segundos % 3600) //60
        seg = segundos % 60
        # aquí se indica el formato del temporizador. 2 dígitos, horas, minutos, segundos
        tiempo_restante = f"{hor:02d}:{min:02d}:{seg:02d}"
        actualizar_tiempo_restante(tiempo_restante)
        time.sleep(1)
        segundos-= 1
    actualizar_tiempo_restante("Tiempo finalizado")

# ejecutar la interfaz
if __name__ == "__main__":
    crear_interfaz(temporizador)