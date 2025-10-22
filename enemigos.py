import random
from personajes import Personaje

class Enemigo(Personaje):
    def __init__(self, nombre, nivel, vida, fuerza, defensa, velocidad, experiencia, comportamiento, habilidad):
        super().__init__(nombre=nombre, vida=vida, fuerza=fuerza, defensa=defensa, velocidad=velocidad, experiencia=experiencia, nivel=nivel, habilidad=habilidad)
        self.comportamiento = comportamiento


    #Sobreescribir atacar
    def atacar(self, jugador):
        dano_base = self.fuerza
        dano_final = random.randint(int(dano_base*0.8), int(dano_base*1.2))
        print(f'⚔️{self.nombre} ataca a {jugador.nombre} | Daño: {dano_final}')
        jugador.recibir_dano(dano_final)

    def usar_habilidad(self, jugador):
        if self.habilidad:
            print(f'{self.nombre} usa su habilidad especial: {self.habilidad}!')
            dano_habilidad = self.fuerza + 5
            jugador.recibir_dano(dano_habilidad)


def obtener_enemigos(maz):
    if maz == 1:
        return [
            Enemigo(nombre='Ladrón 🗡️', nivel=1, vida=25, fuerza=7, defensa=3, velocidad=10,
                    experiencia=15, comportamiento='Escurridizo', habilidad='Cuchilla rápida'),
            Enemigo(nombre='Hambriento 🍗', nivel=1, vida=40, fuerza=10, defensa=5, velocidad=6,
                    experiencia=20, comportamiento='Desesperado', habilidad='Golpe con Huesos')
            ]
    elif maz == 2:
        return [
            Enemigo(nombre='Duende 💰', nivel=2, vida=50, fuerza=12, defensa=7, velocidad=15,
                    experiencia=40, comportamiento='Tramposo', habilidad='Lluvia de Monedas'),
            Enemigo(nombre='Ogro 💪', nivel=2, vida=70, fuerza=15, defensa=10, velocidad=4,
                    experiencia=50, comportamiento='Tramposo', habilidad='Pisotón')
            ]
    elif maz == 3:
        return [Enemigo(nombre='Águila Gigante 🦅', nivel=3, vida=60, fuerza=18, defensa=8, velocidad=25,
                        experiencia=70, comportamiento='Veloz', habilidad='Picoteo'),
                Enemigo(nombre='Dragón 🔥', nivel=3, vida=150, fuerza=30, defensa=20, velocidad=25,
                        experiencia=200, comportamiento='Final', habilidad='Fuego')
                ]
    else:
        raise ValueError('Número de mazmorra inválido')
