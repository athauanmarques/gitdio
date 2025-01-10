num1 = int(input("Digite o primeiro número: "))
num2 = int(input("Digite o segundo número: "))
operacao = input("Digite a operação (+, -, *, /): ")

if operacao == "+":
    print(f"Resultado: {num1 + num2}")
elif operacao == "-":
    print(f"Resultado: {num1 - num2}")
elif operacao == "*":
    print(f"Resultado: {num1 * num2}")
elif operacao == "/":
    print(f"Resultado: {num1 / num2}")
else:
    print("Operação inválida")