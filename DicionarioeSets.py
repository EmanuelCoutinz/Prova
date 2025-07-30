#DICIONARIO E SETS

contato = {
    "nome": "",
    "telefone": "",
    "email": ""
}

contato["nome"] = input("Digite o nome do contato: ")
contato["telefone"] = input("Digite o telefone do contato: ")
contato["email"] = input("Digite o email do contato: ")

print(f"Nome: {contato['nome']}")
print(f"Telefone: {contato['telefone']}")
print(f"Email: {contato['email']}")
