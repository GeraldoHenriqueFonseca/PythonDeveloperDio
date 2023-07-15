###############################################################################
# Geraldo Henrique Fonseca
# Projeto básico sistema bancário
# Simula saque, depósito e mostra o extrato de uma conta
# Limite diário de cada saque é 500 e só pode fazer 3 saques ao mesmo dia
# Tem que avaliar se tem saldo suficiente, não pode deixar o saldo ser negativo
###############################################################################
# mostra as 3 operações disponíveis para movimentar a conta: saque, depósito ou extrato
menu =''' Qual o opção que deseja realizar:
        1 - Depósito
        2 - Saque
        3 - Extrato
        Q - Sair
'''
LIMITE_SAQUE = 3
saldo = 0
qtd_saques = 0
extrato = []

def saque(valor_saque,saldo):
    saldo = saldo - valor_saque
    return saldo

def deposito(valor_deposito,saldo):
    saldo = saldo + valor_deposito
    return saldo

while True:
    print(menu)
    opcao = input()
    if opcao=='1':
        print('Depósito')
        print('Digite o valor que será depositado')
        valor_deposito = float(input().replace(',','.'))
        if valor_deposito<0:
            while valor_deposito<0:
                print('Digite um valor válido')
                valor_deposito = float(input().replace(',','.'))
        saldo=deposito(valor_deposito,saldo)
        extrato.append(f'Depósito: R${valor_deposito:.2f}')
    elif opcao=='2':
        print('Saque')
        if qtd_saques<LIMITE_SAQUE:
            print('Digite o valor que deseja sacar')
            valor_saque = float(input().replace(',','.'))
            if valor_saque<0:
                while valor_saque<0:
                    print('Digite um valor válido')
                    valor_saque = float(input().replace(',','.'))
            elif saldo < valor_saque:
                print('Saldo insuficiente.')
                print(f'Saldo disponível: {saldo}')
            elif valor_saque>500:
                print('Limite máximo de saque é de R$500,00')
            else:
                print('teste saque')
                saldo = saque(valor_saque, saldo)
                extrato.append(f'Saque: R${valor_saque:.2f}')
                qtd_saques+=1
        elif qtd_saques>=LIMITE_SAQUE:
            print('Atingiu o limite diário de saques')
    elif opcao=='3':
        print('Extrato')
        for values in range(len(extrato)):
            print(extrato[values])
    elif opcao.lower()=='q':
        print('Obrigado por nos escolher. Operação finalizada')
        break
    else:
        print('Escolha uma operação válida.')