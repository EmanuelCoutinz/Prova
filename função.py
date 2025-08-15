#FUNÇÃO
#def nomeFunção (entrada = PARAMENTRO):


# def esporte (lutar):
#     return f'Eu gosto de {lutar}'

# print(esporte(lutar='muay thai'))

# def somaDeNumeros (numero = int):
#     return f'{numero} + {numero} = {numero + numero}'

# numero = int(input('DIGITE UM NUMERO:'))
# print(somaDeNumeros(numero))
    
# def idadeDoUsuario (idade = int): 
#     if idade >= 18: 
#       return f'Voce é maior de idade' 
#     else:
#        return 'Voce é menor de idade' 

# idade = int(input('DIGITE SUA IDADE:'))
 
# print(idadeDoUsuario(idade))
 
 
# def calculadora (num1 = int, num2 = int, op = str): 
#     while True:
#      if op == '+':
#         return f'{num1} + {num2} = {num1 + num2}'
#      elif op == '-':
#          return f'{num1} - {num2} = {num1 - num2}'
#      elif op == '*':
#         return f'{num1} * {num2} = {num1 * num2}'
#      elif op == '/':
#         return f'{num1} / {num2} = {num1 / num2}'
#     else:
#         return 
    
# num1 = int(input('DIGITE O PRIMEIRO NUMERO:'))
# num2 = int(input('DIGITE O SEGUNDO NUMERO:'))
# op = input('DIGITE A OPERAÇÃO:')

# print(calculadora(num1, num2, op))


def soma (num1 = int, num2 = int):
    return num1 + num2
def subtracao (num1 = int, num2 = int):
    return num1 - num2
def multiplicacao (num1 = int, num2 = int):
    return num1 * num2
def divisao (num1 = int, num2 = int):
    return num1 / num2

while True:
    print('''
    1 - SOMA
    2 - SUBTRAÇÃO
    3 - MULTIPLICACAO
    4 - DIVISAO
    5 - SAIR
    ''')
    opcao = str(input('DIGITE A OPÇÃO DESEJADA:')) 
     
    if opcao == '5':
         print ('SAINDO...')
         break
     
    num1input = float(input('DIGITE O PRIMEIRO NUMERO:')) 

    