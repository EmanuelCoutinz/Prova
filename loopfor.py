#
#
#  

# for estado in range(0,5,1):
#     print(estado)

#for estado in range(5,501,5):
    # print(estado)
     
#i = index 
# (for i in range (5,501,5) print i )
# acumulador = 0
# for i in range (3):
#     nota = float(input('DIGITE SUA NOTA:'))
#     acumulador += nota
# media = acumulador / 3
# print(media) 

# if media >= 5:
#   print('PARABENS')
# else
# print('VA ESTUDAR')
# numero = int(input('DIGITE UM NUMERO:'))

# for i in range (1,11,1):
#     print(f'{numero} x {i} = {numero*i}')
# acumuador =  1
# for i in range (1,101,1):
#     print (f'{acumuador} + {i} = {acumuador+i}')

# for i in range (10,0,-1): 
#     print (i)
# print('FELIZ ANO NOVO')
positivo = 0
negativo = 0
for i in range (10):
    numero = float(input(f'Digite o {i+1}° numero:'))
    
    if numero > 0:
        positivo += 1
    else:
        negativo += 1
        
print (f'TOTAL POSITIVOS:{positivo}')
print (f'TOTAL NEGATIVOS: {negativo}')
    
    



