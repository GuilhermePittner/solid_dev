class Circo:

    def apresentar(self, apresentador: any) -> None:
        apresentador.apresentarShow()


class Palhaco:
    
    def apresentarShow(self):
        print('Palhaço apresentando show.')


class Domador:
    
    def apresentarShow(self):
        print('Domador apresentando show.')


class Malabarista:
    
    def apresentarShow(self):
        print('Malabarista apresentando show.')


circo = Circo()
malabarista = Malabarista()
circo.apresentar(malabarista)