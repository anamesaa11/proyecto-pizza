from models.Jugador import crear_personaje_mazmorra
from utils.utilidades import limpiar_pantalla, mostrar_titulo_juego, mostrar_texto_lento
from game.mazmorras import (generar_mapa, mostrar_mapa, mover_jugador,
                            generar_enemigos_en_mapa, colocar_salida)
from game.combate import iniciar_combate
from config.game_data import ESCENARIOS_DATA
import time


def final_juego(jugador):
    limpiar_pantalla()
    mostrar_texto_lento('🍕 Después de un largo viaje, atravesando 3 mazmorras...')
    mostrar_texto_lento('🔥 Venciendo dragones, duendes y ladrones hambrientos...')
    mostrar_texto_lento(f'👤 Finalmente, {jugador.nombre} llega al castillo del cliente.')
    time.sleep(1)

    limpiar_pantalla()
    mostrar_texto_lento('🏰 El cliente abre la puerta lentamente...')
    mostrar_texto_lento(' 👤 - ¡Al fin! Pensé que nunca llegaría mi pizza.')
    mostrar_texto_lento(' 🍕 - Está un poco fría... pero huele deliciosa.')
    mostrar_texto_lento(' 👤 - Toma tu propina, valiente repartidor.')
    time.sleep(1.5)

    limpiar_pantalla()
    mostrar_texto_lento('💰 Has recibido 1000 monedas de oro en propina $.')
    mostrar_texto_lento('🏆 ¡Has completado la GRAN ENTREGA!')
    mostrar_texto_lento(f'👏 Felicitaciones {jugador.nombre}, ¡has salvado el negocio!')
    time.sleep(1.5)

    limpiar_pantalla()
    mostrar_texto_lento('🎬 FIN DEL JUEGO')
    print('\nGracias por jugar 🍕⚔️')
    input('\nPresiona ENTER para volver al menú principal...')


def jugar_mazmorra(maz):
    #limpiar_suave()
    limpiar_pantalla()
    print(f'\n -- NIVEL {maz} --')
    escenario = ESCENARIOS_DATA.get(maz, ESCENARIOS_DATA[1])
    print(f'{escenario["nombre"]}\n {escenario["descripcion"]}\n')

    #Crea el personaje en la mazmorra
    jugador = crear_personaje_mazmorra(maz)
    jugador.mostrar_estado()

    input('\nPresiona ENTER para comenzar...')

    mapa, posicion_inicio = generar_mapa(5, 20, escenario=escenario)
    jugador_pos = posicion_inicio

    #Enemigos en el mapa
    enemigos_colocados = generar_enemigos_en_mapa(maz, mapa)
    enemigos_objetivo = 0
    for enemigo in enemigos_colocados:
        if enemigo[3]:
            enemigos_objetivo += 1  # Contar enemigos
    portal_pos = None

    print(f'\nObjetivo: Elimina {enemigos_objetivo} enemigos del camino para abrir el portal.')

    while True:
        limpiar_pantalla()

        print(f'{escenario["nombre"]}')
        print(f'Enemigos restantes en el camino: {enemigos_objetivo}')

        mostrar_mapa(mapa, jugador_pos)

        mov = input('Mover (w/a/s/d, q para salir): ')
        if mov == 'q':
            print('🏃 Saliste de la mapa.')
            break

        nueva_posicion = mover_jugador(mov, jugador_pos, mapa)
        jugador_pos = nueva_posicion

        #Combate
        for (ex, ey, enemigo, es_objetivo) in enemigos_colocados[:]:
            if jugador_pos == (ex, ey) and enemigo.con_vida():
                print(f'\n⚔️ ¡Te encontraste con un {enemigo.nombre}!')
                print(f'Comportamiento: {enemigo.comportamiento}')

                iniciar_combate(jugador, enemigo)

                if not enemigo.con_vida():

                    print(f'\n💀Derrotaste al {enemigo.nombre}!')
                    mapa[ex][ey] = escenario["suelo"]
                    if es_objetivo:
                        enemigos_objetivo -= 1
                        print(f'Enemigos del camino restantes: {enemigos_objetivo}')

                #Enemigos derrotados
                    enemigos_colocados.remove((ex, ey, enemigo, es_objetivo))
                elif not jugador.con_vida():
                    print('\nPerdiste ... :(')
                    return False
                break

        if enemigos_objetivo == 0 and portal_pos is None:
            print(f'\n¡Camino liberado!')
            mostrar_texto_lento(f'¡Mazmorra {maz} completada!')
            portal_pos = colocar_salida(mapa, escenario)

        if portal_pos and jugador_pos == portal_pos:
            if maz < 3:  # si no es la última
                mostrar_texto_lento('Avanzando al siguiente nivel...')
                input('Presiona ENTER para avanzar...')
                return jugar_mazmorra(maz + 1)
            else:
                final_juego(jugador)
                return True

    return False


def mostrar_menu():
    limpiar_pantalla()
    mostrar_titulo_juego()

    print('MENÚ PRINCIPAL')
    print('=' * 30)
    print('1. Nueva Aventura')
    print('2. Salir')
    print('=' * 30)


def main():
    while True:
        mostrar_menu()
        opcion = input('Elige una opción: ').strip()

        if opcion == '1':
            print('\n🚀 ¡Comenzando nueva aventura!')
            mostrar_texto_lento('🍕 Un cliente ha pedido una pizza...')
            mostrar_texto_lento('📍 Pero vive al otro lado de 3 peligrosas mazmorras...')
            mostrar_texto_lento('⚔️ ¿Podrás entregarla a tiempo?')

            input('\nPresiona ENTER para comenzar...')

            resultado = jugar_mazmorra(1)

            if resultado:
                input('\nPresiona ENTER para volver al menú principal')
            else:
                input('\nPresiona ENTER para volver al menú principal...')

        elif opcion == '2':
            print('Gracias por jugar ❤️')
            break

        else:
            print('Opcion no válida. Intenta de nuevo.')
            input('Presiona ENTER para continuar')


if __name__ == "__main__":
    main()
