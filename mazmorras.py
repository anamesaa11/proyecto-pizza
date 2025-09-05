import random

def mostrar_mapa(mapa, jugador_pos):
    """
    Muestra el mapa en consola con el jugador en su posición actual.
    @ representa al jugador
    """
    for i, fila in enumerate(mapa):
        fila_str = ""
        for j, casilla in enumerate(fila):
            if (i, j) == jugador_pos:
                fila_str += "@ "
            else:
                fila_str += casilla + " "
        print(fila_str)
    print()

def mover_jugador(direccion, jugador_pos, mapa):
    """
    Mueve al jugador según la tecla ingresada:
    w = arriba, s = abajo, a = izquierda, d = derecha
    """
    x, y = jugador_pos
    filas = len(mapa)
    columnas = len(mapa[0])

    if direccion == "w" and x > 0:  # arriba
        x -= 1
    elif direccion == "s" and x < filas - 1:  # abajo
        x += 1
    elif direccion == "a" and y > 0:  # izquierda
        y -= 1
    elif direccion == "d" and y < columnas - 1:  # derecha
        y += 1
    else:
        print("Movimiento inválido.")

    return (x, y)

def generar_mapa(filas=5, columnas=20):

    mapa = [["🌳" for _ in range(columnas)] for _ in range(filas)]

    fila = random.randint(0, filas - 1)
    col = 0

    while col < columnas:
        mapa[fila][col] = "🛣️"
        movimiento = random.choice(["derecha", "arriba", "abajo"])

        if movimiento == "derecha" and col < columnas - 1:
            col += 1
        elif movimiento == "arriba" and fila > 0 and col < columnas - 2:
            fila -= 1
            mapa[fila][col] = "🛣️"
            col += 1
            mapa[fila][col] = "🛣️"
        elif movimiento == "abajo" and fila < filas - 1 and col < columnas - 2:
            fila += 1
            mapa[fila][col] = "🛣️"
            col += 1
            mapa[fila][col] = "🛣️"
        else:
            col += 1

    return mapa
