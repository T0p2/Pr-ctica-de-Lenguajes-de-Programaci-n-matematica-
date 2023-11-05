import math

def metodo_simpson(funcion, a, b, n):
    i = 0
    h = (b-a)/n
    sumatoria_4, sumatoria_2 = 0, 0



    for i in range(1, int(n / 2) + 1):
        sumatoria_4 += funcion(a + (2 * i - 1) * h)

    for i in range(1, int(n / 2)):
        sumatoria_2 += funcion(a + 2 * i * h)

    
    return h/3 * (funcion(a) + funcion(b) + 4 * sumatoria_4 + 2* sumatoria_2)




def funcion(x):
    return math.sin(x)

print(metodo_simpson(funcion, 0, math.pi, 4))