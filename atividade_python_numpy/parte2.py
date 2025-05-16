
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
    # Temperaturas entre 15°C e 35°C
    array = np.random.uniform(15, 35, size=12)
    media = array.mean()
    centralizado = array - media
    
    # Exibição formatada
    print("Temperaturas originais (°C):")
    print(np.round(array, 2))
    print("\nTemperaturas centralizadas (°C):")
    print(np.round(centralizado, 2))

    return array, centralizado

def comparar_arrays_aleatorios():
    a = np.random.randint(0, 10, (1, 10))
    b = np.random.randint(0, 10, (1, 10))
    comparacao = a > b
    return a, b, comparacao, np.sum(comparacao)

