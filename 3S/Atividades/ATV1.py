from abc import ABC, abstractmethod 
class Computador(ABC):
    preco_pc_base = 30
    @classmethod
    def get_preco_base(cls):
        return cls.preco_base
    @classmethod
    def set_preco_base(cls, novo_valor):
        cls.preco_base = novo_valor
    qtd_pc = 0
    @classmethod
    def get_qtd_pc(cls):
        return cls.get_qtd_pc
    def __init__(self, categoria): # Atributo da instância
        self.categoria = categoria
        Computador.qtd_pc += 1   # incrementa o atributo de classe
    def get_categoria(self):  # Método concreto
        return self.categoria
    def set_categoria(self, categoria): # Met Concreto
        self.categoria = categoria
    @abstractmethod
    def preco_diaria(self): # Met Abstrato
        pass
class Basico(Computador): # Superclasse básico, herda da superclasse Computador
    def __init__(self, categoria):
        super().__init__(categoria) # Chamaa Constrturor da sp.c
    def preco_diaria(self):
        val_diaria = Computador.get_preco_base() + Computador.get_preco_base() * 1.05
        return val_diaria

class Potente(Computador):
    def __init__(self, categoria):
        super().__init__(categoria)
    def preco_diaria(self):
        return Computador.get_preco_base() * 1.30
    
if __name__ == '__main__':
    # não tem como instanciar abstract class Computador
    Computador.set_preco_base(50)
    print("Preço inicial do aluguel:", Computador.get_preco_base())
    print('Qtd. Computadores na lan house:', Computador.get_qtd_pc())
    o_bas = Basico('Escritorio')
    print(f'- O Computador {o_bas.get_categoria()} com:')  # Método de superclasse
    print(f'Preço básico: {Computador.get_preco_base()}')  # Método de classe
    print(f'Diária: R$ {o_bas.preco_diaria():.2f}')  # Método da subclasse
    o_pot = Potente('Gamer')
    print(f'- O computador {o_pot.get_categoria()} com')
    print(f'preço básico: {o_pot.get_preco_base()}')
    print('Diária: R$ {:.2f}'.format(o_pot.preco_diaria()))
    Computador.set_preco_base(50.00)  # NomeSuperclasse.nome_metodo_classe(argumento)
    print(f'- O computador {o_bas.get_categoria()} com:')
    print(f'Preço básico: {o_bas.get_preco_base()}')
    print('Diária: R$ {:.2f}'.format(o_bas.preco_diaria()))
    print(f'- O computador {o_pot.get_categoria()} com:')
    print(f'Preço básico: {o_pot.get_preco_base()}')
    print('Diária: R$ {:.2f}'.format(o_pot.preco_diaria()))

    
