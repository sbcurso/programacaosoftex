#quantos foram aprovados em cada turma
#maior nota de cada turma
# qual aluno teve maior nota de todas as turmas

turmas = ["A", "B", "C", "D"]
MaioresNotas = {"A":0, "B":0, "C":0, "D":0}
AlunosMaioresNotas = {"A": "", "B": "", "C": "", "D": ""}
AprovadosporTurma = {"A":0, "B":0, "C":0, "D":0}
for turma  in turmas:
    print(f"Turma {turma}: ")
    for n in range (25):
        nome = input("informe o nome: ")
        nota = float(input("Informe a nota:"))
        maiorNotaAtual = MaioresNotas [turma]

        if nota > maiorNotaAtual:
            MaioresNotas[turma] = nota
            AlunosMaioresNotas[turma] = nome

            if nota >= 7:
                AprovadosporTurma[turma] += 1

maiorNotaGeral =0
turmaMaiorNotaGeral = 0
alunoMaiorNota = ""
for turma, nota in MaioresNotas.items():
    if nota > maiorNotaGeral:
        maiorNotaGeral = nota
        turmaMaiorNotaGeral = turma

alunoMaiorNota = AlunosMaioresNotas[turmaMaiorNotaGeral]

for turma, aprovados in AprovadosporTurma.items():
    print(f"aprovados na turma {turma}: {aprovados}")
    print(f"Maior nota da turma {turma}: {MaioresNotas[turma]}")

print(f"Aluno com a maior nota: {alunoMaiorNota}")

print(f"Maior nota Geral: {maiorNotaGeral}")
