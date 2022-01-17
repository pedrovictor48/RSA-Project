from functions.number_theory import *

def toTable(texto: str) -> list:
    converter = lambda x: ord(x) - ord('a') + 2 if x != ' ' else 28
    vetor = list(map(converter, texto))
    return vetor

def toText(vetor: list) -> str:
    converter = lambda x: chr((x - 2 + ord('a')) % 0x10FFFF) if x != 28 else ' '
    s = ''.join(map(converter, vetor))
    return s

def checarMensagem(msg: str):
    possiveis = set(range(2, 29))
    for caractere in toTable(msg):
        if caractere not in possiveis:
            return False
    return True