def calculadora(numero1, numero2, operacao):
    if operacao == '1':
        return numero1 + numero2
    elif operacao == '2':
        return numero1 - numero2
    elif operacao == '3':
        return numero1 * numero2
    elif operacao == '4':
            return numero1 / numero2
    else:
        return "Operação inválida!"

# Pedir para o usuário digitar
n1 = float(input("Digite o primeiro número: "))
n2 = float(input("Digite o segundo número: "))

# Menu de operações
print("Escolha a operação\n"
      "1 - Somar\n"
      "2 - Subtrair\n"
      "3 - Multiplicar\n"
      "4 - Dividir")
op = input("Digite a opção: ")

print("Resultado: ", calculadora(n1, n2, op))
