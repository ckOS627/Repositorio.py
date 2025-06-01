idade = int(input("Digite a sua idade: "))
if idade < 18:
    desconto = 10.0
elif idade > 60:
    desconto = 5.0
else: 
    desconto = 0.0
print(f"O desconto por idade é de {desconto}% para a idade de {idade} anos.")
# Fim do programa