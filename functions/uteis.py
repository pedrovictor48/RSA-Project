def toTable(texto: str) -> list:
    converter = lambda x: ord(x) - ord('a') + 2 if x != ' ' else 28
    vetor = list(map(converter, texto))
    return vetor

def toText(vetor: list) -> str:
    converter = lambda x: chr(x - 2 + ord('a')) if x != 28 else ' '
    s = ''.join(map(converter, vetor))
    return s
