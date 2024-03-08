class Banco:
    def __init__(self, nome, endereco, telefone, saldo_inicial):
        self.nome = nome
        self.endereco = endereco
        self.telefone = telefone
        self.saldo = saldo_inicial

    def get_nome(self):
        return self.nome
    def set_nome(self, novo_nome):
        self.nome = novo_nome

    def get_endereco(self):
        return self.endereco
    def set_endereco(self, novo_endereco):
        self.endereco = novo_endereco

    def get_telefone(self):
        return self.telefone
    def set_telefone(self, novo_telefone):
        self.telefone = novo_telefone

    def get_saldo(self):
        return self.saldo
    
    def depositar(self, valor):
        if valor > 0:
            self.saldo += valor
            print(f'Depósito de R${valor:.2f} realizado.\nNovo saldo: R${self.saldo:.2f}')
        else:
            print('Valor inválido para depósito.')
    
    def sacar(self, valor):
        if valor > 0 and valor <= self.saldo:
            self.saldo -= valor
            print(f'Saque de R${valor:.2f} realizado.\nNovo saldo: R${self.saldo:.2f}')
        else:
            print('Saldo insuficiente ou valor inválido para saque.')

if __name__ == '__main__':
    banco1=  Banco('XYZ', 'Rua Principal, 111', '(61) 1234-5678', 1000.00)
    banco2 = Banco('ABC', 'Avenida Secundária, 222', '(62) 9876-5432', 1500.00)
    banco3 = Banco('QuickFinance', 'Praça Central, 333', '(63) 5555-4444', 2000.00)
    bancos = [banco1, banco2, banco3]

    for banco in bancos:
        print('Informações do Banco:')
        print('Nome do banco:', banco.get_nome())
        print('Endereço:', banco.get_endereco())
        print('Número de telefone:', banco.get_telefone())
        print('Saldo Inicial:', banco.get_saldo())
        banco.depositar(500.00)
        banco.sacar(200.00)
        print('Saldo Final:', banco.get_saldo())
        if banco is banco2:  # Verifica se o objeto é o banco2
            banco2.set_nome('ABC bank')
            print('Nome do banco atualizado:', banco2.get_nome())
        print('='*30)
