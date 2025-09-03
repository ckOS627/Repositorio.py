# Exercício 1
largura = int(input("digite a largura: "))
altura = int(input("digite a altura: "))

for i in range(altura):          # controla as linhas
    for j in range(largura):     # controla as colunas
        print("#", end="")       # imprime sem pular linha
    print()  # quebra de linha no fim de cada linha