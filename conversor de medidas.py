#LER EM METROS E EXIBE EM CENTÍMETROS E MILÍMETROS

#RECEBE A QUANTIDADE DE METROS
v = input('Digite a quantidade metros: ')
b = ','

#CASO O ÚSUARIO TENHA DIGITADO COM VÍRGULAS ELE PROCURA E SUBSTITUI POR PONTOS
for i in range(0, len(b)):
    v = v.replace(b[i], ".")

#CONVERTE PARA NÚMERO COM PONTO FLUTUANTE
v = float(v)

#EXIBI OS RESULTADOS: VALOR EM METROS, CENTÍMETROS E MILÍMETROS
print('{} metros equivale à:\n{} decímetros\n{} centímetros\n{} milímetros\n{} quilômetros\n{} hectômetros\n{} decâmetros'.format(v,v*10, v*100, v*1000, v/1000, v/100, v/10))