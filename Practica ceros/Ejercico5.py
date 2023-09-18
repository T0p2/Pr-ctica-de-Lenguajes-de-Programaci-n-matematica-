''' 5. Separar las ra´ıces reales de la ecuaci´on xe−x − x
2 + 1 = 0, y obtenerlas
con ocho cifras decimales exactas por el m´etodo de Newton, aplicando
previamente la Regla de Fourier.
 '''
import math
from Metodo_Newton_Raphson import newton_raphson



def funcion(x):
    return(x*math.e**x - x*x + 1)

def funcionPrima(x):
    return(math.e**x + x*math.e**x - 2*x)


raiz_aprox = newton_raphson(funcion, funcionPrima, 0, 10**-8)

print(raiz_aprox)