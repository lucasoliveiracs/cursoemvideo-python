#RECEBE O VALOR EM REAIS E RETORNA QUANTOS DOLÁRES PODE-SE COMPRAR

#RECEBE UM VALOR EM REAIS
vr = input('Quantos reais você tem: R$')
b = ','

#CASO O ÚSUARIO TENHA DIGITADO COM VÍRGULAS ELE PROCURA E SUBSTITUI POR PONTOS
for i in range(0, len(b)):
    vr = vr.replace(b[i], ".")

#CONVERTE PARA FLOAT
vr = float(vr)

#CALCULA O CÂMBIO
vd = (vr*30.58)/100

#EXIBI O RESULTADO
print('Você pode comprar US${:.2f} com R${}'.format(vd, vr))