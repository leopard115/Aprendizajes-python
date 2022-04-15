# variables
import math
a=0
b=0
bandera=True

# funciones
def sumar(x1, x2):
    a=int(input("introduce el primer número: "))
    b=int(input("introduce el segundo número: "))
    resultado=a + b
    return resultado
def resta(x1, x2):
    a=int(input("introduce el primer número: "))
    b=int(input("introduce el segundo número: "))
    resultado=a - b
    return resultado
def multi(x1, x2):
    a=int(input("introduce el primer número: "))
    b=int(input("introduce el segundo número: "))
    resultado=a * b
    return resultado
def div(x1, x2):
    a=int(input("introduce el primer número: "))
    b=int(input("introduce el segundo número: "))
    try:
        resultado=a / b
        return resultado
    except:
        return ("0")
def ptnc(x1, x2):
    a=int(input("introduce una base: "))
    b=int(input("introduce un exponente: "))
    resultado=math.pow(a, b)
    return resultado
def raiz(x1):
    a=int(input("introduce un valor para calcular su raiz cuadrada: "))
    resultado=math.sqrt(a)
    return resultado
def areacrcl(x1):
    a=int(input("introduce el valor del radio: "))
    sqrrad=math.pow(a, 2)
    pi=math.pi
    resultado=pi*sqrrad
    return resultado

# seleccion de operacion
while bandera==True:
    print("1) suma"
          "\n2) resta"
          "\n3) multiplicacion"
          "\n4) division"
          "\n5) potencia"
          "\n6) raiz cuadrada"
          "\n7) area circulo")
    slct=int(input("seleccione el número correspondiente a su operacion: "))

    if slct == 1:
        print(sumar(a, b))
    elif slct==2:
        print(resta(a, b))
    elif slct==3:
        print(multi(a, b))
    elif slct==4:
        print(div(a, b))
    elif slct==5:
        print(ptnc(a, b))
    elif slct==6:
        print(raiz(a))
    elif slct==7:
        print(areacrcl(a))


    rept=input("quieres hacer otra operacion? s/n: ")
    if rept == "n" or rept == "N" or rept == "no" or rept == "No" or rept == "nO" or rept == "NO":
        bandera = False
