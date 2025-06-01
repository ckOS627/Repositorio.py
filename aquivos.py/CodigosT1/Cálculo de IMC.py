#calc
import math
# Cálculo do IMC
peso = int(input("Digite o seu peso (em kg): "))
altura = float(input("digite a sua altura (em metros):"))
peso * altura ** 2
imc = peso / altura ** 2
print("O seu imc e:", imc)
if imc < 18.5:
    print("Você está abaixo do peso")
elif imc >= 18.5 and imc < 24.9:
    print("Você está com peso normal")
elif imc >= 25 and imc < 29.9:
    print("Você está com sobrepeso")
elif imc >= 30 and imc < 34.9:
    print("Você está com obesidade")
#Fim do programa