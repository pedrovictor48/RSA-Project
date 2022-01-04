from functions.number_theory import *
from functions.uteis import *

def encriptar(msg: str, n: int, e: int):
    tabela = toTable(msg)
    M = lambda m: pow(m, e, n)
    tabelaEncriptada = list(map(M, tabela))
    textoEncriptado = " ".join(map(str, tabelaEncriptada))
    with open("mensagem_encriptada.txt", "w") as file:
        file.write(textoEncriptado)

def desencriptar(p: int, q: int, e: int):
    #calculando d:
    tot = totienteEuler(p, q)
    d = inversoModulo(e, tot)
    n = p * q
    m = lambda M: pow(M, d, n)
    textoEncriptado = str()
    with open("mensagem_encriptada.txt", "r") as file:
        textoEncriptado = file.read()
    tabelaEncriptada = list(map(int, textoEncriptado.split(' ')))
    tabelaDesencriptada = list(map(m, tabelaEncriptada))
    textoDesencriptado = toText(tabelaDesencriptada)
    with open("mensagem_desencriptada.txt", "w") as file:
        file.write(textoDesencriptado)
    
    return textoDesencriptado
