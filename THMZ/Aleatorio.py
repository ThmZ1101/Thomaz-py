import random
import math

# Gera um número inteiro aleatório entre 0 e 50
N1 = random.randint(0, 50)


if N1 > 25:
    N2 = (N1**2) - (N1*2)
    print(f'Numero1: {N1} \nNumero2 {N2}')
else:
    N2 = N1/3 + N1
    print(f'Numero1: {N1} \nNumero2 {N2}')