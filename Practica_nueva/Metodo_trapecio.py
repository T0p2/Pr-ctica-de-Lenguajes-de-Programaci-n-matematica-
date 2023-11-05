import math
import pandas as pd

sumatoria_value =[]
n_value =[]
i_value=[]
h_value = []




def metodo_trapecio(funcion, a, b, n):

    i = 1
    h = (b-a)/n
    sumatoria = 0
    #encuentro el resultado de la sumatoria para ponerla en la regla
    for i in range(1, n):
        sumatoria = sumatoria + funcion(a + i * h)
        
        sumatoria_value.append(sumatoria)
        n_value.append(n)
        i_value.append(i)
        h_value.append(h)
    
    
    data ={
        "Iteracion" : i_value,
        "Sumatoria": sumatoria_value,
        "n" : n_value,
        "h": h_value
    }

    tabla = pd.DataFrame(data)
    print(tabla)


    
    return h/2 * (funcion(a) + funcion(b) + 2 * sumatoria)



def funcion (x):
    return math.sin(x)


print(metodo_trapecio(funcion, 0, math.pi, 3))