print("================================")
print("   ASSISTENTE DE APROVAÇÃO")
print("================================")


def pedir_nota(numero):
    while True:
        try:
            nota = float(input(f"Digite a {numero}ª nota (0 a 10): "))

            if 0 <= nota <= 10:
                return nota

            print("❌ Nota inválida! Digite um valor entre 0 e 10.")

        except ValueError:
            print("❌ Digite apenas números.")


def calcular_situacao():
    nome = input("\nDigite o nome do aluno: ")

    nota1 = pedir_nota(1)
    nota2 = pedir_nota(2)
    nota3 = pedir_nota(3)
    nota4 = pedir_nota(4)

    media = (nota1 + nota2 + nota3 + nota4) / 4

    print("\n================================")
    print("Aluno:", nome)
    print("Média:", round(media, 2))

    if media >= 7:
        print("Situação: APROVADO ✅")
    elif media >= 5:
        print("Situação: RECUPERAÇÃO ⚠️")
    else:
        print("Situação: REPROVADO ❌")

    print("================================")


while True:
    print("\n1 - Calcular situação de um aluno")
    print("2 - Sair")

    opcao = input("\nEscolha uma opção: ")

    if opcao == "1":
        calcular_situacao()

    elif opcao == "2":
        print("\nAté logo! 👋")
        break

    else:
        print("\n❌ Opção inválida. Escolha 1 ou 2.")
