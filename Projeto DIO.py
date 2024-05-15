# Sistema Bancário V1
# Para essa primeira versão do sistema vamos utilizar apenas 3 operações
# Deposito: Pode ser depositado valores positivos para a conta bancária e depois ser exibido no extrato.
# Saque: O sistema permite realizar no máximo 3 saques com limite máximo de R$ 500.00 reais.
# Extrato: O sistema vai exibir todas suas operações de deposito e saque, incluindo no final o saldo da conta bancária no formato R$ xxxx.xx

print('==================== SEJA BEM VINDO AO SISTEMA BANCÁRIO D.I.O ====================')
menu = '[D] Depósitar \n[S] Sacar \n[E] Extrato \n[S] Sair \nSelecione a operação desejada: '

saldo = 0
limite = 500
extrato = ""
numero_saques = 0
LIMITE_SAQUES = 3

while True:
    opçao = input(menu).upper().strip()
    if opçao == 'D':
        valor_deposito = float(input('Valor a ser depósitado: '))
        if valor_deposito >0:
            print(f'O valor de R${valor_deposito:.2f} reais foi depositado')
            saldo += valor_deposito
            extrato += f'Depósito de R$ {valor_deposito} reais realizado com sucesso.\n'


    elif opçao == 'S':
        valor_saque = float(input('Valor a ser sacado: '))
        numero_saques +=1
        if numero_saques > LIMITE_SAQUES:
            print('Você atingiu o limite de saque diário')
            break            
        elif valor_saque >0:
            if valor_saque <= limite:
                if valor_saque <= saldo:
                    print(f'Saque de R${valor_saque} reais foi realizado com sucesso')
                    saldo -= valor_saque
                    print(f'Limite de saques diários disponíveis: {LIMITE_SAQUES - numero_saques}')
                    extrato += f'Saque de R$ {valor_saque} reais realizado com sucesso.\n'
                else:
                    print('Não é possível sacar o dinheiro por falta de saldo')      
            else:
                print('Não foi possível realizar este saque, limite de saque até R$ 500.00 reais.')
                print('Faça a operação novamente de acordo com as normas.')
    elif opçao == 'E':
        print('\n==========Exibindo o histórico do extrato==========\n')
        print('EXTRATO\n')
        print(extrato)
        print(' ')
        print(f'Saldo atual da sua conta bancária é de R$ {saldo:.2f}\n')
        print('FIM\n')
    elif opçao == 'Q':
        print('Obrigado por usar nosso sistema. Volte sempre.')
        break

    else:
        print('Operação inválida!\n Por favor selecione novamente a operação desejada')    
