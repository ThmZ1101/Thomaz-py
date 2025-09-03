import math

binarios = []

while True:
    numero = int(input("Digite o dado: "))
    
    
    if numero == 0 or numero ==1:
        binarios.append(numero)  
    elif numero != 0 or numero !=1 :
        break  

#declara a quantidade de dados no conjunto binarios 
QuantidadeDados = len(binarios)
print(QuantidadeDados)  


# 1. Calcula o logaritmo na base 2 do número
    # O resultado é o expoente da maior potência de 2
expoente = math.floor(math.log2(QuantidadeDados))
# 2. Calcula 2 elevado ao expoente para obter o número binário
maior_potencia_de_2 = 2 ** expoente

 # 3. Exibe o resultado
print(f"O maior número na base 2 menor ou igual a {QuantidadeDados} é {maior_potencia_de_2}.")


    
# Variável a ser adicionada
novo_elemento = 3

# Adicionando na posição 2 (índice começa em 0)
minha_lista.insert(2, novo_elemento)
