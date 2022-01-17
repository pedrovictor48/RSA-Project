def ehPrimo(n: int) -> bool:
    i = 2
    while i * i <= n:
        if n % i == 0:
            return False
        i += 1
    return True

def mdcDiofantino(a: int, b: int):
    if b == 0:
        return a, 1, 0
    mdc, s1, t1 = mdcDiofantino(b, a % b)
    s, t = t1, s1 - t1 * (a // b)
    return mdc, s, t

def inversoModulo(a: int, b: int):
    a %= b
    mdc, s, t = mdcDiofantino(a, b)
    if mdc != 1:
        return 0
    s %= b
    return s

def totienteEuler(p: int, q: int):
    return (p - 1) * (q - 1)