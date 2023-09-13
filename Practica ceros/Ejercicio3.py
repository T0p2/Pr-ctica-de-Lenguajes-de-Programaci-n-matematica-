'''Aplicar el M´etodo de bisecci´on a F(x) = x
3−17 = 0, a fin de determinar
la ra´ız c´ubica de 17 con un error menor que 0.125.'''

from Biseccion import biseccion, Iterations_funtions


def funcion(x):
    return(x**3 -17)

raiz_aprox = biseccion(funcion, 1, 3, Iterations_funtions(1, 3, 10**-4) )
#segun calculadora
raiz_real = 2.571281591

error = (raiz_real-raiz_aprox)/raiz_real


print(f"la raiz aproximada es {raiz_aprox} la raiz real es {raiz_real}, y el error relativo de este metodo es: {error}")
