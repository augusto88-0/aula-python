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
op = input('escolha uma operação (+, -, *, /): ')

if op == '+':
    print(f'O resultado é: {soma(x, y)}')
elif op == '-':
    print(f'O resultado é: {subtracao(x, y)}')
elif op == '*':
    print(f'O resultado é: {multiplicacao(x, y)}')
elif op == '/':
    print(f'O resultado é: {divisao(x, y)}')
else:
    print('Operação inexistente')

