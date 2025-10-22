from Jugador import Jugador, crear_personaje_mazmorra
from enemigos import obtener_enemigos
from utilidades import mostrar_inventario, usar_item_inventario, limpiar_pantalla
from mazmorras import generar_mapa, mostrar_mapa, mover_jugador, ESCENARIOS, generar_enemigos_en_mapa, colocar_salida
from combate import iniciar_combate



def jugar_mazmorra(maz):
    limpiar_pantalla()
    print(f'\n -- NIVEL {maz} --')
    escenario = ESCENARIOS.get(maz, ESCENARIOS[1])

    #Crea el personaje en la mazmorra
    jugador = crear_personaje_mazmorra(maz)
    jugador.mostrar_estado()

    mapa, inicio = generar_mapa(5, 20, escenario=escenario)
    jugador_pos = inicio

    #Enemigos en el mapa
    enemigos_colocados = generar_enemigos_en_mapa(maz, mapa)
    enemigos_objetivo = sum(1 for e in enemigos_colocados if e[3]) # Contar enemigos
    portal_pos = None

    while True:
        mostrar_mapa(mapa, jugador_pos)
        mov = input('Mover (w/a/s/d, q para salir): ')
        if mov == 'q':
            print('🏃 Saliste de la mapa.')
            break

        jugador_pos = mover_jugador(mov, jugador_pos, mapa)

        #Combate
        for (ex, ey, enemigo, es_objetivo) in enemigos_colocados:
            if jugador_pos == (ex, ey) and enemigo.con_vida():
                print(f'\n⚔️ ¡Te encontraste con un {enemigo.nombre}!')
                iniciar_combate(jugador, enemigo)

                if not enemigo.con_vida():
                    mapa[ex][ey] = "🛣️"
                    if es_objetivo:
                        enemigos_objetivo -= 1
                        print(f'📉 Enemigos del camino restantes: {enemigos_objetivo}')
                #Enemigos derrotados
                enemigos_colocados = [e for e in enemigos_colocados if e[2].con_vida()] #ver
                break

        if enemigos_objetivo == 0 and portal_pos is None:
            print(f'\n¡Camino liberado!¡Mazmorra {maz} completada!')
            portal_pos = colocar_salida(mapa)

        if portal_pos and jugador_pos == portal_pos:
            print('Avanzando al siguiente nivel.')
            if maz < 3:  # si no es la última
                input('Presiona ENTER para pasar a la siguiente mazmorra...')
                jugar_mazmorra(maz + 1)
            else:
                print('\n🏆 ¡Has completado todas las mazmorras! 🏆')
            break


if __name__ == "__main__":
    jugar_mazmorra(1)
