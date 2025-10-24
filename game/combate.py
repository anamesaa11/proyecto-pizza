#Sistema de combate

import random
from utils.inventario import mostrar_inventario
from models.items import generar_item
from config.game_settings import (
    PROBABILIDAD_HUIR, PROBABILIDAD_ITEM, VIDA_PIZZA_INICIAL, REDUCCION_VIDA_PIZZA_POR_TURNO)


def turno_jugador(jugador, enemigo):
    while True:
        print('\n📜 Opciones:')
        print('1️⃣ Atacar')
        print('2️⃣ Defender')
        print('3️⃣ Usar ítem')
        print('4️⃣ Intentar huir')

        opcion = input('ELige una opción: ')

        if opcion == '1':
            jugador.atacar(enemigo)
            break

        elif opcion == '2':
            print(f'{jugador.nombre} se prepara para defenderse!')
            jugador.defendiendo = True
            break

        elif opcion == '3':
            if len(jugador.inventario) > 0:
                mostrar_inventario(jugador)
                try:
                    nro_i = int(input('Selecciona número de ítem para usar (0 para cancelar): '))
                    if nro_i > 0:
                        usar = nro_i - 1
                        if 0 <= usar < len(jugador.inventario):
                            item = jugador.inventario.pop(usar)
                            item.usar(jugador)
                    else:
                        print('X')
                except ValueError:
                    print('Entrada inválida.')
            else:
                print('No tienes Ítems en tu inventario.')
            break

        elif opcion == '4':
            if intentar_huir():
                print('\n🏃‍♂️ Lograste huir del combate.')
                #fin del combate
                enemigo.vida = 0
                break
            else:
                print('\nNo pudiste huir.')
                break
        else:
            print('Opción no válida. Intenta de nuevo.')


def turno_enemigo(jugador, enemigo):
    if not enemigo.con_vida():
        return

    if enemigo.habilidad:
        accion = random.choice(['atacar', 'habilidad'])
    else:
        accion = 'atacar'

    if accion == 'habilidad':
        enemigo.usar_habilidad(jugador)
    else:
        enemigo.atacar(jugador)

    jugador.defendiendo = False


def intentar_huir():
    #probabilidad de huir
    return random.random() < PROBABILIDAD_HUIR


def iniciar_combate(jugador, enemigo):
    print(f'⚔️ ¡COMBATE! {enemigo.nombre}')
    print(f'🍕 vs 👹')
    turno = 1
    vida_pizza = VIDA_PIZZA_INICIAL

    while jugador.con_vida() and enemigo.con_vida():
        print(f'\n--- Turno {turno} ---')
        print(f'Vida 🍕: {vida_pizza}')
        print(f'👤 {jugador.nombre} | ️Vida: {jugador.vida}/{jugador.vidamax}')
        print(f'👹 {enemigo.nombre} | Vida: {enemigo.vida}')

        turno_jugador(jugador, enemigo)

        if not enemigo.con_vida():
            print(f'\n⚔️ ¡{jugador.nombre} derrotó a {enemigo.nombre}!')
            print(f'Ganaste {enemigo.experiencia} puntos de EXP.')
            jugador.ganar_experiencia(enemigo.experiencia)

            # probabilidad de item
            if random.random() < PROBABILIDAD_ITEM:
                item_drop = generar_item()
                jugador.inventario.append(item_drop)
                print(f'\n🎁 {enemigo.nombre} dejó caer: {item_drop.nombre}')
                mostrar_inventario(jugador)
            else:
                print('\n:( No obtuviste ningún ítem esta vez...')

            break

        turno_enemigo(jugador, enemigo)

        if not jugador.con_vida():
            print(f'\n💀 {jugador.nombre} ha caído en combate...')
            print('🍕 La pizza nunca llegará a su destino.')
            break

        vida_pizza -= REDUCCION_VIDA_PIZZA_POR_TURNO
        if vida_pizza <= 0:
            print('\n❌ La pizza se ha enfriado demasiado. Perdiste :(')
            jugador.vida = 0
            break

        turno += 1
        input('\nPresiona ENTER para continuar...')
