def jogar():

    print("*********************************")
    print("Bem vindo ao jogo de Adivinhação!")
    print("*********************************")

    palavra_secreta = "python"
    letras_acertadas = ["_","_","_","_","_","_"]

    enforcou = False
    acertou = False

    print(letras_acertadas)

    # Enquanto não enforcou e não acertou, fica no loop game.
    while(not enforcou and not acertou):

        chute = input('Qual a letra? ')
        # A função strip vai remover qualquer espaço em branco.
        chute = chute.strip()

        index = 0
        for letra in palavra_secreta:
            if (chute.upper() == letra.upper()):
                letras_acertadas[index] = letra
            index = index + 1

        print(letras_acertadas)

    print("Fim do jogo")

if(__name__ == "__main__"):
    jogar()