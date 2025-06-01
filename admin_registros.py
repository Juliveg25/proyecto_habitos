#US09 para implementar cuando se agregue persistencia.
import visualizacion_puntos

def guardar_puntajes(historial_puntajes, calcular_puntaje_total):
    historial_puntajes.append(calcular_puntaje_total)

def ver_historial(historial_puntajes):
    return historial_puntajes

def borrar_registro(historial_puntajes):
    historial_puntajes.clear()
    return historial_puntajes