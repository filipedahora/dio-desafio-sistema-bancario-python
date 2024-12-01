""" Desafio da Dio criar uma simulação de banco: saque, depósito e extrato.
 Com: 
 1. limite de operações de saque;
 2. limite de valores de saque;
 3. opção de imprimir o extrato
 
 Desafio-2 - atualizar código
 1. criar duas funções: cadastrar usuário e criar conta bancária (vinculada ao usuário)
 2. cada função deve ter uma regra na passagem de argumentos: função de saque --> deve receber
 apenas agumentos por nome (keyword only); função de depóstito recebe argumentos por posição
 (positional only); a função extrato deve receber argumentos posição e nome.
 3. criar novas funções 
 
 """

from datetime import datetime
import pprint
#BANCO DE DADOS
#numero de contas
n_conta = 0
#USUARIOS
usuarios = {}
# INFORMAÇÕES DE CONTA
contas = {}

#MSGS
CONTINUAR = "Deseja continuar? [s] sim / [n] não: "
SAIR = 'SAINDO... VOLTE SEMPRE!'

#util
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

# verificação de contas, cpfs e usuarios

def verifica_cpf(cpf):
    for char in cpf:
        if cpf.isnumeric():
            ...
        else:
            return False
    return True

def verificar_contas(cpf):
    """verificar se já existe alguma conta com o cpf digitado.
      Se não houver retorna o número do cpf, mas se hover
    retorna 0"""
    if verifica_cpf(cpf):
        
        if cpf in usuarios.keys():
            return 0
        else:
            numero = cpf
            return numero
    else:
        padrao_print("Operação falhou. Você deve digitar apenas números")
        
def verifica_usuario(cpf):
    if verifica_cpf(cpf):
        if cpf in usuarios.keys():
            padrao_print("Este usuário já possui uma conta")
            return True
        else:
            return False
    else:
        padrao_print("Número de cpf inválido")
        return True

#programa

#criar conta e usuário 
def criar_usuario(cpf): 
    """Criar um usuario e associa o usuario a uma conta"""

    padrao_print("Cadastrar Usuário")
    usuario = {}
    resultado  = verifica_usuario(cpf)
    if not resultado:
        
        usuario["nome"] = input("Digite seu nome: ")
        usuario["data_nascimento"] = input("Data de nascimento: ")
        logradouro = input("Logradouro: ")
        numero = input("Número: ")
        bairro = input("Bairro: ")
        cidade= input("Cidade: ")
        UF= input("UF: ")
        usuario["endereco"] = f'{logradouro}, nº{numero}, {bairro} - {cidade}-{UF}'
        

        return usuario
    
            
    
def criar_conta(cpf, usuario, n_conta):
    #cria uma lista de contas vinculadas ao cpf do usuário
    padrao_print("Registrando a primeira conta")

    nome = usuario["nome"].split(' ')[0]
    lmt_por_saque = float(input("Digite limite de diário de saque permitido para esta conta: "))
    print("registrado","\n")
    lmt_de_saque = int(input("Digite número de saque por dia permitido para esta conta: "))
   
    contas_usuario = {
           "usuario":nome,
           "agencia":"0001",
           "numero_da_conta": n_conta + 1,
           "tipo": "Conta Corrente",
           "saldo":0,
           "extrato_diario":'Transações:\n- ',
           "numero_de_saques": 0,
           "limite_por_saque":lmt_por_saque,
           "limite_de_saques_diarios": lmt_de_saque}
    
    padrao_print(f" Uma conta foi criada no nome de {nome} ")
    return cpf, contas_usuario


# menu
def tela_inicial(usuarios, contas, n_conta):
    msg='''
    SEJA BEM VINDO AO BANCO trilhaPyBank!
    [e] entrar em uma conta
    [c] cadastra usuário
    [r] registrar nova conta
    [s] sair
    '''
    option = input(msg).lower().strip()
    cont = True
    while cont:
        
        if option =='e':
            cpf = input("Digite somente os números do seu CPF: ").strip()
            if verifica_usuario(cpf):
                option="t"
            else:
                print("Não existe usuário registrado com este CPF.")
                resposta = input("Deseja cadastrar usuário? s/sim e n/não:").lower().strip()
                if resposta =='s':
                    option="c"
                else:
                    option="s"

        elif option == 'c':
            cpf = input("Digite somente os números do seu CPF: ").strip()
            usuarios[cpf] = criar_usuario(cpf)

            if usuarios[cpf]:
                cpf, contas_usuario = criar_conta(cpf, usuarios[cpf], n_conta)
                contas[cpf] = [contas_usuario] 
                option = "t"
        
        elif option=="r":
            cpf = input("Digite somente os números do seu CPF: ").strip()
            if verifica_usuario(cpf):
                cpf, nova_conta = criar_conta(cpf, usuarios[cpf], n_conta)
                contas[cpf].append(nova_conta)
                n_conta = nova_conta["numero_da_conta"]
                option="t"
            else:
                padrao_print("A operação falhou. Tente novamente!")
                option="r"
            

        elif option =="t":
            transacao_inicial = input("Deseja fazer uma movimentação? s/sim ou n/não").lower().strip()
            if transacao_inicial == "s":
                usuarios, contas, n_conta =  tela_menu(cpf, usuarios, contas)

            if input("Gostaria de fazer outra operação? s/sim ou n/não: ").lower().strip() == "s":
               option = input(msg).lower().strip()
            else:
                option="s"

        elif option == 's':
            cont = False

    return usuarios, contas, n_conta

def tela_menu(cpf, usuarios, contas):
    ativo = True
    conta = None
    for i in contas[cpf]:
        print("número da conta: ", i["numero_da_conta"],"\n")

    conta_escolhida = input("Digite o número da conta: ").lower().strip()

    #usuario seleciona a conta
    if conta_escolhida.isnumeric():
        conta_escolhida = int(conta_escolhida)
    for c in contas[cpf]:
        if c["numero_da_conta"] == conta_escolhida:
            conta = c
            
    

    #apresenta o menu indicando em qual usuário e conta está logado
    while ativo:
        option = menu(usuarios[cpf], conta, conta['numero_da_conta'])
        if option == 'd':
            conta = deposito(conta)
            for c in range(len(contas[cpf])):
                if conta['numero_da_conta'] in contas[cpf][c]:
                    contas[cpf][c] == conta

        elif option == 's':
            valor_de_saque = get_valor(input("Digite o valor do saque: "))
            conta = saque(conta=conta, valor_de_saque=valor_de_saque)

        elif option == 'e':
            extrato(conta["saldo"],extrato=conta["extrato_diario"])

        elif option == 'q':
            sair = input("Gostaria de sair desta conta [S] Sim ou [N] Não:\n  ").lower().strip() == 's'
            if sair:
                ativo = False
        else:
            print()
            print("Opção invalida. Tente uma opção válida!".center(60, ' '))

    

    return usuarios, contas, conta['numero_da_conta']
    
def menu (usuario, conta, n_conta):
    """função para apresentar o menu da conta do usuário"""
    
    msg = f'''
            Logado em: {usuario["nome"]} - Agência:{conta["agencia"]} - Conta: {n_conta} - \n
            Olá, selecione uma opção abaixo:\n
            [d] Depósito
            [s] Saque
            [e] Extrato
            [q] Sair\n
            '''
    option = input(msg).lower().strip()
    return option


    
# Tipos de movimentação     

def deposito(conta,/):
    """função para a operação de depósito.
      O valor deve ser inteiro e positivo"""
    
    saldo = conta["saldo"]
    lds = conta ["limite_de_saques_diarios"]
    sr = conta['numero_de_saques']
    ms = conta['limite_por_saque']
    
    padrao_print(" Operação: Depósito. ")
    msg_deposito = ''
    valor_depositado = get_valor(input("Digite o valor: "))

    if valor_depositado:
        saldo += valor_depositado
        msg_deposito = f"{datetime.now().strftime("%d/%m/%Y - %H:%M")} | Depósito - R$ {str(valor_depositado).replace('.',',')} \n- "
        conta["saldo"] = saldo
        conta["extrato_diario"] += msg_deposito
        print("Déposito realizado com sucesso")
        padrao_print("EXTRATO")
        print(conta["extrato_diario"])
        print(f'Seus saldo atual é: R$ {str(saldo).replace('.',',')}')
        padrao_print("Saindo da operação depósito")

        return conta
    else: 
        print("Não foi possível realizar operação")
    
def saque(*, conta, valor_de_saque ):

    """
    Função para saque. O máximo operações diária: 3.
    controla os valores: não pode sacar valor negativo;
    limite por saque R$ 500,00
    """
    valor_de_saque = valor_de_saque
    n_saque = conta["numero_de_saques"]
    padrao_print(" Operação: Saque ") 
    msg_saque=''
    
    if n_saque > conta["limite_de_saques_diarios"] -1:
        print("Limite de saque diário ultrapassado. Tente novamente outro dia")
        valor_de_saque=False

    elif valor_de_saque > conta["limite_por_saque"]:
        print("Valor solicitado maior do que o limite disponível. Tente um valor menor.")
        valor_de_saque=False
        
    elif valor_de_saque > conta["saldo"]:
        print ("Saldo insuficiente.")
        valor_de_saque=False
        
    else:
        conta["saldo"] -= valor_de_saque
        msg_saque = f"{datetime.now().strftime("%d/%m/%Y - %H:%M")} | Saque - R$ {str(valor_de_saque).replace('.',',')} \n-"
        conta["extrato_diario"] += msg_saque
        conta["numero_de_saques"] +=1
        
    return  conta

def extrato( saldo,/, *, extrato):
    padrao_print("EXTRATO")
    print(extrato)
    print(f'Seus saldo atual é: R$ {str(saldo).replace('.',',')}')
    
    

usuarios, contas, n_conta = tela_inicial(usuarios, contas,n_conta)




