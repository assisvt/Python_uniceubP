############### AGREGAÇÃO ####################
"""  CEUB  -  Bacharelado em Ciência da Computação (BCC)  -  Prof. Barbosa
ctlr<d>, duplica linha. ctrl<y>, apaga linha. ctrl</>, comenta linha.

- Neste exercício, não vamos usar herança e nem classe abstrata (ABC).

- Vamos implementar a classe conta corrente.

- Primeira ideia dos atributos da classe ccnta corrente:

número da conta;
nome do titular;
sobrenome do titular;
cpf do titular;
saldo da conta; e
vl_limite da conta.

Obs.: o valor limite é um valor que o banco disponibiliza e o titular pode usar.

- Ideia de agregação:

. Estamos como muitos atributos e uma conta corrente não tem os atributos:
nome, sobrenome e cpf.
. Pois, esses atributos são do titular e não da conta corrente.
. Assim, crie uma nova classe (classe Titular) e faça uma agregação, ou seja,
agrege um objeto da classe Titular a uma conta corrente.
. Portanto, a classe Conta tem um  objeto da classe Titular.
. Os atributos de Conta também podem ser referência (objeto) para outra classe

- Vamos usar agregação na implementação:
Crie a classe Titular com os atributos:
nome do titular;
sobrenome do titular;
cpf do titular.

Crie a classe Conta com os atributos:
número da conta;
obj_titular;
saldo; e
vl_limite.

- Resumo:
Um atributo de uma classe pode ser um objeto de outra classe.
- Exemplo:
O atributo obj_titular da classe Conta é um objeto da classe Titular.

- Valor default na classe Conta:
Na declaração dos parâmetros no construtor da classe Conta, atribua um
valor default (padrão) de 1000.00 reais para o parâmetro valor limite.

- Implemente:
 1- Crie a classe Titular com os atributos cpf, nome, sobrenome
 2- Crie alguns métodos gets e sets
 3- Crie (instancie) um objeto da classe Titular
 4- Crie o método funcional que retora o nome completo do titular, teste
 5- Crie a classe Conta com os atributos numero, obj_titular, saldo, limite.
 6- Crie alguns métodos gets e sets
 7- Crie um objeto da classe Conta usando o objeto da classe Titular criado
 8- No main, mostre o endereço do objeto titular criado
 9- No main, mostre o endereço do objeto conta criado
10- No main, mostre o nome, sobrenome e cpf usando o objeto da classe Titular
11- Altere o nome do objeto titular, teste.
12- No main, mostre o nome, sobrenome e cpf usando o objeto da classe Conta.
13- Altere o nome do objeto titular usando o objeto da classe Conta, teste.

14- Crie o método extrato reduzido para mostrar os seguintes dados:
    número da conta e saldo da conta
15- Crie o método extrato normal para mostrar os seguintes dados:
    nome, sobrenome, cpf, número da conta e saldo da conta
16- Na classe Conta, crie o método parar mostrar todos os dados do atributo
    titular da classe Conta.

17- Faça um depósito, teste.
18- Faça um saque, teste.
19- Refaça o método anterior com uma RN (regra de negócio) do banco,
    ou seja, com crítica.
20- Cadastre mais uma conta corrente, teste
21- Faça uma transferência, teste.
22- Use sua criatividade, elabore o enunciado e implemente mais uma método
    funcional neste sistema.
"""
class Titular(object):
    def __init__(self, cpf, nome, sobrenome):
        self.cpf = cpf
        self.nome = nome
        self.sobrenome = sobrenome
    def get_cpf(self):
        return self.cpf
    def get_nome(self):
        return self.nome
    def set_nome(self, novo_nome):
        self.nome = novo_nome
    def get_sobrenome(self):
        return self.sobrenome
    def nome_completo(self): # Método fucional
        nome_c = self.nome + " " + self.sobrenome # Usa concatenação de strings
        # nome_c = f'{self.nome} {self.sobrenome}' # Usa f-string
        # As duas linhas acima são equivalentes
        return nome_c
class Conta(object): # class Conta:
    def __init__(self, numero, obj_titular, saldo, limite=1000.0):
        self.numero = numero
        self.titular = obj_titular
        # O atributo self.titular recebe o endereço objeto da classe Titular
        self.saldo = saldo
        self.limite = limite
    def get_saldo(self):
        return self.saldo
    def set_saldo(self, novo_saldo):
        self.saldo = novo_saldo
    def get_titular(self):
        return self.titular
    def get_titular_nome(self):
        return self.titular.get_nome()
    def extrato_reduzido(self):
        print(f"Extrato 1:\nNúmero: {self.numero}, Saldo: {self.saldo}")
    def extrato_normal(self):
        print(f'Extrato 2:\nNome: {self.titular.get_nome()}')
        f'{self.titular.get_sobrenome()} CPF: {self.titular.get_cpf()}'
        print(f"\nNúmero : {self.numero}, Saldo: {self.saldo}")
    def deposito(self, valor):          # Métodos funcionais
        self.saldo += valor   
    def saque(self, valor):          # Sem RN (Regra de Negócio)
        self.saldo -= valor 
    def saque_rn(self, valor):       # RN obrigatória (natural do banco)
        if valor > self.saldo:
            print('Saldo insuficiente.')
        else:
            self.saldo -= valor
    def transfere_para(self, destino): # sem critica
        valor = float(input("Valor da retirada:"))
        self.saldo -= valor
        destino.saldo += valor

if __name__ == '__main__':  # Atalho: mai <tab>
    titular1 = Titular('038342045-09', 'Lia', 'Oliveira') # Objeto da classe Titular #3
    print('Nome:', titular1.get_nome())
    print('Nome completo:', titular1.nome_completo())
    conta1 = Conta('123', titular1, 1200.0, 2000.0) 
    titular2 = Titular('038343041-09', 'Lucas', 'Zaher')
    conta2 = Conta('345', titular2, 200.0, 300.0)
    print(titular1) #8
    print(conta1) #9
    conta1.transfere_para(conta2)
