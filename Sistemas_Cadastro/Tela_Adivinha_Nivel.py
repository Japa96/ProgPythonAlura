import PySimpleGUI as sg

class Tela_Dificuldade:
    def __init__(self):
        #Layout
        layout = (
            [sg.Text('Dificuldade:', size=(10,0)), sg.Input(size=(20,0))],
            [sg.Text('Fácil (1), Médio (2), Difícil (3)')],
            [sg.Button('Enviar dificuldade')]
        )

        #Janela
        janela = sg.Window('Dados do Jogo').layout(layout)

        #Extrair os dados da tela
        self.Button, self.values = janela.Read()

    def Iniciar(self):
        print(self.values)

tela = Tela_Dificuldade()
tela.Iniciar()