#calc
numero1 = int(input("Digite o primeiro numero: "))
numero2 = int(input("Digite o segundo numero: "))
operador = input("Digite a operacao (+, -, *, /): ")
if operador == '+':
    resultado = numero1 + numero2
elif operador == '-':
    resultado = numero1 - numero2
elif operador == '*':
    resultado = numero1 * numero2
elif operador == '/':
    if numero2 != 0:
        resultado = numero1 / numero2
    else:
        resultado = "Erro: Divisao por zero"
print("O resultado da operaçao e:", resultado)
#fim do programa
