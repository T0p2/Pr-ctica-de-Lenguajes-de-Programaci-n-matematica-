#Ejercicio 15 b

import sympy as sp
x = sp.Symbol('x')


def funcion(r, n):
    return (1/10) * (1/n - r)



n_values = [i for i in range(1, 25)]
#n_values = n_values[::-1]

# Inicializar el valor para n = 0
resultado_anterior = sp.integrate((x ** 0) / (x + 10), (x, 1 , 0)).evalf()
''' estamos buscando el valor aprox de n = 25, que es aprox a n = 24
    Entonces calculamos el n = 0, para empezar a calcular el valor de n = 1
    ya que en la funcion se calcula el resultado actual, con el anterior.'''



for n in n_values:
    funcion_actual = (x ** n) / (x + 10)
    integral = sp.integrate(funcion_actual, (x, 1, 0))
    resultado_integral = integral.evalf()
    

    # Calcular el resultado usando la fórmula dada
    resultado_actual = funcion(resultado_anterior, n)

    print(f"n = {n}: Integral I_n = {resultado_actual}")

    # Actualizar el resultado anterior
    resultado_anterior = resultado_actual

# Asumir que I25 ≈ I24
resultado_i25 = resultado_anterior
print(f"I25 ≈ I24: {resultado_i25}")




