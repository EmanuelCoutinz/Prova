
usuario_correto = "admin"
senha_correta = "1234"

tentativas_max = 3
tentativas = 0

while tentativas < tentativas_max:
    usuario = input("Digite o nome de usuário: ")
    senha = input("Digite a senha: ")
    tentativas += 1

    if usuario == usuario_correto and senha == senha_correta:
        print("Bem-vindo! Login efetuado com sucesso.")
        break
    else:
        tentativas_restantes = tentativas_max - tentativas
        if tentativas_restantes > 0:
            print(f"Credenciais incorretas. Você tem {tentativas_restantes} tentativas restantes.")
        else:
           
            for _ in range(1):
                print("Acesso bloqueado.")
