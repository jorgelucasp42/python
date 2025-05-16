
# PARTE 2 - NumPy Intermediário

import numpy as np

def numeros_primos_ate_50():
    def eh_primo(n):
        if n < 2:
            return False
        for i in range(2, int(n**0.5) + 1):
            if n % i == 0:
                return False
        return True
    array = np.arange(1, 51)
    primos = array[[eh_primo(n) for n in array]]
    return primos

def matriz_distancias_euclidianas():
    pontos = np.arange(5)
    matriz = np.abs(pontos[:, None] - pontos[None, :])
    return matriz.astype(float)

def centralizar_dados_temperatura():
    array = np.random.rand(12) * 30  # Exemplo: temperaturas entre 0 e 30
    media = array.mean()
    centralizado = array - media
    return array, centralizado

def comparar_arrays_aleatorios():
    a = np.random.randint(0, 10, (1, 10))
    b = np.random.randint(0, 10, (1, 10))
    comparacao = a > b
    return a, b, comparacao, np.sum(comparacao)

