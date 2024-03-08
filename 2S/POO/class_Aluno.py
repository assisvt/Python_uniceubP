class Aluno: # class Aluno(): # class Aluno(object):
    def __init__(self, nome, mensalidade, idade): # construtor da classe
        self.nome = nome
        self.mensalidade = mensalidade 
        self.idade = idade
    def get_nome(self): # Métodos gets (consulta)
        return self.nome
    def set_nome(self, novo_nome):  # Métodos sets (altera)
        self.nome = novo_nome
    def get_mensalidade(self):
        return self.mensalidade
    def set_mensalidade(self, valor):
        self.mensalidade = valor
    def get_idade(self):
        return self.idade
    def set_idade(self, nova_idade):
        self.idade = nova_idade
    def mostra_dados(self): # 7. Solução 1, com atributos
        print('- Nome: ', self.nome)
        print('Mensalidade:', self.mensalidade)
        print('Idade:', self.idade)
    def retorna_dados(self): # 8. Métodos funcionais
        # dados = f'{self.nome}, {self.mensalidade}, {self.idade}'
        dados = f'{self.get_nome()}, {self.get_mensalidade()}, {self.get_idade()}'
        return dados
    def aumento_mensalidade_valor(self, aumento): # 9
        self.mensalidade += aumento # FALTA TESTAR NO MÉTODO MAIN
if __name__ == '__main__':
    aluno1 = Aluno('Vitor', 1000.00, 23) # Chama método __init__ (construtor)
    print(aluno1) # Mostra o end. hexadecimal onde o objeto foi armazenado
    aluno2 = Aluno('Carla', 900.00, 20)
    print(aluno2)
    print('- Aluno 1:')
    print('Nome:', aluno1.get_nome()) #print(nome_objeto.nome_metodo()) # 5
    print('Mensalidade:', aluno1.get_mensalidade())
    print('-Aluno 2:')
    print(f'Nome: {aluno2.get_nome}') # print(nome_objeto.nome_metodo())
    aluno1.set_nome('Ailton') # nome_objeto.nome_metodo() - não retorna nada # 6
    print('Nome atualizado:', aluno1.get_nome()) # Verifica (testa)
    aluno1.mostra_dados() # nome_objeto.nome_metodo() - não retorna dado
    aluno2.mostra_dados()
    print('Dados concatenados do aluno 1: \n', aluno1.retorna_dados()) # 8
    print('Dados concatenados do aluno 2: \n', aluno2.retorna_dados()) # 8
