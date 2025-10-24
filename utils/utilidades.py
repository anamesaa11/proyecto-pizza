import os
import sys
import time
from config.game_settings import VELOCIDAD_TEXTO


def limpiar_pantalla():
    comando = "cls" if os.name == "nt" else "clear"
    os.system(comando)


def mostrar_texto_lento(texto, velocidad=VELOCIDAD_TEXTO):
    """imprime texto como narración (efecto RPG)."""
    for char in texto:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(velocidad)
    print()


ascii_path = os.path.join("ascii", "ascii-art.txt")


def mostrar_titulo_juego(path=ascii_path):
    with open(path, "r", encoding="utf-8") as f:
        print(f.read())


def final_juego(jugador):
    limpiar_pantalla()
    mostrar_texto_lento('🍕 Después de un largo viaje, atravesando 3 mazmorras...')
    mostrar_texto_lento('🔥 Venciendo dragones, duendes y ladrones hambrientos...')
    mostrar_texto_lento(f'👤 Finalmente, {jugador.nombre} llega al castillo del cliente.')
    time.sleep(1)

    limpiar_pantalla()
    mostrar_texto_lento('🏰 El cliente abre la puerta lentamente...')
    mostrar_texto_lento(' 👤 - ¡Al fin! Pensé que nunca llegaría mi pizza.')
    mostrar_texto_lento(' 🍕 - Está un poco fría... pero huele deliciosa.')
    mostrar_texto_lento(' 👤 - Toma tu propina, valiente repartidor.')
    time.sleep(1.5)

    limpiar_pantalla()
    mostrar_texto_lento('💰 Has recibido 1000 monedas de oro en propina $.')
    mostrar_texto_lento('🏆 ¡Has completado la GRAN ENTREGA!')
    mostrar_texto_lento(f'👏 Felicitaciones {jugador.nombre}, ¡has salvado el negocio!')
    time.sleep(1.5)

    limpiar_pantalla()
    mostrar_texto_lento('🎬 FIN DEL JUEGO')
    print('\nGracias por jugar 🍕⚔️❤️')
    input('\nPresiona ENTER para volver al menú principal...')


#Ver
def mensaje_centro(mensaje, ancho=50):
    espacios = (ancho - len(mensaje) // 2)
    print(" " * espacios + mensaje)


def pausa(segundos=1):
    time.sleep(segundos)


#Ver
def mostrar_barravida(vida_actual, vida_max, ancho=20):
    porcentaje = vida_actual / vida_max
    bloque_lleno = int(porcentaje * ancho)
    bloque_vacio = ancho - bloque_lleno

    barra = "█" * bloque_lleno + "░" * bloque_vacio
    print(f'❤️  [{barra}] {vida_actual}/{vida_max}')
