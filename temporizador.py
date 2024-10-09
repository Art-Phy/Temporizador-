### Temporizador ###

import time

def temporizador(segundos):
    while segundos > 0:
        hor = segundos // 3600
        min = (segundos % 3600) //60
        seg = segundos % 60
        # aquí se indica el formato del temporizador. 2 dígitos, horas, minutos, segundos
        tiempo_restante = f"{hor:02d}:{min:02d}:{seg:02d}"
        print(tiempo_restante, end="\r")
        time.sleep(1)
        segundos-= 1
    print("Tiempo finalizado")

# func para aceptar horas, min y seg en diferentes formatos
def convertir_a_segundos(tiempo):
    horas, minutos, segundos = 0, 0, 0
    if 'h' in tiempo:
        horas = int(tiempo.split('h')[0])
        tiempo = tiempo.split('h')[1]
    if 'm' in tiempo:
        minutos = int(tiempo.split('m')[0])
        tiempo = tiempo.split('m')[1]
    if 's' in tiempo:
        segundos = int(tiempo.split('s')[0])
        tiempo = tiempo.split('s')[1]

    total_segundos = horas *3600 + minutos *60 + segundos
    return total_segundos

tiempo_ingresado = (input("Ingresa el tiempo (indica si son horas, minutos, segundos): "))
segundos_totales = convertir_a_segundos(tiempo_ingresado)

temporizador(segundos_totales)
