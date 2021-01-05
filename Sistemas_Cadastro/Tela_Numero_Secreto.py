import PySimpleGUI as sg

class Tela_Numero:
    def __init__(self):
        #Layout
        layout = (
            
            [sg.Text('Numero secreto'), sg.Input()],
            [sg.Button('Enviar dados')]
        )

        #Janela
        janela = sg.Window('Dados do Jogo').layout(layout)

        #Extrair os dados da tela
        self.Button, self.values = janela.Read()

    def Iniciar(self):
        print(self.values)

tela = Tela_Numero()
tela.Iniciar()