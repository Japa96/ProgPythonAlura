def jogar():

    print("*********************************")
    print("Bem vindo ao jogo de Adivinhação!")
    print("*********************************\n")

    palavra_secreta = "ler".upper()

    # Esse recurso abaixo se chama List Comprehension
    letras_acertadas = ["_" for letra in palavra_secreta]

    enforcou = False
    acertou = False
    erros = 0

    print(letras_acertadas)

    # Enquanto não enforcou e não acertou, fica no loop game.
    while(not enforcou and not acertou):

        chute = input('Qual a letra? ')

        # A função strip vai remover qualquer espaço em branco.
        chute = chute.strip().upper()

        if(chute in palavra_secreta):
            index = 0
            for letra in palavra_secreta:
                if (chute == letra):

                    # Abaixo estamos acessando a letra informando pelo Index da posição da lista.
                    letras_acertadas[index] = letra
                index += 1


        else:
            erros +=1
            print("Ops, você errou a letra! Faltam {} tentativas.".format(6-erros))

        enforcou = erros == 6
        acertou = "_" not in letras_acertadas
        print(letras_acertadas)

    if(acertou):
        print("Parabéns! Você acertou a palavra secreta.")

    else:
        print("Que pena, você não acertou a palavra. Continue jogando :)")

if(__name__ == "__main__"):
    jogar()