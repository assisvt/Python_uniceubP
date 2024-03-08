# - Elabore o programa que gere a sequência dos números naturais pares até 12.

# OPÇÃO 1
for par in range(0, 13, 2):
    print(par, end=" ")                     # Na horizontal.
# o end=" " evita a quebra de linha, o padrão é end="\n"
--

# OPÇÃO 2
for par in range(0, 12 + 1, 1):
    if (par % 2 == 0):
        print(par, end=" ")
