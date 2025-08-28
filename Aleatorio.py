import random
import math

# Gera um número inteiro aleatório entre 0 e 50
N1 = random.randint(0, 50)


if N1 < 25:
    N2 = N1**2 - N1*2
    print(f'Numero1: {N1} \n Numero2 {N2}')