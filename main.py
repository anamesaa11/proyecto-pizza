import random
from personajes import crear_personaje, mostrar_estado
from enemigos import generar_enemigo
from items import generar_item, usar_item
from utilidades import combate
from mazmorras import ESCENARIOS, generar_mapa, mostrar_mapa, mover_jugador

def main():
    print("=== REPARTIDOR DE PIZZA MEDIEVAL ===")

    # Crear personaje principal
    jugador = crear_personaje("Pizzerito")
    print("¡Bienvenido, valiente repartidor!\n")
    mostrar_estado(jugador)

    # Elegir mazmorra
    print("\nElige tu mazmorra:")
    for k, v in ESCENARIOS.items():
        print(f"{k}. {v['nombre']} - {v['descripcion']}")
    eleccion = int(input("Número: "))
    escenario = ESCENARIOS.get(eleccion, ESCENARIOS[1])

    # Generar mapa
    mapa, jugador_pos = generar_mapa(5, 20, escenario)
    print(f"\nEntraste en: {escenario['nombre']}")

    # Bucle de juego
    while True:
        mostrar_mapa(mapa, jugador_pos)
        accion = input("Movimiento (w/a/s/d, q salir): ").lower()

        if accion == "q":
            print("¡Fin de la aventura!")
            break

        jugador_pos = mover_jugador(accion, jugador_pos, mapa)

        # Eventos aleatorios
        evento = random.choice(["nada", "enemigo", "item"])
        if evento == "enemigo":
            enemigo = generar_enemigo()
            print(f"\n¡Un {enemigo['nombre']} aparece! 🍄")
            combate(jugador, enemigo)
        elif evento == "item":
            item = generar_item()
            print(f"\n¡Encontraste un {item['nombre']}! 🎁")
            usar = input("¿Quieres usarlo? (s/n): ").lower()
            if usar == "s":
                usar_item(jugador, item)

        # Revisar si jugador está vivo
        if jugador["vida"] <= 0:
            print("\n☠️ Has caído en la aventura. ¡Game Over!")
            break

if __name__ == "__main__":
    main()
