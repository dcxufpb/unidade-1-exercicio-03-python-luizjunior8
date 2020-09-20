import cupom;
 

cupom.nome_loja = "Arcos Dourados Com. de Alimentos LTDA"
cupom.logradouro = "Av. Projetada Leste"
cupom.numero = 500
cupom.complemento = "EUC F32/33/34"
cupom.bairro = "Br. Sta Genebra"
cupom.municipio = "Campinas"
cupom.estado = "SP"
cupom.cep = "13080-395"
cupom.telefone = "(19) 3756-7408"
cupom.observacao = "Loja 1317 (PDP)"
cupom.cnpj = "42.591.651/0797-34"
cupom.inscricao_estadual = "244.898.500.113"

def test_loja_completa():
    assert cupom.imprime_dados_loja() == '''Arcos Dourados Com. de Alimentos LTDA
Av. Projetada Leste, 500 EUC F32/33/34
Br. Sta Genebra - Campinas - SP
CEP:13080-395 Tel (19) 3756-7408
Loja 1317 (PDP)
CNPJ: 42.591.651/0797-34
IE: 244.898.500.113
'''

def test_nome_vazio():
    global nome_loja
    cupom.nome_loja = ""
    assert cupom.imprime_dados_loja() == '''O campo nome da loja é obrigatório'''
    cupom.nome_loja = "Arcos Dourados Com. de Alimentos LTDA"

def test_logradouro_vazio():
    global logradouro
    cupom.logradouro = ""
    assert cupom.imprime_dados_loja() == '''O campo logradouro do endereço é obrigatório'''
    cupom.logradouro = "Av. Projetada Leste"

def test_numero_zero():
    global numero
    cupom.numero = 0
    assert cupom.imprime_dados_loja() == '''Arcos Dourados Com. de Alimentos LTDA
Av. Projetada Leste, s/n EUC F32/33/34
Br. Sta Genebra - Campinas - SP
CEP:13080-395 Tel (19) 3756-7408
Loja 1317 (PDP)
CNPJ: 42.591.651/0797-34
IE: 244.898.500.113
'''
    cupom.numero = 500

def test_municipio_vazio():
    global municipio
    cupom.municipio = ""
    assert cupom.imprime_dados_loja() == '''O campo município do endereço é obrigatório'''
    cupom.municipio = "Campinas"

def test_estado_vazio():
    global estado
    cupom.estado = ""
    assert cupom.imprime_dados_loja() == '''O campo estado do endereço é obrigatório'''
    cupom.estado = "SP"

def test_cnpj_vazio():
    global cnpj
    cupom.cnpj = ""
    assert cupom.imprime_dados_loja() == '''O campo CNPJ da loja é obrigatório'''
    cupom.cnpj = "42.591.651/0797-34"

def test_inscricao_estadual_vazia():
    global inscricao_estadual
    cupom.inscricao_estadual = ""
    assert cupom.imprime_dados_loja() == '''O campo inscrição estadual da loja é obrigatório'''
    cupom.inscricao_estadual = "244.898.500.113"

def test_exercicio2_customizado():
    global nome_loja
    global logradouro
    global numero
    global complemento
    global bairro
    global municipio
    global estado
    global cep
    global telefone
    global observacao
    global cnpj
    global inscricao_estadual
    
    # Defina seus próprios valores para as variáveis a seguir
    cupom.nome_loja = "Jr Tech"
    cupom.logradouro = "Rua Geraldo Correia de Melo"
    cupom.numero = 100
    cupom.complemento = "Casa"
    cupom.bairro = "Centro"
    cupom.municipio = "Araçagi"
    cupom.estado = "PB"
    cupom.cep = "58270-000"
    cupom.telefone = "(83) 98111-2697"
    cupom.observacao = "Matriz"
    cupom.cnpj = "66.651.293/0001-85"
    cupom.inscricao_estadual = "222.333.444.555"
    
    #E atualize o texto esperado abaixo
    assert cupom.imprime_dados_loja() == '''Jr Tech
Rua Geraldo Correia de Melo, 100 Casa
Centro - Araçagi - PB
CEP:58270-000 Tel (83) 98111-2697
Matriz
CNPJ: 66.651.293/0001-85
IE: 222.333.444.555
'''
