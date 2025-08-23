import random

def jugar():
    opciones = ['piedra', 'papel', 'tijera']

    victorias = 0
    derrotas = 0
    empates = 0

    while True:
        jugador_dos = random.choice(opciones)
        jugador = input("Elige piedra, papel o tijera (o 'salir' para terminar): ").lower()

        if jugador == 'salir':
            print("\n--- Resultado final ---")
            print(f"Victorias: {victorias}")
            print(f"Derrotas: {derrotas}")
            print(f"Empates: {empates}")
            print("¡Gracias por jugar! Hasta luego.")
            break

        if jugador not in opciones:
            print("Opción inválida. Intenta de nuevo.\n")
            continue

        print(f"Computadora eligió: {jugador_dos}")

        if jugador == jugador_dos:
            print("¡Empate!\n")
            empates += 1
        elif (jugador == 'piedra' and jugador_dos == 'tijera') or \
             (jugador == 'papel' and jugador_dos == 'piedra') or \
             (jugador == 'tijera' and jugador_dos == 'papel'):
            print("¡Ganaste!\n")
            victorias += 1
        else:
            print("¡Perdiste!\n")
            derrotas += 1


if __name__ == "__main__":
    jugar()
