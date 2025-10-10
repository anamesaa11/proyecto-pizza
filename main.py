from personajes import Personaje, crear_personaje_mazmorra
from enemigos import Enemigo, crear_enemigo
from items import lista_items
from utilidades import mostrar_inventario, usar_item_inventario, limpiar_pantalla
from mazmorras import generar_mapa, mostrar_mapa, mover_jugador
from combate import iniciar_combate

progreso = 1

# def prueba_personaje():
#     print('\nPRUEBA DE PERSONAJE')
#     heroe = Personaje('Pizzerito', 'Plebeyo')
#     heroe.inventario.extend(lista_items[:3])
#     heroe.mostrar_estado()
#     mostrar_inventario(heroe)
#
#     print('\nUsando 1er ítem del Inventario...')
#     usar_item_inventario(heroe, 0)
#     heroe.mostrar_estado()


def prueba_mapa():
    limpiar_pantalla()
    print('\nPRUEBA MAZMORRA')
    mapa = generar_mapa(5, 10)
    jugador_pos = (0, 0)

    while True:
        mostrar_mapa(mapa, jugador_pos)
        mov = input('Mover (w/a/s/d, q para salir): ')
        if mov == 'q':
            print('Saliendo de la mazmorra...')
            break
        jugador_pos = mover_jugador(mov, jugador_pos, mapa)


#def prueba_combate():
#    limpiar_pantalla()
#    print('\nPRUEBA COMBATE')
#    jugador = Personaje('Pizzerito', 'Plebeyo')
#    enemigo =
#    iniciar_combate(jugador, enemigo)


def main():
    while True:
        print('\nMENÚ DE PRUEBAS')
        print('1. Probar Juego-Mazmorra.')
        print('2. Probar Mapa y Movimiento.')
        print('3. Probar Combate.')
        print('4. Salir.')

        opcion = input('Ingrese opción: ')

        if opcion == '1':
            jugar_mazmorra(1)
        elif opcion == '2':
            prueba_mapa()
        elif opcion == '3':
            #prueba_combate()
            pass
        elif opcion == '4':
            print('Saliendo...')
            break
        else:
            print('Opción no válida.')


def jugar_mazmorra(maz):
    limpiar_pantalla()
    print(f'\n -- NIVEL {maz} --')

    jugador = crear_personaje_mazmorra(maz)
    jugador.mostrar_estado()
    mapa = generar_mapa()
    mostrar_mapa(mapa, (0, 0))
    enemigo = crear_enemigo(maz)
    iniciar_combate(jugador, enemigo)


if __name__ == "__main__":
    main()