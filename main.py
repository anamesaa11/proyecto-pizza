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


Plebeyo = Personaje('Pizzerito', 'Plebeyo')
Plebeyo.mostrar_estado()
Plebeyo.recibir_dano(30)
Plebeyo.curar(20)
Plebeyo.ganar_experiencia(110)