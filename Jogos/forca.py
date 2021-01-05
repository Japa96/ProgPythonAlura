def jogar():

    print("*********************************")
    print("Bem vindo ao jogo de Adivinhação!")
    print("*********************************")

    palavra_secreta = "python"

    enforcou = False
    acertou = False

    # Enquanto não enforcou e não acertou, fica no loop game.
    while(not enforcou and not acertou):

        chute = input('Qual a letra? ')
        chute = chute.strip()

        index = 0
        for letra in palavra_secreta:
            if (chute.upper() == letra.upper()):
                print("Encontrei a letra {} na posição {}".format(letra, index))
            index = index + 1

    print("Fim do jogo")

if(__name__ == "__main__"):
    jogar()