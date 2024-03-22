"""            Comentários de várias linhas.

  CEUB  -  FATECS  -  BCC  -  ADS  -  Programação  -  Prof. Barbosa
ctlr<d>, duplica linha. ctrl<y>, apaga linha. ctrl</>, comenta linha.

Teoria:
- Uma classe abstrata deve herdar de ABC (Abstract Base Classes)
- A superclasse abstrata FormaGeometrica com os métodos abstratos area e perímetro.
- As subclasses concretas Circulo e Quadrado herdam da superclasse abstrataf
  FormaGeometrica e tem que implementar todos os métodos abstratos da superclasse.

- Analise o problema da figura geométrica e o cálculo da área e do perímetro.
O gerente do sistema precisa implantar a RN (regra de negócio) que toda subclasse
incluida no sistema precisa ter a funcionalidade de cálculo da área e cálculo
do perímetro.

Implemente os itens:

1- Crie a superclasse abstrata FormaGeometrica que herda de ABC (Abstract Base Classes)
2- Crie os dois métodos abstratos area e perímetro
3- Crie um objeto da superclasse abstrata FormaGeometrica, teste
4- Crie a subclasse Quadrado que herda da superclasse abatrata FormaGeometrica
5- Crie o construtor com o atributo lado, teste
6- Crie os métodos get e set, teste
7- Sobreescreva o método abstrato area da superclasse abstrata FormaGeometrica
   area = lado ao quadrado.
8- Crie um objeto da subclasse Quadrado, teste
9- Sobreescreva também o método perímetro da superclasse abstrata
   perimetro = 4 . lado
10- Crie um objeto da subclasse Quadrado, teste
11- Altere o valor do lado, teste
12- Crie a subclasse Circulo que herda da superclasse abstrata FormaGeometrica
13- Crie o construtor com o atributo raio, teste
14- Crie os métodos get e set, teste
15- Sobreescreva o método abstrato area da superclasse abstrata FormaGeometrica
    area = π . raio ao quadrado
16- Crie um objeto da subclasse Circulo, teste
17- Sobreescreva também o método perímetro da superclasse abstrata
    perimetro = 2 . π . raio
18- Crie um objeto da subclasse Circulo, teste
19- Refaça a subclasse Circulo com a constante pi do Python, mostre com duas casas decimais
20- Crie um método concreto na superclasse para mostrar uma menscagem fixa, teste

21- Crie mais um método concreto para mostrar uma mensagem na superclasse
    e identifique o objeto da subclasse que chamou o método, teste
22- Refaça o anterrior sem mostrar o endereço hexadecimal, mostre só o nome da classe

23- O sistema precisa informar quantas figuras geométricas foram cadastradas na
    memória (instanciadas). Para isso, crie o atributo de classe e o método de
    classe necessários para atender essa necessidade (funcionalidade).
    Esse método de classe não recebe nada e retorna a quantidade de figuras criadas.

Prof. Barbosa
"""


from abc import ABC, abstractmethod  # Importa o módulo abc (abstract base classes)
class FormaGeometrica(ABC):          # Classe abstrata, herda da classe ABC
    qtd_figura = 0                   # Atributos de classe
    @classmethod                     # Métodos de classe (decorator)
    def get_qtd_figura(cls):
        return cls.qtd_figura        # return cls.nomeAtributoClasse
        # return FormaGeometrica.qtd_figura  # return NomeClasse.nomeAtributoClasse
    def __init__(self):
        FormaGeometrica.qtd_figura += 1
    @abstractmethod                  # Decorator
    def area(self):                  # Método abstrato
        ...                          # Equivalente: pass
    @abstractmethod                  # Decorator
    def perimetro(self):             # Método abstrato
        pass                         # Equivalente: ...
    def mensagem(self):              # Método concreto
        print('Método concreto da superclasse abstrata FormaGeometrica, herda de ABC')
    def mensagem2(self):             # Método concreto
        print('Método concreto da superclasse abstrata FormaGeometrica, herda de ABC')
        print('Dados do obejto:', self)
    def mensagem3(self):             # Método concreto
        print('Método concreto da superclasse abstrata FormaGeometrica, herda de ABC')
        print('Nome da classe:', self.__class__.__name__)

class Quadrado(FormaGeometrica):  # class NomeSubclasse(NomeSuperclasse):  (sintaxe)
    def __init__(self, lado):
        super().__init__()
        self.lado = lado
    def get_lado(self):
        return self.lado
    def set_lado(self, valor):
        self.lado = valor
    def area(self):                     # Obrigatório
        vl_area = self.lado ** 2        # vl_area = self.lado * self.lado
        return vl_area
    def perimetro(self):                # Obrigatório
        vl_perimetro = 4 * self.lado
        return vl_perimetro

class Circulo(FormaGeometrica):  # class NomeSubclasse(NomeSuperclasse):  (sintaxe)
    def __init__(self, raio=1):             # Construtor
        super().__init__()
        self.raio = raio                    # Atributo
    def get_raio(self):
        return self.raio
    def set_raio(self, valor):
        self.raio = valor
    def area(self):                         # Obrigatório
        vl_area = 3.14 * pow(self.raio, 2)  # vl_area = 3.14 * self.raio ** 2
        return vl_area
    def perimetro(self):                    # Obrigatório
        vl_perimetro = 2 * 3.14 * self.raio
        return vl_perimetro

if __name__ == '__main__':
    obj_quad = Quadrado(3)                  # Objeto da subclasse Quadrado
    print('Área:', obj_quad.area())
    print('Perímetro:', obj_quad.perimetro())
    obj_quad.set_lado(4)                    # Altera o valor do lado
    print('Lado:', obj_quad.get_lado())
    print('Área:', obj_quad.area())
    print('Perímetro:', obj_quad.perimetro())
    obj_circ = Circulo(3)                   # Objeto da subclasse Circulo
    print('- Círculo:\nRaio:', obj_circ.get_raio())
    print('Área:', obj_circ.area())
    print('Perímetro:', obj_circ.perimetro())
    obj_circ.set_raio(2)
    print(f"Área: {obj_circ.area():.3f}")          # Com três casas decimais
    print('Perímetro:', obj_circ.perimetro())

