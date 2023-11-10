'''Metodo de romberg se trata de generar
una matriz trinagular cuyos elementos 
son estimaciones numericas de la integral
definida como: S [a, b] f(x) dx  (integral)'''


from Metodo_trapecio import metodo_trapecio
import math

def romberg_integration(f, a, b, n_max):
    # Implementa el método de Romberg para integrar la función f desde a hasta b
    # n_max es el número máximo de subdivisiones
    tabla_romberg = [[0] * (n_max + 1) for _ in range(n_max + 1)]

    for i in range(n_max + 1):
        tabla_romberg[i][0] = metodo_trapecio(f, a, b, 2**i)

    for j in range(1, n_max + 1):
        for i in range(j, n_max + 1):
            tabla_romberg[i][j] = (4**j * tabla_romberg[i][j - 1] - tabla_romberg[i - 1][j - 1]) / (4**j - 1)

    return tabla_romberg[n_max][n_max]



def funcion(x):
    return math.sin(x)


integral = romberg_integration(funcion, 0, math.pi, 3) 
print(integral)