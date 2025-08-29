import math
import random

numeros = []

for _ in range(10):
    numero = random.randint(1, 100)
    numeros.append(numero)
print(f'Lista de numeros: {numeros}')

impar = 0
par = 0

for num in numeros:
    if num % 2 == 0:
        par += 1 
    else:
        impar += 1
        
print(f'Pares: {par}\nImpar: {impar}')