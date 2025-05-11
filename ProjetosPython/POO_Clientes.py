class Clientes:
    def __init__(self, nome, email, plano):
        self.nome = nome
        self.email = email
        self.lista_planos = ['Gold', 'Platinum']
        if plano in self.lista_planos:
            self.plano = plano
        else:
            raise Exception('Plano inválido.')

    def mudar_plano(self, novo_plano):
        if novo_plano in self.lista_planos:
            self.plano = novo_plano
        else:
            print('Plano inválido.')

    def ver_filme(self, filme, plano_filme):
        if self.plano == plano_filme:
            print(f'Ver filme: {filme}')
        elif self.plano == 'Platinum' and plano_filme == 'Gold':
            print(f'Ver filme: {filme}')
        else:
            print('Este filme não está no catálogo do seu plano atual.')

cliente1 = Clientes('João', 'joaovdsfontenelle07@gmail.com', 'Platinum')

cliente1.mudar_plano('Gold')

print('Nome:', cliente1.nome, '\nE-mail:', cliente1.email, '\nPlano:', cliente1.plano)

cliente1.ver_filme('Star Wars', 'Platinum')