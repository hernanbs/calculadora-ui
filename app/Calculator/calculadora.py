from inteiro import Inteiro


class Calculadora:
    """Calcula de dois numeros"""
    def __init__(self):
        self.__num1 = Inteiro()
        self.__num2 = Inteiro()

    def sumOp(self):
        if self.getNum1() is None or self.getNum2() is None:
            return None
        return self.getNum1() + self.getNum2()

    def subtract(self):
        if self.getNum1() is None or self.getNum2() is None:
            return None
        return self.getNum1() - self.getNum2()

    def divide(self):
        if self.getNum1() is None or self.getNum2() is None:
            return None
        return self.getNum1() / self.getNum2()

    def multiple(self):
        if self.getNum1() is None or self.getNum2() is None:
            return None
        return self.getNum1() * self.getNum2()

    def getNum1(self):
        return self.__num1.getValor()

    def getNum2(self):
        return self.__num2.getValor()

    def setNum1(self, valor):
        return self.__num1.setValor(valor)

    def setNum2(self, valor):
        return self.__num2.setValor(valor)

if __name__ == "__main__":

    calculo = Calculadora()
    print(calculo)
    calculo.setNum1(10)
    calculo.setNum2(20)
    print('\n')
    print('Primeiro número == %.2f' % calculo.getNum1())
    print('Segundo número == %.2f' % calculo.getNum2())
    print('Resultados ...\n')
    print('Operação          Valor')
    print('Soma              %.2f' % calculo.sumOp())
    print('Subtração         %.2f' % calculo.subtract())
    print('Divisão           %.2f' % calculo.divide())
    print('Multiplicação     %.2f' % calculo.multiple())

