import math

def toTable(texto: str) -> list:
    converter = lambda x: ord(x) - ord('a') + 2 if x != ' ' else 28
    vetor = list(map(converter, texto))
    return vetor

def toText(vetor: list) -> str:
    converter = lambda x: chr(x - 2 + ord('a')) if x != 28 else ' '
    s = ''.join(map(converter, vetor))
    return s

def requisitarEscolha():
    print(bcolors.WARNING + "À qualquer momento, digite " + bcolors.FAIL + "'q'" + bcolors.WARNING + " para sair!\n" + bcolors.ENDC)
    print("Escolha uma opção:\n(1) Gerar chave pública\n(2) Encriptar\n(3) Desencriptar")
    opcao = input()
    while not opcao in set(['1', '2', '3', 'q']):
        print(bcolors.FAIL + "Entrada inválida!" + bcolors.ENDC)
        print("Escolha uma opção:\n(1) Gerar chave pública\n(2) Encriptar\n(3) Desencriptar")
        opcao = input()
    if opcao == 'q':
        exit()
    return int(opcao)

def requisitarInteiro():
    p = input()
    while(not p.isdigit()):
        if p == 'q':
            exit()
        print(bcolors.WARNING + "Entrada inválida!" + bcolors.ENDC)
        p = input()
    return int(p)

def gerarChavePublica():
    print(bcolors.OKGREEN + "Digite um número primo" + bcolors.BOLD + " p :" + bcolors.ENDC, end = " ")
    p = requisitarInteiro()
    print(bcolors.OKGREEN + "Digite um número primo" + bcolors.BOLD + " q :" + bcolors.ENDC, end = " ")
    q = requisitarInteiro()
    totiente = (p - 1) * (q - 1)
    print(bcolors.OKGREEN + f"Digite um relativamente primo à {totiente}" + bcolors.BOLD + " q :" + bcolors.ENDC, end = " ")
    e = requisitarInteiro()
    while(math.gcd(totiente, e) != 1):
        print(bcolors.WARNING + f"{e} não é coprimo de {totiente}!" + bcolors.ENDC)
        e = requisitarInteiro()

    print(f"n = {p*q}, e = {e}")

    arquivo = open("./chave_publica.txt", "w")
    arquivo.write(f"n = {p*q}, e = {e}")
    arquivo.close()

def printHead():
    print(
bcolors.WARNING + 
""" 
          _____                    _____                    _____          
         /\    \                  /\    \                  /\    \         
        /::\    \                /::\    \                /::\    \        
       /::::\    \              /::::\    \              /::::\    \       
      /::::::\    \            /::::::\    \            /::::::\    \      
     /:::/\:::\    \          /:::/\:::\    \          /:::/\:::\    \     
    /:::/__\:::\    \        /:::/__\:::\    \        /:::/__\:::\    \    
   /::::\   \:::\    \       \:::\   \:::\    \      /::::\   \:::\    \   
  /::::::\   \:::\    \    ___\:::\   \:::\    \    /::::::\   \:::\    \  
 /:::/\:::\   \:::\____\  /\   \:::\   \:::\    \  /:::/\:::\   \:::\    \ 
/:::/  \:::\   \:::|    |/::\   \:::\   \:::\____\/:::/  \:::\   \:::\____\ 
\::/   |::::\  /:::|____|\:::\   \:::\   \::/    /\::/    \:::\  /:::/    /
 \/____|:::::\/:::/    /  \:::\   \:::\   \/____/  \/____/ \:::\/:::/    / 
       |:::::::::/    /    \:::\   \:::\    \               \::::::/    /  
       |::|\::::/    /      \:::\   \:::\____\               \::::/    /   
       |::| \::/____/        \:::\  /:::/    /               /:::/    /    
       |::|  ~|               \:::\/:::/    /               /:::/    /     
       |::|   |                \::::::/    /               /:::/    /      
       \::|   |                 \::::/    /               /:::/    /       
        \:|   |                  \::/    /                \::/    /        
         \|___|                   \/____/                  \/____/         
"""
+ bcolors.ENDC
    )

    print(
        bcolors.HEADER + "Projeto de Criptografia RSA\n" + 
        bcolors.OKBLUE + "GRUPO:\n" + bcolors.ENDC +
        " * Daniel Sival\n * Eduardo Melo\n * Pedro Ferreira\n * Vinícius Teixeira\n" +
        bcolors.OKBLUE + "PROFESSOR:\n" + bcolors.ENDC +
        " * Bruno Almeida Pimentel\n"
    )

class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKCYAN = '\033[96m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'
