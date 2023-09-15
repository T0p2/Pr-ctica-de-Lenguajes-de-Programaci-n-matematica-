
import sympy as sp
import pandas as pd
import math


pn_values =[]
raiz_values = []
tolerance_values = []

def newton_raphson(f, fprima, pn, tolerancia):

    raiz = pn
    while (f(raiz) > tolerancia):

        #cargar datos para el dataframe:
        pn_values.append(pn)
        raiz_values.append(raiz)
        tolerance_values.append(tolerancia)

        raiz = pn - (f(pn)/ fprima(pn))

        if (abs(raiz-pn) < tolerancia):
            return(raiz)
        
        pn = raiz
  
    pn_values.append(pn)
    raiz_values.append(raiz)
    tolerance_values.append(tolerancia)
    tabla_values = pd.DataFrame({"Iteracion": " ", "pn-1": pn_values, "Valor de raices": raiz_values, "tolerancia": tolerance_values })
    print(tabla_values)


    return(raiz)



