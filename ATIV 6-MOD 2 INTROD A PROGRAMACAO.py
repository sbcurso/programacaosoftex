import enum

class Candidato(enum.Enum):
    candidato_X = 889
    candidato_Y = 847
    candidato_Z = 515
    branco = 0

    votar = True
    votosX = 0
    votosY = 0
    votosZ = 0
    votosBrancos = 0
    votosNulos = 0
    While votar:
        #codigo para votar
        #pedir votos
        #verificar se o voto e valido
        #computar voto
        votoInvalido = True
        voto = -1
        while votoInvalido:
            try:
                voto = int(input("Informe seu voto: "))
                votoInvalido = False
            except:
                print("Informe um valor valido. Vote novamente.")

    # aqui ja temos um voto valido
    if Candidato.candidato_X.value == voto:
        votosX += 1
    elif Candidato.candidato_Y.value ==voto:
        votosY += 1
    elif Candidato.candidato_Z.value ==voto:
        votosZ += 1
    elif Candidato.branco.value == voto:
        votosBrancos += 1
    else:
        votosNulos += 1

    opcao = int(input("Deseja continuar votando? (1-SIM, 2-NAO): "))
    if opcao == 1:
        votar = True
    if opcao == 2:
        votar = False

    print("Votos para o(a) candidato(a) {}: {}".format(Candidato.candidato_X.name, votosX))
    print("Votos para o(a) candidato(a) {}: {}".format(Candidato.candidato_Y.name, votosY))
    print("Votos para o(a) candidato(a) {}: {}".format(Candidato.candidato_Z.name, votosZ))
    print("Votos nulos: {}".format(votosNulos))
    print("Votos brancos: {}".format(votosBrancos))
    
    
