import random
import os
import sys
import time
from items import lista_items


def elegir_item_random():
    """devuelve un ítem al azar como drop de enemigo."""
    return random.choice(lista_items)


def mostrar_inventario(personaje):
    """mestra el inventario del personaje."""
    if not personaje.inventario:
        print(f"{personaje.nombre} no tiene ítems.")
        return
    print(f"Inventario de {personaje.nombre}:")
    for i, item in enumerate(personaje.inventario, 1):
        print(f"{i}. {item.nombre} ({item.tipo})")


def usar_item_inventario(personaje, indice):
    """usa y elimina un ítem del inventario por índice."""
    if 0 <= indice < len(personaje.inventario):
        item = personaje.inventario.pop(indice)
        item.usar(personaje)
    else:
        print("Índice inválido.")


def limpiar_suave():
    os.system("cls" if os.name == "nt" else "clear")


def limpiar_pantalla():
    if os.name == "nt":
        os.system("cls")
    else:
        os.system("clear")
    sys.stdout.write("\033[H\033[J")
    sys.stdout.flush()


def mostrar_texto_lento(texto, velocidad=0.03):
    """imprime texto como narración (efecto RPG)."""
    for char in texto:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(velocidad)
    print()
