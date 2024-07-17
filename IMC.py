import os
import funcoes_imc

os.system("cls")

print ("Calculando IMC")

nome = input("Escreva seu nome: ")
peso = float(input("Informe seu peso:   "))
altura = float(input("Informe sua altura:  "))

funcoes_imc.calcular_imc (peso, altura)

funcoes_imc.calcular_situacao_imc(nome)


input("Digite <ENTER> para continuar")