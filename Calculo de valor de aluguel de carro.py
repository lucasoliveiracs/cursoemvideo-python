n = input('Digite seu nome: ')
d = int(input('Por quantos dias o carro foi alugado: '))
km = float(input('Quantos quilômetros percorridos: '))
print('{}, O total à pagar é R${}'.format(n, d*60 + km*0.15))