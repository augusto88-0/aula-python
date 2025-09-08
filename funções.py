# Desafio 7: Funções
# Objetivo: criar e usar uma função

def calcular_media(notas):
    return sum(notas) / len(notas)

notas = [7.5, 8.0, 9.0]
print("Notas:", notas)
print("Média:", calcular_media(notas))
