import tkinter as tk
import random

def jugar(eleccion_jugador):
    opciones = ['piedra', 'papel', 'tijera']
    computadora = random.choice(opciones)

    if eleccion_jugador == computadora:
        resultado = "¡Empate!"
    elif (eleccion_jugador == 'piedra' and computadora == 'tijera') or \
         (eleccion_jugador == 'papel' and computadora == 'piedra') or \
         (eleccion_jugador == 'tijera' and computadora == 'papel'):
        resultado = "¡Ganaste!"
    else:
        resultado = "¡Perdiste!"

    etiqueta_resultado.config(
        text=f"Tú elegiste: {eleccion_jugador}\nComputadora eligió: {computadora}\n{resultado}"
    )

# Crear ventana
ventana = tk.Tk()
ventana.title("Piedra, Papel o Tijera")
ventana.geometry("400x300")

# Etiqueta de instrucciones
etiqueta = tk.Label(ventana, text="Elige tu jugada:", font=("Arial", 14))
etiqueta.pack(pady=10)

# Botones de opciones
frame_botones = tk.Frame(ventana)
frame_botones.pack()

boton_piedra = tk.Button(frame_botones, text="🪨 Piedra", font=("Arial", 12), command=lambda: jugar("piedra"))
boton_piedra.grid(row=0, column=0, padx=10)

boton_papel = tk.Button(frame_botones, text="📄 Papel", font=("Arial", 12), command=lambda: jugar("papel"))
boton_papel.grid(row=0, column=1, padx=10)

boton_tijera = tk.Button(frame_botones, text="✂️ Tijera", font=("Arial", 12), command=lambda: jugar("tijera"))
boton_tijera.grid(row=0, column=2, padx=10)

# Etiqueta del resultado
etiqueta_resultado = tk.Label(ventana, text="", font=("Arial", 12), fg="blue")
etiqueta_resultado.pack(pady=20)

# Iniciar loop de la ventana
ventana.mainloop()
