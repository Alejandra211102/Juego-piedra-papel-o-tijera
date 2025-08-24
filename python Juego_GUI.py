from flask import Flask, render_template_string, request
import random

app = Flask(__name__)

# HTML con interfaz (emojis y estilo simple)
html = """
<!DOCTYPE html>
<html lang="es">
<head>
    <meta charset="UTF-8">
    <title>Piedra, Papel o Tijera</title>
    <style>
        body {
            font-family: Arial, sans-serif;
            text-align: center;
            margin-top: 50px;
            background: #f4f6f9;
        }
        h1 {
            color: #333;
        }
        .botones button {
            font-size: 20px;
            padding: 15px 25px;
            margin: 10px;
            border: none;
            border-radius: 8px;
            cursor: pointer;
            background-color: #4CAF50;
            color: white;
            transition: 0.3s;
        }
        .botones button:hover {
            background-color: #45a049;
        }
        .resultado {
            margin-top: 30px;
            font-size: 18px;
            color: #222;
        }
    </style>
</head>
<body>
    <h1>✊✋✌️ Piedra, Papel o Tijera</h1>
    <p>Elige tu jugada:</p>
    <div class="botones">
        <form method="POST">
            <button type="submit" name="jugada" value="piedra">🪨 Piedra</button>
            <button type="submit" name="jugada" value="papel">📄 Papel</button>
            <button type="submit" name="jugada" value="tijera">✂️ Tijera</button>
        </form>
    </div>

    {% if resultado %}
    <div class="resultado">
        <p><b>Tú elegiste:</b> {{ jugador }}</p>
        <p><b>Computadora eligió:</b> {{ computadora }}</p>
        <h3>{{ resultado }}</h3>
    </div>
    {% endif %}
</body>
</html>
"""

@app.route("/", methods=["GET", "POST"])
def index():
    resultado = None
    jugador = None
    computadora = None

    if request.method == "POST":
        jugador = request.form["jugada"]
        opciones = ["piedra", "papel", "tijera"]
        computadora = random.choice(opciones)

        if jugador == computadora:
            resultado = "¡Empate!"
        elif (jugador == "piedra" and computadora == "tijera") or \
             (jugador == "papel" and computadora == "piedra") or \
             (jugador == "tijera" and computadora == "papel"):
            resultado = "¡Ganaste! 🎉"
        else:
            resultado = "¡Perdiste! 😢"

    return render_template_string(html, resultado=resultado, jugador=jugador, computadora=computadora)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
