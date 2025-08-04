
numero_secreto = 4


tentativas_max = 3
tentativas = 0

print("Tente adivinhar o número entre 1 e 10. Você tem 3 tentativas.")

while tentativas < tentativas_max:
    palpite = int(input(f"Tentativa {tentativas + 1}: Qual é o seu palpite? "))
    tentativas += 1

    if palpite == numero_secreto:
        print("Parabéns! Você acertou o número!")
        break
else:
    print(f"Que pena! Você não acertou. O número era {numero_secreto}.")
