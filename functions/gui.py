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
            [sg.Button('Gerar'), sg.Button('Sair')]
        ]
        sg.theme('DarkTeal7')
        self.janela = sg.Window('Chave Pública', layout)
 
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
                if ehPrimo(p) and ehPrimo(q) and math.gcd(e, totienteEuler(p, q)) == 1:
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
            [sg.Text('Insira a mensagem:')],
            [sg.Input(key = 'msg')],
            [sg.Text('Insira N:', size = (6, 0)), sg.Input(key = 'n', size = (25, 0))],
            [sg.Text('Insira E:', size = (6, 0)), sg.Input(key = 'e', size = (25, 0))],
            [sg.Button('Encriptar'), sg.Button('Sair')],
        ]
        sg.theme('DarkTeal7')
        self.janela = sg.Window('Encriptar', layout)
 
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
                try:
                    with open('chaves_publicas.txt', 'r') as file:
                        encriptar(valores['msg'].lower(), n, e)
                    print('Encriptado')
                    sg.popup('Mensagem encriptada')
                    self.janela.close()
                    break

                except Exception as ee:
                    print(ee)
                    sg.popup('Você ainda não definiu as chaves públicas!')
                    print('Chaves inexistentes')
                    self.janela.close()
                    break
 
class Decript:
    def __init__(self):
        layout = [
            [sg.Text('Insira P:', size = (6, 0)), sg.Input(key = 'p', size = (25, 0))],
            [sg.Text('Insira Q:', size = (6, 0)), sg.Input(key = 'q', size = (25, 0))],
            [sg.Text('Insira E:', size = (6, 0)), sg.Input(key = 'e', size = (25, 0))],
            [sg.Button('Desencriptar'), sg.Button('Sair')]
        ]
        sg.theme('DarkTeal7')
        self.janela = sg.Window('Desencriptar', layout)

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