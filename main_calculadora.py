from Calculadora import Calculadora

# Instanciando a classe Calculadora
calculadora = Calculadora(10, 5, '+')
calculadora.mostrar_resultado()

# Teste com outras operações
calculadora.operacao = '-'
calculadora.mostrar_resultado()

calculadora.operacao = '*'
calculadora.mostrar_resultado()

calculadora.operacao = '/'
calculadora.mostrar_resultado()

# Teste com divisão por zero
calculadora.valor_b = 0
calculadora.operacao = '/'
calculadora.mostrar_resultado()

# Teste com operação inválida
calculadora.operacao = '^'
calculadora.mostrar_resultado()

# Instanciando a classe Calculadora com entrada de dados
calculadora = Calculadora(0, 0, '')
calculadora.entrada_dados()
calculadora.mostrar_resultado()