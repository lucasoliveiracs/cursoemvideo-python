#CALCULA ÁREA DE UMA PAREDE E RETORNA QUANTOS LITROS É NECESSÁRIO PARA PINTAR TODA PAREDE

#RECEBE ALTURA EM METROS
b = ','
a = input('Digite a altura(em metros): ')

#CASO O ÚSUARIO TENHA DIGITADO COM VÍRGULAS ELE PROCURA E SUBSTITUI POR PONTOS
for x in range(0, len(b)):
    a = a.replace(b[x], '.')

#RECEBE LARGURA EM METROS
l = input('Digite a largura(em metros): ')

#CASO O ÚSUARIO TENHA DIGITADO COM VÍRGULAS ELE PROCURA E SUBSTITUI POR PONTOS
for x in range(0, len(b)):
    l = l.replace(b[x], '.')

#CONVERTE OS VALORES PARA NÚMEROS COM PONTO FLUTUANTE
a = float(a)
l = float(l)

#RECEBE A COR DA TINTA QUE VOCÊ PRETENDE USAR
ct = input('Qual a cor(tinta) que você pretende usar: ')

#EXIBE RESULTADOS
print('Área: {} m²'.format(a*l))
print('Você precisa de {:.0f} litros de tinta {} para pintar toda parede!'.format((a*l)/2, ct))

