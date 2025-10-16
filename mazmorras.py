import random
from enemigos import obtener_enemigos, Enemigo

ESCENARIOS = {
    1: {"nombre": "Mazmorra 1 – Pueblo/ciudad 🏘️",
        "descripcion": "Callejones llenos de ladrones y clientes exigentes.",
        "suelo": "🛣️", "relleno": "🌿"},
    2: {"nombre": "Mazmorra 2 – Bosque encantado 🌲",
        "descripcion": "Donde los árboles cobran vida y te roban la pizza.",
        "suelo": "🌳", "relleno": "🍄"},
    3: {"nombre": "Mazmorra 3 – Cielos de Pepperoni ☁️",
        "descripcion": "Nubes de queso flotante y tormentas de orégano.",
        "suelo": "☁️", "relleno": "🪶"},
    4: {"nombre": "Mazmorra 4 – Castillo del Dragón 🏰🔥",
        "descripcion": "El último desafío antes de entregar la Gran Pizza Suprema.",
        "suelo": "🏰", "relleno": "🔥"}
}

def generar_mapa(ancho=6, largo=20, escenario=None):
    """Genera un mapa con un camino principal y escenario alrededor"""
    if escenario is None:
        escenario = ESCENARIOS[1]

    # mapa lleno de relleno (pasto o similar)
    mapa = [[escenario["relleno"] for _ in range(largo)] for _ in range(ancho)]

    # camino principal
    fila_camino = ancho // 2  # fila central inicial
    for col in range(largo):
        mapa[fila_camino][col] = escenario["suelo"]

        # curvas aleatorias del camino
        if random.random() < 0.2:
            cambio = random.choice([-1, 1])
            nueva_fila = fila_camino + cambio
            if 0 <= nueva_fila < ancho:
                fila_camino = nueva_fila
                mapa[fila_camino][col] = escenario["suelo"]

    # inicio del jugador
    inicio = (ancho // 2, 0)
    return mapa, inicio

def mostrar_mapa(mapa, posicion_jugador):
    """Muestra el mapa en consola con el jugador 🍕"""
    for i, fila in enumerate(mapa):
        for j, celda in enumerate(fila):
            if (i, j) == posicion_jugador:
                print("🍕", end=" ")
            else:
                print(celda, end=" ")
        print()

def mover_jugador(direccion, posicion, mapa):
    """Mueve al jugador dentro del mapa respetando los límites"""
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

def generar_enemigos_en_mapa(maz, mapa):
    """Genera enemigos en posiciones aleatorias dentro del mapa"""
    filas, columnas = len(mapa), len(mapa[0])
    enemigos_disponibles = obtener_enemigos(maz)
    cantidad = random.randint(5, 7)

    enemigos_colocados = []
    posiciones_ocupadas = set()

    for _ in range(cantidad):
        enemigo_base = random.choice(enemigos_disponibles)

        # encontrar posición libre
        while True:
            x = random.randint(0, filas - 1)
            y = random.randint(0, columnas - 1)
            if (x, y) not in posiciones_ocupadas and mapa[x][y] != "🍕":
                posiciones_ocupadas.add((x, y))
                break

        enemigo = Enemigo(
            enemigo_base.nombre,
            enemigo_base.nivel,
            enemigo_base.vida,
            enemigo_base.ataque,
            enemigo_base.defensa,
            enemigo_base.velocidad,
            enemigo_base.experiencia,
            enemigo_base.comportamiento,
            enemigo_base.habilidad
        )

        enemigos_colocados.append((x, y, enemigo))
        mapa[x][y] = "😈"
    return enemigos_colocados
