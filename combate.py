import random
from utilidades import elegir_item_random, mostrar_inventario


def turno_jugador(jugador, enemigo):
    while True:
        print('\n📜 Opciones:')
        print('1️⃣ Atacar')
        print('2️⃣ Defender')
        print('3️⃣ Usar ítem')
        print('4️⃣ Huir')

        opcion = input('ELige una opción: ')

        if opcion == '1':
            jugador.atacar(enemigo)
            break

        elif opcion == '2':
            print(f'{jugador.nombre} se Defiende! ¡Más fuerte ante daños!')
            jugador.defendiendo = True
            break

        elif opcion == '3':
            if jugador.inventario:
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
                print('No tienes Ítems aún.')
            break

        elif opcion == '4':
            if intentar_huir():
                print('\n🏃‍♂️ Lograste huir del combate.')
                #fin del combate
                enemigo.vida = 0
                break
            else:
                print('No pudiste huir.')
                break
        else:
            print('Opción no válida. Intenta de nuevo.')


def turno_enemigo(jugador, enemigo):
    if not enemigo.con_vida():
        return

    accion = random.choice(['atacar', 'habilidad']) if enemigo.habilidad else 'atacar'

    if accion == 'habilidad':
        enemigo.usar_habilidad(jugador)
    else:
        enemigo.atacar(jugador)

    jugador.defendiendo = False


def intentar_huir():
    #probabilidad de huir
    return random.random() < 0.5


def iniciar_combate(jugador, enemigo):
    print(f'⚔️ ¡COMBATE! {enemigo.nombre}')
    turno = 1
    vida_pizza = 100

    while jugador.con_vida() and enemigo.con_vida():
        print(f'\n--- Turno {turno} ---')
        print(f'Vida 🍕: {vida_pizza}')
        print(f'👤 {jugador.nombre} | ️Vida: {jugador.vida}/{jugador.vidamax}')
        print(f'👹 {enemigo.nombre} | Vida: {enemigo.vida}/{enemigo.vidamax}')

        turno_jugador(jugador, enemigo)
        if not enemigo.con_vida():
            print(f'\n⚔️ {jugador.nombre} derrotó a {enemigo.nombre} y ganó {enemigo.experiencia} EXP.')
            jugador.ganar_experiencia(enemigo.experiencia)

            # probabilidad de item
            if random.random() < 0.6:
                item_drop = elegir_item_random()
                jugador.inventario.append(item_drop)
                print(f'\n🎁 {enemigo.nombre} dejó: {item_drop.nombre}')
                mostrar_inventario(jugador)
            else:
                print('\n:( No obtuviste ningún ítem esta vez...')

            break

        turno_enemigo(jugador, enemigo)
        if not jugador.con_vida():
            print(f'\n💀 {jugador.nombre} ha caído en combate...')
            break

        vida_pizza -= 5
        if vida_pizza <= 0:
            print('\n❌ La pizza se ha enfriado demasiado. Perdiste :(')
            break

        turno += 1
