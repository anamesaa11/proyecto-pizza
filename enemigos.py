import random


class Enemigo:
    def __init__(self, nombre, nivel, vida, ataque, defensa, velocidad, experiencia, comportamiento, habilidad):
        self.nombre = nombre
        self.nivel = nivel
        self.vida = vida
        self.ataque = ataque
        self.defensa = defensa
        self.velocidad = velocidad
        self.experiencia = experiencia
        self.comportamiento = comportamiento
        self.habilidad = habilidad

    def con_vida(self):
        return self.vida > 0

    def recibir_dano(self, cantidad):
        dano_real = max(0, cantidad - self.defensa)
        self.vida -= dano_real
        print(f'{self.nombre} recibió {dano_real} de daño. | Vida restante: {self.vida}')
        if self.vida <= 0:
            print(f'{self.nombre} ha sido eliminado.')

    def atacar(self, jugador):
        dano = random.randint(int(self.ataque*0.8), int(self.ataque*1.2))
        print(f'⚔️{self.nombre} ataca a {jugador.nombre} | Daño: {dano}')
        jugador.recibir_dano(dano)

    def usar_habilidad(self, jugador):
        if self.habilidad:
            print(f'{self.nombre} usa su habilidad especial: {self.habilidad}!')
            jugador.recibir_dano(self.ataque + 5)


def obtener_enemigos(maz):
    if maz == 1:
        return [
            Enemigo(nombre='Ladrón 🗡️', nivel=1, vida=25, ataque=7, defensa=3, velocidad=10,
                    experiencia=15, comportamiento='Escurridizo', habilidad='Cuchilla rápida'),
            Enemigo(nombre='Hambriento 🍗', nivel=1, vida=40, ataque=10, defensa=5, velocidad=6,
                    experiencia=20, comportamiento='Desesperado', habilidad='Golpe con Huesos')
            ]
    elif maz == 2:
        return [
            Enemigo(nombre='Duende 💰', nivel=2, vida=50, ataque=12, defensa=7, velocidad=15,
                    experiencia=40, comportamiento='Tramposo', habilidad='Lluvia de Monedas'),
            Enemigo(nombre='Ogro 💪', nivel=2, vida=70, ataque=15, defensa=10, velocidad=4,
                    experiencia=50, comportamiento='Tramposo', habilidad='Pisotón')
            ]
    elif maz == 3:
        return [Enemigo(nombre='Águila Gigante 🦅', nivel=3, vida=60, ataque=18, defensa=8, velocidad=25,
                        experiencia=70, comportamiento='Veloz', habilidad='Picoteo'),
                Enemigo(nombre='Dragón 🔥', nivel=3, vida=150, ataque=30, defensa=20, velocidad=25,
                        experiencia=200, comportamiento='Final', habilidad='Fuego')
                ]
    else:
        raise ValueError('Número de mazmorra inválido')
