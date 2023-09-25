"""   
- Desenvolva a função converte em minutos. Ela recebe dois valores
inteiros que corresponde ao horário no formato (hora e minuto) e
retorna um valor inteiro que corresponde ao horário convertido em
minutos.
O programa principal (main) lê o horário (hora e minuto), chama a
função converte em minutos passando os dois argumentos (hora e minuto)
e com o valor retornado pela função, mostra uma mensagem apropriada,
ou seja, o horário convertido em minutos. No final do programa
principal, mostre também o valor da hora e do minuto lidos.

Teste 1: Entrada: horas: 1, minutos: 30     Saída: 90 minutos.
Teste 2: Entrada: horas: 2, minutos: 10     Saída: 130 minutos.  """

def converte_em_minuto(horas, minutos):     # Assinatura da função
    """ Converte hh:mm em minutos. """      # docstring
    vl_minutos = horas * 60 + minutos
    return vl_minutos                       # Retorna o valor calculado
# Início do programa principal
if __name__ == '__main__':                  # Atalho: mai <tab>
    h = int(input("Horas: "))               # Lê os dados de entrada
    m = int(input("Minutos: "))
    retorno = converte_em_minuto(h, m)      # Chama a função
    print(h, "horas e", m, "minutos =", retorno, "minutos.")
    print("{} horas e {} minutos = {} minutos." .format(h, m, retorno))
    print(f"{h} horas e {m} minutos = {retorno} minutos.")
''' ----- ALTERAÇÕES:
a. Chame a função converte_em_minuto pelo menos duas vezes.
   retorno = converte_em_minuto(10, 20)  # Acrescente no final do main.  # a.
   print(f"{h} horas e {m} minutos = {retorno} minutos.")
b. Crie a função converte_em_minuto_2, que recebe dois números inteiros
   (hora e minuto) e mostra o valor da conversão. A função não retorna nada.
def converte_em_minuto_2(horas, minutos):   # Assinatura da função       # b.
    vl_minutos = horas * 60 + minutos
    print(f"{horas} horas e {minutos} minutos totalizam {vl_minutos} minutos.")
if __name__ == '__main__':                          
    h = int(input("Horas: "))                       # Lê os dados de entrada
    m = int(input("Minutos: "))
    converte_em_minuto_2(h, m)                      # Chama a função

c. Crie a função le_valor_inteiro. Ela não recebe nada e retorna o valor lido. 
   No programa principal, substitua os dois inputs por duas chamadas a função 
   le_valor_inteiro.

'''
