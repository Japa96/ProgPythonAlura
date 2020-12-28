#Importação da biblioteca Random
import random

def jogar():

    print("*********************************")
    print("Bem vindo ao jogo de Adivinhação!")
    print("*********************************")

    # Gerando um número inteiro de 0 a 99
    numero_secreto = random.randrange(1,101)
    total_de_tentativas = 0
    pontuacao = 1000

    print("Qual o níve de dificuldade do jogo?\n")
    print("Fácil (1)")
    print("Médio (2)")
    print("Difícil (3)")

    nivel = int(input("\nInforme o nível do jogo: "))

    if (nivel == 1):
        total_de_tentativas = 20
    elif (nivel == 2):
        total_de_tentativas = 10
    else:
        total_de_tentativas = 5

    for rodada in range(1, total_de_tentativas + 1):

        print("Tentativa {} de {}".format(rodada, total_de_tentativas))
        print("Sua pontuacação é de {}".format(pontuacao))

        # Usuário vai inputar o número que ele acredita que seja o número secreto!
        chute_str = input("Digite um número entre 1 e 100: ")
        chute = int(chute_str)

        if (chute >= 1 and chute <= 100):

            # Aqui o sistema vai ter as condições de comparação!
            acertou = int(chute) == numero_secreto
            maior = int(chute) > numero_secreto
            menor = int(chute) < numero_secreto

            if (acertou):
                print("\nVocê acertou o número secreto!.")
                break
            else:
                if(maior):
                    print("Você errou o número secreto. O seu chute foi maior que o número secreto.\n")
                elif(menor):
                    print("Você errou o número secreto. O seu chute foi menor que o número secreto.\n")

                # Calculo de perda de pontos.
                # Exemplo : Chute igual a 40 e o numero é 20, perde 20 pontos.
                # Usar a função abs() para pegar sopmente o número independente do sinal.
                pontos_perdidos = abs(numero_secreto - chute)
                pontos = pontuacao - pontos_perdidos

        else:
            print("\nDigite um número entre 1 e 100!\n")
            continue

    print("Fim do jogo! O número secreto é {}!".format(numero_secreto), "Sua pontuação final é de {}".format(pontos))

if (__name__ == "__main__"):
    jogar()