import os


#Declarando a funcao
def calcular_media(nomeAluno, turmaAluno,  nota1, nota2, nota3):
    global media 
    media = (nota1 + nota2 + nota3) / 3
    print ("Ola,", nomeAluno, "da turma", turmaAluno, "sua média foi: ", media)
 
    
def calcularMediaComRetorno(nota1, nota2, nota3):
    global media
    media = (nota1 + nota2 + nota3) / 3
    return media


    
def verificar_situacao_do_aluno(nome):
    if (media >=6):
        print (nome, "parabéns foi Aprovado!")    
    
    elif (media >=4 and media <=5):
        print (nome, "você ficou de recuperação! ")
    
    else:
        print (nome, "você foi REPROVADO! ")

def exibir_titulo(TituloDoPrograma):
    print (TituloDoPrograma)
