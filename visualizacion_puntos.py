# visualizacion_puntos.py

from sistema_puntos import puntaje_agua, puntaje_sueno, puntaje_ejercicio

historial_puntajes = [] #temporal para 1era version, hay que cambiarlo por bd o json

def calcular_puntaje_total(habitos):
    puntos_agua = puntaje_agua(habitos.agua)
    puntos_sueno = puntaje_sueno(habitos.sueno)
    puntos_ejercicio = puntaje_ejercicio(habitos.ejercicio)

    total = puntos_agua + puntos_sueno + puntos_ejercicio

    return total

