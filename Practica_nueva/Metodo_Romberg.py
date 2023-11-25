'''Metodo de romberg se trata de generar
una matriz trinagular cuyos elementos 
son estimaciones numericas de la integral
definida como: S [a, b] f(x) dx  (integral)'''


import math



def metodo_trapecio(funcion, a, b, n):

    i = 1
    h = (b-a)/n
    sumatoria = 0
    #encuentro el resultado de la sumatoria para ponerla en la regla
    for i in range(1, n):
        sumatoria = sumatoria + funcion(a + i * h)

    
    return h/2 * (funcion(a) + funcion(b) + 2 * sumatoria)





def romberg_integration(f, a, b, n_max):
# n_max es el número máximo de subdivisiones
    tabla_romberg = [[0] * (n_max + 1) for _ in range(n_max + 1)]
#tabla_romberg sale como una matriz de todos 0

#aca calculamos la primeras columnas usando el metodo del trapecio
    for i in range(n_max + 1):
        tabla_romberg[i][0] = metodo_trapecio(f, a, b, 2**i)

#aca calculamos las columnas restantes con la extrapolacion de Richardson
    for j in range(1, n_max + 1):
        for i in range(j, n_max + 1):
#aca aplicamos el metodo de Richardson.
            tabla_romberg[i][j] = (4**j * tabla_romberg[i][j - 1] - tabla_romberg[i - 1][j - 1]) / (4**j - 1)

    return tabla_romberg[n_max][n_max]



def funcion(x):
    return math.sin(x)


integral = romberg_integration(funcion, 0, math.pi, 3) 
print(integral)