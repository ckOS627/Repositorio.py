# Exercício 2
largura = int(input("digite a largura: "))
altura = int(input("digite a altura: "))

for i in range(altura):          # percorre as linhas
    for j in range(largura):     # percorre as colunas
        # condição: borda do retângulo
        if i == 0 or i == altura - 1 or j == 0 or j == largura - 1:
            print("#", end="")
        else:
            print(" ", end="")   # espaço dentro do retângulo
    print()  # quebra de linha no fim de cada linha