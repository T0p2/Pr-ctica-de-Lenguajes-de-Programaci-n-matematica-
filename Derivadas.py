
from sympy import Symbol

x = Symbol('x') #definimos a x como un simbolo

y = x**2 #numero a derivar

derivada = y.diff(x)
print(derivada)