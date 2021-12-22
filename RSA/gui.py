import PySimpleGUI as sg
import funcoes as f

class ChavePub:
    def __init__(self):
        layout = [
            [sg.Text('Insira P:', size = (6, 0)), sg.Input(key = 'p', size = (25, 0))],
            [sg.Text('Insira Q:', size = (6, 0)), sg.Input(key = 'q', size = (25, 0))],
            [sg.Text('Insira E:', size = (6, 0)), sg.Input(key = 'e', size = (25, 0))],
            [sg.Button('Gerar'), sg.Button('Sair')]
        ]
        sg.theme('DarkTeal7')
        self.janela = sg.Window('Chave Pública', layout)

    def Run(self):
        while True:
            self.eventos, self.valores = self.janela.read()
            if self.eventos == sg.WINDOW_CLOSED or self.eventos == 'Sair':
                self.janela.close()
                break
            if self.eventos == 'Gerar':
                if not self.valores['p'].isdigit() or not self.valores['q'].isdigit() or not self.valores['e'].isdigit():
                    sg.popup_error('Input inválido! Tente novamente.')
                    print('Input errado')
                elif f.eh_primo(int(self.valores['p'])) and f.eh_primo(int(self.valores['q'])):
                    n = int(self.valores['p'])*int(self.valores['q'])
                    e = int(self.valores['e'])
                    with open('chaves_publicas.txt', 'w') as file:
                        file.write(str(n) + '\n')
                        file.write(str(e) + '\n')
                    sg.popup('Chave gerada com sucesso!')
                    print('Chave gerada')
                else:
                    sg.popup_error('Número(s) inválido(s)!')
                    print('Numeros invalidos')

class Encript:
    def __init__(self):
        layout = [
            [sg.Text('Insira a mensagem:')],
            [sg.Input(key = 'msg')],
            [sg.Button('Encriptar'), sg.Button('Sair')]
        ]
        sg.theme('DarkTeal7')
        self.janela = sg.Window('Encriptar', layout)

    def Run(self):
        while True:
            self.eventos, self.valores = self.janela.read()
            if self.eventos == sg.WINDOW_CLOSED or self.eventos == 'Sair':
                self.janela.close()
                break
            if self.eventos == 'Encriptar':
                try:
                    with open('chaves_publicas.txt', 'r') as file:
                        n = int(file.readline())
                        e = int(file.readline())
                        print(n)
                        print(e)
                        #CONTINUACAO...
                except:
                    sg.popup('Você ainda não definiu as chaves públicas!')
                    print('Chaves inexistentes')
                    self.janela.close()
                    break

class Hub:
    def __init__(self):
        layout = [
            [sg.Text('O que deseja fazer?')],
            [sg.Button('Gerar Chave Pública')],
            [sg.Button('Encriptar')],
            [sg.Button('Desencriptar')],
            [sg.Button('Sair')]
        ]
        sg.theme('DarkTeal7')
        self.janela = sg.Window('Criptografia RSA', layout, element_justification = 'c', size = (300, 160))

    def Run(self):
        while True:
            self.eventos, self.valores = self.janela.read()
            if self.eventos == sg.WINDOW_CLOSED or self.eventos == 'Sair':
                self.janela.close()
                break
            if self.eventos == 'Gerar Chave Pública':
                geracao_chave = ChavePub()
                geracao_chave.Run()
            if self.eventos == 'Encriptar':
                encriptar = Encript()
                encriptar.Run()
