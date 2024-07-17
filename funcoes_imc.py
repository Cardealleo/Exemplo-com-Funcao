#declarando funcao:
def calcular_imc (peso, altura):
    global imc
    imc = peso / (altura * altura)
    
    
def calcular_situacao_imc (nome):
    if (imc <18.5):
        print ("Ola", nome, "seu Imc é de:", imc, "\nClassificação: Abaixo do peso\nInterpretação: Peso baixo, possivel desnutrição!")
    
    elif (imc >= 18.5 and imc <= 24.9 ):
        print ("Ola", nome, "seu Imc é de:", imc,"\nClassificação: Peso normal\nInterpretação: Peso saudável dentro da faixa considerada normal!")
    
    elif (imc >= 25.0 and imc <= 29.9):
        print ("Ola", nome, "seu Imc é de:", imc,"\nClassificação: Sobrepeso\nInterpretação: Excesso de peso corporal, não necessariamente prejudicial à saúde!")
    
    elif (imc >= 30.0 and imc <= 34.9):
        print ("Ola", nome, "seu Imc é de:", imc,"\nClassificação:  Obesidade Grau I (Leve)\nInterpretação: Risco aumentado de problemas de saúde relacionados à obesidade!")
    
    elif (imc >= 35.0 and imc <= 39.9):
        print ("Ola", nome, "seu Imc é de:", imc,"\nClassificação: Obesidade Grau II (Moderada)\nInterpretação: Risco significativamente aumentado de problemas de saúde!")
    
    elif (imc >= 40.0):
        print ("Ola", nome, "seu Imc é de:", imc,"\nClassificação: Obesidade Grau III (Grave)\nInterpretação: Risco muito elevado de problemas de saúde graves!")
    
    else:
        print("Erro, favor recalcular!")