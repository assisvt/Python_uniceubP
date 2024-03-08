""" 
- Com base nos conceitos de POO (Programação Orientada a Objetos),
implemente a entidade ponto no plano cartesiano com estas características:

O valor da coordenada x no plano cartesiano;
O valor da coordenada y no plano cartesiano.

-Implemente os itens:

1- Crie um novo projeto e a classe Point.
2- Crie o método construtor, ele atribui o valor default zero para os parâmetros
   de x e y
3- No construtor, crie os atributos x e y.
4- Na função main, crie o objeto p1 (ponto p1) sem passar argumentos. Teste
5- Crie os métodos gets e sets.
6- Mostre o valor do atributo x e y.
7- Faça pelo menos uma crítica no método set_x (evitar dados inconsistentes), teste
8- Na função main, crie o objeto p2 (ponto p2) passsndo os valores 2 e 3 como
   argumento. Teste
9- Sobrescreva o método __str__. Ele recebe self e retorna todos os atributos
   concatenados. Teste
10- Na função main, crie o objeto p3 (ponto p3) passsndo somente o argumento x.
    Teste
11- Na função main, crie o objeto p4 (ponto p4) passsndo somente o argumento y.
    Teste
12- Crie o método funcional distância de um ponto qualquer a origem (0, 0) do
    plano cartesiano. Ele retorna o valor calculado.
    distancia = raiz_quadrada((x1-x2)^2 + (y1-y2)^2)
    - Obs.:(x1-x2)^2 elevado ao quadrado
    Teste 1: (p2) x = 2 e y = 3                 Distância = 3.605551275463989
    Teste 2: (p4) x = 0 e y = 5                 Distância = 5
13- Crie método funcioanl distancia_dois_pontos, ele retorna a distância de dois
    pontos quaisquer no plano
    Teste 1: P2 (2, 3) e P3 (3, 0)              Distância:  3.1622776601683795
    Teste 2: P2 (2, 3) e P4 (0, 5)              Distância:  2.8284271247461903

"""


import math
# O nome de classe começa com letra maiúscula e as outras letras minúsculas.
# Nome de classe: primeira letra de cada palavra com letra maiúscula
# class Point:
# class Point():
class Point(object):  # Três formas eauivalentes de criar uma classe
    def __init__(self, x=0.0, y=0.0):  # def __init__(self, x, y) # Construtor
        self.x = x              # Atributos de objeto (instância)
        self.y = y
    def get_x(self):            # Método get (retorna o valor de um atributo)
        return self.x
    # def set_x(self, novo_x):  # Método set (altera o valor de um atributo)
    #     self.x = novo_x
    def set_x(self, novo_x):    # Método set com crítica
        # if isinstance(novo_x, int) or isinstance(valor, float):  # Equivalentes
        # if isinstance(novo_x, (int, float)):
        if type(novo_x) in (int, float):
            self.x = novo_x
        else:
            print('Erro: tipo tem que ser int ou float.')
    def get_y (self):
        return self.y
    def set_y(self, novo_y):
        self.y = novo_y
    def __str__(self):                          # Método especial (dunder)
        # s = '('+str(self.get_x()) + ', ' + str(self.get_y()) + ')'
        # s = "({}, {})" .format(self.get_x(), self.get_y())  # (x, y) # (2, 3)
        # s = f"({self.get_x()}, {self.get_y()})"   # (x, y)   # (2, 3)
        s = f"({self.x}, {self.y})"             # (x, y)   # (2, 3)
        return s
    def distancia_origem(self):                 # Método funcional
        distancia = math.sqrt((self.get_x() - 0)**2 + pow(self.get_y() - 0, 2))
        # distancia = math.sqrt(pow(self.x - 0, 2) + (self.y - 0)**2)
        return distancia
    def distancia_dois_pontos(self, objeto2):  # O método recebe 2 objetos
        # distancia = math.sqrt((self.get_x() - objeto2.get_x())**2 +
        #                       (self.get_y() - objeto2.get_y())**2)
        distancia = math.sqrt((self.x - objeto2.x)**2 + (self.y - objeto2.y)**2)
        return distancia
        # return (((self.x - objeto.x) **2) + ((self.y - objeto.y) **2)) ** (1/2)


if __name__ == '__main__':       # Atalho: mai <tab>
    p1 = Point()                 # Instantiate an object of type Point
    print("Objeto p1 da classe Point", p1)  # Duas linhas equivalentes
    print("Objeto p1 da classe Point", p1.__str__())
    # Objeto p1 da classe Point <ponto.Point object at 0x000001CAD8916F70>
    print("Atributo x do ponto p1=", p1.get_x())
    print("Atributo y do ponto p1=", p1.get_y())
    p1.set_x(2)                         # Teste, argumento correto
    print("Atributo x do ponto p1=", p1.get_x())
    p1.set_x('Mensagem')                # Teste, argumento errado
    print("Atributo x do ponto p1=", p1.get_x())
    p2 = Point(2, 3)                    # Chama o método construtor __init__
    print("Dados do objeto p2 da classe Point", p2)  # 2 linhas equivalentes
    print("Dados do objeto p2 da classe Point", p2.__str__())
    print("Atributo x do ponto p2=", p2.get_x())
    print("Atributo y do ponto p2=", p2.get_y())
    p3 = Point(3)                       # Passa só o valor do x
    print("Dados do objeto p3:", p3)    # print("__str__ ", p3.__str__())
    print("Atributo x do ponto p1=", p3.get_x())
    print("Atributo y do ponto p1=", p3.get_y())
    # p4 = Point(0, 5)                  # Solução 1, não é uma boa solução
    p4 = Point(y=5)                     # Solução 2, a solução correta
    print("Dados do objeto p4:", p4)    # print("__str__ ", p4.__str__())
    print("Atributo x do ponto p1=", p4.get_x())
    print("Atributo y do ponto p1=", p4.get_y())
    d2 = p2.distancia_origem()          # Usando variável
    print('Distância da origem de p2:', d2)
    print("Distância da origem:", p2.distancia_origem())
    print("Distância da origem:", p4.distancia_origem())
    # Sintaxe: objeto1.nome_metodo(objeto2)
    print('Distância de 2 pontos:', p2.distancia_dois_pontos(p3))
    print('Distância de 2 pontos:', p2.distancia_dois_pontos(p4))
