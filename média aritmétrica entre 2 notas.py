#CALCULA MÉDIA ARITMÉTRICA ENTRE DUAS NOTAS
nome = input('Aluno: ')
n1 = int(input('Primeira nota: '))
n2 = int(input('Segunda nota: '))
m = (n1+n2)/2
print('A média de {} é: {}'.format(nome, m), end=' ')
if m >= 7:
    print('(APROVADO)')
else:
    print('(REPROVADO)')