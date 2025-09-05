import math
dados = [1,1,1,0,0,1]
mantica = ['x','x',1,'x',1,1,0,'x',0,1]
resultadoPosicaoBinarioInvertido = [None] * len(mantica)
    # Itera sobre a lista, obtendo o índice (i) e o valor (elemento)
for i, elemento in enumerate(mantica):
        
        # 1. Procura no conjunto mantica[] que terá 0 ou 1 ou x, se encontrar 1 ou 0
        if elemento == 0 or elemento == 1:
            
            # 2. Deve pegar o índice dele, somar +1
            possicao = i + 1
            
            # 3. Converter para binário
            # A função bin() retorna uma string binária com prefixo '0b'.
            # O slicing [2:] remove este prefixo, deixando apenas os bits.
            # [::-1] para inverter o codigo binario da possição
            binario = bin(possicao)[2:][::-1]
            
            # Armazena o resultado no dicionário para exibição
            resultadoPosicaoBinarioInvertido[i] = binario
            
print(resultadoPosicaoBinarioInvertido)

osD = []

# O loop irá de 0 até o número de elementos na lista 'dados' (ex: de 0 a 4)
for i in range(len(dados)):
    # Usa uma f-string para criar o elemento 'Dx'
    # O 'i' dentro das chaves {} será substituído pelo valor do índice do loop.
    elemento = f"D{i+1}"
    
    # Adiciona o elemento criado à lista
    osD.append(elemento)

# Imprime a lista final para verificar o resultado
print(f"Lista de dados: {dados}")
print(f"Novos elementos gerados: {osD}")








for i in (resultadoPosicaoBinarioInvertido):
    elemento = resultadoPosicaoBinarioInvertido[i]
    elemento_str = str(elemento)
    digito = elemento_str
    j = 0
    print(f'{resultadoPosicaoBinarioInvertido[i]} = {j} / {digito[j]}')
    j = j+1
    
    # Adiciona o elemento criado à lista
    osD.append(elemento)



# Seu conjunto (lista em Python) de números
numeros = [10, 20, 33, 432]

# Passo 1: Acesse o elemento.
# No Python, as posições (índices) começam do 0.
# Para pegar o 33, usamos o índice 2.
elemento = numeros[2]
print(f"O elemento que vamos usar é: {elemento}") # Output: 33

# Passo 2: Converta o elemento para string.
# Isso permite que você trate o número como uma sequência de caracteres.
elemento_str = str(elemento)
print(f"O elemento como string é: '{elemento_str}'") # Output: '33'

# Passo 3: Puxe o dígito específico.
# O segundo dígito está no índice 1.
digito = elemento_str[1]
print(f"O dígito que você quer é: {digito}") # Output: 3


#**  Encontrar ince do conjunto mantica que possui 1 ou 0, somar +1       
#**  transformar o resultado em conjunto binário e inverter
#**  criar um conjunto com os D(x) para cada dado
#  criar um conjunto[variáveis usadas] com 2 ** índice vezes o numero presente no índice, 
#  para todo o conjunto binário
#  excluir os resultados = 0
#  Assim teremos a conta exata da soma das variáveis 
# 
# 
#  Exemplo:
#  Indice do dado 10(+1) = 11
#  Em binário = 1011
#  inverter = 1101
#  1 (indece0) 1 (indice1) 0 (indice2) 1 (indice3)
#  2**0*1 = 1 + 2**1*1=2 + 2**2*0=0 + 2**3*1=8
#  1 + 2 + 8 = 11
