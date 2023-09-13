'''
Ejercicio 8: Sea p el valor exacto de un nmero y p* una aproximacion. 
Estime el error absoluto y el error porcentual:
'''



import math
from fractions import Fraction

def valores_especiales(valor_texto):
    valor_texto = valor_texto.strip().lower()  # Limpiar y convertir a minúsculas
    if valor_texto == "pi":
        return math.pi
    elif valor_texto == "e":
        return math.e
    else:
        try:
            return float(valor_texto)  # Intentar convertir a float
        except ValueError:
            try:
                return float(Fraction(valor_texto))  # Intentar convertir fracción a float
            except ValueError:
                return None



true_value_text= input ("Ingrese el valor verdadero/exacto: ")
true_value = valores_especiales(true_value_text)
false_value_text = input("Ingrese el valor aproximado: ")
false_value = valores_especiales(false_value_text)


if (true_value is None):
    true_value = float(true_value_text)

if(false_value is None):
    false_value = float(false_value_text)




error_abs = abs(true_value - false_value)
error_relativo = error_abs / true_value
error_porcentual = error_relativo * 100


print("tus errores son: ")
print("Error absoluto: " , error_abs)
print("Error relativo: " , error_relativo)
print("Error porcentual: " , error_porcentual)



