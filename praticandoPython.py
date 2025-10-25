#Importando biblioteca com alias
import matplotlib.pyplot as plt

import math

#importando função específica da biblioteca
from random import choice, randrange, randint

# Criando primeiro gráfico

estudantes_2 = ["João", "Maria", "José"]
# notas = [8.5, 9, 6.5]

# plt.bar(x = estudantes, height= notas)
# plt.show()

# Importando função específica de uma biblioteca

# estudante = choice(estudantes_2)
# print(estudante)

# # import numpy as np

# Crie um programa que leia a seguinte lista de números e escolha um número desta aleatoriamente

# lista = [8, 12, 54, 23, 43, 1, 90, 87, 105, 77]

# escolhaRandomica = choice(lista)
# print(escolhaRandomica)

# Crie um programa que sorteia, aleatoriamente, um número inteiro positivo menor que 100
# escolhaRandomica = randrange(100)
# print(escolhaRandomica)

#Crie um programa que solicite à pessoa usuária digitar dois números inteiros e calcular a potência do 1º número elevado ao 2º.

# num1 = int(input("Digite o primeiro valor: "))
# num2 = int(input("Digite o segundo valor: "))

# potencia = math.pow(num1, num2)

# print(f"O valor {num1} elevado à potência de {num2} é  igual a: {potencia}")

#Um programa deve ser escrito para sortear uma pessoa seguidora de uma rede social para ganhar um prêmio. A lista de participantes é numerada e devemos escolher aleatoriamente um número de acordo com a quantidade de participantes. Peça à pessoa usuária para fornecer o número de participantes do sorteio e devolva para ela o número sorteado.

# qtdParticipantes = int(input("Digite a quantidade de participantes do sorteio: "))
# sorteio = randint(1, qtdParticipantes)

# print(f"O participante sorteado foi o : {sorteio}")

#  Você recebeu uma demanda para gerar números de token para acessar o aplicativo de uma empresa. O token precisa ser par e variar de 1000 até 9998. Escreva um código que solicita à pessoa usuária o seu nome e exibe uma mensagem junto a esse token gerado aleatoriamente.
# nome = input("Qual o seu nome?")

# token = randrange(1000, 9998 )

# print(f"Olá {nome} seu token de acesso é {token}. Seja bem vindo.")

#Trabalhando com Funções

# Notas do Estudante
notas = {'1ºTrimestre': 8.5, '2º Semestre': 9.5, '3º Trimestre': 7}

# # Calculando a soma
# soma = 0

# #Com Loop
# for nota in notas.values():
#     soma += nota

#     print(soma)

# #Usando função embutida sum()
# somatorio = sum(notas.values())
# print(somatorio)

# #Usando a função embutida len()
# qtd_notas = len(notas)
# print(qtd_notas)

# #Calculando a média
# media = somatorio / qtd_notas
# print(media)

# #Arredondando o valor
# print(round(media,1)

#Criando função sem parâmetro

# def media():
#     calculo = (10 + 9 + 8) / 3
#     print(calculo)

# media()    

#Criando função com parâmetro

# def media(nota_1, nota_2, nota_3):
#     calculo = (nota_1 + nota_2 + nota_3) / 3
#     print(calculo)

# media(3, 6, 9)

# notas = [8.5, 9.0, 6.0, 10.0]

# def media(lista):
#     calculo = sum(lista) / len(lista)
#     print(calculo)

# media(notas)    

#Criando função com retorno

# notas = [8.5, 9.0, 6.0, 10.0]

# def boletim(lista):
#     media = sum(lista) / len(lista)

#     if media >= 6:
#         situacao = "Aprovado"
#     else:
#         situacao = "Reprovado"

#     return (media, situacao)

#Criando função lambda

# qualitativo = lambda x: x + 0.5

# print(qualitativo(8))

#Escreva um Código que lê a lista abaixo e faça: 
#   A leitura do tamanho da lista. 
#   A leitura do maior e menor valor
#   A soma dos valores da lista

# lista = [16, 14, 63, 105, 17, 99, 70, 11, 20, 48, 79, 32, 17, 89, 8, 25, 66]
# maior = 0
# menor = 0
# soma = 0
# contador = 0

# for elemento in lista:

#     soma += elemento

#     if(maior == 0 and menor == 0):
#         maior = elemento
#         menor = elemento
#     elif(elemento > maior):
#         maior = elemento
#     elif(elemento < menor):
#         menor = elemento    

# print(f"A lista possui {len(lista)} números em que o maior número é {maior} e o menor número é {menor}. A soma dos valores presentes nela é igual a {soma}")

# Escreva uma função que gere a tabuada de um número inteiro de 1 a 10, de acordo com a escolha da pessoa usuária. Como exemplo, para o número 7, a tabuada deve ser mostrada no seguinte formato:

# numeroEscolhido = int(input("Digite a tabuada desejada: "))

# def geraTabuada(numTabuada):
#     for i in range(11):

#         print(f"{numeroEscolhido} X {i} = ", numeroEscolhido * i)

# geraTabuada(numeroEscolhido)
    
# Crie a função que leia a lista abaixo e retorne uma nova lista com os múltiplos de 3:

# array = [97, 80, 94, 88, 80, 1, 16, 53, 62, 32, 24, 99]
# mult_3 = [None] * 12


# def multiplosTres(array):
    
#     contador = 0

#     for i in array:
#         mult_3[contador] = i * 3
#         contador+=1
    
#     return mult_3

# print(multiplosTres(array))

# Crie uma lista dos quadrados dos números da seguinte lista [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]. Lembre-se de utilizar as funções lambda e map() para calcular o quadrado de cada elemento da lista.

# array = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# quadrados_iterador = map(lambda x: x * 2, array)
# quadrados = list(quadrados_iterador)


# print(quadrados)

# Para atender a uma demanda de uma instituição de ensino para a análise do desempenho de seus(suas) estudantes, você precisa criar uma função que receba uma lista de 4 notas e retorne:

# maior nota
# menor nota
# média
# situação (Aprovado(a) ou Reprovado(a))

# def analiseDesempenho():

#     notas = [None] * 4
#     maior = None
#     menor = None
#     soma = 0
#     media = 0
#     qtdNotas = len(notas)

#     for nota in notas:
#         nota = int(input("Digite a nota: "))

#         if(maior == None and menor == None): 
#             maior = nota
#             menor = nota
#         elif(nota > maior):
#             maior = nota
#         elif(nota < menor):
#             menor = nota

#         soma += nota
    
#     media = soma/qtdNotas
#     situacao = "Aprovado" if media >= 5 else "Reprovado"

#     return f"A média do aluno é {media}, ele se encontra {situacao}. A maior nota é: {maior} e a  menor nota é: {menor}"

# print(analiseDesempenho())

# Você recebeu uma demanda para tratar 2 listas com os nomes e sobrenomes de cada estudante concatenando-as para apresentar seus nomes completos na forma Nome Sobrenome. As listas são:

# nomes = ["joão", "MaRia", "JOSÉ"]
# sobrenomes = ["SILVA", "souza", "Tavares"]


# def unirNomeSobrenome(arrayNome, arraySobrenome):
#     nomeCompleto = []
    

#     for indice , nome in enumerate(arrayNome) :
#         nomeCompleto.append(f"{nome} {arraySobrenome[indice]}")

        
        
#     return nomeCompleto

# print(unirNomeSobrenome(nomes, sobrenomes))
        
# gols_marcados = [2, 1, 3, 1, 0]
# gols_sofridos = [1, 2, 2, 1, 3]

# def identificarVencedor(marcados, sofridos):

#     resultados = []

#     for indice, (marcado, sofrido) in enumerate(zip(marcados, sofridos)):
        
#         status = "Ganhou a partida" if marcado > sofrido else "Empatou a partida" if marcado == sofrido else "Perdeu a partida"

#         resultados.append(status)

#     return resultados    

# print(identificarVencedor(gols_marcados, gols_sofridos))

# Você iniciou um estágio em uma empresa que trabalha com processamento de linguagem natural (NLP). Sua líder requisitou que você criasse um trecho de código que recebe uma frase digitada pela pessoa usuária e filtre apenas as palavras com tamanho maior ou igual a 5, exibindo-as em uma lista. Essa demanda é voltada para a análise do padrão de comportamento de pessoas na escrita de palavras acima dessa quantidade de caracteres.

frase = "Aprender Python aqui na Alura é muito bom" 


def identificarQtdLetras(frase):
    
    palavras = frase.split()
    palvrasComMaisDeCincoLetras = []

    for  palavra in palavras:
        for indice, letra in enumerate(palavra):
            indice += 1

            if(indice >= 5):
                palvrasComMaisDeCincoLetras.append(palavra)
            
    return palvrasComMaisDeCincoLetras
 
# print(identificarQtdLetras(frase))

print(identificarQtdLetras(frase))