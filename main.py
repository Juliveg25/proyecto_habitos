# main.py

from sistema_registro import registrar_habitos
from visualizacion_puntos import calcular_puntaje_total
from view import mostrar_menu
from admin_registros import guardar_puntajes

def main():
    historial = []
    while True:
        mostrar_menu()
        opcion = input("Selecciona una opción: ")

        if opcion == "1":
            habitos_dia = registrar_habitos()
            if habitos_dia:
                print("Registro realizado")
                
        elif opcion == "2":
            if 'habitos_dia' in locals():
                puntaje = calcular_puntaje_total(habitos_dia)
                print(f"Tu puntaje de bienestar hoy es: {puntaje}")
            else:
                print("No tienes puntaje acumulado.")

        elif opcion == "3":
            if 'habitos_dia' in locals():
                if 'puntaje' not in locals():
                    puntaje = calcular_puntaje_total(habitos_dia)
                # Añadimos el puntaje al historial directamente
                historial.append(puntaje)
                # Llamamos a guardar_puntajes pero sin asignar su retorno a historial
                guardar_puntajes(historial, puntaje)
                print("\nTotal de puntajes diarios:")
                for i, puntaje_hist in enumerate(historial, 1):
                    print(f"Día {i}: {puntaje_hist} puntos")
            else:
                print("No has registrado hábitos todavía.")

        elif opcion == "4":
            print("Salida")
            break
        else:
            print("Error, opción inválida")

if __name__ == "__main__":
    main()
