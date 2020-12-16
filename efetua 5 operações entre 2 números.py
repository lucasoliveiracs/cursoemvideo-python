# Subtração, Adição, Multiplicação e Divisão

# Entrando com os valores

n1 = int(input("Digite o primeiro número: "))
n2 = int(input("Digite o segundo número: "))

# Calculando

so = n1 + n2
sub = n1 - n2
mul = n1 * n2
div = n1 / n2
pot = n1 ** n2
# Exibindo resultados

print('A soma entre {} e {} vale: {}'.format(n1, n2, so))
print('A subtração entre {} e {} vale: {}'.format(n1, n2, sub))
print('A multiplicação entre {} e {} vale: {}'.format(n1, n2, mul))
print('A divisão entre {} e {} vale {:.2f}'.format(n1, n2, div))
print('A potênciação de {} elevado à {} vale: {}'.format(n1, n2, pot))


