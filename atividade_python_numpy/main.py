from parte1 import conta_vogais, flatten, ordenar_por_soma, valida_cpf
from parte2 import numeros_primos_ate_50, matriz_distancias_euclidianas, centralizar_dados_temperatura, comparar_arrays_aleatorios
from parte3 import simular_random_walk_2d

def main():
    print("=== Parte 1 ===")
    print("Vogais:", conta_vogais("Exemplo de Texto"))
    print("Flatten:", flatten([1, [2, [3, 4], 5], 6]))
    print("Ordenação:", ordenar_por_soma([[0,1,0],[1,2,-3],[1,2]]))
    print("CPF válido?", valida_cpf("123.456.789-00"))

    print("\n=== Parte 2 ===")
    print("Primos até 50:", numeros_primos_ate_50())
    print("Matriz de Distâncias:\n", matriz_distancias_euclidianas())
    array = centralizar_dados_temperatura()
    print("Array Centralizado:", array)
    print("Comparação de Arrays:", comparar_arrays_aleatorios())

    print("\n=== Parte 3 ===")
    distancia_max = simular_random_walk_2d()
    print("Distância máxima na Random Walk:", distancia_max)

if __name__ == "__main__":
    main()
