
import math
from Metodo_Newton_Raphson import newton_raphson
import sympy as sp

sp.symbols('x')


def funcion (x):
    return(x**2 + math.log(x))

def funcionderivada (x):
    return(2*x + (1/x))

raiz = newton_raphson(funcion, funcionderivada, 2/3, 10**-6)


print(raiz)