# variables
Diagonales = ("///" * 6)
Separador = ("~~" * 5)
MensajeBn = "\tBienvenido\t"

# Presentacion del programa
print(Diagonales + "\n" + MensajeBn + "\n" + Diagonales)
print((Separador * 3) + "\n" "Este programa es una calculadora!!" + "\n" + (Separador * 3))

# seleccion de valores
N1 = int(input("introduce un numero: "))
print(Separador * 2)
N2 = int(input("introduce otro numero: "))
# seleccion de operacion
print(Separador + "\n" + "selecciona el tipo de operacion que quieres hacer"
      "\n1) sumar"
      "\n2) restar"
      "\n3) multiplicar"
      "\n4) dividir" + "\n" + Separador)
Operacion = int(input("escoge la operacion: "))
if Operacion == 1:
    print(Diagonales + "\nel resultado de", N1, "+", N2, "es: ", (N1 + N2), "\n" + Diagonales)
elif Operacion == 2:
    print(Diagonales + "\nel resultado de", N1, "-", N2, "es: ", (N1 - N2), "\n" + Diagonales)
elif Operacion == 3:
    print(Diagonales + "\nel resultado de", N1, "*", N2, "es: ", (N1 * N2), "\n" + Diagonales)
elif Operacion == 4:
    try:
        print(Diagonales + "\nel resultado de", N1, "/", N2, "es: ", (N1 / N2),  "\n" + Diagonales)
    except:
        print ("estas dividiendo entre 0")
else:
    print(Diagonales + "\n" + "\t adios" + "\n" + Diagonales)
