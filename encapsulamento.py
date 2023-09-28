class Calculadora():
    

    def calcular(self, op, num_one, num_two):
        if op == 'soma':
            return self.__mais(num_one, num_two)
        
        elif op == 'subtrair':
            return self.__menos(num_one, num_two)
        
        else:
            return 'n/a operacao.'
        
    
    def __mais(self, num_one, num_two):
        return num_one + num_two
    

    def __menos(self, num_one, num_two):
        return num_one - num_two
    

cassio = Calculadora()
resultado = cassio.calcular('soma', 10, 10)
print(resultado)