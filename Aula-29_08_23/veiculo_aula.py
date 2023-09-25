""" 
- Com base nos conceitos de POO (Programação Orientada a Objetos), implemente
a entidade veículo com estas características:
modelo, ano e valor.

- Implemente:

1- Crie um programa .py e a classe Veiculo
2- Crie o construtor da classe com os atributos: modelo, ano, valor
3- No main, crie pelo menos dois objetos da classe. Teste
4- Crie os métodos gets dos atributos. Teste os gets
   def get_nome_atributo1(self):              # Modelo do método get (consulta)
       return self.nome_atributo1
5- Crie os métodos sets dos atributos. Teste os sets
   def set_nome_atributo1(self, novo_valor):  # Modelo do método set (altera)
       self.nome_atributo1 = novo_valor
   Com o método set_modelo, altere o modelo do veiculo. Teste
6- Altere o valor do veiculo, com o método set_valor. Teste
7- Faça uma crítica no método set_valor para evitar dados inconsistentes. Teste
8- Crie o método mostra_dados. Ele mostra todos os atributos da classe. Teste
9- Crie o método retorna_dados, ele retorna os dados (atritutos) concatenados.
   Teste
10- Crie o método aumenta_valor. Ele recebe o valor do aumento em reais que será
    acrescentado ao atributo valor do carro. Teste
11- Peça pro usuário fornecer o valor do aumento do veículo. Teste
12- Altere o construtor para o usuário instanciar um objeto sem valor,
    valor default 0. Ele fornece somente o modelo e ano. Teste, crie um novo
    objeto só com o modelo e ano.
13- Crie mais um objeto passando apenas o modelo do veículo, teste
14- Crie mais um objeto passando apenas o modelo e o valor, não passe o ano.
    Teste

"""


# O nome de classe começa com letra maiúscula e as outras letras minúsculas
# class Veiculo:
# class Veiculo():
class Veiculo(object):                # Três formas equivalentes de criar classe
    # def __init__(self, modelo, ano, valor):  # Atalho: def _ <tab>  # Construtor
    def __init__(self, modelo, ano=0, valor=0.00):  # Construtor com valor default
        self.modelo = modelo                 # Atributos
        self.ano = ano
        self.valor = valor
    def get_modelo(self):                       # Método get (consulta)
        return self.modelo
    def set_modelo(self, novo_modelo):          # Método set (altera)
        self.modelo = novo_modelo
    def get_ano(self):
        return self.ano
    def set_ano(self, novo_ano):
        self.ano = novo_ano
    def get_valor(self):
        return self.valor
    # def set_valor(self, novo_valor):          # Sem crítica
    #     self.valor = novo_valor
    def set_valor(self, novo_valor):            # Com crítica
        if novo_valor > 0:
            self.valor = novo_valor
        else:
            print("Erro: valor inconsistente, valor negativo.")
    def mostra_dados(self):                     # Solução 1, com atributos
        print('Modelo:', self.modelo)
        print('Ano:', self.ano)
        print('Valor:', self.valor)
    def retorna_dados(self):
        dados = f'{self.modelo}, {self.ano}, {self.valor}'          # f-string
        return dados
        # retun f'{self.modelo}, {self.ano}, {self.valor}'
    def aumenta_valor(self, valor_aumento):
        self.valor = self.valor + valor_aumento   # self.valor += valor_aumento
    def aumenta_pct(self, pct):
        self.valor = self.valor + self.valor * pct / 100


if __name__ == '__main__':                  # Atalho: mai <tab>
    carro1 = Veiculo('HB', 2022, 80000.00)  # chama o método __init__ (construtor)
    print("Objeto carro 1:", carro1)        # Teste
    # <veiculo.Veiculo object at 0x0000024149FF6FD0>  # Endereço hexadecimal
    carro2 = Veiculo('Corolla', 2021, 100000.00)
    print("Objeto carro 2:", carro2)
    # <veiculo.Veiculo object at 0x0000024149FF6F70>
    print("- Dados do carro 1:")
    retorno = carro1.get_modelo()               # Usa variável
    print("Modelo:", retorno)
    # print("Modelo:", carro1.get_modelo())     # Equivalente as 2 anteriores
    print("Ano:", carro1.get_ano())
    print(f"Valor: R$ {carro1.get_valor():.2f}")  # Valor com duas casas decimais
    print("- Dados do carro 2:")
    print("Modelo:", carro2.get_modelo())       # Direto no print
    print("Ano:", carro2.get_ano())
    print(f"Valor: R$ {carro2.get_valor():.2f}")
    carro1.set_modelo('HB20')           # Altera (substitui) o vavlor do objeto
    print("Modelo atualizado:", carro1.get_modelo())  # Confirma a alterção
    carro2.set_valor(122000.00)         # Altera (substitui) o valor do objeto
    print("Valor atualizado:", carro1.get_valor())    # Confirma a alterção
    carro2.set_valor(-62000.00)         # Argumento (valor) inconsitente
    print("Valor atualizado:", carro2.get_valor())    # Verifica se alterou
    carro1.mostra_dados()
    carro2.mostra_dados()
    print('Dados concatenados do carro 1:', carro1.retorna_dados())
    print('Dados concatenados do carro 2:', carro2.retorna_dados())
    carro1.aumenta_valor(1900.00)               # Passa o argumento (1900.00)
    print("Valor atualizado:", carro1.get_valor())  # Confirma
    vl_aumento = float(input("Valor aumento: "))    # vl_aumento = 22.22
    carro2.aumenta_valor(vl_aumento)            # Usuário digitou no input
    print("Valor atualizado com input:", carro2.get_valor())  # Confirma
    carro3 = Veiculo('Honda', 2020)     # Chama o método __init__ (construtor)
    print("- Carro 3:")
    print("Valor:", carro3.get_valor())         # Testes
    carro3.mostra_dados()
    print('Dados concatenados:', carro3.retorna_dados())
    carro4 = Veiculo('Argo')            # Chama o método __init__ (construtor)
    print("- Carro 4:")
    carro4.mostra_dados()                # teste
    carro5 = Veiculo('Argo', valor=80000.0)  # Coloca o nome do parâmetro
    carro5.mostra_dados()                # teste
