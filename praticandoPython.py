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


    