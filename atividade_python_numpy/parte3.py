
# PARTE 3 - Caminhada Aleatória 2D
import numpy as np

def simular_random_walk_2d(n_passos=1000):
    passos_x = np.random.choice([-1, 1], size=n_passos)
    passos_y = np.random.choice([-1, 1], size=n_passos)
    posicoes_x = np.cumsum(passos_x)
    posicoes_y = np.cumsum(passos_y)
    posicoes = np.column_stack((posicoes_x, posicoes_y))
    distancias = np.sqrt(posicoes[:, 0]**2 + posicoes[:, 1]**2)
    return np.max(distancias)
