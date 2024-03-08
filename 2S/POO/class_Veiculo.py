################# terminar de arrumar ##########################
class Veiculo:
    def __init__(self, modelo, ano, valor):
        self.modelo = modelo
        self.ano = ano
        self.valor = valor
        Veiculoqtd_veiculo += 1
    def get_modelo(self):
        return self.modelo
    def set_modelo(self, novo_modelo):
        self.modelo = novo_modelo
    def get_ano(self):
        return self.ano
    def set_ano(self, novo_ano):
        self.ano = novo_ano
    def get_valor(self):
        return self.valor
    def set_valor(self, novo_valor):
        if novo_valor > 0:
            self.valor = novo_valor
        else:
            print('Erro: valor inconsistente, valor negativo.')
    def mostra_dados(self):
        print('Modelo:', self.modelo)
        print('Ano:', self.ano)
        print('Valor:', self.valor)
    def retorna_dados(self):
        dados = f'Modelo: {self.modelo}, {self.ano}, {self.valor}'
        return dados
    def aumenta_valor(self, valor_aumento):
        self.valor = self.valor + valor_aumento
    def aumenta_pct(self, pct):
        dados = f'{self.modelo}, {self.ano}, {self.valor}'
        return dados
if __name__ == '__main__':
    carro1 = Veiculo('HB', 2022, 80000.00)
    print('Objeto carro 1:', carro1)
    carro2 = Veiculo('Corolla', 2021, 100000.00)
    print('Objeto carro 2:', carro2)
    print('- Dados do carro 1:')
    print('Modelo:', carro1.get_modelo())
    print('Ano:', carro1.get_ano())
    print(f'Valor: R$ {carro1.get_valor():.2f}')
    print('- Dados do carro 2:')
    print('Modelo:', carro2.get_modelo())
    print('Ano:', carro2.get_ano())
    print(f'Valor: R$ {carro2.get_valor():.2f}')
    carro1.set_modelo('HB20')
    print('Modelo carro 1, antes "HB", agora atualizado:', carro1.get_modelo())
    carro2.set_valor(122000.00)
    print('Valor atualizado carro 1:', carro1.get_valor())
    carro2.set_valor(-62000.00)
    print('Valor atualizado carro2:', carro2.get_valor())
    print('='*30)
    carro1.mostra_dados()
    carro2.mostra_dados()
    print('Dados concatenados do carro 1:', carro1.retorna_dados())
    print('Dados concatenados do carro 2', carro2.retorna_dados())
    carro1.aumenta_valor(1900.00)
    print('Valor atualizado:', carro1.get_valor())
    vl_aumento = float(input('Valor aumento:'))
    carro2.aumenta_valor(vl_aumento)
    print
