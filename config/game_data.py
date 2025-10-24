#Datos del Juego

#Escenarios de las Mazmorras
ESCENARIOS_DATA = {
    1: {"nombre": "Mazmorra 1 – Pueblo 🏘️",
        "descripcion": "Callejones llenos de ladrones y clientes exigentes.",
        "suelo": "🛣️",
        "relleno": "🌿"},
    2: {"nombre": "Mazmorra 2 – Bosque encantado 🌲",
        "descripcion": "Donde los árboles cobran vida y te roban la pizza.",
        "suelo": "🌳",
        "relleno": "🍄"},
    3: {"nombre": "Mazmorra 3 – Cielos de Pepperoni ☁️",
        "descripcion": "Nubes de queso flotante y tormentas de orégano.",
        "suelo": "🪶",
        "relleno": "☁️"},
    4: {"nombre": "Mazmorra 4 – Castillo del Dragón 🏰🔥",
        "descripcion": "El último desafío antes de entregar la Gran Pizza Suprema.",
        "suelo": "🏰",
        "relleno": "🔥"}
}

PERSONAJES_BASE = {
    1: {
        "nombre": "Greg",
        "tipo": "Plebeyo 👞",
        "vida": 80,
        "fuerza": 8,
        "defensa": 10,
        "velocidad": 10
    },
    2: {
        "nombre": "Bruto",
        "tipo": "Bárbaro",
        "vida": 120,
        "fuerza": 20,
        "defensa": 6,
        "velocidad": 5
    },
    3: {
        "nombre": "Nox",
        "tipo": "Hechicero",
        "vida": 150,
        "fuerza": 10,
        "defensa": 20,
        "velocidad": 15
    }
}

ENEMIGOS_DATA = {
    1: [
        {
            "nombre": "Ladrón 🗡️",
            "nivel": 1,
            "vida": 25,
            "fuerza": 7,
            "defensa": 3,
            "velocidad": 10,
            "experiencia": 15,
            "comportamiento": "Escurridizo",
            "habilidad": "Cuchilla Rápida"
        },
        {
            "nombre": "Hambriento 🍗",
            "nivel": 1,
            "vida": 40,
            "fuerza": 10,
            "defensa": 5,
            "velocidad": 6,
            "experiencia": 20,
            "comportamiento": "Desesperado",
            "habilidad": "Golpe con Huesos"
        }
    ],
    2: [
        {
            "nombre": "Duende 💰",
            "nivel": 2,
            "vida": 50,
            "fuerza": 12,
            "defensa": 7,
            "velocidad": 15,
            "experiencia": 40,
            "comportamiento": "Tramposo",
            "habilidad": "Lluvia de Monedas"
        },
        {
            "nombre": "Ogro 💪",
            "nivel": 2,
            "vida": 70,
            "fuerza": 15,
            "defensa": 10,
            "velocidad": 4,
            "experiencia": 50,
            "comportamiento": "Bruto",
            "habilidad": "Pisotón"
        }
    ],
    3: [
        {
            "nombre": "Águila Gigante 🦅",
            "nivel": 3,
            "vida": 60,
            "fuerza": 18,
            "defensa": 8,
            "velocidad": 25,
            "experiencia": 70,
            "comportamiento": "Veloz",
            "habilidad": "Picoteo"
        },
        {
            "nombre": "Dragón 🔥",
            "nivel": 3,
            "vida": 150,
            "fuerza": 30,
            "defensa": 20,
            "velocidad": 25,
            "experiencia": 200,
            "comportamiento": "Jefe Final",
            "habilidad": "Aliento de Fuego"
        }
    ]
}

ITEMS_DATA = [
    {
        "nombre": "Poción de Vida",
        "tipo": "consumible",
        "efecto": "vida",
        "valor": 30
    },
    {
        "nombre": "Espátula de Hierro",
        "tipo": "equipable",
        "efecto": "fuerza",
        "valor": 10
    },
    {
        "nombre": "Caja de Cartón",
        "tipo": "equipable",
        "efecto": "defensa",
        "valor": 3
    },
    {
        "nombre": "Zapatillas de Reparto",
        "tipo": "equipable",
        "efecto": "velocidad",
        "valor": 5
    },
    {
        "nombre": "Elixir de Queso Fundido",
        "tipo": "consumible",
        "efecto": "vida",
        "valor": 50

    }
]
