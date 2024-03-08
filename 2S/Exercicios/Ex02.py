class Iphone():
    def __init__(self, modelo, cor='Nula', valor=0.00):
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
        if novo_valor > 0: # Crítica
            self.valor = novo_valor
        else:
            print('Inconsistência de valor')
    
    def mostra_dados(self):
        print('Modelo:', self.modelo)
        print('Cor:', self.cor)
        print('Valor:', self.valor)

    def retorna_dados(self):
        dados = f'{self.modelo}, {self.cor}, {self.valor}'
        return dados
    def diminui_valor(self, valor_diminui):
        self.valor -= valor_diminui

if __name__ == '__main__':
    iphone1 = Iphone('iPhone 12', 'Preto', 5499.00)
    print('Objeto iPhone 1:', iphone1) # end hexa
    print('- Dados do iPhone 1:')
    retorno = iphone1.get_modelo()
    print('Modelo:', retorno)
    print('Cor:', iphone1.get_cor())
    print(f'Valor: R$ {iphone1.get_valor():.2f}')
    iphone1.set_modelo('Iphone 12 mini')
    print('Modelo atualizado iPhone 1:', iphone1.get_modelo())
    iphone1.diminui_valor(500.00)
    print('Valor atualizado iPhone 1:', iphone1.get_valor())
    iphone1.mostra_dados()
    
    print('- Dados do iPhone 2:')
    iphone2 = Iphone('iPhone 14 Pro Max', 'Dourado')
    print('Objeto iPhone 2', iphone2)
    iphone2.mostra_dados()

    print('- Dados do iPhone 3:')
    iphone3 = Iphone('iPhone SE')
    print('Objeto iPhone 3', iphone3)
    iphone3.mostra_dados()
