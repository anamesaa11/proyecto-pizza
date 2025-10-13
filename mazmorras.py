import random

ESCENARIOS = {
    1: {
        "nombre": "Mazmorra 1 – Pueblo/ciudad 🏘️",
        "descripcion": "Callejones llenos de ladrones y clientes exigentes.",
        "suelo": "🛣️",
        "relleno": "🏘️"
    },
    2: {
        "nombre": "Mazmorra 2 – Bosque encantado 🌲",
        "descripcion": "Donde los árboles cobran vida y te roban la pizza.",
        "suelo": "🌳",
        "relleno": "🍄"
    },
    3: {
        "nombre": "Mazmorra 3 – Cielos de Pepperoni ☁️",
        "descripcion": "Nubes de queso flotante y tormentas de orégano.",
        "suelo": "☁️",
        "relleno": "🪶"
    },
    4: {
        "nombre": "Mazmorra 4 – Castillo del Dragón 🏰🔥",
        "descripcion": "El último desafío antes de entregar la Gran Pizza Suprema.",
        "suelo": "🏰",
        "relleno": "🔥"
    }
}


def generar_mapa(ancho, largo, escenario):

    mapa = [[escenario["suelo"] for _ in range(largo)] for _ in range(ancho)]

    # Agregar algunos elementos aleatorios (relleno)
    for _ in range(random.randint(5, 15)):
        x, y = random.randint(0, ancho - 1), random.randint(0, largo - 1)
        mapa[x][y] = escenario["relleno"]

    inicio = (ancho // 2, largo // 2)
    return mapa, inicio


def mostrar_mapa(mapa, posicion_jugador):

    for i, fila in enumerate(mapa):
        for j, celda in enumerate(fila):
            if (i, j) == posicion_jugador:
                print("🧍", end=" ")
            else:
                print(celda, end=" ")
        print()


def mover_jugador(direccion, posicion, mapa):

    x, y = posicion
    max_x, max_y = len(mapa), len(mapa[0])

    if direccion == "w" and x > 0:
        x -= 1
    elif direccion == "s" and x < max_x - 1:
        x += 1
    elif direccion == "a" and y > 0:
        y -= 1
    elif direccion == "d" and y < max_y - 1:
        y += 1
    else:
        print("🚫 No puedes moverte en esa dirección.")

    return (x, y)

