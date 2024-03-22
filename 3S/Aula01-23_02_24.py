"""             Comentários de várias linhas.
  CEUB  -  FATECS  -  BCC  -  ADS  -  Programação  -  Prof. Barbosa
ctlr<d>, duplica linha. ctrl<y>, apaga linha. ctrl</>, comenta linha.

- Implemente:
 1- Crie a classe Livro com os atributos: título, autor, páginas e preço.
 2- Crie o método construtor (init) que recebe quatro parâmetros e
   use pelo menos um desses parâmetros com valor default (padrão) 
 3- Crie o objeto livro1 passando os quatro argumentos, teste
 4- Crie o objeto livro2 passando apenas três argumentos, teste
 5- Crie pelo menos um método get e pelo menos um método set, teste
 6- No item anterior, faça crítica no método set, teste
 7- Crie o método funcional aumento_preco com o objetivo de atualizar o preço do livro.
   Esse método recebe o valor do aumento e atualiza o atributo preco. Teste
 8- Use (teste) todos os métodos criados na classe Livro para os objetos livro1 e livro2.
 9- Crie o método mostra_dados, mostra todos os valores dos atributos
 10- Crie o método funcional aumento_porcentagem para atualizar o preço
 11- Crie o mètodo __str__
 12- Elabore o enunciado de mais um método funcional importante para a classe

- O sistema precisa informar quantos livros foram cadastrados.
14- Crie o método de classe para recuperar essa informação

15- Armazene os livros criados (instanciados).
16- Crie o método para mostrar todos os livros cadastrados (instanciados).
- Acrescente o número do livro, a seguência.
18- Mostre os atributos de todos os livros.

"""

class Livro(object):
    qtd_titulo = 0
    @classmethod
    def get_qtd_titulo(cls):
      return cls.qtd_titulo
    
    def __init__(self, titulo, autor, paginas, preco=0.0):
      self.titulo = titulo
      self.autor = autor
      self.paginas = paginas
      self.preco = preco

    def get_titulo(self):
      return self.titulo
    
    def get_preco(self):
      return self.preco
    
    def set_titulo(self, novo_titulo):
      if type(novo_titulo) == str:
            self.titulo = novo_titulo
      else:
          print('Erro: nome deve ser string.')
    def aumenta_preco(self, preco_aumento):
      self.preco = self.preco + preco_aumento

    def mostra_dados(self): # Mostra atributos
      print('- Título:', self.titulo)
      print('Autor:', self.autor)
      print('Páginas:', self.paginas)
      print('Preço:', self.preco)
    
    def aumento_pct(self, pct):
      self.preco = self.preco + self.preco * pct/100
      print(f'Novo valor do livro é {self.preco} reais.')

    def __str__(self):
        s = f'{self.titulo}, {self.autor}, {self.paginas}, {self.preco}'
        return s
    
if __name__ == '__main__':
  livro1 = Livro('Harry Potter', 'J.K. Rowling', 210, 41.42)
  print(livro1)
  livro2 = Livro('Torto Arad', 'Lygia Fagundes Telles', 190)
  print(livro2)
  retorno = livro1.get_titulo()
  print('Titulo:', retorno)
  livro1.set_titulo('Harry Potter e a Pedra filosofal')
  print('Novo título:', livro1.get_titulo())
  livro1.set_titulo(8)
  livro1.aumenta_preco(10)
  print('Novo preço Livro 1:', livro1.get_preco())
  livro2.set_titulo('Torto Arado')
  print('Novo título Livro 2:', livro2.get_titulo())
  livro2.aumenta_preco(100)
  print('Novo preço livro 2:', livro2.get_preco())
  livro1.mostra_dados()
  livro1.aumento_pct(10)
  print('Preço:', livro1.get_preco())
   
    
