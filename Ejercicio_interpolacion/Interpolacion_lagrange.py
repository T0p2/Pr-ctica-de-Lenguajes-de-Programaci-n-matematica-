'''
Interpolacion de Lagranje: sirve para encontrar un polinomio que pase a traves de puntos dados, y en estos casos vamos a retornar un punto evaluado en ese polinomio.
Entrada: los puntos (x0, y0)...(xn, yn), a (punto a evaluar)
Salida: P(a) (polinomio evaluado)
Hacemos 2 bucles porque pasamos una lista de puntos, osea el bucle de i va a ser para correr cada punto, 
y el bucle de j para analizar cada punto adentro de la pos i de la lista.
'''
import sympy as sp

def interpolacion_lagrange(puntos, a):
    #n es la longitud de los puntos que vienen en una lista.
    n = len(puntos)
    resultado = 0.0

    for i in range(n):
        #tomo las coordenadas de la lista
        xi, yi = puntos[i]
        #termino representa el valor y en el punto x
        termino = yi

        for j in range(n):
            #aseguramos que no estemos multiplicando el termino por si mismo.
            if i != j:
                #para cada j se extrae la x
                xj, _ = puntos[j]
                #fromula de Lagranje, termino es igual a la multiplicacion de cada polinomio de cada punto de x
                termino *= (a - xj) / (xi - xj)

        resultado += termino

    return resultado



def interpolacion_lagrange_polinomio(puntos):

    # n es la longitud de los puntos que vienen en una lista.
    n = len(puntos)
    x = sp.symbols('x')
    polinomio = 0

    for i in range(n):
        # Tomo las coordenadas de la lista
        xi, yi = puntos[i]
        termino = yi

        for j in range(n):
            # Aseguramos que no estemos multiplicando el término por sí mismo.
            if i != j:
                # Para cada j se extrae la x
                xj, _ = puntos[j]
                # Formula de Lagrange, término es igual a la multiplicación de cada polinomio de cada punto de x
                termino *= (x - xj) / (xi - xj)

        polinomio += termino

    return polinomio