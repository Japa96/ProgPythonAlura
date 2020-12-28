#Importação da biblioteca Random
import random

print("*********************************")
print("Bem vindo ao jogo de Adivinhação!")
print("*********************************")

# Gerando um número inteiro de 0 a 99
numero_secreto = random.randrange(100)

total_de_tentativas = 3

for rodada in range(1, total_de_tentativas + 1):

    print("Tentativa {} de {}".format(rodada, total_de_tentativas))

    # Usuário vai inputar o número que ele acredita que seja o número secreto!
    chute_str = input("Digite um número entre 1 e 100: ")
    chute = int(chute_str)

    if (chute >= 1 and chute <= 100):

        # Aqui o sistema vai ter as condições de comparação!
        acertou = int(chute) == numero_secreto
        maior = int(chute) > numero_secreto
        menor = int(chute) < numero_secreto

        if (acertou):
            print("\nVocê acertou o número secreto.")
            break
        else:
            if(maior):
                print("Você errou o número secreto. O seu chute foi maior que o número secreto.\n")
            elif(menor):
                print("Você errou o número secreto. O seu chute foi menor que o número secreto.\n")

    else:
        print("\nDigite um número entre 1 e 100!\n")
        continue

print("Fim do jogo! O número secreto é {}".format(numero_secreto))