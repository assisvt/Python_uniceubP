# O nome de classe começa com letra maiúscula e as outras letras minúsculas.
# class Conta:
# class Conta():
class Conta(object):                    # Superclasse
    def __init__(self, nome, saldo=0.0):  # Construtor  com default
        self.nome = nome                # Atributos de instância (objeto)
        self.saldo = saldo
    def get_nome(self):                 # Consulta
        return self.nome
    def set_nome(self, novo_nome):      # Altera
        self.nome = novo_nome
    def get_saldo(self):
        return self.saldo
    def __str__(self):                  # Sobrescreve o método __str__ do Python
        # s = 'Nome: ' + self.nome + ', R$ ' + str(self.saldo)  # Concatenação
        s = f'Nome: {self.nome}, R$ {self.saldo}'               # f-string
        return s
    def deposito(self, valor):          # Métodos funcionais
        self.saldo += valor             # self.saldo = self.saldo + valor
    def retirada(self, valor):          # Sem RN (Regra de Negócio)
        self.saldo -= valor             # self.saldo = self.saldo - valor
    def retirada_rn(self, valor):       # RN obrigatória (natural do banco)
        if valor > self.saldo:
            print('Saldo insuficiente.')
        else:
            self.saldo -= valor


# O nome de classe começa com letra maiúscula e as outras letras minúsculas.
# class NomeSubclasse(NomeSuperclasse):     # Sintaxe
class Conta_PF(Conta):      # Subclasse Conta_PF herda da superclasse Conta
    def __init__(self, nome, saldo=0.0, genero='m', cpf=''):  # Valores default
        super().__init__(nome, saldo)   # Chama o construtor da superclasse
        self.genero = genero
        self.cpf = cpf
    def get_genero(self):               # Consulta
        return self.genero
    def set_genero(self, novo_genero):  # Altera
        self.genero = novo_genero
    def get_cpf(self):
        return self.cpf
    def set_cpf(self, novo_cpf):
        self.cpf = novo_cpf


""" - As principais modalidades de PJ:
1 - MEI (Microempreendedor Individual)
2 - ME – Microempresa
3 - EPP (Empresa de Pequeno Porte)
4 - EI (Empresário Individual) 
5 - EIRELI (Empresa Individual de Responsabilidade Limitada)
6 - Sociedade Limitada – LTDA
7 - Sociedade Anônima (SA)                                  """

# O nome de classe começa com letra maiúscula e as outras letras minúsculas.
# class NomeSubclasse(NomeSuperclasse):   # Sintaxe
class Conta_PJ(Conta):  # Subclasse Conta_PJ que herda da superclasse Conta
    def __init__(self, nome, saldo=0.0, modalidade='MEI', cnpj=''):  # Construtor
        super().__init__(nome, saldo)       # Chama o construtor da superclasse
        # super(Conta_PJ, self).__init__(nome, saldo)
        # Conta.__init__(self, nome, saldo)
        self.modalidade = modalidade
        self.cnpj = cnpj
    def get_modalidade(self):
        return self.modalidade
    def get_cnpj(self):
        return self.cnpj
    def set_cnpj(self, novo_cnpj):
        self.cnpj = novo_cnpj


if __name__ == '__main__':
    c = Conta('Alice')                  # Chama o construtor da classe Conta
    print(c)                            # print(c.__str__())
    print('- Superclasse:\nNome:', c.get_nome())  # Métodos da superclasse
    print('Saldo:', c.get_saldo())
    c.set_nome('Emily')
    print('Nome alterado:', c.get_nome())
    print(c.__str__())                  # print(c)
    pf1 = Conta_PF('Ana', 3000.0, 'f', '1234')  # Objeto da subclasse
    print(pf1)                          # Chama o método __str__()
    print('- Pessoa Física 1:\nNome:', pf1.get_nome())  # Método na superclasse
    print("Saldo:", pf1.get_saldo())
    pf2 = Conta_PF('Ailton', 7000.0)    # Objeto da subclasse Conta_PF
    print(pf2)                          # Chama o método __str__()
    print('- Pessoa Física 2:\nNome:', pf2.get_nome())  # Método na superclasse
    print("Saldo:", pf2.get_saldo())
    print('CPF:', pf2.get_cpf())        # Método da subclasse
    pf2.set_cpf('123456789')            # Altera
    print('CPF alterado:', pf2.get_cpf())  # Verifica alteração
    print('Saída usando as funções vars e __dict__ do Python:')
    print(vars(pf2))                    # Usa os métodos do Python
    print(pf2.__dict__)
    # {'nome': 'Ana', 'saldo': 3000.0, 'genero': 'm', 'cpf': ''}
    pj1 = Conta_PJ('Café ABC', 15000.0)  # objeto (instância) da subclasse Conta_PJ
    print(pj1)
    print('- Pessoa Jurídica:\nNome:', pj1.get_nome())  # Método da superclasse
    print("Saldo:", pj1.get_saldo())
    print('CNPJ:', pj1.get_cnpj())                      # Método da subclasse
    print(pj1)
    print(vars(pj1))                                    # Usa os métodos do Python
    print(pj1.__dict__)
    pf1.deposito(11)                                    # Depósito
    print("- Pessoa Física 1:\nSaldo:", pf1.get_saldo())  # Verifica alteração
    pj1.deposito(22)
    print("- Pessoa Jurídica 1:\nSaldo:", pj1.get_saldo())  # Verifica alteração
    pf1.retirada(10)                                        # Retirada sem RN
    print("- Pessoa Física 1:\nSaldo:", pf1.get_saldo())    # Verifica alteração
    pj1.retirada(21)
    print("- Pessoa Jurídica 1:\nSaldo:", pj1.get_saldo())  # Verifica alteração
    pf1.retirada_rn(10)                                     # Retirada com RN
    print("- Pessoa Física 1:\nSaldo:", pf1.get_saldo())    # Verifica alteração
    pj1.retirada_rn(21)
    print("- Pessoa Jurídica 1:\nSaldo:", pj1.get_saldo())  # Verifica alteração
    pj1.retirada_rn(20000.0)                                # Retirada, msg erro
    print('Saldo: ', pj1.get_saldo())                       # Verifica alteração
