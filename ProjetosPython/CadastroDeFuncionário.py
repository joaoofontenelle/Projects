import time
import os

funcionarios = []

def formatar_cpf(cpf):
    return f'{cpf[:3]}.{cpf[3:6]}.{cpf[6:9]}-{cpf[9:]}'

def formatar_rg(rg):
    return f'{rg[:2]}.{rg[2:5]}.{rg[5:8]}-{rg[8:]}'

def formatar_data(data):
    if len(data) == 8:  # Ex: 01012000 -> 01/01/2000
        return f'{data[:2]}/{data[2:4]}/{data[4:]}'
    return data

def cadastrar_funcionarios():
    nome = input('\nQual é o nome do funcionário?: ').title()
    endereço = input('Qual é o endereço do funcionário?(Rua/Trav./Av./Viela; - Num.; - Bairro; - Cidade; - Estado; - CEP;): ').title()

    cpf = input('Qual é o CPF do funcionário?: ')
    while not cpf.isdigit() or len(cpf) != 11:
        cpf = input('CPF inválido! Insira um CPF válido (11 dígitos): ')
    cpf_formatado = formatar_cpf(cpf)

    rg = input('Qual é o RG do funcionário?: ')
    while not rg.isdigit() or len(rg) != 9:
        rg = input('RG inválido! Insira um RG válido (9 dígitos): ')
    rg_formatado = formatar_rg(rg)

    idade = input('Qual é a idade do funcionário?: ')
    while not idade.isdigit() or int(idade) <= 0:
        idade = input('Idade inválida! Insira uma idade válida: ')

    datadenasc = input('Qual é a data de nascimento do funcionário?: ').title()
    while not datadenasc.isdigit() or len(datadenasc) != 8:
        datadenasc = input('Data inválida! Insira uma data no formato DD/MM/AAAA: ')
    data_formatada = formatar_data(datadenasc)
    
    dependente = input('O funcionário tem dependentes?(S/N): ').title().strip()
    if dependente == 'S':
        idade_dependente = input('Qual a idade do dependente mais novo? ')
    else:
        idade_dependente = 'Sem dependentes'

    cargo = input('Qual é o cargo do funcionário?: ').title()
    salario = float(input('Qual é salário do funcionário?: R$'))

    funcionarios.append({
        'Nome': nome, 'Endereço': endereço, 'CPF': cpf_formatado, 'RG': rg_formatado, 'Idade': idade,
        'Data de Nascimento': data_formatada, 'Idade do dependente': idade_dependente,
        'Cargo': cargo, 'Salário': salario, 'Status': 'Ativo'
    })

    print(f'Funcionário "{nome}" adicionado com sucesso!\n')

def exibir_tds_funcio():
    ativos = [f for f in funcionarios if f['Status'] == 'Ativo']

    if ativos:
        for indice, funcionario in enumerate(ativos, start=1):
            print(f'\nFUNCIONÁRIOS CADASTRADOS:\n\n{indice}° Funcionário:')
            print(f'Nome: {funcionario["Nome"]}')
            print(f'Endereço: {funcionario["Endereço"]}')
            print(f'CPF: {funcionario["CPF"]}')
            print(f'RG: {funcionario["RG"]}')
            print(f'Idade: {funcionario["Idade"]}')
            print(f'Data de Nascimento: {funcionario["Data de Nascimento"]}')
            print(f'Idade do dependente mais novo: {funcionario["Idade do dependente"]}')
            print(f'Cargo: {funcionario["Cargo"]}')
            print(f'Salário: R${funcionario["Salário"]:.2f}\n')
    else:
        print('Nenhum funcionário ativo cadastrado.\n')

def atualizar_informacoes():
    if not funcionarios:
        print('\nNenhum funcionário cadastrado para atualizar.\n')
        return

    exibir_tds_funcio()
    indice = input('\nDigite o número do funcionário que deseja atualizar: ')

    if indice.isdigit():
        indice = int(indice)
        ativos = [f for f in funcionarios if f['Status'] == 'Ativo']

        if 1 <= indice <= len(ativos):
            funcionario = ativos[indice - 1]

            nome = input('\nNovo nome (ou deixe em branco para manter o atual): ').title()
            endereço = input('Novo endereço (ou deixe em branco para manter o atual): ').title()
            cpf = input('Novo CPF (ou deixe em branco para manter o atual): ')
            rg = input('Novo RG (ou deixe em branco para manter o atual): ')
            idade = input('Nova idade (ou deixe em branco para manter a atual): ')
            datadenasc = input('Nova data de nascimento (ou deixe em branco para manter a atual): ')
            dependente = input('Novo dependente (ou deixe em branco para manter o atual): ').title().strip()
            cargo = input('Novo cargo (ou deixe em branco para manter o atual): ').title()
            salario = input('Novo salário (ou deixe em branco para manter o atual): R$')

            if nome:
                funcionario['Nome'] = nome
            if endereço:
                funcionario['Endereço'] = endereço
            if cpf:
                while not cpf.isdigit() or len(cpf) != 11:
                    cpf = input('CPF inválido! Insira um CPF válido (11 dígitos): ')
                funcionario['CPF'] = formatar_cpf(cpf)
            if rg:
                while not rg.isdigit() or len(rg) != 9:
                    rg = input('RG inválido! Insira um RG válido (9 dígitos): ')
                funcionario['RG'] = formatar_rg(rg)
            if idade:
                funcionario['Idade'] = idade
            if datadenasc:
                while not datadenasc.isdigit() or len(datadenasc) != 8:
                    datadenasc = input('Data inválida! Insira uma data no formato DDMMAAAA: ')
                funcionario['Data de Nascimento'] = formatar_data(datadenasc)
            if dependente:
                funcionario['Idade do dependente'] = dependente
            if cargo:
                funcionario['Cargo'] = cargo
            if salario:
                funcionario['Salário'] = float(salario)

            print('\nInformações atualizadas com sucesso!')
        else:
            print('\nNúmero de funcionário inválido.\n')
    else:
        print('Entrada inválida. Por favor, insira um número.\n')

def bloquear_funcionario():
    if not funcionarios:
        print('\nNenhum funcionário cadastrado para remover.\n')
        return

    exibir_tds_funcio()
    indice = input('\nDigite o número do funcionário que deseja bloquear: ')

    if indice.isdigit():
        indice = int(indice)
        ativos = [f for f in funcionarios if f['Status'] == 'Ativo']

        if not ativos:
            print('Não há funcionários ativos para bloquear.\n')
            return

        if 1 <= indice <= len(ativos):
            funcionarios[funcionarios.index(ativos[indice - 1])]['Status'] = 'Inativo'

            print(f'\nFuncionário "{ativos[indice - 1]["Nome"]}" foi bloqueado e está agora inativo.\n')
        else:
            print('\nNúmero de funcionário inválido.\n')
    else:
        print('\nEntrada inválida. Por favor, insira um número.\n')

def gerenciar_bloqueio():
    inativos = [f for f in funcionarios if f['Status'] == 'Inativo']

    if inativos:
        for indice, funcionario in enumerate(inativos, start=1):
            print(f'\n{indice}° Funcionário Inativo:')
            print(f'Nome: {funcionario["Nome"]}')
            print(f'Endereço: {funcionario["Endereço"]}')
            print(f'CPF: {funcionario["CPF"]}')
            print(f'RG: {funcionario["RG"]}')
            print(f'Idade: {funcionario["Idade"]}')
            print(f'Data de Nascimento: {funcionario["Data de Nascimento"]}')
            print(f'Idade do dependente mais novo: {funcionario["Idade do dependente"]}')
            print(f'Cargo: {funcionario["Cargo"]}')
            print(f'Salário: R${funcionario["Salário"]:.2f}\n')
    else:
        print('\nNenhum funcionário inativo cadastrado.\n')
        return

    indice = input('\nDigite o número do funcionário que deseja desbloquear: ')

    if indice.isdigit():
        indice = int(indice)

        if 1 <= indice <= len(inativos):
            funcionarios[funcionarios.index(inativos[indice - 1])]['Status'] = 'Ativo'

            print(f'\nFuncionário "{inativos[indice - 1]["Nome"]}" foi desbloqueado e está agora ativo.\n')
        else:
            print('\nNúmero de funcionário inválido.\n')
    else:
        print('\nEntrada inválida. Por favor, insira um número.\n')

while True:
    print('\n' + '=' * 32)
    print('MENU'.center(30))
    print('=' * 32)

    opcao = input('\n1. Cadastrar novos funcionários\n2. Exibir todos os funcionários cadastrados\n3. Atualizar as informações de um funcionário existente\n4. Bloquear um funcionário\n5. Desbloquear um funcionário\n6. Sair do sistema\n\nEscolha: ')

    if opcao == '1':
        cadastrar_funcionarios()
    elif opcao == '2':
        exibir_tds_funcio()
    elif opcao == '3':
        atualizar_informacoes()
    elif opcao == '4':
        bloquear_funcionario()
    elif opcao == '5':
        gerenciar_bloqueio()
    elif opcao == '6':
        os.system('cls')
        mensagens = ['Saindo do sistema.', 'Saindo do sistema..', 'Saindo do sistema...']

        for c in range(0, 2):
            for mensagem in mensagens:
                print(mensagem)
                time.sleep(0.5)
                os.system('cls')
        print('Volte sempre!!!')
        break
    
    else:
        print('Opção inválida. Por favor, escolha uma opção de 1 a 6.\n')