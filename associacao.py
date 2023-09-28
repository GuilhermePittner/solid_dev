from typing import Type

class Interruptor:

    def __init__(self, comodo: str):
        self.__comodo = comodo

    def acender_luz(self):
        print(f'acendendo luz do(a) {self.__comodo}')

    def apagar_luz(self):
        print(f'apagando luz do(a) {self.__comodo}')


class Pessoa:

    def acender_luz(self, interruptor: Type[Interruptor]):
        interruptor.acender_luz()

    def apagar_luz(self, interruptor: Type[Interruptor]):
        interruptor.apagar_luz()

    def dormir(self):
        print('partiu festa do japa: japacama kkkkkkkkkkkk')


interruptor_sala = Interruptor('sala')
interruptor_sala.acender_luz() # aqui é o método de acender do próprio interruptor (ninguém acendeu)

cassio = Pessoa()
cassio.apagar_luz(interruptor_sala) # aqui o cássio apaga a luz do cômodo definido
cassio.dormir()