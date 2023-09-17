
from Metodo_Punto_Fijo import punto_fijo
import math

def f(x):
    return(x**3+4*x**2-10)

def g(x):
    return(math.sqrt(10/x+ 4))




raiz = punto_fijo (g, 1.5, 10**-4, 100)
print(raiz)