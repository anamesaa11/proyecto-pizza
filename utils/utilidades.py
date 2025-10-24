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


def mostrar_titulo_juego():
    titulo = " "
    #Insertar titulo

    print(titulo)


def mensaje_centro(mensaje, ancho=50):
    espacios = (ancho - len(mensaje) // 2)
    print(" " * espacios + mensaje)


def pausa(segundos=1):
    time.sleep(segundos)


def mostrar_barravida(vida_actual, vida_max, ancho=20):
    porcentaje = vida_actual / vida_max
    bloque_lleno = int(porcentaje * ancho)
    bloque_vacio = ancho - bloque_lleno

    barra = "█" * bloque_lleno + "░" * bloque_vacio
    print(f'❤️  [{barra}] {vida_actual}/{vida_max}')
