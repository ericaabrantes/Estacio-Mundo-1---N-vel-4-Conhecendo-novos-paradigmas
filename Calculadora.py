class Calculadora:
    def __init__(self, valor_a, valor_b, operacao):
        self.__valor_a = valor_a
        self.__valor_b = valor_b
        self.__operacao = operacao

    @property
    def valor_a(self):
        return self.__valor_a

    @valor_a.setter
    def valor_a(self, valor_a):
        self.__valor_a = valor_a

    @property
    def valor_b(self):
        return self.__valor_b

    @valor_b.setter
    def valor_b(self, valor_b):
        self.__valor_b = valor_b

    @property
    def operacao(self):
        return self.__operacao

    @operacao.setter
    def operacao(self, operacao):
        self.__operacao = operacao

    def validar_operacao(self):
        if self.__operacao in ['+', '-', '*', '/']:
            return True
        else:
            return False

    def calcular(self):
        if not self.validar_operacao():
            print("Operação inválida!")
            return None
        

        if self.__operacao == '+':
            return self.__valor_a + self.__valor_b
        elif self.__operacao == '-':
            return self.__valor_a - self.__valor_b
        elif self.__operacao == '*':
            return self.__valor_a * self.__valor_b
        elif self.__operacao == '/':
            if self.__valor_b == 0:
                print("Divisão por zero não é permitida!")
                return None
            return self.__valor_a / self.__valor_b

    def mostrar_resultado(self):
        resultado = self.calcular()
        if resultado is not None:
            print(f"{self.__valor_a} {self.__operacao} {self.__valor_b} = {resultado}")


    # Adicione o método entrada_dados aqui
    def entrada_dados(self):
        self.__valor_a = float(input("Digite o primeiro valor: "))
        self.__valor_b = float(input("Digite o segundo valor: "))
        self.__operacao = input("Digite a operação (+, -, *, /): ")