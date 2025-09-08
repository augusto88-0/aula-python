# Desafio 10: Projeto Final
# Objetivo: criar uma calculadora simples

def soma(a, b):
    return a + b

def subtracao(a, b):
    return a - b

def multiplicacao(a, b):
    return a * b

def divisao(a, b):
    if b != 0:
        return a / b
    else:
        return "Erro! Divisão por zero."

print("=== Calculadora Simples ===")
x = float(input("Digite o primeiro número: "))
y = float(input("Digite o segundo número: "))

print("Soma:", soma(x, y))
print("Subtração:", subtracao(x, y))
print("Multiplicação:", multiplicacao(x, y))
print("Divisão:", divisao(x, y))
