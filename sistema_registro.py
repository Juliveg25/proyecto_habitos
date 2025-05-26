class Habitos:
    def __init__(self):
        self.agua = 0
        self.sueno = 0
        self.ejercicio = 0

    def registrar_agua(self, litros):
        self.agua = litros

    def registrar_sueno(self, horas):
        self.sueno = horas

    def registrar_ejercicio(self, minutos):
        self.ejercicio = minutos
        
def registrar_habitos():
    habitos = Habitos()

    try:
        litros = float(input("¿Cuántos litros de agua consumiste hoy? "))
        horas = float(input("¿Cuántas horas dormiste? "))
        minutos = int(input("¿Cuántos minutos hiciste ejercicio? "))
    except ValueError:
        print("Error, valor inválido")
        return None

    habitos.registrar_agua(litros)
    habitos.registrar_sueno(horas)
    habitos.registrar_ejercicio(minutos)

    return habitos

    # def obtener_habitos(self):
    # return {
    #     "agua": self.agua,
    #     "sueno": self.sueno,
    #     "ejercicio": self.ejercicio
    # }
