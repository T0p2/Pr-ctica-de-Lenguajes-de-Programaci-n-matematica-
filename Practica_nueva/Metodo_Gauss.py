'''Metodo de gauss, trianguliza la matriz dejando 
'0' por debajo de la diagonal y '1' en la diagonal o no
- Se comienza diviendo la primer fila por matriz[1,1]
- Conseguimos 0 debajo del elemetno matriz[1,1]
- Segundo paso: conseguir un 1 en la digonal matriz[2,2]
- y reptimos
- por ultimo resolvemos el sistema de ecuaciones.



En el algoritmo tenemos el paso de trianguliazcion (Descendente)
Y el paso de resolver el sistema de ecuaciones (Ascendente porque va de abajo hacia arriba)
'''


import numpy as np

def gauss_elimination(matrix):

    matrix = np.array(matrix, dtype=float)
#filas y columnas
    rows, cols = matrix.shape

    for p in range(rows):
        pivot_value = matrix[p, p]
#divido por el pivote la fila p
        matrix[p, :] /= pivot_value
#cuando haga la primera fila, la segunda y la tercera paso por aca
        for j in range(p + 1, rows):
#consigo los 1 por debajo del pivote.
            factor = matrix[j, p]
            matrix[j, :] -= factor * matrix[p, :]
    
    # Resolver el sistema (ascendente)
#x es para almacenar el resultado.
    x = np.zeros(rows)
    x[rows - 1] = matrix[rows - 1, cols - 1]

    for i in range(rows - 2, -1, -1):
    # Sustitución hacia atrás para encontrar las soluciones
        x[i] = matrix[i, cols - 1] - np.sum(matrix[i, i + 1:rows] * x[i + 1:rows])

    return x

# Definir la matriz aumentada [A | B] para el sistema de ecuaciones
matrix = np.array([[-2,0,-2,-10], [2,2,4,16], [0,1,0,0]])

# Aplicar el método de Gauss para resolver el sistema de ecuaciones
solution = gauss_elimination(matrix)

# Asignar las soluciones a variables específicas
x1, x2, x3 = solution

# Imprimir la solución
print("Solución del sistema de ecuaciones:")
print("Ecuación 1: 2*x1 - x2 + x3 = 8")
print("Ecuación 2: -3*x1 - x2 + 2*x3 = -11")
print("Ecuación 3: -2*x1 + x2 + 2*x3 = -3")
print("\nSoluciones:")
print("x1 =", x1)
print("x2 =", x2)
print("x3 =", x3)
