from errno import ESHLIBVERS
from tkinter import E


nome = input("Informe o nome do aluno: ")
nota1 = float(input("Informe a primeira nota: "))
nota2 = float(input("Inform a segunda nota: "))
faltas = int(input("informe a quantidade de faltas: "))

media = (nota1 + nota2)/2
if media < 7:
    print(f"{nome} REPROVADO")
elif faltas > 3:
    print(f"{nome} REPROVADO")
else:
    print(f"{nome} APROVADO!!")
