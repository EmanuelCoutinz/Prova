
inicio = int(input("Digite o número inicial do intervalo: "))
fim = int(input("Digite o número final do intervalo: "))

soma_pares = 0
pares_encontrados = []  

for numero in range(inicio, fim + 1):
    if numero % 2 == 0:
        soma_pares += numero
        pares_encontrados.append(numero)
else:
    if pares_encontrados:
        print("\nNúmeros pares encontrados no intervalo:")
        print(pares_encontrados)
        print(f"Soma dos números pares entre {inicio} e {fim}: {soma_pares}")
    else:
        print(f"\nNão há números pares no intervalo entre {inicio} e {fim}.")
