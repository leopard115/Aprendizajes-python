mstr=200
dano=25
vida=15
while mstr > 0:
    # seleccion = 0

    print("acciones realizables:"
          "\n 1) atacar"
          "\n 2) curar")
    seleccion = int(input("que accion quieres llevar a cabo? "))
    if mstr < 0:
        mstr=0
    if seleccion==1:
        mstr-= dano
        print("hiciste {} de daño y el enemigo tiene {} de vida".format(dano, mstr))
    elif seleccion==2:
        mstr+=vida
        print("curaste al enemigo con {} puntos de vida y ahora tiene {} de salud".format(vida, mstr))
