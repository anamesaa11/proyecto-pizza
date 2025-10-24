#Sistema de items

import random
from config.game_data import ITEMS_DATA


class Item:
    def __init__(self, nombre, tipo, efecto, valor):
        self.nombre = nombre
        self.tipo = tipo
        self.efecto = efecto
        self.valor = valor

    def usar(self, personaje):
        if self.efecto == "vida":
            personaje.curar(self.valor)
        elif self.efecto == "fuerza":
            personaje.fuerza += self.valor
            print(f"{personaje.nombre} gana +{self.valor} fuerza.")
        elif self.efecto == "defensa":
            personaje.defensa += self.valor
            print(f"{personaje.nombre} gana +{self.valor} defensa.")
        elif self.efecto == "velocidad":
            personaje.velocidad += self.valor
            print(f"{personaje.nombre} gana +{self.valor} velocidad.")
        else:
            print("Este ítem no tiene efecto.")

    def __str__(self):
        return f"{self.nombre} ({self.tipo}, {self.efecto} +{self.valor})"


def crear_items():
    items = []
    for datos in ITEMS_DATA:
        item = Item(
            nombre=datos["nombre"],
            tipo=datos["tipo"],
            efecto=datos["efecto"],
            valor=datos["valor"]
        )
        items.append(item)

    return items


def generar_item():
    """Devuelve un ítem aleatorio de la lista."""
    items_disponibles = crear_items()
    item = random.choice(items_disponibles)
    print(f"Has encontrado un {item.nombre} 🎁")
    return item


def usar_item(jugador, item):
    """Usa el ítem sobre el jugador."""
    print(f"Usando {item.nombre}...")
    item.usar(jugador)
