# -- Sistema de Gerenciamento de Abrigo de Animais
# -- 
# -- Criação das Tabelas:
# -- 
# -- Utilizando SQL, crie as tabelas necessárias para armazenar as informações do sistema 
# -- de gerenciamento de um abrigo de animais. 
# -- Certifique-se de definir as chaves primárias e estrangeiras conforme apropriado.
# -- 
# -- Inserção de Dados:
# -- Insira dados de exemplo nas tabelas para simular um ambiente de abrigo de animais. 
# -- Certifique-se de incluir uma variedade de animais, informações sobre o abrigo e registros de adoção.
# -- 
# -- Consultas SQL:
# -- Escreva consultas SQL para realizar as seguintes operações:
# -- 
# -- Listar todos os animais disponíveis no abrigo.
# -- Encontrar todos os animais adotados no momento.
# -- Localizar os animais de um tipo específico.
# -- Verificar o número de animais disponíveis de um determinado tipo.
# -- 
# -- Atualizações e Exclusões:
# -- Escreva consultas SQL para atualizar e excluir registros do banco de dados, 
# -- por exemplo, para marcar um animal como adotado ou remover um animal do abrigo.

import sqlite3

abrigo = sqlite3.connect('abrigo')
cursor = abrigo.cursor()

# cursor.execute('''DROP TABLE Animal''')
# cursor.execute('''DROP TABLE Parceiros''')
# cursor.execute('''DROP TABLE Alimentos''')
# cursor.execute('''DROP TABLE Responsavel''')
# cursor.execute('''DROP TABLE Abrigo''')

cursor.execute('''
    CREATE TABLE IF NOT EXISTS Abrigo (
        abrigo_id SERIAL PRIMARY KEY, 
        nome VARCHAR(100) NOT NULL
    )
''')

cursor.execute('''
    CREATE TABLE IF NOT EXISTS Responsavel (
        responsavel_id SERIAL PRIMARY KEY,
        nome VARCHAR(100) NOT NULL, 
        telefone INT, 
        endereco VARCHAR(150) NOT NULL,
        abrigo_id,
        FOREIGN KEY (abrigo_id) REFERENCES Abrigo(abrigo_id)
    )
''')

cursor.execute('''
    CREATE TABLE IF NOT EXISTS Parceiros (
        parceiro_id SERIAL PRIMARY KEY, 
        nome VARCHAR(100) NOT NULL, 
        telefone INT, 
        especialidade VARCHAR(50) NOT NULL,
        abrigo_id,
        FOREIGN KEY (abrigo_id) REFERENCES Abrigo(abrigo_id)
    )
''')

cursor.execute('''
    CREATE TABLE IF NOT EXISTS Animal (
        animal_id SERIAL PRIMARY KEY, 
        nome VARCHAR(100) NOT NULL, 
        especie VARCHAR(50) NOT NULL, 
        raca VARCHAR(50), 
        idade INT, 
        cuidados VARCHAR(50), 
        responsavel_id, 
        abrigo_id,
        FOREIGN KEY (responsavel_id) REFERENCES Responsavel(responsavel_id),
        FOREIGN KEY (abrigo_id) REFERENCES Abrigo(abrigo_id)
    )
''')

cursor.execute(
    '''CREATE TABLE IF NOT EXISTS Alimentos (
        alimento_id SERIAL PRIMARY KEY, 
        especie VARCHAR(50), 
        produto VARCHAR(100), 
        quantidade VARCHAR(50),
        abrigo_id,
        FOREIGN KEY (abrigo_id) REFERENCES Abrigo(abrigo_id)
    )
''')

#  Insira dados de exemplo nas tabelas para simular um ambiente de abrigo de animais. 
# -- Certifique-se de incluir uma variedade de animais, informações sobre o abrigo e registros de adoção.

# cursor.execute('''
#     insert into Abrigo (abrigo_id, nome) values
#         ( 1, "Lar doce Lar"),
#         ( 2, "AbriCão")
# ''')

# cursor.execute('''
#     insert into Responsavel (responsavel_id, nome, telefone, endereco, abrigo_id) values
#         ( 1, "João", "123456789", "Rua A, 123", 1),
#         ( 2, "Joel", "993456789", "Rua b, 321", 1),
#         ( 3, "Maria", "99124578", "Rua d 456", 2),
#         ( 4, "Luisa Mell", "999999888", "Rua São Paulo, 876", 2 )
# ''')

# cursor.execute('''
#     insert into Parceiros (parceiro_id, nome, telefone, especialidade, abrigo_id) values
#         ( 1, "João Pedro", "123456789", "Clínico Geral", 1),
#         ( 2, "Jose", "993456789", "Ortopedista", 1),
#         ( 3, "Claudia", "981456789", "Neurologista", 2),
#         ( 4, "Luisa Mell", "999999888", "Patrocinadora", 1 )
# ''')

# cursor.execute('''
#     insert into Alimentos (alimento_id, especie, produto, quantidade, abrigo_id) values
#         ( 1, "Gato", "Ração Whiskas", "10 quilos", 1),
#         ( 2, "Cachorro", "Ração Premier", "15 quilos", 1),
#         ( 3, "Cachorro", "Ração Magnus", "15 quilos", 2)
# ''')

# cursor.execute('''
#     insert into Animal (animal_id, nome, especie, raca, idade, cuidados, responsavel_id, abrigo_id) values
#         ( 1, "Rex", "Cachorro", "Vira-lata", 3, Null, 1, 1),
#         ( 2, "Matrix", "Cachorro", "Poodle", 1, Null, Null, 1),
#         ( 3, "Master", "Gato", "Siamês", 10, "Problemas do coluna", Null, 1),
#         ( 4, "Max", "Cachorro", "Labrador", 4, Null, 3, 2),
#         ( 5, "Mel", "Tartaruga", "Sem raça", 3, "Com fratura", Null, 2),
#         ( 6, "Bobi", "Rato", "Sem raça", 1, Null, Null, 2),
#         ( 7, "Pablo", "Gato", "Siamês", 4, "não anda", 3, 2),
#         ( 8, "Marvel", "Cachorro", "Pastor", 7, Null, Null, 2),
#         ( 9, "Bobi", "Rato", "Sem raça", 1, Null, Null, 2)
#     '''
# )

# Listar todos os animais disponíveis no abrigo.
cursor.execute(''' SELECT * FROM Animal where responsavel_id == Null''')

# -- Encontrar todos os animais adotados no momento.
cursor.execute(''' SELECT * FROM Animal where responsavel_id != Null''')

# -- Localizar os animais de um tipo específico.
cursor.execute(''' SELECT * FROM Animal where especie= "Gato"''')

# -- Verificar o número de animais disponíveis de um determinado tipo.
cursor.execute(''' SELECT especie, COUNT(*) AS quantidade_disponivel FROM Animal WHERE abrigo_id = 1 GROUP BY especie = "Cachorro"''')

# -- Escreva consultas SQL para atualizar e excluir registros do banco de dados, 
cursor.execute(''' UPDATE Animal SET responsavel_id = 3 where responsavel_id = 1''')

# -- por exemplo, para remover um animal do abrigo.
cursor.execute(''' DELETE from Animal where animal_id = 1 AND abrigo_id = 1''')


abrigo.commit()


# -- Encontrar todos os animais no momento.
abrigos = cursor.execute('select * from Abrigo').fetchall()
responsaveis = cursor.execute('select * from Responsavel').fetchall()
parcerias = cursor.execute('select * from Parceiros').fetchall()
alimentos = cursor.execute('select * from Alimentos').fetchall()
animais = cursor.execute('select * from Animal').fetchall()

abrigo.close()