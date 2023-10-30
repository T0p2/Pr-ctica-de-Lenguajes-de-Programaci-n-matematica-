def func(x):
    # Define la función que quieres integrar
    return x**2  # Ejemplo: x^2

def trapezoidal_rule(f, a, b, n):
    # Regla del trapecio para aproximar la integral definida
    h = (b - a) / n
    result = 0.5 * (f(a) + f(b))
    for i in range(1, n):
        result += f(a + i * h)
    result *= h
    return result

def romberg_integration(f, a, b, n_max):
    # Inicializa la matriz de Romberg
    romberg_matrix = [[0] * (n_max + 1) for _ in range(n_max + 1)]

    # Calcula las aproximaciones iniciales usando la regla del trapecio
    for i in range(n_max + 1):
        romberg_matrix[i][0] = trapezoidal_rule(f, a, b, 2**i)

    # Aplica la extrapolación de Richardson
    for j in range(1, n_max + 1):
        for i in range(j, n_max + 1):
            romberg_matrix[i][j] = (4**j * romberg_matrix[i][j - 1] - romberg_matrix[i - 1][j - 1]) / (4**j - 1)

    # La última entrada de la matriz tiene la mejor aproximación
    return romberg_matrix[n_max][n_max]

# Ejemplo de uso:
a = 0
b = 1
n_max = 4  # Puedes ajustar el número máximo de iteraciones

resultado = romberg_integration(func, a, b, n_max)
print(f"Resultado de la integración: {resultado}")
