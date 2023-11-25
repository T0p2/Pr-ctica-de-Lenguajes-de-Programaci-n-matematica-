import math



def metodo_trapecio(funcion, a, b, n):

    i = 1
    h = (b-a)/n
    sumatoria = 0
    #encuentro el resultado de la sumatoria para ponerla en la regla
    for i in range(1, n):
        sumatoria = sumatoria + funcion(a + i * h)

    
    return h/2 * (funcion(a) + funcion(b) + 2 * sumatoria)



def funcion (x):
    return math.sin(x)

integral = metodo_trapecio(funcion, 0, math.pi, 4)
print(integral)
