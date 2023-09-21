''' Algoritmo de Biseccion: 
    datos de entrada: [a;b], eps (error analitco) , k (cantidad de iteraciones) y la funcion f(x)
    datos de salida: xm = x* (valor real o aproximado)
'''
import math
import pandas as pd

# Definimos la función para la que queremos encontrar la raíz, por ejemplo, f(x) = x^2 - 4
def funcion_ejemplo(x):
    return math.cos(x) - x



#aca me pasa la maxima itraciones que quieren que se haga y calculo la tolerancia.
def tolerance_funtion (a, b, max_iteraciones):
    return(((b-a) / 2** max_iteraciones))


#aca me pasa el error que esta dispuesto a tolerar y calculo las iteraciones.
def Iterations_funtions(a, b, error):
    return(int(round((math.log10((b-a)/error))/math.log10(2))))


iteraciones =[]
a_values =[]
b_values =[]
m_values =[]
tolerancia_values =[]


def biseccion_con_tolerancia(funcion, a, b, tolerancia):
    max_iteraciones = Iterations_funtions(a, b, tolerancia)

    if funcion(a) * funcion(b) >= 0:
        raise ValueError("La función debe tener diferentes signos en a y b.")
    
    iteracion = 0
    max_iteraciones+=1
    while ((b - a) / 2.0) > tolerancia and iteracion < max_iteraciones:
        c = (a + b) / 2.0
        raiz = c

        iteraciones.append(iteracion)
        a_values.append(a)
        b_values.append(b)
        m_values.append(c)
        tolerancia_values.append(tolerancia)
        
        if funcion(c) == 0.0000:
            break
        elif funcion(c) * funcion(a) < 0:
            b = c
        else:
            a = c
        iteracion += 1
    
    #CREO LA VAR PARA MOSTRAR LOS DATOS COMO UNA TABLA
    table_values = pd.DataFrame({"Iteraciones": "", "valores de a": a_values, "valores de b": b_values, "valores de m": m_values, "Tolerancia": tolerancia_values})
    print(table_values)

    return raiz
    






def biseccion_con_iteraciones(funcion, a, b, max_iteraciones):
    tolerancia = tolerance_funtion(a, b, max_iteraciones)


    if funcion(a) * funcion(b) >= 0:
        raise ValueError("La función debe tener diferentes signos en a y b.")
    
    iteracion = 0

    while ((b - a ) / 2.0) > tolerancia or iteracion < max_iteraciones  :
            
        c = (a + b) / 2.0
        raiz = c

        iteraciones.append(iteracion)
        a_values.append(a)
        b_values.append(b)
        m_values.append(c)
        tolerancia_values.append(tolerancia)
        
        if funcion(c) == 0.0000:
            break
        elif funcion(c) * funcion(a) < 0:
            b = c
        else:
            a = c
        iteracion = iteracion + 1

    #CREO LA VAR PARA MOSTRAR LOS DATOS COMO UNA TABLA
    table_values = pd.DataFrame({"Iteraciones": "", "valores de a": a_values, "valores de b": b_values, "valores de m": m_values, "Tolerancia": tolerancia_values})
    print(table_values)

    return raiz
    

