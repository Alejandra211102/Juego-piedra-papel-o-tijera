document.addEventListener("DOMContentLoaded", () => {
  const opciones = ["piedra", "papel", "tijera"];

  let victorias = 0;
  let derrotas = 0;
  let empates = 0;

  const victoriasEl = document.getElementById("victorias");
  const derrotasEl = document.getElementById("derrotas");
  const empatesEl = document.getElementById("empates");
  const jugadorEl = document.getElementById("jugador");
  const computadoraEl = document.getElementById("computadora");
  const mensajeEl = document.getElementById("mensaje");

  function jugar(jugador) {
    const computadora = opciones[Math.floor(Math.random() * opciones.length)];

    jugadorEl.textContent = jugador;
    computadoraEl.textContent = computadora;

    if (jugador === computadora) {
      mensajeEl.textContent = "¡Empate!";
      empates++;
    } else if (
      (jugador === "piedra" && computadora === "tijera") ||
      (jugador === "papel" && computadora === "piedra") ||
      (jugador === "tijera" && computadora === "papel")
    ) {
      mensajeEl.textContent = "¡Ganaste!";
      victorias++;
    } else {
      mensajeEl.textContent = "¡Perdiste!";
      derrotas++;
    }

    victoriasEl.textContent = victorias;
    derrotasEl.textContent = derrotas;
    empatesEl.textContent = empates;
  }

  // Agregar eventos a botones
  document.querySelectorAll(".choice").forEach(btn => {
    btn.addEventListener("click", () => jugar(btn.dataset.choice));
  });

    // Reiniciar el juego
  document.getElementById("reiniciar").addEventListener("click", () => {
    victorias = 0;
    derrotas = 0;
    empates = 0;

    victoriasEl.textContent = victorias;
    derrotasEl.textContent = derrotas;
    empatesEl.textContent = empates;
    jugadorEl.textContent = "—";
    computadoraEl.textContent = "—";
    mensajeEl.textContent = "Elige una opción para comenzar…";
  });
});
