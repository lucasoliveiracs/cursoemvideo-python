#LER UM NÚMERO E MOSTRA SUA TABUADA DE 1 À 10
n = int(input('Digite um número: '))
m = 1
for x in range(0,10):
    print('{} x {} = {}'.format(n, m, n * m))
    m += 1