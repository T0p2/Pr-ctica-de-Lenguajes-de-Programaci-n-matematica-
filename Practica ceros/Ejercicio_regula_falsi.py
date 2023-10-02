from Metodo_Regula_falsi import regula_falsi
import sympy as sp

sp.symbols('x')

def funcion(x):
    return((-1/10)*x**2)+3

raiz = regula_falsi(funcion,1,7, 9.8*10**-5)