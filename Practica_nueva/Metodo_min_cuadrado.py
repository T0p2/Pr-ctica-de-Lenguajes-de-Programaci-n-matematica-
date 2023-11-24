'''
m = n* sum(x*y) - sum(x)-sum(y)  /   n*sum(x**2) - sum(x) **2

b = sum(y) - m*sum(x)   / n

n : representa el valor de la cantidad de datos que nos dan

m : pendiente de nuestra ecuacion lineal

b : valor de origen de coordenadas



'''





import pandas as pd
import numpy as np
import sympy 

x = sympy.Symbol('x')

# datos: lista de valores (x, y)
def min_cuadrado(lista_x, lista_y):

    if len(lista_x) != len(lista_y):
        print("Las longitudes de la listas no son iguales")
    else:
        n = len(lista_x)
    #convierto a tipo Numpy las listas dadas por parametro, ya que es mas
    #facil de laburar
        values_x = np.array(lista_x)
        values_y = np.array(lista_y)


    #calculo las sumatorias
        sum_x = np.sum(values_x)
        sum_y = np.sum(values_y)
        sum_xy = np.sum(values_x*values_y)
        sum_x_x = np.sum(values_x*values_x)


    #utilizo las formulas para obtener 'm' y 'b'
    #m = n* sum(x*y) - sum(x)-sum(y)  /   n*sum(x**2) - sum(x) **2
        
        m = ((n * sum_xy) - (sum_x * sum_y)) / ((n * sum_x_x) - (sum_x**2))
    
    #b = sum(y) - m*sum(x)   / n

        b = (sum_y - m * sum_x) / n


        return(m * x) + b



lista_x = [1, 2, 3, 4]
lista_y = [1.4, 1.1, 0.7, 0.1]


ecuacion = min_cuadrado (lista_x, lista_y)
print(ecuacion)
