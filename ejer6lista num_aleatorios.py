from statistics import mean, median, mode

mi_lista = [1,2,5,5,3]
print (mean(mi_lista))

import random

numeros_aleatorios = [random.randint(1, 100) for i_ in range(50)]

moda = mode(numeros_aleatorios)
mediana = median(numeros_aleatorios)
media = mean(numeros_aleatorios)

if media > mediana > moda:
    resultado = "Sesgo positivo o a la derecha"
elif media < mediana < moda:
    resultado = "Sesgo negativo o a la izquierda"
else:
    resultado = "Sin sesgo"

print(f"Moda: {moda}")
print(f"Mediana: {mediana}")
print(f"Media: {media:.2f}")
print(f"Resultado: {resultado}")
