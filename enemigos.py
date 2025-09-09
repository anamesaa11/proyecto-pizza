import random
#from Personajes import Personaje


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
        print(f'{self.nombre} ataca a (Personaje) | Daño: {dano}')
        jugador.recibir_dano()

    def usar_habilidad(self, jugador):
        if self.habilidad:
            print(f'{self.nombre} usa su habilidad especial: {self.habilidad}!')
            jugador.recibir_dano(self.ataque + 5)