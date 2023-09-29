

import math
import pandas as pd

def funcion_aproximada(x, h):
    numerator = math.exp(x + h) - math.exp(x)
    return numerator / h

def funcion_real(x):
    return math.exp(x)



true_value = funcion_real(0)

h_values = [2**(-i) for i in range(1, 31)]
approx_values = [funcion_aproximada(0, h) for h in h_values]
error_absoluto = [abs(approx_value - true_value) for approx_value in approx_values]
error_relativo = [abs(error_absoluto/true_value) for error_absoluto in error_absoluto]



data = pd.DataFrame({
    "valores de h": h_values,
    "valores aproximados": approx_values,
    "valor real": true_value,
    "error absoluto": error_absoluto,
    "error relativo": error_relativo
})


print(data)















#Graficos nada que ver.
'''
# Gráfico de los valores aproximados
plt.figure(figsize=(10, 6))
plt.plot(h_values, approx_values, marker='o')
plt.xscale('linear')
plt.yscale('linear')
plt.xlabel('h')
plt.ylabel('Aproximación')
plt.title('Valores Aproximados de la Función')



# Gráfico de los errores absolutos
plt.figure(figsize=(10, 6))
plt.plot(h_values, error_absoluto, marker='o', color='r')
plt.xscale('linear')
plt.yscale('linear')
plt.xlabel('h')
plt.ylabel('Error Absoluto')
plt.title('Error Absoluto')




# Grafico de error relativo
plt.figure(figsize=(10, 6))
plt.plot(h_values, error_relativo, marker='o', color='r')
plt.xscale('linear')
plt.yscale('linear')
plt.xlabel('h')
plt.ylabel('Error Relativo')
plt.title('Errores Relativo')


#En este caso, como el valor verdaddero es siempre '1', 
#los errores realtivos y absolutos son iguales


plt.tight_layout()
plt.show()
'''