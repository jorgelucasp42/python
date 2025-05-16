# PARTE 1 - Python Básico

def conta_vogais(texto):
    vogais = 'aeiouAEIOU'
    return sum(1 for char in texto if char in vogais)

def flatten(lista):
    resultado = []
    for item in lista:
        if isinstance(item, list):
            resultado.extend(flatten(item))
        else:
            resultado.append(item)
    return resultado

def ordenar_por_soma(lista_de_listas):
    return sorted(lista_de_listas, key=sum)

def valida_cpf(cpf):
    import re
    return bool(re.fullmatch(r'\d{3}\.\d{3}\.\d{3}-\d{2}', cpf))

