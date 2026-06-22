def somar(a: float, b: float) -> float:
    return a + b


def subtrair(a: float, b: float) -> float:
    return a - b


def multiplicar(a: float, b: float) -> float:
    return a * b


def dividir(a: float, b: float) -> float:
    if b == 0:
        raise ValueError("Não é possível dividir por zero")
    return a / b


def potencia(base: float, expoente: int) -> float:
    return base ** expoente


def eh_par(numero: int) -> bool:
    return numero % 2 == 0
