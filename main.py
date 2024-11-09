
from datetime import datetime
""" Desafio da Dio criar uma simulação de banco: saque, depósito e extrato.
 Com: 
 1. limite de operações de saque;
 2. limite de valores de saque;
 3. opção de imprimir o extrato"""

saldo = 2000.00
extrato = 'Transações:\n- ' #deve armazenar as movimentações
n_saque = 0

LIMITE_DE_SAQUE= 500.0
MAX_SAQUE = 3
CONTINUAR = "Deseja continuar? [s] sim / [n] não: "
SAIR = 'SAINDO... VOLTE SEMPRE!'


MENU = '''
[d] Depósito
[s] Saque
[e] Extrato
[q] Sair\n
'''
def padrao_print(texto):
    print()
    print(texto.center(60,"="))
    print()
  
def continua():
    if input(CONTINUAR).lower() == 's':
            return True
    else:
        padrao_print(SAIR)
        return  False

def get_valor(valor):
    """valida a operação"""
    valor = valor
    if valor.startswith('-'):
        # verifica se o valor é maior que zero ou se é um valor válido
        print(f"Valor inválido. Tente outro valor de depósito.\n")
        return False
    else:
        if valor.isnumeric():
            return float(valor)
        else:
            print(f"Valor inválido. Tente outro valor de depósito.\n")
            return False


def deposito(saldo):
    """função para a operação de depósito.
      O valor deve ser inteiro e positivo"""
    
    padrao_print(" Operação: Depósito. ")
    msg_deposito = ''
    valor_depositado = get_valor(input("Digite o valor: "))

    if valor_depositado:
        saldo += valor_depositado
        msg_deposito = f"{datetime.now().strftime("%d/%m/%Y - %H:%M")} /| Depósito - R$ {str(valor_depositado).replace('.',',')} \n- "
             
    
    return msg_deposito, valor_depositado, saldo  
    


def saque(saldo):

    """
    Função para saque. O máximo operações diária: 3.
    controla os valores: não pode sacar valor negativo;
    limite por saque R$ 500,00
    """
    
    padrao_print(" Operação: Saque ") 
    msg_saque=''
    valor_de_saque = get_valor(input("Digite o valor do saque: "))
    if n_saque > MAX_SAQUE -1:
        print("Limite de saque diário ultrapassado. Tente novamente outro dia")
        valor_de_saque=False
    elif valor_de_saque > LIMITE_DE_SAQUE:
        print("Valor solicitado maior do que o limite disponível. Tente um valor menor.")
        valor_de_saque=False
    elif valor_de_saque > saldo:
        print ("Saldo insuficiente.")
        valor_de_saque=False
    else:
        saldo -= valor_de_saque
        msg_saque = f"{datetime.now().strftime("%d/%m/%Y - %H:%M")} | Saque - R$ {str(valor_de_saque).replace('.',',')} \n-"

    return  msg_saque, valor_de_saque, saldo  
        
ativo = True

while ativo:
    padrao_print("Menu")
    option = input(MENU).lower().strip()
    if option == 'd':
        resultado = deposito(saldo)
        if resultado[1]:
            saldo = resultado[2]
            extrato += resultado[0]

    elif option == 's':
        resultado = saque(saldo)
        if resultado[1]:
            saldo = resultado[2]
            extrato += resultado[0]
            n_saque += 1
        
    elif option == 'e':
       padrao_print("EXTRATO")
       print(extrato)
       print(f'Seus saldo atual é: R$ {str(saldo).replace('.',',')}')
    elif option == 'q':
        sair = input("Gostaria de sair do programa? [S] Sim ou [N] Não:\n  ").lower().strip() == 's'
        if sair:
            ativo = False
    else:
        print()
        print("Opção invalida. Tente uma opção válida!".center(60, ' '))