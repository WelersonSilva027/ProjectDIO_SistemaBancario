import sys

# Configurando a saída padrão para suportar encoding UTF-8
sys.stdout.reconfigure(encoding='utf-8')

banco = "Heringer Cote"

apresentar = f"""
----------------------------------------------------
Olá Meu Nome é {banco},
Seja Bem Vindo(a) ao seu sistema bancário.
Selecione uma das opções para dar continuidade.
----------------------------------------------------
"""
tecla_errada = f"""
Você pressionou uma tecla errada!
Retornando para a página inicial,
Aguarde...
"""

# Saldo das contas
saldo_Poupanca = 4000
saldo_Universitaria = 2400

# Função para visualizar o extrato
def visualizar_extrato(saldo):
    print(f"Seu saldo é: R$ {saldo:.2f}")

# Função para realizar um saque
def realizar_saque(saldo):
    valor = float(input("Digite o valor a ser sacado: "))
    if valor <= saldo:
        saldo -= valor
        print(f"Saque realizado com sucesso! Seu novo saldo é: R$ {saldo:.2f}")
    else:
        print("Saldo insuficiente.")
    return saldo

# Função para realizar um depósito
def realizar_deposito(saldo):
    valor = float(input("Digite o valor a ser depositado: "))
    saldo += valor
    print(f"Depósito realizado com sucesso! Seu novo saldo é: R$ {saldo:.2f}")
    return saldo

print(apresentar)
print('Qual Conta Você Gostaria de Acessar?')
print('1 - Poupança')
print('2 - Conta Universitária')

conta = input("Escolha a conta (1 ou 2): ")

if conta == '1':
    print('Você escolheu: Conta Poupança.')
    saldo = saldo_Poupanca
elif conta == '2':
    print('Você escolheu: Conta Universitária.')
    saldo = saldo_Universitaria
else:
    print(tecla_errada)
    sys.exit()

print('O que você deseja fazer?')
print('0 - Visualizar Extrato')
print('1 - Realizar Saque')
print('2 - Realizar Depósito')

opcao = input("Escolha a operação (0, 1 ou 2): ")

if opcao == '0':
    visualizar_extrato(saldo)
elif opcao == '1':
    saldo = realizar_saque(saldo)
elif opcao == '2':
    saldo = realizar_deposito(saldo)
else:
    print(tecla_errada)
