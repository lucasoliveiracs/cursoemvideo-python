#RECEBE O SALÁRIO E RETORNA O SALÁRIO COM 15% DE AUMENTO

#RECEBE O SALÁRIO
s = input('Digite o salário: ')
b = ','

#SUBSTITUI VÍRGULAS POR PONTOS
for x in range(0, len(b)):
    s = s.replace(b[x], '.')

#CONVERTE PARA NÚMEROS COM PONTO FLUTUANTE
s = float(s)

#CALCULA O AUMENTO
a = 15/100*s

#EXIBE O RESULTADO
print('O salário com aumento de 15% é R${:.2f}'.format(s+a))