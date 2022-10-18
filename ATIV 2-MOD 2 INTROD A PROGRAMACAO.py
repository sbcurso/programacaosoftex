rodas = int(input("Quantas rodas o veiculo possui?"))
peso = float(input("qual o peso do veiculo? (kg)"))
passageiros = int(input("Quantos passageiros o veiculo comporta?"))

#nessa ordem porque o tipo C so pode dirigir veiculos até 8 pessoas
if rodas >= 4 and peso > 6000:
    print("A carterira recomendada é do tipo E!")
elif rodas >= 4 and passageiros > 8:
    print("A carteira recomendada é do tipo D!")
elif rodas >= 4 and 3500 <= peso <= 6000:
    print("A carteira recomendada é do tipo C")
elif rodas == 4 and passageiros == 8 and peso < 3500:
    print("A carteira recomendada é do tipo B")
elif 2 <= rodas <= 3:
    print("A carteira recomendada é do tipo A!")
else:    
    print("Esse veículo não possui carteira recomendada no sistema")
