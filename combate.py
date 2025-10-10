import random


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
            print('No tienes Ítems aún.') #IMPLEMENTAR FUNCION DE ITEMS

        elif opcion == '4':
            if intentar_huir():
                print('🏃‍♂️ Lograste huir del combate.')
                enemigo.vida = 0    #Esto seria FIN DEL COMBATE
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

    if accion == 'atacar':
        enemigo.atacar(jugador)
    else:
        enemigo.usar_habilidad(jugador)

    jugador.defendiendo = False


def intentar_huir():
    return random.random() < 0.5 #probabilidad de HUIR


def iniciar_combate (jugador, enemigo):
    print(f'COMBATE! {enemigo}')
    turno = 1
    vida_pizza = 100

    while jugador.con_vida() and enemigo.con_vida():
        print(f'\n--- Turno {turno} ---')
        print(f'Vida 🍕: {vida_pizza}')
        print(f'👤 {jugador.nombre} | Vida: {jugador.vida}')
        print(f'👹 {enemigo.nombre} | Vida: {enemigo.vida}')

        turno_jugador(jugador, enemigo)
        if not enemigo.con_vida():
            print(f'⚔️{jugador.nombre} derrotó a {enemigo.nombre} y ganó {enemigo.experiencia} EXP.')
            jugador.ganar_experiencia(enemigo.experiencia)
            break

        turno_enemigo(jugador, enemigo)
        if not jugador.con_vida():
            print(f'💀 {jugador.nombre} ha caído en combate...')
            break

        vida_pizza -= 5
        if vida_pizza <= 0:
            print('❌ La pizza se ha enfriado demasiado. Perdiste :(')
            break

        turno += 1
