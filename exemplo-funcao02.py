import os

#importando as funcoes do arquivo FUNCOES.PY
import FUNCOES

os.system("cls")
 
FUNCOES.exibir_titulo("Calculando a Média com Funções")


nome = input ("Digite o nome do Aluno:  ")
nometurma = input ("Digite o nome da turma:  ")

nota1 = float(input("Digite a Primeira Nota: "))
nota2 = float(input("Digite a Segunuda Nota: "))
nota3= float(input("Digite a Terceira Nota: "))

FUNCOES.calcular_media(nome, nometurma,  nota1, nota2, nota3)


#Declarando Funcao: 
resultadoFinal = FUNCOES.calcularMediaComRetorno(nota1, nota2, nota3)
print ("Resultado Media (com retorno) : ", resultadoFinal)
FUNCOES.calcularMediaComRetorno

FUNCOES.verificar_situacao_do_aluno(nome)

input ("Digite <ENTER> para continuar")