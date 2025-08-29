import math
import random


numeros = []

while True:
    numero = int(input("Digite um número(ou 0 para finalizar): "))
    
    
    if numero > 0:
        numeros.append(numero)  
    elif numero == 0:
        break  
    
    soma = sum(numeros)
print(f"Soma dos numeros Possitivos são: {soma}")

