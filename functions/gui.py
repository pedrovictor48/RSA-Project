import PySimpleGUI as sg
from functions.uteis import *
from functions.number_theory import *
from functions.criptografia import *
import math


class ChavePub:
    def __init__(self):
        layout = [
            [sg.Text('Insira P:', size = (6, 0)), sg.Input(key = 'p', size = (25, 0))],
            [sg.Text('Insira Q:', size = (6, 0)), sg.Input(key = 'q', size = (25, 0))],
            [sg.Text('Insira E:', size = (6, 0)), sg.Input(key = 'e', size = (25, 0))],
            [sg.Checkbox('Verificar a validade dos números', default=True, key='testar')],
            [sg.Button('Gerar'), sg.Button('Sair')]
        ]
        self.janela = sg.Window(
            'Chave Pública',
            layout=layout,
            element_justification='c',
            background_color='#2C2C3C',
            )
 
    def Run(self):
        while True:
            eventos, valores = self.janela.read()
            if eventos == sg.WINDOW_CLOSED or eventos == 'Sair':
                self.janela.close()
                break
            if eventos == 'Gerar':
                if not valores['p'].isdigit() or not valores['q'].isdigit() or not valores['e'].isdigit():
                    sg.popup_error('Input inválido! Tente novamente.')
                    print('Input errado')
                    continue
                p, q, e = int(valores['p']), int(valores['q']), int(valores['e'])
                querChecar = valores['testar'] #log(min(e, tot(p, q))
                if not querChecar or (ehPrimo(p) and ehPrimo(q) and math.gcd(e, totienteEuler(p, q))) == 1:
                    n = p * q
                    if n <= 27:
                        sg.popup_error('N muito pequeno, tente um valor maior que tal que p*q > 27')
                        print('N muito pequeno')
                        continue
                    with open('chaves_publicas.txt', 'w') as file:
                        file.write(str(n) + '\n')
                        file.write(str(e) + '\n')
                    sg.popup('Chave gerada com sucesso!')
                    print('Chave gerada')
                    self.janela.close()
                    break
                else:
                    sg.popup_error('Número(s) inválido(s)!')
                    print('Numeros invalidos')

class Encript:
    def __init__(self):
        layout = [
            [sg.Text('Insira a mensagem:', background_color='#2C2C3C', font=('Bebas', 20), pad=10)],
            [sg.Multiline(key = 'msg', size=(32, 10))],
            [sg.Text('Insira N:', size = (6, 0)), sg.Input(key = 'n', size = (25, 0))],
            [sg.Text('Insira E:', size = (6, 0)), sg.Input(key = 'e', size = (25, 0))],
            [sg.Button('Encriptar'), sg.Button('Sair')],
        ]
        self.janela = sg.Window(
            'Encriptar',
            layout=layout,
            background_color='#2C2C3C',
            element_justification='c',
            )
 
    def Run(self):
        while True:
            eventos, valores = self.janela.read()
            if eventos == sg.WINDOW_CLOSED or eventos == 'Sair':
                self.janela.close()
                break

            if not checarMensagem(valores['msg'].lower()):
                sg.popup_error('Caracteres inválidos')
                print('Caracteres inválidos')
                continue

            if not valores['n'].isdigit() or not valores['e'].isdigit():
                sg.popup_error('Número(s) inválido(s)!')
                print('Numeros invalidos')
                continue
            n, e = int(valores['n']), int(valores['e'])
            if eventos == 'Encriptar':
                encriptar(valores['msg'].lower(), n, e)
                print('Encriptado')
                sg.popup('Mensagem encriptada')
                self.janela.close()
                break
 
class Decript:
    def __init__(self):
        layout = [
            [sg.Text('DESENCRIPTAR', background_color='#2C2C3C', font=('Bebas', 20), pad=10)],
            [sg.Text('Insira P:', size = (6, 0)), sg.Input(key = 'p', size = (30, 20))],
            [sg.Text('Insira Q:', size = (6, 0)), sg.Input(key = 'q', size = (30, 3))],
            [sg.Text('Insira E:', size = (6, 0)), sg.Input(key = 'e', size = (30, 3))],
            [sg.Button('Desencriptar'), sg.Button('Sair')]
        ]
        self.janela = sg.Window(
            'Desencriptar',
            layout=layout,
            background_color='#2C2C3C',
            element_justification='c'
            )

    def Run(self):
        while True:
            eventos, valores = self.janela.read()
            if eventos == sg.WINDOW_CLOSED or eventos == 'Sair':
                self.janela.close()
                break
            if not valores['p'].isdigit() or not valores['q'].isdigit() or not valores['e'].isdigit():
                sg.popup_error('Número(s) inválido(s)!')
                print('Numeros invalidos')
                continue
            
            p, q, e = int(valores['p']), int(valores['q']), int(valores['e'])

            if eventos == 'Desencriptar':
                if math.gcd(totienteEuler(p, q), e) != 1:
                    sg.popup_error('E precisa ser coprimo de (p - 1) * (q - 1)')
                    print("E não coprimo")
                    continue

                textoDesencriptado = desencriptar(p, q, e)
                sg.popup('Mensagem desencriptada:\n' + textoDesencriptado)
                self.janela.close()
                break


class Hub:
    def __init__(self):
        layout = [
            [sg.Button('Gerar Chave Pública', button_color='#0BA484', size=(25, 2), font=('Bebas', 20), pad=10)],
            [sg.Button('Encriptar', button_color='#0BA484', size=(25, 2), font=('Bebas', 20), pad=10)],
            [sg.Button('Desencriptar', button_color='#0BA484', size=(25, 2), font=('Bebas', 20), pad=10)],
            [sg.Button('Sair', button_color='#565656', size=(25, 2), font=('Bebas', 20), pad=10)],
        ]
        self.janela = sg.Window(
            'Criptografia RSA',
            layout=layout,
            background_color='#2C2C3C',
            size = (500, 500),
            element_justification='c',
            )
 
    def Run(self):
        while True:
            eventos, valores = self.janela.read()
            if eventos == sg.WINDOW_CLOSED or eventos == 'Sair':
                self.janela.close()
                break
            if eventos == 'Gerar Chave Pública':
                geracao_chave = ChavePub()
                geracao_chave.Run()
            if eventos == 'Encriptar':
                janelaEncriptar = Encript()
                janelaEncriptar.Run()
            if eventos == 'Desencriptar':
                janelaDesencriptar = Decript()
                janelaDesencriptar.Run()
