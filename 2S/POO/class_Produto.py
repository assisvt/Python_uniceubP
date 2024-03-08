class Produto: # class Aluno(): # class Aluno(object):
    def __init__(self, nome, vlr_compra, vlr_venda, qtd_estoque, qtd_minima):
        self.nome = nome
        self.vlr_compra = vlr_compra 
        self.vlr_venda = vlr_venda
        self.qtd_estoque = qtd_estoque
        self.qtd_minima = qtd_minima
    def get_nome(self): # Métodos gets (consulta)
        return self.nome
    def set_nome(self, novo_nome):  # Métodos sets (altera)
        self.nome = novo_nome

    def get_vlr_compra(self):
        return self.vlr_compra
    def set_vlr_compra(self, novo_vlr_compra):
        self.vlr_compra = novo_vlr_compra

    def get_qtd_estoque(self):
        return self.qtd_estoque
    def set_qtd_estoque(self, nova_qtd_estoque):
        if type(nova_qtd_estoque) == int: # if isinstance(nova_qtd_estoque, int):
            self.qtd_estoque = nova_qtd_estoque
        else:
            print('Erro: qtd. estoque deve ser int.')

    def get_qtd_minima(self):
        return self.qtd_minima
    def set_qtd_minima(self, novo_qtd_minima):
        self.qtd_minima = novo_qtd_minima

    def __str__(self):
        s = f'Nome: {self.nome}, {self.vlr_compra}, {self.vlr_venda},'\
            f'{self.qtd_estoque}, {self.qtd_minima}'
        return s
    def lucro(self): # TESTAR
        vlr_lucro = self.vlr_venda - self.vlr_compra
        return vlr_lucro
    def atualiza_estoque(self, qtd_vendida): # TESTAR
        self.qtd_estoque -= qtd_vendida
    def repor_produto(self, qtd_comprada): # TESTAR
        self.qtd_estoque += qtd_comprada
    def alerta_estoque(self): # TESTAR
        if self.qtd_estoque < self.qtd_minima:
            var = True
        else:
            var = False
        return var
if __name__ == '__main__':
    prod_1 = Produto('Arroz', 19.00, 27.50, 67, 20) # Chama método __init__ (construtor)
    print(prod_1) # Mostra o end. hexadecimal onde o objeto foi armazenado # quanto usa o def __str__ ele é chamado assim, subscrevendo o end hexa
    print('Produto 1:\nNome:', prod_1.get_nome(), '\nQtd. Estoque:', prod_1.get_vlr_compra(),
    '\nValor de Compra:', prod_1.get_vlr_compra(), '\nQtd. minima:', prod_1.get_qtd_minima())
    qtd = int(input('Quantidade minima: ')) # qtd = 22
    prod_1.set_qtd_minima(qtd)
    print('Qtd. minima alterada:', prod_1.get_qtd_minima())
    prod_1.set_qtd_estoque(30)
    print('Qtd. estoque alterado:', prod_1.get_qtd_estoque())
    prod_1.set_qtd_estoque('Nome')
    print('Qtd. estoque não alterou:', prod_1.get_qtd_estoque())
