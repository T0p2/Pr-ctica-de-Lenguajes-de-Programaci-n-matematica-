from Biseccion import biseccion
import math

def funcion(x):
    return (x*(math.e)**x)-1

raiz_aprox = biseccion(funcion, 0, 1, 7)
print(f"la raiz aproximada es {raiz_aprox}")
