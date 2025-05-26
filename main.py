# main.py

from sistema_registro import registrar_habitos
from visualizacion_puntos import calcular_puntaje_total, ver_historial
from view import mostrar_menu

def main():
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
            historial = ver_historial()
            print("\n Total de puntajes diarios:")
            for i, puntaje in enumerate(historial, 1):
                print(f"Día {i}: {puntaje} puntos")
                
        elif opcion == "4":
            print("Salida")
            break
        else:
            print("Error, opción inválida")

if __name__ == "__main__":
    main()
