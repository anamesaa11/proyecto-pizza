from models.personajes import Personaje
from config.game_data import PERSONAJES_BASE
from config.game_settings import (
    EXP_PARA_SUBIR_NIVEL, BONUS_VIDA_NIVEL, BONUS_FUERZA_NIVEL,
    BONUS_DEFENSA_NIVEL, BONUS_VELOCIDAD_NIVEL)


class Jugador(Personaje):
    def __init__(self, nombre, tipo, vida, fuerza, defensa, velocidad):
        super().__init__(nombre=nombre,
                         vida=vida,
                         fuerza=fuerza,
                         defensa=defensa,
                         velocidad=velocidad,
                         experiencia=0,
                         nivel=1)
        self.tipo = tipo
        self.inventario = []
        self.estado = 'Normal'
        #self.defendiendo = False

    def mostrar_estado(self):
        super().mostrar_estado()
        print(f'Tipo: {self.tipo}')
        print(f'Inventario: {len(self.inventario)} ítems | Estado: {self.estado}')

    def subir_nivel(self):
        self.nivel += 1
        self.experiencia = 0
        self.vidamax += BONUS_VIDA_NIVEL
        self.vida = self.vidamax
        self.fuerza += BONUS_FUERZA_NIVEL
        self.defensa += BONUS_DEFENSA_NIVEL
        self.velocidad += BONUS_VELOCIDAD_NIVEL

        print(f'{self.nombre} sube a nivel {self.nivel}!')

    def ganar_experiencia(self, cantidad):
        self.experiencia += cantidad
        print(f'✨ {self.nombre} gana {cantidad} de experiencia.')
        if self.experiencia >= EXP_PARA_SUBIR_NIVEL:
            self.subir_nivel()
            

def crear_personaje_mazmorra(maz):
    if maz not in PERSONAJES_BASE:
        raise ValueError(f'Número de mazmorra inválido: {maz}')
    datos = PERSONAJES_BASE[maz]
    return Jugador(
        nombre=datos["nombre"],
        tipo=datos["tipo"],
        vida=datos["vida"],
        fuerza=datos["fuerza"],
        defensa=datos["defensa"],
        velocidad=datos["velocidad"]
    )
