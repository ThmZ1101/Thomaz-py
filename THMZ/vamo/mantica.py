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


# 1. Calcula o logaritmo na base 2 do número
    # O resultado é o expoente da maior potência de 2
expoente = math.floor(math.log2(QuantidadeDados))
# 2. Calcula 2 elevado ao expoente para obter o número binário
maior_potencia_de_2 = 2 ** expoente

 # 3. Exibe o resultado
print(f"O maior número na base 2 menor ou igual a {QuantidadeDados} é {maior_potencia_de_2}.")
    
mantica = [binarios]
potencias = []

# Inicia com a primeira potência de 2, que é 2^0 = 1
potencia_de_2 = 1
        
        # Loop para encontrar e adicionar todas as potências de 2 na lista
while potencia_de_2 <= maior_potencia_de_2:
            # Adiciona o valor atual na lista
            potencias.append(potencia_de_2)
            
            # Multiplica o valor por 2 para obter a próxima potência de 2
            potencia_de_2 *= 2
            
        # Exibe o resultado final, mostrando a lista completa
print(f"As potências de 2 menores ou iguais a {maior_potencia_de_2} são:")
print(potencias)


mantica = [binarios]
print(potencias[2])

# Variável a ser adicionada
novo_elemento = 3


# Adicionando na posição 2 (índice começa em 0)
mantica.insert(2, novo_elemento)