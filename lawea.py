import math as mate

# variables
Bandera = True
Diagonales = ("///" * 6)
Separador = ("~~" * 5)
MensajeBn = "\tBienvenido\t"

# funciones
def suma(x1, x2):
    Resultado = x1 + x2
    return Resultado
def resta(x1, x2):
    Resultado = x1 - x2
    return Resultado
def multi(x1, x2):
    Resultado = x1 * x2
    return Resultado
def div(x1, x2):
    try:
        Resultado = x1 / x2
        return Resultado
    except:
        return("0")
def potencia(x1, x2):
    resultado = mate.pow(x1,x2)
    return resultado

# Presentacion del programa
print((Diagonales * 2) + "\n" + MensajeBn + "\n" + (Diagonales * 2))
print((Separador * 3) + "\n" "Este programa es una calculadora!!" + "\n" + (Separador * 3))

# seleccion de valores
N1 = int(input("introduce un numero: "))
print(Separador * 2)
N2 = int(input("introduce otro numero: "))
# seleccion de operacion
while Bandera == True:
    print(Separador + "\n" + "selecciona que accion quieres hacer:"
        "\n1) sumar"
        "\n2) restar"
        "\n3) multiplicar"
        "\n4) dividir"
        "\n5) potencia"
        "\n6) escoger otros numeros"
        "\n7) salir")
    Operacion = int(input("escoge la operacion: "))
    if Operacion == 1:
        print(Diagonales + "\nel resultado de {}+{}".format(N1,N2), suma(N1, N2), "\n" + Diagonales)
    elif Operacion == 2:
        print(Diagonales + "\nel resultado de {}-{} es:".format(N1, N2), resta(N1, N2), "\n" + Diagonales)
    elif Operacion == 3:
        print(Diagonales + "\nel resultado de {}*{} es: ".format(N1, N2), multi(N1, N2), "\n" + Diagonales)
    elif Operacion == 4:
        print(Diagonales + "\nel resultado de {}/{} es: ".format(N1, N2), div(N1, N2),  "\n" + Diagonales)
    elif Operacion == 5:
        print(Diagonales + "\nel resultado de {}^{} es: ".format(N1,N2), potencia(N1, N2), "\n" + Diagonales)
    elif Operacion == 6:
        N1 = int(input("introduce un numero: "))
        print(Separador * 2)
        N2 = int(input("introduce otro numero: "))
    elif Operacion == 7:
        print((Separador * 2) + "\n" + "\tadios\n" + (Separador * 2))
        break
    else:
        print(Diagonales + "\n" + "opcion no valida" + "\n" + Diagonales)
    Respuesta = input("quieres hacer otro calculo? s/n")
    if Respuesta == "n" or Respuesta == "N":
        Bandera = False
