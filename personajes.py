class Personaje:
    def __init__ (self, nombre, vida, fuerza, defensa, velocidad, experiencia=0, nivel=1, habilidad=None):
        self.nombre = nombre
        self.vida = vida
        self.vidamax = vida
        self.fuerza = fuerza
        self.defensa = defensa
        self.velocidad = velocidad
        self.experiencia = experiencia
        self.nivel = nivel              # 0 y 1 para Jugadores, valor fijo para Enemigos (propio de su clase)
        self.habilidad = habilidad
        self.defendiendo = False

    def con_vida(self):
        return self.vida > 0
    
    def recibir_dano(self, cantidad:int):
        dano_recibido = max(0, cantidad - self.defensa)
        self.vida -= dano_recibido
        if self.vida < 0:
            self.vida = 0
        print(f'{self.nombre} recibe {dano_recibido} de daño. Vida restante {self.vida}')
        
        if self.vida == 0:
            print(f'{self.nombre} ha sido eliminado.')

    def atacar(self, objetivo):
        dano_base = self.fuerza
        print(f"{self.nombre} ataca a {objetivo.nombre}. Causa {dano_base} de daño (antes de defensa).")
        objetivo.recibir_dano(dano_base)

    def mostrar_estado(self):
        print('-- ESTADO DEL PERSONAJE --')
        print(f'Nombre: {self.nombre} - {self.tipo}')
        print(f'Vida: {self.vida} / {self.vidamax}')
        print(f'Nivel: {self.nivel} | EXP {self.experiencia}')
        print(f'Fuerza: {self.fuerza} | Defensa: {self.defensa} | Velocidad: {self.velocidad}')
        print(f'Inventario: {len(self.inventario)} ítems')

    def curar(self, cantidad:int):
        self.vida += cantidad
        if self.vida > self.vidamax:
            self.vida = self.vidamax
        print(f'{self.nombre} recupera {cantidad} de vida. Vida actual: {self.vida}')
