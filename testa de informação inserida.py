# TESTANDO INFORMAÇÕES
v = input('Digite algo: ')
if v.isalnum() == True:
    if v.isalpha() == True:
        print(v,'é alfabetico')
        if len(v) > 1:
            print('e é uma cadeia de caracteres')
            if v.islower() == True:
                print('que está em mínusculo')
            else:
                print('que esta ou contém letras em maiúsculo')
        else:
            print('e é uma letra')
            if v.islower() == True:
                print('que está em mínusculo')
            else:
                print('que esta em maiúscula')
    elif v.isnumeric() == True:
        print(v,'é um caractere númerico')
    else:
        print(v, 'contém um combinação de caracteres alfanúmericos')
elif v.isspace() == True:
    print('(',v,')','contém apenas espaços')
else:
    if len(v) > 1:
        print(v,'possui caracteres especiais')
    else:
        print(v,'é um caractere especial')


