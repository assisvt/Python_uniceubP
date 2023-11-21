""" 
- Desenvolva a função converte_em_minuto. Ela recebe o horário no
formato (hora e minuto) e retorna o valor correspondente em minutos.

A função main lê dois horários (hora e minuto) e chama a função
converte_em_minuto duas vezes. Com os valores retornado pela função
converte_em_minuto, a função main mostra a diferença entre os dois
horários em minutos.

Teste 1: Entrada: horas: 2, minutos: 10
         Entrada: horas: 1, minutos: 30   Saída: diferença: 40 minutos."""

def converte_em_minuto(horas, minutos):  # Assinatura da função
    """ Converte hh:mm em minutos. """   # docstring
    vl_minutos = horas * 60 + minutos
    return vl_minutos                    # Retorna o valor calculado

# Início do programa principal
if __name__ == '__main__':               # Atalho: mai <tab>
    h = int(input("Horas: "))            # Lê os dados do horário 1
    m = int(input("Minutos: "))
    horario1 = converte_em_minuto(h, m)  # Chama a função
    h = int(input("Horas: "))            # Lê os dados do horário 2
    m = int(input("Minutos: "))
    horario2 = converte_em_minuto(h, m)  # Chama a função
    diferenca = horario2 - horario1
    print("\nDiferença em minutos dos dois horários: ", diferenca)
