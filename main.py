from Personajes import Personaje

# def main():
#     #crear personajes
#     heroe = Personaje("Héroe")
#     enemigo = Personaje("Enemigo")
#
#     #mmstrar estado inicial
#     print(f"\n--- COMIENZA LA BATALLA ---")
#     print(f"{heroe.nombre}: Vida {heroe.vida}, Nivel {heroe.nivel}")
#     print(f"{enemigo.nombre}: Vida {enemigo.vida}, Nivel {enemigo.nivel}\n")
#
#     #simular acciones
#     enemigo.recibir_dano(30)   #el héroe ataca
#     heroe.ganar_experiencia(50)
#
#     heroe.recibir_dano(20)     #el enemigo ataca
#     heroe.curar(15)
#
#     heroe.ganar_experiencia(60)  #experiencia acumulada --sube de nivel

# if __name__ == "__main__": git
#     main()


#Plebeyo = Personaje('Pizzerito', 'Plebeyo')
#lebeyo.mostrar_estado()
#Plebeyo.recibir_dano(30)
#Plebeyo.curar(20)
#Plebeyo.ganar_experiencia(110)
#from mazmorras import mostrar_mapa, mover_jugador

#def main():
    #mapa5x5
 #   mapa = [
   #     [".", ".", ".", ".", "."],
    #    [".", ".", ".", ".", "."],
    #    [".", ".", "X", ".", "."],
     #   [".", ".", ".", ".", "."],
      #  [".", ".", ".", ".", "."],
  #  ]

   # jugador_pos = (0, 0)

    #while True:
     #   mostrar_mapa(mapa, jugador_pos)
      #  mov = input("Mover (w/a/s/d, q para salir): ")
       # if mov == "q":
        #    print("Saliste del juego.")
         #   break
        #jugador_pos = mover_jugador(mov, jugador_pos, mapa)

#if __name__ == "__main__"
 #   main()

from Personajes import Personaje
from items import pocion_vida, espada, escudo, botas, elixir
from utilidades import mostrar_inventario, usar_item_inventario

# Crear un personaje de prueba
jugador = Personaje("Pizzerito", "Plebeyo")

# Agregar ítems al inventario
jugador.inventario.append(pocion_vida)
jugador.inventario.append(espada)
jugador.inventario.append(elixir)

# Mostrar estado inicial
jugador.mostrar_estado()

# Mostrar inventario
mostrar_inventario(jugador)

# Usar el primer ítem (la poción de vida)
print("\n--- Usando poción ---")
usar_item_inventario(jugador, 0)

# Usar el segundo ítem (la espada)
print("\n--- Usando espada ---")
usar_item_inventario(jugador, 0)

# Mostrar estado final
jugador.mostrar_estado()
