#Ejercicio 15 a


import sympy as sp
x = sp.Symbol('x')


def funcion(n):
    return (x ** n) / (x + 10)



for n in range (0, 25):
    
    integral = sp.integrate(funcion(n), (x, 0,1))

    #Los valores salen como sumas de logaritmos, asi que 
    #implemento un metodo de sympy, para que me resuelva eso

    resultado_integral =  integral.evalf()
    
    print(f"n = {n}: Integral I_n = {resultado_integral}")




