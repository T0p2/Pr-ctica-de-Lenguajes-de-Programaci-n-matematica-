import math
from Metodo_Secante import secante


def funcion(x):
    return(x - (0.5 * math.tan(x)))

raiz = secante(funcion, 1, 1.2, 10**-4)
print(raiz)