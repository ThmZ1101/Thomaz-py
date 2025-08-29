import math
import random

numeros = []

for _ in range(5):
    numero = random.randint(1, 100)
    numeros.append(numero)
print(f'Lista de numeros: {numeros}')

maior = 0

for num in numeros:
    if num > maior:
        maior = num
            
print(f'Maior numero é: {maior}')