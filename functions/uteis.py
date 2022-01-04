from functions.number_theory import *
import math
import os

def toTable(texto: str) -> list:
    converter = lambda x: ord(x) - ord('a') + 2 if x != ' ' else 28
    vetor = list(map(converter, texto))
    return vetor

def char(x):
    try:
        return chr(x - 2 + ord('a'))
    except:
        return '#'

def toText(vetor: list) -> str:
    converter = lambda x: char(x - 2 + ord('a')) if x != 28 else ' '
    s = ''.join(map(converter, vetor))
    return s

def checarMensagem(msg: str):
    possivels = set(range(2, 29))
    for caractere in toTable(msg):
        if caractere not in possivels:
            return False
