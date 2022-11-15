class Gato:
    '''classe para trabalhar com gatos'''
    tipo_animal = 'Felino'
    def __init__(self, nome):
        '''inicializa o objeto capturando o nome do animal'''
        self.nome = nome
        print('Seu gatinho se chama', self.nome)
    def peso_gato(self, peso):
        self.peso = peso
        if (self.peso > 5.0):  
            print('Seu gato esta obeso')
        elif (self.peso > 3.5):
            print('O peso está normal')
        else:
            print('O animal esta abaixo do peso!')    
    def _dieta_especial_gato(self):
        self.msg = 'tudo ok!'
        if (self.peso   < 3.5):
            self.msg = 'Aumente a ração'
        if (self.peso >= 5.0):
            self.msg = 'Diminua a ração'
        return self.msg
    def dados_gato(self):
        print('\nO gato', self.nome,'esta com', self.peso,'kg')
        print(self._dieta_especial_gato())


nome_gato = input('Digite o nome do seu gato: ')
g1 = Gato(nome_gato)

peso = float(input('\nQual o peso do seu gato, em kg: '))
g1.peso_gato(peso)

g1.dados_gato()
