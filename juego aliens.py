import random
marcianos = [["alien1", 20], ["alien2", 20], ["alien3", 20], ["alien4", 20], ["alien5", 20]]
vivos = True
while vivos == True:

    for i in range(len(marcianos)):
        numero_azar = random.randrange(4)
        if i == 0:
            if numero_azar == 0:
                marcianos[0][1] = 0
                if marcianos[0][1] == 0:
                    print(marcianos[0][0], "esta muerto")
        if i == 1:
            if numero_azar == 1:
                marcianos[1][1] /= 2
                if marcianos[1][1] <= 5:
                    marcianos[1][1] = 0
                    print(marcianos[0][0], "esta muerto")
        if i == 2:
            if numero_azar == 2:
                marcianos[0][1] /= 2
                marcianos[2][1] -= 10
                if marcianos[2][1] == 0:
                    print(marcianos[2][0], "esta muerto")
        if i == 3:
            if numero_azar == 0:
                marcianos[3][1] /= 2
                if marcianos[3][1] <= 5:
                    marcianos[3][1] = 0
                    print(marcianos[3][0], "esta muerto")
        if i == 4:
            if numero_azar == 3:
                marcianos[0][1] = 10
                marcianos[1][1] = 10
                marcianos[2][1] = 10
                marcianos[3][1] = 10
                marcianos[4][1] = 0
                if marcianos [4][1] == 0:
                    print(marcianos[4][0], "esta muerto")
        if marcianos[0][1] == 0 and marcianos[1][1] == 0 and marcianos[2][1] == 0 and marcianos[3][1] == 0 and marcianos[4][1] == 0:
            vivos = False
print("todos estan muertos!! :D")
