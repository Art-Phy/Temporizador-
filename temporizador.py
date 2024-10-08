### Temporizador ###

import time

# func que inicia el temporizador
def iniciar_temporizador(segundos, actualizar_tiempo_restante, root):
    cuenta_atras(segundos, actualizar_tiempo_restante, root)

# func de cuenta atrás
def cuenta_atras(segundos, actualizar_tiempo_restante, root):
    if segundos > 0:
        horas = segundos // 3600
        minutos = (segundos % 3600) // 60
        segundos_restantes = segundos % 60

        # aquí se indica el formato del temporizador. 2 dígitos, horas, minutos, segundos
        tiempo_restante = f"{horas:02d}:{minutos:02d}:{segundos_restantes:02d}"

        # se actualiza el tiempo en la interfaz
        actualizar_tiempo_restante(tiempo_restante)

        # se llama de nuevo a esta función después de 1s
        root.after(1000, lambda: cuenta_atras(segundos -1, actualizar_tiempo_restante, root))
    else:
        actualizar_tiempo_restante("Tiempo finalizado")
