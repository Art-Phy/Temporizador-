### Temporizador ###

import time

# func que inicia el temporizador
def iniciar_temporizador(segundos, actualizar_tiempo_restante):
    cuenta_atras(segundos, actualizar_tiempo_restante)

# func de cuenta atrás
def cuenta_atras(segundos, actualizar_tiempo_restante):
    if segundos > 0:
        hor = segundos // 3600
        min = (segundos % 3600) // 60
        seg = segundos % 60

        # aquí se indica el formato del temporizador. 2 dígitos, horas, minutos, segundos
        tiempo_restante = f"{hor:02d}:{min:02d}:{seg:02d}"

        # se actualiza el tiempo en la interfaz
        actualizar_tiempo_restante(tiempo_restante)

        # se llama de nuevo a esta función después de 1s
        time.sleep(1)
        cuenta_atras(segundos - 1, actualizar_tiempo_restante)
    else:
        actualizar_tiempo_restante("Tiempo finalizado")
        