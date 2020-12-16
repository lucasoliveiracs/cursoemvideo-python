# TESTE O TIPO PRIMITIVO

v = input('Digite a informação: ')
if v.isnumeric() == True:
    print(v,'é um número')
elif v.isalpha() == True:
    if len(v) > 1:
        print(v,'é uma palavra ou um conjunto de várias palavras')
    else:
        print(v,'é uma letra')
else:
    print('Não foi possível identificar')
