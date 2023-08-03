#EXERCICIO DE ESTRUTUTA DE CONTROLE 

print('questão 1')
a = 10 
b = 20 

if a >= b:
    print('a é menor que B')
else:
    print('aaaa')

print('------------------------------')
print('questão 2')

#creiterios para doação de sangue: ter entre 16 a 69 anos, pesar mais de 50kg, e ter dormido mais de 6h nas ultimas 24h.

# idade = int(input('Insira sua idade: '))
# peso = int(input('Insira seu peso: '))
# sono = int(input('Quantas horas dormiu na ultima noite?'))

# if idade >= 16 or idade <= 69 and peso >= 50 and sono >= 6:
#     print('apto para doação')
# else:
#     print('não possui os requisitos para doação')

#se for maior que 20 a soma dos numeros somar 8, menor que 20, subtrair 5.

numero1 = int(input('Digite um numero: '))
numero2 = int(input('Digite outro numero:'))
resultado = numero1 + numero2
print(resultado)

if resultado > 20:
    resultado += 8
    print(resultado)
else:
    resultado -= 5
    print(resultado)

