class Livro:
    def __init__(self, nome, registro='Nulo', valor=0.00):
        self.nome = nome
        self.registro = registro
        self.valor = valor

    def get_nome(self):
        return self.nome
    def set_nome(self, novo_nome):
        self.nome = novo_nome
    
    def get_registro(self):
        return self.registro
    def set_registro(self, novo_registro):
        self.registro = novo_registro

    def get_valor(self):
        return self.valor
    def set_valor(self, novo_valor):
        if novo_valor > 0:
            self.valor = novo_valor
        else:
            print('Inconsistência de valor')
    
    def mostra_dados(self):
        print('Nome:', self.nome)
        print('Registro:', self.registro)
        print('Valor:', self.valor)
        
    def aumenta_valor(self, valor_aumento):
        self.valor += valor_aumento

    def __str__(self):
        s = f"{self.nome}, {self.registro}, {self.valor}"                
        return s

if __name__ == '__main__':
        livro1 = Livro('Ciranda Pedra', 12, 59.99)
        print('Objeto livro 1:', livro1)
        livro2 = Livro('A Cor Púrpura', 321)
        print('Objeto livro 2:', livro2)
        livro3 = Livro('O milagre da manhã')
        print('Objeto livro 3', livro3)
        print('-Dados livro 1:\nNome:', livro1.get_nome(), '\nRegistro:', 
        livro1.get_registro(), '\nValor:', livro1.get_valor())
        print('-Dados livro 2:\nNome:', livro2.get_nome(), '\nRegistro:', 
        livro2.get_registro())
        print('-Dados livro 3:\nNome:', livro3.get_nome())
        livro1.set_nome('Ciranda de Pedra')
        print('#'*30)
        print('Nome atualizado:', livro1.get_nome())
        livro1.set_registro(123)
        print('Registro Atualizado:', livro1.get_registro())
        livro1.set_valor(65.99)
        print('Valor atualizado:', livro1.get_valor())
        livro1.aumenta_valor(2.00)
        print('Valor com aumento:', livro1.get_valor())
        print('#'*30)
        livro1.mostra_dados()
        print('Dados concatenados:', livro1.__str__())
