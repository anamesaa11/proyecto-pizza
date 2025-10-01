class Item:
    def __init__(self, nombre, tipo, efecto, valor):
        self.nombre = nombre
        self.tipo = tipo
        self.efecto = efecto
        self.valor = valor

    def usar(self, personaje):
        if self.efecto == "vida":
            personaje.curar(self.valor)
        elif self.efecto == "fuerza":
            personaje.fuerza += self.valor
            print(f"{personaje.nombre} gana +{self.valor} fuerza.")
        elif self.efecto == "defensa":
            personaje.defensa += self.valor
            print(f"{personaje.nombre} gana +{self.valor} defensa.")
        elif self.efecto == "velocidad":
            personaje.velocidad += self.valor
            print(f"{personaje.nombre} gana +{self.valor} velocidad.")
        else:
            print("Este ítem no tiene efecto.")

    def __str__(self):
        return f"{self.nombre} ({self.tipo}, {self.efecto} +{self.valor})"



pocion_vida = Item("Poción de Vida", "consumible", "vida", 30)
espada = Item("Espátula de Hierro", "equipable", "fuerza", 5)
escudo = Item("Caja de Cartón", "equipable", "defensa", 3)
botas = Item("Zapatillas de Reparto", "equipable", "velocidad", 2)
elixir = Item("Elixir de Queso Fundido", "consumible", "vida", 50)

lista_items = [pocion_vida, espada, escudo, botas, elixir]
