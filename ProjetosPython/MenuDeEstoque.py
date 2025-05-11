import time
import os
estoque = []

while True:
    try:
        print('=' * 59)
        print('                        MENU DA LOJA        ')
        print('=' * 59)
        print('''(1) Adicionar Estoque
(2) Consultar Estoque
(3) Remover do Estoque
(4) Sair''')
        
        opcao = int(input('Escolha uma opção: '))
    except ValueError:
        print('Entrada inválida, digite um número.')
        continue

    if opcao == 1: # Adicionar
        nome_produto = input('Digite o nome do produto: ')
        
        for item in estoque:
            if item['Produto'] == nome_produto:
                try:
                    quantidade = int(input('Digite a quantidade adicional: '))
                    item['Quantidade'] += quantidade
                    print(f'Quantidade atualizada: {item["Quantidade"]}')
                except ValueError:
                    print('Entrada inválida, digite um número.')
                break
        else:
            
            try:
                quantidade = int(input('Digite a quantidade que deseja adicionar: '))
                estoque.append({'Produto': nome_produto, 'Quantidade': quantidade})
                time.sleep(0.2)
                print('Produto adicionado com sucesso')
            except ValueError:
                print('Entrada inválida, digite um número')

    elif opcao == 2:
        print('=' * 55)
        if estoque:
            for indice, item in enumerate(estoque, start=1):
                print(f'{indice}. Produto: {item['Produto']}  | Quantidade: {item['Quantidade']}')
        else:
            print('Nenhum produto cadastrado.')

    elif opcao == 3:
        if estoque:
            for indice, item in enumerate(estoque, start=1):
                print(f'{indice}. Produto: {item["Produto"]}  | Quantidade: {item["Quantidade"]}')
            try:
                indice = int(input('Digite o número do produto que deseja alterar: ')) - 1
                if 0 <= indice < len(estoque):
                    produto_selecionado = estoque[indice]
                    print(f'Produto selecionado: {produto_selecionado["Produto"]} | Quantidade: {produto_selecionado["Quantidade"]}')
                    
                    remover_tudo = input('Deseja remover todo o produto? (s/n): ').strip().lower()
                    if remover_tudo == 's':
                        removido = estoque.pop(indice)
                        print(f'Produto {removido["Produto"]} removido com sucesso!')
                    else:
                        try:
                            quantidade_remover = int(input('Digite a quantidade que deseja remover: '))
                            if quantidade_remover <= produto_selecionado['Quantidade']:
                                produto_selecionado['Quantidade'] -= quantidade_remover
                                print(f'Quantidade atualizada: {produto_selecionado["Quantidade"]}')
                                if produto_selecionado['Quantidade'] == 0:
                                    estoque.pop(indice)
                                    print(f'Produto {produto_selecionado["Produto"]} removido completamente.')
                            else:
                                print('Quantidade insuficiente em estoque.')
                        except ValueError:
                            print('Entrada inválida, digite um número.')
                else:
                    print('Índice inválido!')
            except ValueError:
                print('Entrada inválida, digite um número.')
        else:
            print('Nenhum produto cadastrado.')

    elif opcao == 4: # Sair
        mensagens = [
            'Saindo do sistema.',
            'Saindo do sistema..',
            'Saindo do sistema...']
        for i in range(3):  # Usando range para repetir 3 vezes
            os.system('cls') 
            print(mensagens[i])
            time.sleep(0.5) 
            os.system('cls') 
        print('Até logo!!!')
        break

    else:
        print('Opção inválida. Tente novamente.')