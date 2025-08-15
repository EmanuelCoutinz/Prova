#DICIONARIO : É UMA COLEÇÃO DE OBJETOS QUE NÃO INDEXADA E MUTAVEL
#OS OBJETOS SÃO GUARDADOS É UMA FORMA DE PAR
#CHAVE(PROPRIEDADES): VALOR 
#ENTÃO SEMṔRE QUE NECESSARIO ACESSAR UM OBJETO 
#DEVE PROCURA-LO PELA CHAVE PERTENCE DELE
#EXISTE DUAS POSSIBILIDADES DE DECLARAR UM DICIONARIO 
#{} OU DICT()
#
#
#
#
#
#
#


# dicionario = {
#     'Estado' : 'Serjipe',
#     'População': 2_291_077 ,
#     'UF': 'SE',
#     'Capital ' : 'Aracaju' ,
    
# }

# print ('dicionario ["População"]  ,dicionario["UF"]')




# user ={
#     'nomes' : ['Davi , Luiz'],
#     'idades' : [32 , 21]  
# }
# print (user['idades'] [1])

# user['idades']. append(25)
# print(user)



# dicionario = {
#     'nomes':[''],
#     'cursos' : [''],
#     'email': ['']
# }

# for i in range (3): 
#     nome = str (input('DIGITE SEU NOME: '))
#     curso = str (input('DIGITE SUA CURSO: '))
#     email = str (input('DIGITE SEU EMAIL: '))
#     dicionario['nomes']. append(nome)
#     dicionario['cursos']. append(curso)
#     dicionario['email']. append(email)
    
    

# print (dicionario)


#
#
#
#
#
#
#
#


#SETs 
#É UM CONJUTO NÃO INDEXADO E IMUTAVEL
#TEM DUAS FORMAS DE DECLARAR SETS 
#{'objeto', 'objeto1'} ou set()

# setPEssoas = {"guilherme" , "pedro" , "joão" , "augusto"}

# for i in range (2) :
#     nome = str (input('DIGITE UM NOME: '))
    

# print(setPEssoas)



# setvazio = set()
# print(type(setvazio))
# setvazio1 = {}
# print(type(setvazio1))

#ATIVIDADES#


# idade = int(input('DIGITE SUA IDADE: '))

# if idade < 12: 
#     print('Criança')
    
# elif idade >= 12 and idade < 17: 
#     print('Adolescente')
    
# elif idade > 18 and idade < 59 : 
#     print('Adulto')
    
# else :
#     print('idoso')


# impares = 0
# pares = 0
# for i in range (10):
#     numero = int(input(f'Digite o numero:'))
    
#     if numero % 2 == 0:
#         pares = pares + 1
#     else:
#         impares = impares +1
        
# print (f'TOTAL PARES:{pares}')
# print (f'TOTAL IMPARES: {impares}')



for i in range (10):
    idade = int(input('DIGITE SUA IDADE: '))
    
if idade < 0 and idade <= 25:
    