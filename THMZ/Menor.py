import math
import random

numeros = []

for _ in range(10):
    numero = random.randint(1, 100)
    numeros.append(numero)
print(f'Lista de numeros: {numeros}')

menor = 101

for num in numeros:
    if num < menor:
        menor = num
            
print(f'Menor numero é: {menor}')