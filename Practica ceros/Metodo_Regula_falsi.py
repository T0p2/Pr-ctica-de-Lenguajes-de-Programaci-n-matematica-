import pandas as pd



a_values=[]
b_values=[]
c_values=[]
f_c_values=[]
tolerancia_values=[]


def regula_falsi(funcion, a, b, tolerancia):
    if funcion(a)* funcion(b) > 0: 
        print("Error en los valores de a y b")

    c = a - ((funcion(a)*(b-a))/(funcion(b)-funcion(a)))
   
    
    while abs(funcion(c)) > tolerancia: 
        c = a - ((funcion(a)*(b-a))/(funcion(b)-funcion(a)))

        if abs(funcion(c)) < tolerancia :
            break
        elif funcion(a)*funcion(c) > 0:
            a = c
        else:   
            b = c


        a_values.append(a)
        b_values.append(b)
        c_values.append(c)
        f_c_values.append(funcion(c))
        tolerancia_values.append(tolerancia)


    a_values.append(a)
    b_values.append(b)
    c_values.append(c)
    f_c_values.append(funcion(c))
    tolerancia_values.append(tolerancia)

    data={
        "Iteracion": "",
        "a": a_values,
        "b": b_values,
        "c": c_values,
        "f(c)": f_c_values,
        "tolerancia": tolerancia_values
    }

    
    tabla = pd.DataFrame(data)
    print(tabla)

    return(c)