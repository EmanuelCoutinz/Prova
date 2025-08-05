
alunos = int(input("Digite o número de alunos: "))

soma_medias = 0 

for i in range(alunos):
    print(f"\nAluno {i + 1}")
    nome = input("Nome do aluno: ")
    
   
    notas = []
    for j in range(1, 4):
        nota = float(input(f"Digite a nota {j}: "))
        notas.append(nota)
    
    media = sum(notas) / 3
    soma_medias += media

   
    status = "Aprovado" if media >= 7.0 else "Reprovado"

   
    print(f"Resultado do aluno: {nome}")
    print(f"Notas: {notas}")
    print(f"Média: {media:.2f}")
    print(f"Situação: {status}")


media_geral = soma_medias / alunos
print(f"Média geral da turma: {media_geral:.2f}")
