''' 6. Dada la ecuaci´on e
x − (x − 2)2 = 0, probar que s´olo posee una ra´ız
real y obtenerla, por el m´etodo de Newton, con seis cifras decimales
exactas'''
import math 
from Metodo_Newton_Raphson import newton_raphson


def funcion(x):
    return(-(x*x) + 4*x + math.e**x -4)

def funcionPrima (x):
    return(-2*x + math.e + 4)

raiz_aprox = newton_raphson(funcion, funcionPrima, 0.5, 10**-6)

print(raiz_aprox)