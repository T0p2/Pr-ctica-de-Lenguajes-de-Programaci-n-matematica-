def func(x):
    # Define la función que quieres integrar
    return x**2  # Ejemplo: x^2

def simpson_rule(f, a, b, n):
    # Regla de Simpson para aproximar la integral definida
    h = (b - a) / n
    result = f(a) + f(b)
    for i in range(1, n, 2):
        result += 4 * f(a + i * h)
    for i in range(2, n-1, 2):
        result += 2 * f(a + i * h)
    result *= h / 3
    return result

# Ejemplo de uso:
a = 0
b = 1
n = 100  # Puedes ajustar el número de intervalos (debe ser par)

resultado_simpson = simpson_rule(func, a, b, n)
print(f"Resultado de la integración usando la regla de Simpson: {resultado_simpson}")
