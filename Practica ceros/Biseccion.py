''' Algoritmo de Biseccion: 
    datos de entrada: [a;b], eps (error analitco) , k (cantidad de iteraciones) y la funcion f(x)
    datos de salida: xm = x* (valor real o aproximado)
'''
import math

# Definimos la función para la que queremos encontrar la raíz, por ejemplo, f(x) = x^2 - 4
def funcion_ejemplo(x):
    return math.cos(x) - x




def tolerance_funtion (a, b, max_iteraciones):
    return((b-a) / 2** max_iteraciones)





def biseccion(funcion, a, b, max_iteraciones):
    tolerancia = tolerance_funtion(a, b, max_iteraciones)

    if funcion(a) * funcion(b) >= 0:
        raise ValueError("La función debe tener diferentes signos en a y b.")
    
    iteracion = 0
    max_iteraciones+=1
    while ((b - a) / 2.0) > tolerancia and iteracion < max_iteraciones:
        c = (a + b) / 2.0
        raiz = c

        print(f"i = {iteracion}:  a = {a}: m = {(a+b)/2.0}: b = {b}: f(c) = {funcion(c)}")
        if funcion(c) == 0.0000:
            break
        elif funcion(c) * funcion(a) < 0:
            b = c
        else:
            a = c
        iteracion += 1
    
    
    return raiz





