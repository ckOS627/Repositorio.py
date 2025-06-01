#Veficador de lados de um triangulo
lado1 = int(input("Digite uma das areas do triangulo:"))
lado2 = int(input("Digite uma das areas do triangulo:"))
lado3 = int(input("Digite uma das areas do triangulo:"))
soma = lado1 + lado2 + lado3
if lado1 < lado2 + lado3 and lado2 < lado1 + lado3 and lado3 < lado1 + lado2:
    print ("Os lados formam um triangulo")
else:
    print ("Os lados nao formam um triangulo")
# Fim do programa