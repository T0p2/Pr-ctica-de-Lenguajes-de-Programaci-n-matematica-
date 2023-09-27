'''2. La ecuaci´on e
x − 3x = 0 tiene por ra´ız a r = 0,61906129. Comenzando
con el intervalo [0,1], realizar seis iteraciones por el m´etodo de bisecci´on
para encontrar la ra´ız aproximada. Cu´antos decimales significativos
tiene dicha aproximaci´on? Cu´antas iteraciones son necesariars para
que la ra´ız obtenida tenga un error menor que 10−4
?'''


from Biseccion import biseccion_con_tolerancia
import math

def funcion (x):
    return(math.e**x - 3*x)

raiz_aprox = biseccion_con_tolerancia(funcion, 0, 1,  10**-4 )

raiz_real = 0.61906129

print(f"Entre la raiz verdadera {raiz_real} y la raiz calculada con el metodo de biseccion {raiz_aprox}, es: {raiz_real - raiz_aprox}")