from mazmorras import generar_mapa, mostrar_mapa, mover_jugador, ESCENARIOS

def main():
    print("=== ELIGE TU MAZMORRA ===")
    for num, esc in ESCENARIOS.items():
        print(f"{num}. {esc['nombre']} -> {esc['descripcion']}")

    eleccion = int(input("Número de mazmorra: "))
    escenario = ESCENARIOS.get(eleccion, ESCENARIOS[2])  # default Bosque

    mapa, jugador_pos = generar_mapa(escenario=escenario)

    print(f"\nEntraste a: {escenario['nombre']}")
    mostrar_mapa(mapa, jugador_pos)

    while True:
        accion = input("Mover (w/a/s/d) o q para salir: ").lower()
        if accion == "q":
            print("¡Hasta la próxima entrega de pizza! 🍕")
            break
        else:
            jugador_pos = mover_jugador(accion, jugador_pos, mapa)
            mostrar_mapa(mapa, jugador_pos)

if __name__ == "__main__":
    main()
