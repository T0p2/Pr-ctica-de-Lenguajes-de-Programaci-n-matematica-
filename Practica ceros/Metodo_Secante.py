import pandas as pd
import math


pn_values=[]
pn1_values=[]
precision_values=[]
raiz_values=[]
f_values = []



def funcion(x):
    return(x - 0.5* math.tan(x))




def secante(f, p0, p1, precision):

    raiz = p1
    print(precision)
    print(  f(raiz))

    while(abs(f(raiz)) > precision):


        raiz = p1 - (f(p1)* (p1-p0)) / (f(p1)-f(p0))

        if (abs(f(raiz)) < precision):
            break

        p0 = p1
        p1 = raiz



        pn_values.append(p0)
        pn1_values.append(p1)
        precision_values.append(precision)
        raiz_values.append(raiz)
        f_values.append(f(raiz))

    pn_values.append(p0)
    pn1_values.append(p1)
    precision_values.append(precision)
    raiz_values.append(raiz)
    f_values.append(f(raiz))

    data = {
            "Iteracion:": "",
            "p0" : pn_values,
            "p1" : pn1_values,
            "Valor de raiz:": raiz_values,
            "Valores de funcion": f_values,
            "Tolerancia:": precision_values

    }

    tabla_values = pd.DataFrame(data)

    print(tabla_values)

    return(raiz)




        

