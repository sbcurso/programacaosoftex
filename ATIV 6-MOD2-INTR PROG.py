import datetime

data = datetime.date.today()
anoAtual = int(data.strftime("%Y"))

while True:
    nome = input("Insira seu nome completo: ")
    anoNascimento = int(input("Insira o ano do seu nascimento: "))

    if anoNascimento >= 1922 and anoNascimento <= anoAtual -1:
        print(f"{nome} tem/terá {anoAtual - anoNascimento} anos em {anoAtual}!" )
        break
    else:
        print("Por favor preencha os dados corretamente!")
         
    
