# Review Criterios de Aceptacion:
#!Agua: +2 puntos por litro (máx. 6 puntos)
#!Sueno: +1 punto por cada hora entre 6 y 9 (fuera de eso, 0)
#!Ejercicio: +1 punto por cada 10 minutos hasta 60 minutos.


def puntaje_agua(litros):
    puntos = litros * 2
    if puntos > 6:
        puntos = 6
    return puntos

def puntaje_sueno(horas):
    if 6 <= horas <= 9:
        return horas 
    return 0

def puntaje_ejercicio(minutos):
    puntos = minutos // 10
    if puntos > 6:
        puntos = 6
    return puntos

