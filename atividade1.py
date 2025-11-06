# 1. Pergunte o nome e guarde na variável 'nome'
nome = input("Qual é o seu nome? ")

# 2. Pergunte a idade e guarde na variável 'idade_texto'
idade_texto = input("Qual é a sua idade? ")

# 3. Converta a idade de texto para número
idade_numero = int(idade_texto)

# 4. Crie a lógica condicional
if idade_numero >= 18:
    # Mensagem para maior de idade
    print(f"Olá, {nome}, você é maior de idade.")
else:
    # Mensagem para menor de idade
    print(f"Olá, {nome}, você é menor de idade.")
 