import random

from personajes import Personaje, crear_personaje_mazmorra
from enemigos import Enemigo, obtener_enemigos
from utilidades import mostrar_inventario, usar_item_inventario, limpiar_pantalla
from mazmorras import generar_mapa, mostrar_mapa, mover_jugador, ESCENARIOS, generar_enemigos_en_mapa
from combate import iniciar_combate

progreso = 1


def prueba_mapa():
    limpiar_pantalla()
    print('\nPRUEBA MAZMORRA')
    mapa, inicio = generar_mapa(5, 10, ESCENARIOS[1])
    jugador_pos = inicio

    while True:
        mostrar_mapa(mapa, jugador_pos)
        mov = input('Mover (w/a/s/d, q para salir): ')
        if mov == 'q':
            print('Saliendo de la mazmorra...')
            break
        jugador_pos = mover_jugador(mov, jugador_pos, mapa)


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
    escenario = ESCENARIOS.get(maz, ESCENARIOS[1])
    mapa, inicio = generar_mapa(5, 20, escenario=escenario)
    jugador_pos = inicio

    #Enemigos en el mapa
    enemigos_colocados = generar_enemigos_en_mapa(maz, mapa)

    while True:
        mostrar_mapa(mapa, jugador_pos)
        mov = input('Mover (w/a/s/d, q para salir): ')
        if mov == 'q':
            print('🏃 Saliste de la mapa.')
            break

        jugador_pos = mover_jugador(mov, jugador_pos, mapa)

        for (ex, ey, enemigo) in enemigos_colocados:
            if jugador_pos == (ex, ey) and enemigo.con_vida():
                print(f'\n⚔️ ¡Te encontraste con un {enemigo.nombre}!')
                iniciar_combate(jugador, enemigo)
                enemigos_colocados = [e for e in enemigos_colocados if e[2].con_vida()] #ver
                if not enemigo.con_vida():
                    print(f'☠️ {enemigo.nombre} ha sido derrotado.')
                    mapa[ex][ey] = "🛣️"  #para limpiar enemigo
                break


if __name__ == "__main__":
    main()
