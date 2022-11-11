import panda as pd 
df = pd.read_csv ("C:\Users\55879\OneDrive\Área de Trabalho\caline\notas alunos.csv")
media = (df["nota_1"] + df["nota_2"])/2

df["media"] = media
print(df.head( ))


df.loc[df["media"] >7, "situacao"] = "APROVADO"
df.loc[df["media"] <7, "situacao"] = "REPROVADO"
df.loc[df["faltas"] >5, "situação"] = "REPROVADO"

df.to_csv ("C:\Users\55879\OneDrive\Área de Trabalho\caline\situacao alunos.csv")

maiorNumFaltas = df["faltas"].max()
print("O maior numero de faltas e: ",+str(maiorNumFaltas))

mediaGeral = df["media"].median()
print("A media geral é: ",+str(mediaGeral))

maiorMedia = df["media"].max()
print("A maior média é: ",+str(maiorMedia))