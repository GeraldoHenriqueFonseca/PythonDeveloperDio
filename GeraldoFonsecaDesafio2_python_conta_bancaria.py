###############################################################################
# Geraldo Henrique Fonseca
# Projeto básico sistema bancário
# Simula saque, depósito, crição de usuário, criação de conta e mostra o extrato de uma conta
# Limite diário de cada saque é 500 e só pode fazer 3 saques ao mesmo dia
# Tem que avaliar se tem saldo suficiente, não pode deixar o saldo ser negativo
###############################################################################

def criar_usuario(usuarios):
    cpf = input("Informe o CPF: ")
    cpf = cpf.replace('.','').replace('-','')
    print(cpf)
    usuario = filtrar_usuario(cpf, usuarios)
    if usuario:
        print("Já existe usuário com esse CPF!")
        return
    nome = input("Informe o nome completo: ")
    data_nascimento = input("Informe a data de nascimento (dd-mm-aaaa): ")
    endereco = input("Informe o endereço (logradouro, nro - bairro - cidade/sigla estado): ")
    usuarios.append({"nome": nome, "data_nascimento": data_nascimento, "cpf": cpf, "endereco": endereco})
    print("Usuário criado com sucesso!")

def filtrar_usuario(cpf, usuarios):
    usuarios_filtrados = [usuario for usuario in usuarios if usuario["cpf"] == cpf]
    return usuarios_filtrados[0] if usuarios_filtrados else None
   
def criar_conta(agencia, numero_conta, usuarios):
    cpf = input("Informe o CPF do usuário: ")
    cpf = cpf.replace('.','').replace('-','')
    usuario = filtrar_usuario(cpf, usuarios)

    if usuario:
        print("\nConta criada com sucesso!")
        return {"agencia": agencia, "numero_conta": numero_conta, "usuario": usuario}

    print("\nUsuário não encontrado, fluxo de criação de conta encerrado!\n")


def listar_contas(contas):
    if len(contas)==0:
        return 'Sem contas.'
    for conta in contas:
        linha = f"""\
            Agência:\t{conta['agencia']}
            C/C:\t\t{conta['numero_conta']}
            Titular:\t{conta['usuario']['nome']}
        """
        print("=" * 100)
        print(textwrap.dedent(linha))


def saque(*,saldo,valor_saque, qtd_saques,limite_saques,limite_saque,extrato):
    if qtd_saques<limite_saques:
        if saldo < valor_saque:
            print('Saldo insuficiente.')
            print(f'Saldo disponível: {saldo}')
        if valor_saque>limite_saque:
            print('Limite máximo de saque é de R$500,00')
            return saldo, qtd_saques, extrato
        else:
            print('Saque')
            extrato.append(f'Saque: R${valor_saque:.2f}')
            saldo = saldo - valor_saque
            qtd_saques+=1
            return saldo, qtd_saques, extrato
    elif qtd_saques>=limite_saques:
        print('Atingiu o limite diário de saques')
        return saldo, qtd_saques, extrato

def deposito(valor_deposito,saldo,extrato,/):
    saldo = saldo + valor_deposito
    extrato.append(f'Depósito: R${valor_deposito:.2f}')
    return saldo, extrato

def exibir_extrato(saldo, /, *, extrato):
    print("\n================ EXTRATO ================")
    if extrato==0:
        print("Não foram realizadas movimentações")
    else:
        for conteudo in extrato:
            print(conteudo)
    print(f"\nSaldo:\t\tR$ {saldo:.2f}")
    print("==========================================")

def menu():
    menu = ''' Qual o opção que deseja realizar:
        1 - Depósito
        2 - Saque
        3 - Extrato
        4 - Nova conta
        5 - Listar contas
        6 - Novo usuário
        Q - Sair '''
    return menu
def main():
    LIMITE_SAQUES = 3
    saldo = 0
    qtd_saques = 0
    LIMITE_SAQUE = 500
    extrato = []
    AGENCIA = "0001"
    usuarios=[]
    contas = []
    while True:
        print(menu())
        print("Digite a opção")
        opcao = input()
        if opcao=='1':
            print('Depósito')
            print('Digite o valor que será depositado')
            valor_deposito = float(input().replace(',','.'))
            if valor_deposito<0:
                while valor_deposito<0:
                    print('Digite um valor válido')
                    valor_deposito = float(input().replace(',','.'))
            saldo,extrato = deposito(valor_deposito,saldo,extrato)
        elif opcao=='2':
            print('Digite o valor que deseja sacar')
            valor_sacado = float(input().replace(',','.'))
            if valor_sacado<0:
                while valor_sacado<0:
                    print('Digite um valor válido')
                    valor_sacado = float(input().replace(',','.'))
            saldo,qtd_saques,extrato = saque(saldo=saldo, valor_saque=valor_sacado,qtd_saques=qtd_saques,limite_saques=LIMITE_SAQUES,limite_saque=LIMITE_SAQUE,extrato=extrato)
        elif opcao=='3':
            print('Extrato')
            exibir_extrato(saldo, extrato=extrato)
        elif opcao=='4':
            numero_conta = len(contas) + 1
            conta = criar_conta(AGENCIA, numero_conta, usuarios)
            if conta:
                contas.append(conta)
        elif opcao=='5':
            listar_contas(contas)
        elif opcao=='6':
            criar_usuario(usuarios)
        elif opcao.lower()=='q':
            print('Obrigado por nos escolher. Operação finalizada')
            break
        else:
            print('Escolha uma operação válida.')
    
main()
