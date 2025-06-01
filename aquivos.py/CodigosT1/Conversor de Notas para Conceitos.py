nota = int(input("Digite a nota do aluno:"))
# coinceitos de a, b, c, d
# Conversor de Notas para Conceitos
if nota >= 9 and nota <= 10:
    conceito = "A"
elif nota >= 7 and nota < 9:
    conceito = "B"
elif nota >= 5 and nota < 7:
    conceito = "C"
elif nota >= 0 and nota < 5:
    conceito = "D"
print("A nota do aluno e:", nota)
print("O conceito do aluno e:", conceito)
# Fim do programa