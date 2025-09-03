import math

binarios = []

#colocando os dados informado para a lista de binarios com lop
while True:
    numero = int(input("Digite o dado: "))
    
    
    if numero == 0 or numero ==1:
        binarios.append(numero)  
    elif numero != 0 or numero !=1 :
        break  

#declara a quantidade de dados no conjunto binarios 
QuantidadeDados = len(binarios)
print(f'Quantidade de Dados= {QuantidadeDados}')  


#-------------------------------------------------------------------



# 1. Calcula o logaritmo na base 2 do número
    # O resultado é o expoente da maior potência de 2
expoente = math.floor(math.log2(QuantidadeDados))
# 2. Calcula 2 elevado ao expoente para obter o número binário
maior_potencia_de_2 = 2 ** expoente

    
potencias = []

# Inicia com a primeira potência de 2, que é 2^0 = 1
potencia_de_2 = 1
        
        # Loop para encontrar e adicionar todas as potências de 2 na lista
while potencia_de_2 <= maior_potencia_de_2:
            # Adiciona o valor atual na lista
            potencias.append(potencia_de_2)
            
            # Multiplica o valor por 2 para obter a próxima potência de 2
            potencia_de_2 *= 2
            

#-------------------------------------------------------------------


#declarando a quantidade dos indices na mantiça
QuantidadeDados = len(binarios)
QuantidadePotenias = len(potencias)

QuantidadeIndices = QuantidadeDados + QuantidadePotenias

Vairaveis = []

# 1. Calcula o logaritmo na base 2 do número
    # O resultado é o expoente da maior potência de 2
expoente1 = math.floor(math.log2(QuantidadeIndices))
# 2. Calcula 2 elevado ao expoente para obter o número binário
maiorVariavel = 2 ** expoente1


# Inicia com a primeira potência de 2, que é 2^0 = 1
Variavel = 1
        
        # Loop para encontrar e adicionar todas as potências de 2 na lista
while Variavel <= maiorVariavel:
            # Adiciona o valor atual na lista
            Vairaveis.append(Variavel)
            
            # Multiplica o valor por 2 para obter a próxima potência de 2
            Variavel *= 2
            
        # Exibe o resultado final, mostrando a lista completa
print(f"A maior variavel é {maiorVariavel} e são:")
print(Vairaveis)



#-------------------------------------------------------------------


# 3. Define o tamanho da nova lista 'mantica' e completando com valor None


mantica = [None] * QuantidadeIndices

# 4. Adiciona 'x' nas posições corretas (índices das potências - 1 pois o indice começa em 0 e a menor potencia de 2 é 1)
for Variavel in Vairaveis:
        indice = Variavel - 1
        if indice < QuantidadeIndices:
            mantica[indice] = 'x'

 # 5. Adiciona os valores da lista 'binarios' nos espaços vazios
indice_binarios = 0
for i in range(len(mantica)):
        # Verifica se a posição atual já foi preenchida com 'x'
        if mantica[i] is None:
            # Se for, coloca o próximo valor de 'binarios'
            # A verificação 'indice_binarios < QuantidadeDados' evita erros
                mantica[i] = binarios[indice_binarios]
                indice_binarios += 1
print(mantica)



#  colocar o indice do dado. (verificar em qual posição possui 1 ou 0)
#  calcular os indices de variaveis (x) que somados são iguais ao indice do dado.
#  somar +1 ao resultado para ter a posição correta do dado. Ex:

#  mantiça : x  x  1
#  Indices : 0  1  2

#  calculo 0 + 1 = 2
#  2+1 = 3, dado está na possição 3 (indice 2).

