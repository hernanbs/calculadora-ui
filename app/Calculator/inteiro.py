class Inteiro:
    """Um numero inteiro"""

    def __init__(self):
        self.__valor: int = 0

    def getValor(self):
        return self.__valor

    def setValor(self, valor):
        if type(valor) is int :
            self.__valor = valor
        else:
            self.__valor = None

if __name__ == "__main__":
    a = Inteiro()
    print(a)
    print(a.getValor())