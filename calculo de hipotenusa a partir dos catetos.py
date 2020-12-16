from math import sqrt
# UTILIZANDO SQRT DA BILIOTECA MATH E CONCEITOS MATEMATICOS
cttoposto = float(input('Digite o cateto oposto: '))
cttadjacente = float(input('Digite o cateto adjacente: '))
cttoposto **= 2
cttadjacente **= 2
r = cttadjacente + cttoposto
r = sqrt(r)
print(r)