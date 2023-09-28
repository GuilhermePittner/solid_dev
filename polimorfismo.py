class PessoaA:

    def __init__(self, name: str):
        self.name = name

    def acenar(self):
        print(f'Olá!!! {self.name}')



class PessoaB:

    def __init__(self, name: str):
        super().__init__()
        self.name = name

    def acenar(self):
        print(f'Eaí!!! Como vai?! {self.name}')


cassio = PessoaA('Cassio')
cassio.acenar()

maycon = PessoaB('Maycon')
maycon.acenar()