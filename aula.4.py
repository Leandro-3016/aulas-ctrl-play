
#desafio 1


mes =int(input('Digite um número entre 1 e 12'))


if mes == 1 :
   print('Jan')
elif mes == 2 :
    print('Feb')
elif mes == 3 :
    print('Mar')
elif mes == 4 :
    print('April')
elif mes == 5 :
    print('May')
elif mes == 6 :
    print('June')
elif mes == 7 :
    print('Jule')
elif mes == 8 :
    print ('Aug')
elif mes == 9 :
    print ('Sep')
elif mes == 10 :
    print ('Oct')
elif mes == 11 :
    print('Nov')
elif mes == 12 :
    print("Dec")
else :
    print("Número inválido, tente novamente")




















#desafio 2

codigo = int(input('Digite o código do lanche'))
quantidade = int(input('Digite a quantidade desejada'))

if codigo == 1 :
    valor = quantidade * 4
    print(f'Valor total: R$w'
          f'{valor:.2f}')
elif codigo == 2 :
    valor = quantidade * 2
    print(f'Valor total: RS{valor:.2f}')
elif codigo == 3 :
    valor = quantidade * 1.5
    print(f'Valor total: R${valor:.2f}')
elif codigo == 4 :
    valor = quantidade * 3.5
    print(f'Valor total: R${valor:.2f}')

#desafio 3
numero = int(input('Digite um número para saber se é impar ou par:'))

if numero % 2 == 1 :
    print('Número é impar')
else :
    print ('Número é par')

#desafio 4
letra = input("Digite uma letra para saber se é vogal ou consoante:")
vogais = "AaEeIiOoUu"

if letra in vogais :
    print("É uma vogal")
else :
    print('É uma consoante')








































