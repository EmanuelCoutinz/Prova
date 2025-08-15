#PEP8 (São as boas praticas de se codar em phyton)



bancosDeDados = []

def addtarefas(nomeTarefa:str,
               descTarefa:str,
               prioridadesTarefa:str,
               categoriaTarefa:str):
   """esta função tem como seu proposito armazenar tarefas"""
   tarefa = {
     'nomeTarefa':nomeTarefa,
     'descTarefa':descTarefa,
     'prioridadesTarefa':prioridadesTarefa,
     'categoriaTarefa':categoriaTarefa
}

   bancosDeDados.append(tarefa)
   return bancosDeDados


def listarTarefas(): 
    '''Etas função tem como listar todas as tarfas armazenadas'''
    
    if len(bancosDeDados) == 0:
        return 'Banco esta vazio'
    else:
        return bancosDeDados
    
    
def marcarTarefaComoConcluida(nomeDaTarefa:str):
    '''Esta função tem como proposito marcar a tarefa como concluida
    e remove-la do banco de dados'''
    
    
    for tarefa in bancosDeDados:
        if nomeDaTarefa == tarefa['nomeDaTarefa']:
            #PEGANDO A POSIÇÃO DA TAREFA
            posicao = bancosDeDados.index(tarefa)
            bancosDeDados.pop(posicao)
            
            return 'Tarefa marcada como concluida'
    return 'Tarefa inexistente!'




def filtrarTarefasPorPrioridades(prioridade):
    listaFiltrada = []
    
    bancosDeDadostupla = tuple(bancosDeDados)
    
    for tarefa in bancosDeDadostupla:
        if prioridade == tarefa ['prioridadesTarefa']:
            listaFiltrada.append(tarefa)
    return listaFiltrada


    adicionarTarefas (nomeDaTarefa= 'varrer a casa',descTarefa ='na segunda eu preciso fazer uma faxina geral na casa',
                   prioridadesTarefa ='MEDIA',
                  categoriaTarefa='LIMPEZA')

   
print(filtrarTarefasPorPrioridades('ALTA'))



while True:
    print('''
    1 - CADASTRO 
    2 - 
    3 - 
    4 - 
    5 - SAIR
    ''')
    opcao = str(input('DIGITE A OPÇÃO DESEJADA:')) 
        

        
        
        
        
    if opcao == '5':
         print ('SAINDO...')
         break
