#Utilidades para manejar el inventario


def mostrar_inventario(personaje):
    """mestra el inventario del personaje."""
    if not personaje.inventario:
        print(f"{personaje.nombre} no tiene ítems.")
        return

    print(f"Inventario de {personaje.nombre}:")
    print("-" * 40)
    for i, item in enumerate(personaje.inventario, 1):
        print(f"{i}. {item.nombre} ({item.tipo})")
        print(f"    Efecto: {item.efecto} +{item.valor}")
    print("-" * 40)


def usar_item_inventario(personaje, indice):
    """usa y elimina un ítem del inventario por índice."""
    if 0 <= indice < len(personaje.inventario):
        item = personaje.inventario.pop(indice)
        item.usar(personaje)
    else:
        print("Índice inválido.")


def contar_items_tipo(personaje, tipo):
    contador = 0
    for item in personaje.inventario:
        if item.tipo == tipo:
            contador += 1
    return contador
