'''
Encontrar los valores de a0 y a1 que hacen mínimo el error cuadrático cuando se
aproxima la lista (−1, 2), (0, −1), (1, 1) y (2, −2) con un polinomio de grado uno.
'''


from Metodo_min_cuadrado import min_cuadrado

lista_x = [-1, 0, 1, 2]
lista_y = [2, -1, 1, -2]


ecuacion = min_cuadrado (lista_x, lista_y)
print(ecuacion)
