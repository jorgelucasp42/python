
def menu_principal():
    print("\n===== MENU DE FUNÇÕES =====")
    print("1. Contar vogais")
    print("2. Flatten de lista aninhada")
    print("3. Ordenar por soma")
    print("4. Validar CPF")
    print("5. Números primos até 50")
    print("6. Matriz de distâncias euclidianas")
    print("7. Centralizar dados de temperatura")
    print("8. Comparar arrays aleatórios")
    print("9. Simular caminhada aleatória 2D")
    print("0. Sair")
    print("============================")

def main():
    from parte1 import conta_vogais, flatten, ordenar_por_soma, valida_cpf
    from parte2 import numeros_primos_ate_50, matriz_distancias_euclidianas, centralizar_dados_temperatura, comparar_arrays_aleatorios
    from parte3 import simular_random_walk_2d

    while True:
        menu_principal()
        escolha = input("Escolha uma opção: ")

        if escolha == "1":
            texto = input("Digite o texto: ")
            print("Número de vogais:", conta_vogais(texto))

        elif escolha == "2":
            lista = eval(input("Digite uma lista aninhada (ex: [1,[2,[3,4]],5]): "))
            print("Flatten:", flatten(lista))

        elif escolha == "3":
            listas = eval(input("Digite uma lista de listas (ex: [[0,1],[3,1],[1,1,1]]): "))
            print("Ordenadas por soma:", ordenar_por_soma(listas))

        elif escolha == "4":
            cpf = input("Digite o CPF (formato XXX.XXX.XXX-YY): ")
            print("CPF válido?" , valida_cpf(cpf))

        elif escolha == "5":
            print("Primos até 50:", numeros_primos_ate_50())

        elif escolha == "6":
            print("Matriz de distâncias:\n", matriz_distancias_euclidianas())

        elif escolha == "7":
            original, centralizado = centralizar_dados_temperatura()
            print("Original:", original)
            print("Centralizado:", centralizado)

        elif escolha == "8":
            a, b, comp, total = comparar_arrays_aleatorios()
            print("Array A:", a)
            print("Array B:", b)
            print("Comparação (A > B):", comp)
            print("Total de True:", total)

        elif escolha == "9":
            distancia = simular_random_walk_2d()
            print("Distância máxima da origem:", distancia)

        elif escolha == "0":
            print("Saindo do programa.")
            break

        else:
            print("Opção inválida. Tente novamente.")

if __name__ == "__main__":
    main()
