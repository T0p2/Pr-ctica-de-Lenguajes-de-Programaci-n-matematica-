import math
import pandas as pd



pn_values =[]
raiz_values = []
tolerance_values = []
f_values=[]
iteraciones_values=[]
error_absoluto =[]

def punto_fijo(g, x0, tol, max_iter):
    """
    Implementación del método del punto fijo para encontrar una solución
    de la ecuación x = g(x).

    :param g: Función g(x) que define la iteración.
    :param x0: Valor inicial.
    :param tol: Tolerancia para la convergencia.
    :param max_iter: Número máximo de iteraciones permitidas.
    :return: Aproximación de la solución y número de iteraciones.
    """
    x = x0
    iteraciones = 0

    while iteraciones < max_iter:
        x_nuevo = g(x)
        if abs(x_nuevo - x) < tol:
            break

              #cargar datos para el dataframe:
        pn_values.append(x)
        raiz_values.append(x_nuevo)
        tolerance_values.append(tol)
        f_values.append(g(x_nuevo))
        iteraciones_values.append(iteraciones)
        error_absoluto.append(abs(x_nuevo - x))


        x = x_nuevo
        iteraciones += 1

  

    data = {
        "Iteracion": iteraciones_values ,
        "pn-1": pn_values,
        "Valor de raices": raiz_values,
        "tolerancia": tolerance_values,
        "Valores de f en cada raiz": f_values,
        "Error absoluto": error_absoluto
    }
    tabla_values = pd.DataFrame(data)

    print(tabla_values)
    return(x_nuevo)    
