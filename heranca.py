class Mae:

    def __init__(self):
        self.address = 'Rua da Pindagoia de Ituberaba Paulista Vargem Grande e Região Limitada'
        self.last_name = 'Fernandez'

    def dormir(self):
        print('Partiu dormir')

    def caminhar(self):
        print('Aoba vou caminhar')

    def torcer(self):
        print('Vai Corinthians!!!!')


class Filha(Mae):

    def __init__(self):
        super().__init__()

    def baguncar(self):
        print('Hehe vou baguncar hahaha')


joana = Filha()
print(joana.last_name)
print(joana.baguncar())
print(joana.torcer())