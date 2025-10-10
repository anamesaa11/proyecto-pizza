import random

ESCENARIOS = {
    1: {
        "nombre": "Mazmorra 1 – Pueblo/ciudad 🏘️",
        "descripcion": "Callejones llenos de ladrones y clientes exigentes.",
        "suelo": "🛣️",
        "relleno": "🏘️"
    },
    2: {
        "nombre": "Mazmorra 2 – Bosque Encantado 🌲",
        "descripcion": "Duendes y animales mágicos intentan quedarse con tu pizza.",
        "suelo": "🛣️",
        "relleno": "🌲"
    },
    3: {
        "nombre": "Mazmorra 3 – Cielos de Pepperoni ☁️",
        "descripcion": "Debes volar en un globo o montura para entregar pizzas en islas flotantes, evitando águilas.",
        "suelo": "🛣️",
        "relleno": "☁️"
    },
    4: {
        "nombre": "Mazmorra 4 – Castillo del Jefe Final 🏰🔥",
        "descripcion": "El Dragón Guardián de la Pizza Suprema espera… con hambre.",
        "suelo": "🛣️",
        "relleno": "🔥"
    }
}


def mostrar_mapa(mapa, jugador_pos):

    for i, fila in enumerate(mapa):
        fila_str = ""
        for j, casilla in enumerate(fila):
            if (i, j) == jugador_pos:
                fila_str += "🍕 "
            else:
                fila_str += str(casilla) + " "  # 🔧 corrección del TypeError
        print(fila_str)
    print()


def mover_jugador(direccion, jugador_pos, mapa):

    x, y = jugador_pos
    filas = len(mapa)
    columnas = len(mapa[0])

    if direccion == "w" and x > 0:
        x -= 1
    elif direccion == "s" and x < filas - 1:
        x += 1
    elif direccion == "a" and y > 0:
        y -= 1
    elif direccion == "d" and y < columnas - 1:
        y += 1
    else:
        print("Movimiento inválido.")

    return (x, y)


def generar_mapa(filas=5, columnas=20, escenario=ESCENARIOS[2]):

    mapa = [[escenario["relleno"] for _ in range(columnas)] for _ in range(filas)]

    fila = random.randint(0, filas - 1)
    col = 0
    inicio_camino = (fila, col)

    while col < columnas:
        mapa[fila][col] = escenario["suelo"]
        movimiento = random.choice(["derecha", "arriba", "abajo"])

        if movimiento == "derecha" and col < columnas - 1:
            col += 1
        elif movimiento == "arriba" and fila > 0 and col < columnas - 2:
            fila -= 1
            mapa[fila][col] = escenario["suelo"]
            col += 1
            mapa[fila][col] = escenario["suelo"]
        elif movimiento == "abajo" and fila < filas - 1 and col < columnas - 2:
            fila += 1
            mapa[fila][col] = escenario["suelo"]
            col += 1
            mapa[fila][col] = escenario["suelo"]
        else:
            col += 1

    return mapa, inicio_camino


class Enemigo:
    def __init__(self, nombre, vida, posicion):
        self.nombre = nombre
        self.vida = vida
        self.posicion = posicion


def crear_enemigos(cantidad, filas, columnas):

    enemigos = []
    for i in range(cantidad):
        x = random.randint(0, filas - 1)
        y = random.randint(0, columnas - 1)
        enemigos.append(Enemigo(f"Enemigo{i+1}", 50, (x, y)))
    return enemigos


def colocar_enemigos_en_mapa(mapa, enemigos):
    for enemigo in enemigos:
        x, y = enemigo.posicion
        mapa[x][y] = "👹"
    return mapa
