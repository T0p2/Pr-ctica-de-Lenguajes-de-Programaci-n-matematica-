
import sympy as sp
import pandas as pd
import math


pn_values =[]
raiz_values = []
tolerance_values = []
f_values=[]


def newton_raphson(f, fprima, pn, tolerancia):

    raiz = pn
    while (f(raiz) > tolerancia or f(raiz) < (-tolerancia)):

        #cargar datos para el dataframe:
        pn_values.append(pn)
        raiz_values.append(raiz)
        tolerance_values.append(tolerancia)
        f_values.append(f(raiz))




        raiz = pn - (f(pn)/ fprima(pn))

        if (abs(raiz-pn) < tolerancia):
            print(abs(raiz-pn))
            break
            #return(raiz)
        
        pn = raiz
  
    pn_values.append(pn)
    raiz_values.append(raiz)
    tolerance_values.append(tolerancia)
    f_values.append(f(raiz))
    
    data = {
        "Iteracion": "" ,
        "pn-1": pn_values,
        "Valor de raices": raiz_values,
        "tolerancia": tolerance_values,
        "Valores de f en cada raiz": f_values
    }
    tabla_values = pd.DataFrame(data)

    print(tabla_values)


    return(raiz)



