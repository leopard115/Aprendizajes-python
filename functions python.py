# funciones
def suma(x1,x2):
    Resultado = x1 + x2
    return Resultado
def resta(x1,x2):
    Resultado = x1 - x2
    return Resultado
def multi(x1,x2):
    Resultado = x1 * x2
    return Resultado
def div(x1,x2):
    try:
        Resultado = x1 / x2
        return Resultado
    except:
        return ("no se puede dividir entre 0 babosa!!")


a = int(input("introduce el primer numero"))
b = int(input("introduce el segundo numero"))
print("el resultado es ", div(a,b))
