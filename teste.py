'''print('hello, world')
print('2'+'2')

print('questão 1')
print(10%1)


print('questão 2')
print('tabuada de 13: ')
cont = 0 
for i in range(11):
    print("13 x", cont, '=', 13*i)
    cont += 1

print('questão 3')

print('exercicio 1')
cotacao = 3.25 
dolar = 65.00 
resultado = dolar/cotacao

print('o valor em reais é de R$',resultado)

print('exercicio 2')
print('Letra A')

celular = 299.99
chaleira = 23.87
gnomo = 66.66
adesivo = 6*1.42
frete = 12.34 

valor_total = celular + chaleira + gnomo + adesivo + frete 
print('o valor em dolar é $',round(valor_total,2))

print('letra B')

cotacao = 3.25 
real = valor_total*cotacao
print('o valor total das compras é de $',round(real,2)) 
iof = 6.38 / 100 
print(iof)
taxaIof = real * iof
print(taxaIof)

resultado2 = taxaIof + real 
print(round(resultado2,2))

print('O valor da taxa IOF é de',round(taxaIof,3))
print('O valor da em dolar é de $',round(valor_total,2))
print('O valor total das compras em real foi de R$',round(real,2))

nome1 = 'silvo santos '
print(nome1 * 3) '''

#idade = input('qual a sua idade?')
#print(idade)

#função Len serve para c

#palavras = 'hoje é um novo dia'
#print(len(palavras))
#print(len('viagem'))

#soma = palavras + palavras
#print(soma)

'''palavra = 'python'
palavra[5]

frase = 'amanha sera um novo dia'
print(frase[0:6])
print(frase[5:7])'''

#função format para adiocionar palavras ou numeros.
''''nome = input('digite seu nome: ')
print(nome)
frases = 'olá, {}'.format(nome)
print(frases)

altura = input('qual a sua altura?')
print(altura)
print(f'olá, meu nome é {nome} e tenho uma altura de {altura}')'''


print('{} x {} = {}'.format(6, 7, 7*6))
print(f'{6} x {7} = {6*7}')

palavra = 'senai'
numero = 0

print(f'O {palavra} é nota {numero}')

#ultilizando indices para fazer o fatiamento das frases/palavras
frase = 'python é muito legal'
print(frase[0:6])
print(frase[7:8])
print(frase[9:14])
print(frase[15:20])
print(len(frase))

palavra1 = 'python'
palavra2 = 'é'
palavra3 = 'muito'
palavra4 = 'legal'

print(len(palavra1))
print(len(palavra2))
print(len(palavra3))
print(len(palavra4))

#método split, função que entrega a frase em formato de lista
#exemplo da utilização do método split
nome2 = 'beatriz dos santos rodrigues'
print(nome2.split())

print(frase.split())

a = 1
b = 2
print(a,b)

a, b = b, a 
print(a,b)

































