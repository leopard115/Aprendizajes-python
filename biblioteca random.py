import random
# variables
dano = 0
danoenem = 0
enemigo = 500
jugador = 150
# batalla
while True:
    dano = (random.randrange(50))
    danoenem = (random.randrange(15))
    if enemigo > 0:
        print("hiciste ", dano, "puntos de daño")
        enemigo -= dano
        print("el enemigo tiene: ", enemigo, "puntos de vida")
    # si el enemigo tiene 0 o menos, su valor de vida se cambiara a 0.
    # mostrara un texto con su vida y diciendo que ganaste. fin del programa

    if enemigo <= 0:
        enemigo = 0
        print("El enemigo esta muerto" + "\n" + "ganaste!!")
        break
        # si el enemigo tiene mas de 0, enemigo recibira daño.
        # se mostrara un texto diciendo la vida de enemigo
    # si el jugador tiene mas de 0, se mostrara un texto diciendo el daño que recibiste.
    # se cambia el valor de la vida del jugador y se mostrara la vida del jugador
    if jugador > 0:
        print("recibiste", danoenem, "puntos de daño")
        jugador -= danoenem
        print("tienes: ", jugador, "puntos de vida")
    # si el jugador tiene 0 o menos, se cambiara el valor del jugador a 0.
    # se mostrara un texto diciendo la vida del jugador y que perdiste. fin del programa
    elif jugador <= 0:
        jugador = 0
        print("el enemigo te mato" + "\n" + "perdiste!!")
        break
