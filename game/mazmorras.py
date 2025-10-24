import random
from models.enemigos import obtener_enemigos, Enemigo
from config.game_data import ESCENARIOS_DATA
from config.game_settings import (
    ANCHO_MAPA, LARGO_MAPA, PROB_CAMBIO_CAMINO, ENEMIGOS_MIN_POR_MAPA,
    ENEMIGOS_MAX_POR_MAPA, PROB_ENEMIGO_OBJETIVO)


def generar_mapa(ancho=ANCHO_MAPA, largo=LARGO_MAPA, escenario=None):
    if escenario is None:
        escenario = ESCENARIOS_DATA[1]

    mapa = [[escenario["relleno"] for _ in range(largo)] for _ in range(ancho)]

    fila_camino = ancho // 2
    for col in range(largo):
        mapa[fila_camino][col] = escenario["suelo"]

        if random.random() < PROB_CAMBIO_CAMINO:
            cambio = random.choice([-1, 1])
            nueva_fila = fila_camino + cambio
            if 0 <= nueva_fila < ancho:
                fila_camino = nueva_fila
                mapa[fila_camino][col] = escenario["suelo"]

    inicio = (ancho // 2, 0)
    return mapa, inicio


def mostrar_mapa(mapa, posicion_jugador):
    for i, fila in enumerate(mapa):
        fila_str = ""
        for j, celda in enumerate(fila):
            if (i, j) == posicion_jugador:
                fila_str += "🍕"
            else:
                fila_str += str(celda) + " "
        print(fila_str)
    print()


def mover_jugador(direccion, posicion, mapa):
    x, y = posicion
    max_x, max_y = len(mapa), len(mapa[0])
    #suelo = escenario["suelo"]
    #relleno = escenario["relleno"]

    #if mapa[x][y] == "🍕" or mapa[x][y] == suelo:
    #    mapa[x][y] = suelo
    #else:
    #    mapa[x][y] = relleno

    if direccion.lower() == "w" and x > 0:
        x -= 1
    elif direccion.lower() == "s" and x < max_x - 1:
        x += 1
    elif direccion.lower() == "a" and y > 0:
        y -= 1
    elif direccion.lower() == "d" and y < max_y - 1:
        y += 1
    else:
        print("🚫 No puedes moverte en esa dirección.")

    return x, y


def generar_enemigos_en_mapa(maz, mapa):

    filas, columnas = len(mapa), len(mapa[0])
    enemigos_disponibles = obtener_enemigos(maz)
    cantidad = random.randint(ENEMIGOS_MIN_POR_MAPA, ENEMIGOS_MAX_POR_MAPA)

    enemigos_colocados = []
    posiciones_ocupadas = set()

    #Define posiciones del camino
    posiciones_camino = []
    for i in range(filas):
        for j in range(columnas):
            if mapa[i][j] in ["🛣️", "🌳", "☁️"]:
                posiciones_camino.append((i, j))

    for _ in range(cantidad):
        enemigo_base = random.choice(enemigos_disponibles)

        #Decide si el enemigo va fuera o dentro del camino
        es_objetivo = random.random() < PROB_ENEMIGO_OBJETIVO

        if es_objetivo and posiciones_camino:
            pos = random.choice(posiciones_camino)
            posiciones_camino.remove(pos)
        else:
            # encontrar posición libre
            intentos = 0
            while intentos < 50:
                x = random.randint(0, filas - 1)
                y = random.randint(0, columnas - 1)
                if (x, y) not in posiciones_ocupadas and mapa[x][y] != "🍕":
                    pos = (x, y)
                    break
                intentos += 1
            else:
                continue

        posiciones_ocupadas.add(pos)
        x, y = pos

        enemigo = Enemigo(
            enemigo_base.nombre,
            enemigo_base.nivel,
            enemigo_base.vida,
            enemigo_base.fuerza,
            enemigo_base.defensa,
            enemigo_base.velocidad,
            enemigo_base.experiencia,
            enemigo_base.comportamiento,
            enemigo_base.habilidad
        )

        enemigos_colocados.append((x, y, enemigo, es_objetivo))
        mapa[x][y] = "😈"

    return enemigos_colocados


def colocar_salida(mapa, escenario):
    filas, columnas = len(mapa), len(mapa[0])
    suelo = escenario["suelo"]

    for fila in range(filas):
        if mapa[fila][columnas - 1] == suelo:
            mapa[fila][columnas - 1] = "🌀"
            return fila, columnas - 1

    mapa[filas - 1][columnas - 1] = "🌀"
    return filas - 1, columnas - 1
