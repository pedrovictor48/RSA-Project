def ehPrimo(n: int) -> bool:
    i = 2
    while i * i <= n:
        if n % i == 0:
            return False
        i += 1
    return True

def mdcDiofantino(a: int, b:int):
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

def solucaoCongruencia(a: int, b: int, m: int):
    a %= m
    b %= m
    if a == 0 and b == 0:
        return 0
    mdc_am, s, t = mdcDiofantino(a, m)
    if b % mdc_am != 0:
        return -1
    inverso_a = inversoModulo(a/mdc_am, m/mdc_am)
    if inverso_a == 0:
        return -1
    solucao = (inverso_a * (b/mdc_am)) % m
    return solucao

def totienteEuler(p: int, q: int):
    return (p - 1) * (q - 1)
