'''Ejercicio 2: Hallar el polinomio de Lagrange que interpola la siguiente tabla 
x -1 0 3/2 2
y -2 -1 ½ 1
'''

from Interpolacion_lagrange import interpolacion_lagrange_polinomio

puntos=[(-1, -2), (0, -1), (3/2, 1/2), (2, 1)]
p = interpolacion_lagrange_polinomio(puntos)
print(p)
