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


    while(f(raiz) > precision):

        pn_values.append(p0)
        pn1_values.append(p1)
        precision_values.append(precision)
        raiz_values.append(raiz)
        f_values.append(f(raiz))


        raiz = p1 - ((f(p1)* (p1-p0))/ (f(p1)-f(p0)))
        p0 = p1
        p1 = raiz

        pn_values.append(p0)
        pn1_values.append(p1)
        precision_values.append(precision)
        raiz_values.append(raiz)
        f_values.append(f(raiz))

        return(raiz)



print(secante(funcion, 1.2, 1, 10**-4))
data = {
        "Iteracion": "" ,
        "p_n": pn_values,
        "p_n+1": pn1_values,
        "Valor de raices": raiz_values,
        "tolerancia": precision_values,
        "valores de f": f_values
    }
tabla_values = pd.DataFrame(data)

print(tabla_values)

        

