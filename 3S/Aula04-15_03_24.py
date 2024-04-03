############ ABC (Abstract Base Classes) ###################
"""            Comentários de várias linhas.

  CEUB  -  Bacharelado em Ciência da Computação (BCC)  -  Prof. Barbosa
ctlr<d>, duplica linha. ctrl<y>, apaga linha. ctrl</>, comenta linha.

- Uma classe abstrata deve herdar de ABC (Abstract Base Classes)
- Analise o problema de locação de carros e o valor da diária.

- O valor do preço básico de locação é o mesmo (R$ 100.00) para
os dois tipos de carro, como podemos modelar as classes.

Obs.: RN (Regra de Negócio) para o carro econômico:
      O preço da diária corresponde ao preço base de locação acrescido de 5%
Obs.: RN (Regra de Negócio) para o carro intermediário:
      O preço da diária corresponde ao preço base de locação acrescido de 10%
Obs.: RN (Regra de Negócio) para carro automático:
      O preço da diárioa corresponde ao preço base de locação acrescido de 25%

- Implemente:

1- Crie a superclasse abstrata Carro
2- Crie o construtor com o atributo de instância modelo
3- Crie os métodos de instância get_modelo e set_modelo
4- Crie o método abstrato preço da diária
5- Crie um objeto da superclasse abstrata Carro, teste
6- Crie o atributo de classe preço base de locação com valor fixo de R$ 100.00
7a- Crie os métodos de classe get_preco_base e set_preco_base
7b- Altere o preço base de locação do carro pelo sistema, teste
8- Crie a subclasse Economico com o atributo modelo.
9- No construtor da subclasse, chame o construtor da superclasse e passe o modelo
10- Crie um objeto da subclasse Economico, teste
11- Sobrescreva o método abstrato da superclasse
    Obs.: RN (Regra de Negócio) para o carro econômico:
    O preço da diária corresponde ao preço base de locação acrescido de 5%
12- Crie um objeto da subclasse Economico, teste
13- Crie a subclasse Intermediário com o atributo modelo.
14- No construtor da subclasse, chame o construtor da superclasse e passe o modelo
15- Crie um objeto da subclasse Intermediário, teste
16- Sobrescreva o método abstrato da superclasse
    Obs.: RN (Regra de Negócio) para o carro intermediário:
    O preço da diária corresponde ao preço base de locação acrescido de 10%
17- Crie um objeto da subclasse Intermediário, teste

18- O sistema precisa informar a quantidade de objetos instanciados (cadastrados).
    Crie o atributo de classe para contar a quantidade de objetos instanciados (criados).
19- Atualize o construtor para implementar esse requisito (funcionalidade).
20- Crie o método de classe para consultar a quantidade de objetos instanciados
    (cadastrados). Teste

21- Refaça o exercício anterior sem usar o atributo de classe, o contador.
    Nesta solução, use uma lista.

"""


from abc import ABC, abstractmethod  # Módulo abc
class Carro(ABC):                # Superclasse abstrata Carro que herda de ABC
    preco_base = 100                 # Atributo de classe
    @classmethod                     # Decorator
    def get_preco_base(cls):         # Método de classe
        return cls.preco_base
    @classmethod
    def set_preco_base(cls, novo_valor):  # Método de classe
        cls.preco_base = novo_valor
    qtd_carro = 0                    # Atributo de classe.
    @classmethod                     # Decorator
    def get_qtd_carro(cls):          # Método de classe
        return cls.qtd_carro
    def __init__(self, modelo):
        self.modelo = modelo         # Atributo de instância
        Carro.qtd_carro += 1         # Incrementa o atributo de classe
    def get_modelo(self):            # Método concreto
        return self.modelo
    def set_modelo(self, modelo):    # Método concreto
        self.modelo = modelo
    @abstractmethod                  # Decorator, obrigatório
    def preco_diaria(self):          # Método abstrato
        pass                         # ...


class Economico(Carro):   # Subclasse Economico que herda da superclasse Carro
    def __init__(self, modelo):
        super().__init__(modelo)     # Chama o construtor da superclasse Carro

    # Método obrigatório, sobrescreve o método abstrato da superclasse
    def preco_diaria(self):          # Método obrigatório
        val_diaria = Carro.get_preco_base() + Carro.get_preco_base() * 0.05
        # val_diaria = Carro.get_preco_base() * 1.05
        # NomeClasse.nome_metodo_classe()
        return val_diaria


class Intermediario(Carro):
    def __init__(self, modelo):
        super().__init__(modelo)                          # Modo 1

    # Método obrigatório, sobrescreve o método abstrato da superclasse
    def preco_diaria(self):
        return Carro.get_preco_base() * 1.10
        # return self.get_preco_base() * 1.10


if __name__ == '__main__':
    # o_carro = Carro('Corolla')                       # TypeError:
    # Can't instantiate abstract class Carro with abstract method retorna_preco_diaria
    Carro.set_preco_base(200)
    print("Preço base de locação:", Carro.get_preco_base())  # NomeClasse.
    # print('Qtd. carros cadastrados:', Carro.get_qtd_carro())
    o_eco = Economico('Uno')  # Objeto da subclasse Economico
    print(f'- O carro {o_eco.get_modelo()} com:')  # Método de superclasse
    # print(f'Preço básico: {o_eco.get_preco_base()}')  # Método de classe, equivalentes
    print(f'Preço básico: {Carro.get_preco_base()}')  # Método de classe
    print(f'Diária: R$ {o_eco.preco_diaria():.2f}')  # Método da subclasse
    print('Diária: R$ {:.2f}'.format(o_eco.preco_diaria()))  # Método da subclasse
    o_int = Intermediario('HB20')
    print(f'- O carro {o_int.get_modelo()} com:')
    print(f'Preço básico: {o_int.get_preco_base()}')
    print('Diária: R$ {:.2f}'.format(o_int.preco_diaria()))
    Carro.set_preco_base(200.00)  # NomeSuperclasse.nome_metodo_classe(argumento)
    print(f'- O carro {o_eco.get_modelo()} com:')
    print(f'Preço básico: {o_eco.get_preco_base()}')
    print('Diária: R$ {:.2f}'.format(o_eco.preco_diaria()))
    o_int = Intermediario('HB20')
    print(f'- O carro {o_int.get_modelo()} com:')
    print(f'Preço básico: {o_int.get_preco_base()}')
    print('Diária: R$ {:.2f}'.format(o_int.preco_diaria()))
