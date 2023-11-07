"""                 Comentários de várias linhas.
  CEUB  -  FATECS  -  BCC  -  ADS  -  Programação  -  Prof. Barbosa
ctlr<d>, duplica linha. ctrl<y>, apaga linha. ctrl</>, comenta linha.

PEGAR O EXERCÍCIO NA SALA ON-LINE (MOODLE) - Aula 07/11

- Implemente estes itens:

- Crie três instâncias da subclasse Conta_PF com quatro, três e dois argumentos,
teste
- Crie duas instâncias (objetos) da subclasse Conta_PJ com três e dois argumentos.
Teste
- Use alguns métodos das classes desenvolvidas
- Faça um depósito, teste
- Faça uma retirada, teste

- Refaça o método retirada usando RNs (Regras de Negócios) bancárias. Teste
- A política do sistema bancário mudou, o depósito continua sem cobrado tarifa.
    No saque, a pessoa física tem tarifa de 2 reais e pessoa juridica de 5 reais.
    Então, substitua o método retirada da superclasse por dois métodos retirada nas
    duas subclasse.
- Teste a alteração anterior.
- Crie o método retirada_rn2, substitua os dois método retirada nas duas subclasses
   por um único método (retirada_rn2) na superclasse

"""
# O nome de classe começa com letra maiúscula e as outras letras minúsculas.
# class Conta:
# class Conta():
class Conta(object):                    # Superclasse
    def __init__(self, nome, saldo):  # Construtor  com default
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


# O nome de classe começa com letra maiúscula e as outras letras minúsculas.
# class NomeSubclasse(NomeSuperclasse):     # Sintaxe
class Conta_PF(Conta):      # Subclasse Conta_PF herda da superclasse Conta
    def __init__(self, nome, saldo, genero, cpf=''):  # Valores default
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
    def __init__(self, nome, saldo, modalidade, cnpj=''):  # Construtor
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
    ...
