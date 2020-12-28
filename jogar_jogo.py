import adivinhacao

print("*********************************")
print("*Bem vindo - Escolha o seu jogo!*")
print("*********************************")

print("Informe o jogo que deseja: ")
jogo =int(input("Adivinhação (1): "))

if (jogo == 1):
    adivinhacao.jogar()
else:
    print("Jogo informado inesxistente!")