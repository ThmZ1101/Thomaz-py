import math

P1 = float(input('Nota da P1: '))
T1 = float(input('Nota T1: '))

M1 = P1*0.7 + T1*0.3

P2 = float(input('Nota da P2: '))
T2 = float(input('Nota T2: '))

M2 = P1*0.8 + T1*0.2

MF = M1*0.4 + M2*0.6

print(f'Media 1 = {M1} \n Media 2 = {M2} \n Media Final = {MF}')
if MF >= 7:
    print(f'Aluno Aprovado')
elif MF <7 and MF>5:
    print(f'Aluno está de exame')
else:
    print(f'Aluno Reprovado')
    
    