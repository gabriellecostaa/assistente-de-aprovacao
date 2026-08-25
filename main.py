print("================================")
print("   ASSISTENTE DE APROVAÇÃO")
print("================================")

nome = input("Digite o nome do aluno: ")

nota1 = float(input("Digite a primeira nota: "))
nota2 = float(input("Digite a segunda nota: "))
nota3 = float(input("Digite a terceira nota: "))
nota4 = float(input("Digite a quarta nota: "))

media = (nota1 + nota2 + nota3 + nota4) / 4

print("\nAluno:", nome)
print("Média:", media)

if media >= 7:
    print("Situação: APROVADO ✅")
elif media >= 5:
    print("Situação: RECUPERAÇÃO ⚠️")
else:
    print("Situação: REPROVADO ❌")
