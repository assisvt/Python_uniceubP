"""                 Comentários de várias linhas.
  CEUB  -  FATECS  -  BCC  -  ADS  -  Programação  -  Prof. Barbosa
ctlr<d>, duplica linha. ctrl<y>, apaga linha. ctrl</>, comenta linha.

- Implemente estes itens:

1- Crie três instâncias da subclasse Conta_PF com quatro, três e dois argumentos,
teste
2- Crie duas instâncias (objetos) da subclasse Conta_PJ com três e dois argumentos.
Teste
3- Use alguns métodos das classes desenvolvidas
4- Faça um depósito, teste
5- Faça uma retirada, teste

6- Refaça o método retirada usando RNs (Regras de Negócios) bancárias. Teste
7- A política do sistema bancário mudou, o depósito continua sem cobrado tarifa.
  No saque, a pessoa física tem tarifa de 2 reais e pessoa juridica de 5 reais.
  Então, substitua o método retirada da superclasse por dois métodos retirada nas
  duas subclasse.
8- Teste a alteração anterior.
9- Crie o método retirada_rn2, substitua os dois método retirada nas duas
  subclasses por um único método (retirada_rn2) na superclasse

- Crie um atributo de classe para armazenar a quantidade de contas (objetos) criados.
    Onde colocar o contador (a atualização)?
- Crie o método de classe get_qtd_conta.
- Teste as alterações anteriores e o método de classe get_qtd_contas.

"""
# O nome de classe começa com letra maiúscula e as outras letras minúsculas.
# class Conta:
# class Conta():
class Conta(object):                    # Superclasse
    qtd_conta = 0                   # Atributos de classe
    @classmethod                      # Métodos de classe (decorator)
    def get_qtd_conta(cls):
        return cls.qtd_conta        # return cls.nomeAtributoClasse
        # return Conta.qtd_conta    # return NomeClasse.nomeAtributoClasse
    def __init__(self, nome, saldo):  # Construtor  com default
        self.nome = nome                # Atributos de instância (objeto)
        self.saldo = saldo
        Conta.qtd_conta += 1            # NomeClasse.atributoClasse
    def get_nome(self):                 # Consulta
        return self.nome
    def set_nome(self, novo_nome):      # Altera
        self.nome = novo_nome
    def get_saldo(self):
        return self.saldo
    def __str__(self):                  # Sobrescreve o método __str__ do Python
        s = f'Nome: {self.nome}, R$ {self.saldo}'               # f-string
        return s
    def deposito(self, valor):          # Métodos funcionais
        self.saldo += valor             # self.saldo = self.saldo + valor
    def retirada(self, valor):          # Sem RN (Regra de Negócio)
        self.saldo -= valor             # self.saldo = self.saldo - valor
    def retirada_rn2(self, valor):  # Retirada na superclasse
        nome_classe = self.__class__.__name__
        if nome_classe == 'Conta_PF':
            total = valor + 2                  # RN de pessoa física
        else:
            total = valor + 5                  # RN de pessoa jurídica
        if total > self.saldo :
            print('Saldo insuficiente.')
        else:
            self.saldo -= total
class Conta_PF(Conta):      # Subclasse Conta_PF herda da superclasse Conta
    def __init__(self, nome, saldo, genero='', cpf=''):  # Valores default
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
class Conta_PJ(Conta):  # Subclasse Conta_PJ que herda da superclasse Conta
    def __init__(self, nome, saldo, modalidade='', cnpj=''):  # Construtor
        super().__init__(nome, saldo)       # Chama o construtor da superclasse
        self.modalidade = modalidade
        self.cnpj = cnpj
    def get_modalidade(self):
        return self.modalidade
    def get_cnpj(self):
        return self.cnpj
    def set_cnpj(self, novo_cnpj):
        self.cnpj = novo_cnpj
if __name__ == '__main__':
    print("Qtd. contas:", Conta.get_qtd_conta())
    # Método de classe (NomeClasse.nome_metodo())
    pf1 = Conta_PF('Ana', 3000.0, 'f', '1234')  # Objeto da subclasse
    print('- Pessoa Física 1:\nNome:', pf1.get_nome())  # Método na superclasse
    pf2 = Conta_PF('Ailton', 7000.0, 'm')  # Objeto da subclasse Conta_PF
    print(pf2)                          # Chama o método __str__()
    print("Saldo:", pf2.get_saldo())
    pf3 = Conta_PF('Alice', 6000.0)    # Objeto da subclasse Conta_PF
    print(pf3)                          # Chama o método __str__()
    print('CPF:', pf3.get_cpf())        # Método da subclasse
    pj1 = Conta_PJ('Café ABC', 15000.0, 'MEI')  # objeto (instância) da subclasse
    print(pj1)
    print('- Pessoa Jurídica:\nNome:', pj1.get_nome())  # Método da superclasse
    pj2 = Conta_PJ('Pão ABC', 17000.0)  # objeto (instância) da subclasse
    print(pj2)
    print("Saldo:", pj1.get_saldo())
    pf1.retirada_rn2(10)                                     # Retirada com RN
    print("- Pessoa Física 1, depois:\nSaldo:", pf1.get_saldo())    # Verifica
    pj1.retirada_rn2(20)
    print("- Pessoa Jurídica 1, depois:\nSaldo:", pj1.get_saldo())  # Verifica
