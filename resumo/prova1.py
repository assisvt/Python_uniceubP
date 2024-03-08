"""
1. Crie uma classe com o método construtor e pelo menos três atributos. E use pelo menos um atributo com valor default (padrão).

2. Crie os métodos gets e sets de todos os atributos.

3. Faça crítica (validação) em pelo menos um dos métodos sets.

4. Crie pelo menos dois métodos funcional, ou seja, mais dois métodos além do construtor e dos métodos gets e sets.

5. Sobrescreva o método nativo do Python __str__ , ele deve retornar os atributos da classe concatenados.

* 6. Crie um método que recebe dois objetos e compara um atributo com o valor dos dois objetos instanciados no main.

7. No método main, teste (use) a classe criada, crie pelo menos três objetos dessa classe, um objeto passando três argumentos, um objeto passando dois argumentos e um objeto passando apenas um argumento.

8. E teste (use) todos os métodos desenvolvidos na classe com pelo menos um dos objetos criados. E teste o método de classe desenvolvido
"""

class Iphone():
    def __init__(self, modelo, cor='nula', valor=0.00):
        self.modelo = modelo
        self.cor = cor
        self.valor = valor
    def get_modelo(self):
        return self.modelo
    def set_modelo(self, novo_modelo):
        self.modelo = novo_modelo
    def get_cor(self):
        return self.cor
    def set_cor(self, novo_cor):
        self.cor = novo_cor
    def get_valor(self):
        return self.valor
    def set_valor(self, novo_valor):
        if type (novo_valor) in (int, float): # ou, mais simples: if novo_valor > 0:
            self.valor = novo_valor
        else:
            print('Iconsistência de valor.')  
    def aumenta_valor(self, valor_aumento):
        self.valor += valor_aumento
    def diminui_valor(self, valor_diminui):
        self.valor -= valor_diminui
    def __str__(self):
        s = f'{self.modelo}, {self.cor}, {self.valor}'
        return s
    def maior_valor(self, objeto2):  
        if self.valor > objeto2.valor:
            print("Maior valor:", self.get_modelo())
        elif objeto2.valor > self.valor:
            print("Maior valor:", objeto2.get_modelo())
        else:
            print('Valores iguais.')

if __name__== "__main__":
    iphone1 = Iphone('Iphone 12', 'preto', 5499.00)
    print('Objeto iphone 1:', iphone1)
    print('- Dados iphone 1:')
    print('Modelo:', iphone1.get_modelo())
    print('Cor:', iphone1.get_cor())
    print('Valor:', iphone1.get_valor())
    iphone2 = Iphone('Iphone 14', 'azul')
    print('Objeto iphone 2:', iphone2)
    print('-Dados iphone 2:')
    print('Modelo:', iphone2.get_modelo())
    print('Cor:', iphone2.get_cor())
    iphone3 = Iphone('Iphone 15 pro max')
    print('Objeto iphone 3:', iphone3)
    print('-Dados iphone 3:')
    print('Modelo: ', iphone3.get_modelo())
    iphone1.set_modelo('Iphone 12 mini')
    print('Modelo iphone 1 atualizado:', iphone1.get_modelo())
    iphone1.set_cor('preto fosco')
    print('Cor iphone 1 atualizado:', iphone1.get_cor())
    iphone1.set_valor(5500.00)
    iphone1.aumenta_valor(1000.00)
    iphone1.diminui_valor(500.00)
    print('Valor iphone 1 atualizado:', iphone1.get_valor())
    iphone1.set_valor('mensagem')
    print('-Dados concatenados:', iphone1.__str__())
    iphone1.maior_valor(iphone2)
