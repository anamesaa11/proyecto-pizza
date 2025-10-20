from personajes import Personaje, crear_personaje_mazmorra
from enemigos import Enemigo, obtener_enemigos
from utilidades import mostrar_inventario, usar_item_inventario, limpiar_pantalla
from mazmorras import generar_mapa, mostrar_mapa, mover_jugador, ESCENARIOS, generar_enemigos_en_mapa
from combate import iniciar_combate

progreso = 1


def jugar_mazmorra(maz):
    limpiar_pantalla()
    print(f'\n -- NIVEL {maz} --')

    #Crea el personaje en la mazmorra
    jugador = crear_personaje_mazmorra(maz)
    jugador.mostrar_estado()
    escenario = ESCENARIOS.get(maz, ESCENARIOS[1])
    mapa, inicio = generar_mapa(5, 20, escenario=escenario)
    jugador_pos = inicio

    #Enemigos en el mapa
    enemigos_colocados = generar_enemigos_en_mapa(maz, mapa)
    enemigos_objetivo = sum(1 for e in enemigos_colocados if e[3]) # Contar enemigos

    while True:
        mostrar_mapa(mapa, jugador_pos)
        mov = input('Mover (w/a/s/d, q para salir): ')
        if mov == 'q':
            print('🏃 Saliste de la mapa.')
            break

        jugador_pos = mover_jugador(mov, jugador_pos, mapa)

        #Combate
        for (ex, ey, enemigo) in enemigos_colocados:
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

    if enemigos_objetivo <= 0:
        print(f'\n¡Camino liberado!¡Mazmorra {maz} completada!')
        if maz < 3:  # si no es la última
            input('Presiona ENTER para pasar a la siguiente mazmorra...')
            jugar_mazmorra(maz + 1)
        else:
            print('\n🏆 ¡Has completado todas las mazmorras! 🏆')
        break

#if __name__ == "__main__":
#    main()
