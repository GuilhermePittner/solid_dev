from typing import Type

class Casa:


    def __init__(self) -> None:
        self.address = 'Rua Japão'


    def chegar(self) -> None:
        print('Querida! Cheguei.')


    def endereco(self) -> str:
        return self.address
    

class Pessoa:

    #def __init__(self, name: str) -> None:
        #self.name = name


    def __init__(self, name: str, address: Type[Casa]) -> None:
        self.name = name
        self.address = address


    #def chegarEmCasa(self, address: Type[Casa]) -> None:
    #address.chegar()
    
    def chegarEmCasa(self) -> None:
        self.address.chegar()
        # agora que passamos o address dentro do construtor, não há motivo para pedir aqui

    
    def pegarEndereco(self, address: Type[Casa]) -> None:
        endereco = address.endereco()
        print(f'Endereco: {endereco}')


lugar_tal = Casa()
people = Pessoa('Ale', lugar_tal)

# people.chegarEmCasa(lugar_tal) // antes era necessário passar o lugar também.

people.chegarEmCasa()