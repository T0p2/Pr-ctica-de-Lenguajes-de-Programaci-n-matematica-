
def trapecio (a, b, f):
    return ((b-a)*(f(a) + f(b)))/2


def funcion (x):
    return x**3 - 6*x**2 + 11*x -6


print(trapecio(1.3, 1.8, funcion))
