from personajes import Personaje

class Jugador(Personaje):
    def __init__(self, nombre, tipo, vida, fuerza, defensa, velocidad):
        super().__init__(nombre, tipo, vida, fuerza, defensa, velocidad, experiencia=0, nivel=1)
        self.tipo = tipo
        self.inventario = []
        self.estado = 'Normal'


    def mostrar_estado(self):
        super().mostrar_estado()
        print(f'Clase: {self.tipo}')
        print(f'Inventario: {len(self.inventario)} ítems | Estado: {self.estado}')


    def subir_nivel(self):
        self.nivel += 1
        self.experiencia = 0
        self.vidamax += 50
        self.vida = self.vidamax
        self.fuerza += 5
        self.defensa += 2
        self.velocidad += 2
        print(f'{self.nombre} sube a nivel {self.nivel}!')


    def ganar_experiencia(self, cantidad:int):
        self.experiencia += cantidad
        print(f'{self.nombre} gana {cantidad} de experiencia.')
        if self.experiencia >= 100:
            self.subir_nivel()


def crear_personaje_mazmorra(maz):
    if maz == 1:
        return Jugador('Greg', 'Plebeyo 👞', vida=80, fuerza=8, defensa=10, velocidad=10)
    elif maz == 2:
        return Jugador('Bruto', 'Bárbaro 🪓', vida=120, fuerza=20, defensa=6, velocidad=5)
    elif maz == 3:
        return Jugador('Nox', 'Hechicero 🔮', vida=150, fuerza=10, defensa=20, velocidad=15)
    else:
        raise ValueError('Número de mazmorra inválido')

