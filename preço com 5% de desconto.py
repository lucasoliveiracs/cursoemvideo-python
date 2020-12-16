#RECEBE O PREÇO DE UM PRODUTO E RETORNA O PREÇO COM 5% DE DESCONTO

#RECEBE O PREÇO DO PRODUTO
p = input('Digite o preço do produto: ')
b = ','

#SUBSTITUI VÍRGULAS POR PONTOS
for x in range(0, len(b)):
    p = p.replace(b[x], '.')

#CONVERTE PARA NÚMEROS COM PONTO FLUTUANTE
p = float(p)

#CALCULA O DESCONTO
d = 5/100*p

#EXIBE O RESULTADO
print('O preço com desconto de 5% é R${:.2f}'.format(p-d))
