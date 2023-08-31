import sympy as sp


x = sp.Symbol('x')

for n in range (1, 26):
    funcion = x ** n / (x + 10)
    integral = sp.integrate(funcion, (x, 1, 0))

    #Los valores salen como sumas de logaritmos, asi que 
    #implemento un metodo de sympy, para que me resuelva eso

    resultado_integral =  integral.evalf()
    
    print(f"n = {n}: Integral I_n = {resultado_integral}")




