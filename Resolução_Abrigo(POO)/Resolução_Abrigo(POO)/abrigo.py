# Sistema de abrigo de animais. 
# Neste caso, o sistema irá lidar com a gestão de animais, adoções e resgates. 
# Aqui estão os requisitos para o sistema:
# 
# Cada animal pode ter um ou mais responsáveis (adotantes, tutores etc.).
# O abrigo controla apenas o nome, o telefone e o endereço de cada responsável.
# Cada animal tem um nome, uma espécie, uma raça (se aplicável), uma idade e um status 
# (disponível para adoção, em processo de adoção, resgatado etc.).
# Quando um animal é adotado, seu status é alterado para "adotado" e o responsável é registrado.
# Alguns animais podem ter necessidades especiais (por exemplo, cuidados médicos, 
# treinamento comportamental).
# O abrigo mantém um registro de todas as transações realizadas.
# Para modelar o sistema, utilize obrigatoriamente os conceitos de classe,
# herança, propriedade, encapsulamento e classe abstrata.

class Pessoa:
    def __init__(self, nome, telefone, endereco):
        self.nome = nome
        self.telefone = telefone
        self.endereco = endereco

class Responsavel(Pessoa):
    def __init__(self, nome, telefone, endereco):
        self.nome = nome
        self.telefone = telefone

class Parceiro_vet(Pessoa):
    def __init__(self, nome, telefone, especialidade):
        super(Parceiro_vet, self).__init__(
            nome=nome, telefone=telefone, endereco=None
        )
        self.especialidade = especialidade      

class Animal:
    def __init__(self, nome, especie, raca, idade, cuidados, responsavel):
        self.nome = nome
        self.especie = especie
        self.raca = raca
        self.idade = idade
        self.cuidados = cuidados
        self.responsavel = responsavel


    # Transforma um metodo da classe numa propriedade
    @property 
    def is_disponivel(self):
        if self.responsavel:
            return False
        return True
    
class Doacao_comida:    
    def __init__(self, especie, produto, quantidade):
        self.especie = especie
        self.produto = produto
        self.quantidade = quantidade

class Abrigo:
    def __init__(self, nome):
        self.nome = nome
        self.responsaveis = {}
        self.animais = {}
        self.adocoes = []
        self.produtos = []
        self.parceiros = []

    def registrar_tutor(self, responsavel_id, nome, telefone, endereco):
        tutor = Responsavel(nome, telefone, endereco)
        self.responsaveis[responsavel_id] = tutor

    def cadastrar_animal(self, animal_id, nome, especie, raca, idade, cuidados = None, responsavel = None):
        animal = Animal(nome = nome, especie =especie, raca = raca, idade = idade, cuidados = cuidados, responsavel = responsavel)
        self.animais[animal_id] = animal

    def adotar_animal(self, animal,responsaveis,data_adocao):
        if animal.responsavel == True:
            adocao = {"data": data_adocao, "responsaveis": responsaveis, "animal": animal }
            self.adocoes.append(adocao)
        else:
            None

    def receber_doacao(self, especie, produto, quantidade):
        produto = Doacao_comida(especie, produto, quantidade)
        self.produtos.append(produto)
    
    def parceiro(self, nome, telefone, especialidade):
        parcerias = Parceiro_vet(nome, telefone, especialidade)
        self.parceiros.append(parcerias)

import abrigo_db

abrigos = abrigo_db.abrigos

obj_abrigos = {}

for abrigo in abrigos:
    obj_abrigos[abrigo[0]] = Abrigo(
        nome=abrigo[1]
    )

parcerias = abrigo_db.parcerias
for parceiro in parcerias:
    obj_abrigo = obj_abrigos[parceiro[4]]
    obj_abrigo.parceiro(
        nome=parceiro[1],
        telefone=parceiro[2],
        especialidade=parceiro[3],
    )

alimentos = abrigo_db.alimentos
for alimento in alimentos:
    obj_abrigo = obj_abrigos[alimento[4]]
    obj_abrigo.receber_doacao(
        especie=alimento[1],
        produto=alimento[2],
        quantidade=alimento[3],
    )

responsaveis = abrigo_db.responsaveis
for responsavel in responsaveis:
    obj_abrigo = obj_abrigos[responsavel[4]]
    obj_abrigo.registrar_tutor(
        responsavel_id=responsavel[0],
        nome=responsavel[1],
        telefone=responsavel[2],
        endereco=responsavel[3],
    )

animais = abrigo_db.animais
for animal in animais:
    obj_abrigo = obj_abrigos[animal[7]]

    responsavel = None
    if animal[6]:
        responsavel = obj_abrigo.responsaveis[animal[6]]

    obj_abrigo.cadastrar_animal(
        animal_id=animal[0],
        nome=animal[1],
        especie=animal[2],
        raca=animal[3],
        idade=animal[4],
        cuidados=animal[5],
        responsavel=responsavel
    )


for abrigo in obj_abrigos.values():
    print(
        f"Abrigo {abrigo.nome}"
    )

    # Exemplo de exibição de Adoções:
    for adocao in abrigo.adocoes:
        print(f"Data: {adocao['data']}, Animal: {adocao['animal'].nome}, Status: {adocao['animal'].status}")

    #Mostrar detalhes dos animais:
    for animal_id, animal in abrigo.animais.items():
        print(f"Nome: {animal.nome}, Especie: {animal.especie}, Raca: {animal.raca}, Idade: {animal.idade}, Cuidados: {animal.cuidados}")

    #Mostrar somente animais disponíveis para Adoções:
    for adocao in abrigo.adocoes:
        if adocao['animal'].responsavel == True:
            print(f"Data: {adocao['data']}, Animal: {adocao['animal'].nome}, Status: {adocao['animal'].responsavel}")
        else:
            print('Animal Indisponível')

    #Mostrar doações comida:
    for produto in abrigo.produtos:
        print(f"Especie: {produto.especie}, Produto: {produto.produto}, Quantidade: {produto.quantidade}")

    #Mostrar parceiros especialistas:
    for parcerias in abrigo.parceiros:
        print(f"Nome: {parcerias.nome}, Telefone: {parcerias.telefone}, Especialidade: {parcerias.especialidade}")
