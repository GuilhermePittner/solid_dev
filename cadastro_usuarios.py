"""
maneira errada
"""

class cadastroErrado:
    
    def checarInformacoes(self, name: str, age: int) -> None:
        if isinstance(name, str) and isinstance(age, int):
            print('Everything is correct!')
            print(f'Creating user {name}, {age} years old...')
        else:
            print('Something went wrong...')

        
#usuario_um = cadastroErrado()
#usuario_um.checarInformacoes('roberto', 19)

#usuario_dois = cadastroErrado()
#usuario_dois.checarInformacoes('renato', '19')


"""
maneira correta
"""

class cadastroCorreto:

    def cadastrarUsuario(self, name: str, age: int) -> None:
        if self.__checarInformacoes(name, age):
           self.__createUser(name, age)
        else:
           self.__showError()


    def __checarInformacoes(self, name: str, age: int) -> bool:
        if isinstance(name, str) and isinstance(age, int):
            return True
        else:
            return False
        

    def __createUser(self, name: str, age: int) -> None:
        print(f'Creating user {name}, {age} years old...')


    def __showError(self) -> None:
        print('Something went wrong...')


usuario_um = cadastroCorreto()
usuario_um.cadastrarUsuario('cassio', 43)

usuario_dois = cadastroCorreto()
usuario_dois.cadastrarUsuario('varanda', '19')