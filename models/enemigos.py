#Enemigos del juego

import random
from models.personajes import Personaje
from config.game_data import ENEMIGOS_DATA


class Enemigo(Personaje):
    def __init__(self, nombre, nivel, vida, fuerza, defensa, velocidad, experiencia, comportamiento, habilidad):
        super().__init__(nombre=nombre,
                         vida=vida,
                         fuerza=fuerza,
                         defensa=defensa,
                         velocidad=velocidad,
                         experiencia=experiencia,
                         nivel=nivel,
                         habilidad=habilidad)
        self.comportamiento = comportamiento

    #Ataque con variación de daño
    def atacar(self, jugador):
        dano_base = self.fuerza
        dano_final = random.randint(int(dano_base*0.8), int(dano_base*1.2))
        print(f'⚔️ {self.nombre} ataca a {jugador.nombre} | Daño: {dano_final}')
        jugador.recibir_dano(dano_final)

    def usar_habilidad(self, jugador):
        if self.habilidad:
            print(f'⚔️ {self.nombre} usa su habilidad especial: {self.habilidad}!')
            dano_habilidad = self.fuerza + 5
            jugador.recibir_dano(dano_habilidad)


def obtener_enemigos(maz):
    if maz not in ENEMIGOS_DATA:
        raise ValueError(f'Número de mazmorra inválido: {maz}')

    enemigos = []

    for datos in ENEMIGOS_DATA[maz]:
        enemigo = Enemigo(
                nombre=datos["nombre"],
                nivel=datos["nivel"],
                vida=datos["vida"],
                fuerza=datos["fuerza"],
                defensa=datos["defensa"],
                velocidad=datos["velocidad"],
                experiencia=datos["experiencia"],
                comportamiento=datos["comportamiento"],
                habilidad=datos["habilidad"]
        )
        enemigos.append(enemigo)

    return enemigos
