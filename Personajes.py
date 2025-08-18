class Personaje:
    def __init__(self, nombre, clase):
        self.nombre = nombre
        self.clase = clase
        self.vida = 100
        self.vidamax = 100
        self.fuerza = 10
        self.velocidad = 10
        self.experiencia = 0
        self.nivel = 1
        self.inventario = []
        self.estado = 'Normal'

    def mostrar_estado(self):
        print('-- ESTADO DEL PERSONAJE --')
        print(f'Nombre: {self.nombre} - {self.clase}')
        print(f'Vida: {self.vida} / {self.vidamax}')
        print(f'Nivel: {self.nivel} | EXP {self.experiencia}')
        print(f'Fuerza: {self.fuerza} | Velocidad: {self.velocidad}')
        print(f'Inventario: {self.inventario}')

    def recibir_dano(self, cantidad:int):
        self.vida -= cantidad
        if self.vida < 0:
            self.vida = 0
        print(f'{self.nombre} recibe {cantidad} de daño. Vida restante {self.vida}')

    def curar(self, cantidad:int):
        self.vida += cantidad
        if self.vida > self.vidamax:
            self.vida = self.vidamax
        print(f'{self.nombre} recupera {cantidad} de vida. Vida actual: {self.vida}')

    def ganar_experiencia(self, cantidad:int):
        self.experiencia += cantidad
        print(f'{self.nombre} gana {cantidad} de experiencia.')
        if self.experiencia >= 100:
            self.subir_nivel()

    def subir_nivel(self):
        self.nivel += 1
        self.experiencia = 0
        self.vidamax = 100
        self.vida = self.vidamax
        self.fuerza += 5
        self.velocidad += 2
        print(f'{self.nombre} sube a nivel {self.nivel}! Agregar atributos??') 
print 
