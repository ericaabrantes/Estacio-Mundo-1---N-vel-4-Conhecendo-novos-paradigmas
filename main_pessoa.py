from Pessoa import Pessoa
from PessoaFisica import PessoaFisica
from PessoaJuridica import PessoaJuridica


pessoa1 = Pessoa(nome="Empresa XYZ", numero_conta="123456", data_abertura_conta="2023-01-01", status=True)
pessoa1.imprimir_detalhes()


pessoa_fisica = PessoaFisica(nome="João", numero_conta="654321", data_abertura_conta="2020-05-05", status=True,
                             data_nascimento="2000-01-01", cpf="000.111.222-33", rg="15975388-1")
pessoa_fisica.imprimir_detalhes()


pessoa_juridica = PessoaJuridica(nome="Empresa ABC", numero_conta="789012", data_abertura_conta="2019-03-15", 
                                 status=True, data_abertura_empresa="2019-03-15", cnpj="00.000.000/0001-00")
pessoa_juridica.imprimir_detalhes()


pessoa1.nome = "Empresa XYZ Alterada"
pessoa_fisica.cpf = "123.456.789-00"  
pessoa_juridica.cnpj = "11.111.111/0001-11"


pessoa1.imprimir_detalhes()
pessoa_fisica.imprimir_detalhes()
pessoa_juridica.imprimir_detalhes()