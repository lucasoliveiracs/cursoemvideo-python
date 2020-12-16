#CALCULA E MOSTRA O ANTECESSOR E O SUCESSOR DE UM NÚMERO
n = int(input('Digite um número: '))
print('O antecessor de {} é {} \nO sucessor de {} é {}'.format(n, n-1, n, n+1))

#CALCULA E MOSTRA O DOBRO, O TRIPLO E A RAIZ QUADRADADA DE UM NÚMERO
print('\nO dobro de {} é {}\nO triplo de {} é {}\nE a raiz quadrada de {} é {:.0f}'.format(n, n*2, n, n*3, n, n**(1/2)))
