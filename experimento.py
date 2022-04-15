import math

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
    resultado = math.pow(x1,x2)
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
        "\n6) raiz cuadrada (se maneja un valor totalmente aparte de los seleccionados anteriormente)"
        "\n7) escoger otros numeros"
        "\n8) salir")
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
        sqr = int(input("introduce un valor para sacar su raiz cuadrada: "))
        raiz = mate.sqrt(sqr)
        print(Diagonales + "\nel resultado de la raiz cuadrada de {} es: ".format(sqr), raiz, "\n" + Diagonales)
    elif Operacion == 7:
        N1 = int(input("introduce un numero: "))
        print(Separador * 2)
        N2 = int(input("introduce otro numero: "))
    elif Operacion == 8:
        print((Separador * 2) + "\n" + "\tadios\n" + (Separador * 2))
        break
    else:
        print(Diagonales + "\n" + "opcion no valida" + "\n" + Diagonales)
    Respuesta = input("quieres hacer otro calculo? s/n")
    if Respuesta == "n" or Respuesta == "N" or Respuesta == "No" or Respuesta == "no" or Respuesta == "NO" or Respuesta == "nO":
        Bandera = False
