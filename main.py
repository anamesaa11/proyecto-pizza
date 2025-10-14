import random
from personajes import crear_personaje_mazmorra
from enemigos import crear_enemigo
from combate import iniciar_combate
from mazmorras import generar_mapa, mostrar_mapa, mover_jugador, ESCENARIOS
from items import generar_item
from utilidades import mostrar_inventario, usar_item_inventario, mostrar_texto_lento


def jugar_mazmorra(nivel):
    print(f"\n -- NIVEL {nivel} --")

    jugador = crear_personaje_mazmorra(nivel)
    mapa, inicio = generar_mapa(5, 20, ESCENARIOS[nivel])
    enemigos = crear_enemigo(nivel)

    posicion_jugador = inicio
    jugando = True

    while jugando:
        print("-- ESTADO DEL PERSONAJE --")
        print(f"Nombre: {jugador.nombre} - {jugador.clase}")
        print(f"Vida: {jugador.vida_actual} / {jugador.vida_maxima}")
        print(f"Nivel: {jugador.nivel} | EXP {jugador.experiencia}")
        print(f"Fuerza: {jugador.fuerza} | Defensa: {jugador.defensa} | Velocidad: {jugador.velocidad}")
        print(f"Inventario: {len(jugador.inventario)} ítems")

        mostrar_mapa(mapa, posicion_jugador)

        accion = input("Mover (w/a/s/d), (c)ombatir, (i)nventario o (q)uit: ").lower()

        if accion in ["w", "a", "s", "d"]:
            posicion_jugador = mover_jugador(accion, posicion_jugador, mapa)

        elif accion == "c":
            # ✅ Corrección: elegir un enemigo individual
            enemigo = random.choice(enemigos)
            print(f"⚔️ ¡COMBATE CONTRA {enemigo.nombre}!")
            iniciar_combate(jugador, enemigo)

        elif accion == "i":
            mostrar_inventario(jugador)
            usar = input("¿Usar ítem? (número o enter para cancelar): ")
            if usar.isdigit():
                usar_item_inventario(jugador, int(usar) - 1)

        elif accion == "q":
            print("👋 Saliendo de la mazmorra...")
            jugando = False

        else:
            print("⚠️ Acción no válida. Intenta otra vez.")


def main():
    print("\nMENÚ DE PRUEBAS")
    print("1. Probar Juego-Mazmorra.")
    print("2. Probar Mapa y Movimiento.")
    print("3. Probar Combate.")
    print("4. Salir.")

    opcion = input("Ingrese opción: ")

    if opcion == "1":
        jugar_mazmorra(1)
    elif opcion == "2":
        mapa, inicio = generar_mapa(5, 20, ESCENARIOS[1])
        mostrar_mapa(mapa, inicio)
    elif opcion == "3":
        jugador = crear_personaje_mazmorra(1)
        enemigos = crear_enemigo(1)
        enemigo = random.choice(enemigos)
        iniciar_combate(jugador, enemigo)
    else:
        print("👋 Saliendo...")


if __name__ == "__main__":
    main()

