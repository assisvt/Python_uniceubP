'''- Resolva sem lista

- Elabore o programa que gere a sequência dos números naturais até 10 na
horizontal.'''

print("- Números naturais na horizontal:")
for num in range (0, 11, 1): # para cada item i no intervalo entre 0 e 10
    print(num, end=" ")  # O end=" " evita a quebra de linha, o default é end="\n" (quebra de linha)
print('\nEncerrou o programa.')

''' ----- ALTERAÇÕES:
a. Coloque cinco espaços entre cada número.
b. Retire os cinco espaços e coloque uma vírgula entre os números da sequência.
c. Retire a vírgula do último número da sequência e coloque um ponto final.  '''

# a.
print("- Números naturais na horizontal:")
for num in range (0, 11, 1): # para cada item i no intervalo entre 0 e 10
    print(num, end="     ")  
# OU print(num, end=" "*5)
print('\nEncerrou o programa.')
--

# b. 
print("- Números naturais na horizontal:")
for num in range (0, 11, 1): # para cada item i no intervalo entre 0 e 10
    print(num, end=", ")  
print('\nEncerrou o programa.')
--

# c. SOLUÇÃO 1
print("- Números naturais na horizontal:")
for num in range (0, 11, 1): # para cada item i no intervalo entre 0 e 10
    if num == 10:
        print(num, end=". ")
    else:
        print(num, end=", ")  
print('\nEncerrou o programa.')

# c. SOLUÇÃO 2

for num in range (0, 10+1, 1):        
    if num <= 9:
        print (num, end=", ")
    else:
        print (num, end=".")  
print('\nEncerrou o programa.')
