#Código 1: 
#programa que leia o nome de uma pessoa e diga se ela tem "SILVA" no nome
 
frase = input('Digite seu nome completo:')
print('Seu nome tem silva?', 'Silva' in frase) 


#Código 2:
#programa que lê o nome completo, nome em maiusculo, nome em minisculo, quantas letras sem os espaços, quantas letras têm o primeiro nome

frase = input('Digite seu nome completo:')
dividido = frase.split()
print('Seu nome maiúsculo:', frase.upper())
print('Seu nome minúsculo:', frase.lower())
print('O total de caracteres do seu nome sem espaço é:', (len(''.join(dividido))))
print('Seu primeiro nome é:', (dividido[0]))

#Código 3:
#programa que leia a frase e diga: quantas vezes aparece a letra a, posicão que ela aparece a 1º vez e a última vez

frase = input('Digite uma frase:')
print('Existem:', frase.lower().count('a'), ',a , na sua frase.')
print('A letra "a", aparece pela primeira vez na posição', frase.lower().find('a'))
print('A letra "a", aparece pela última vez na posição', frase.lower().rfind('a'))

