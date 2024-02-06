import datetime


def cadastrarLivros():
    """ Função para o cadastramento de livros """
    try:
        arquivo = open('dadosLivros.txt','a+')
        arquivo.close()
        dados = {}
        titulo = input('Informe o titúlo do livro: ')
        editora = input('Informe a editora: ')
        generos = []
        qtd_gen = int(input ('Quantos Generos possui? '))
        if qtd_gen >= 0:
            for i in range(qtd_gen):
                generos += input("Insira o {}º genero: ".format(i+1))
        else:
            generos = "Não há Gêneros Cadastrado"
        
        autores = []
        qtd_aut = int(input ('Quantos Autores possui?'))
        if qtd_aut >= 0:
            for i in range(qtd_aut):
                autores += input("Insira o {}º autor(a): ".format(i+1))
        else:
            autores = "Não há autores Cadastrado"
        
        qtd_estoque = input ('Quantos em estoque?')

        dados = {'titulo': titulo, 'editora': editora, 'generos': generos, 'autores': autores, 'qtd_estoque': qtd_estoque}

        #for i in range(len(dados)):
        with open('dadosLivros.txt','a+') as arquivo:
            arquivo.write(str(dados))
            arquivo.write('\n')
            arquivo.close()
        retornarLista = open('dadosLivros.txt','r')
        lista2 = retornarLista.readlines()
        retornarLista.close()
        #return lista2
        #print(lista2)
        print(f'{titulo} cadastrado com sucesso')
            
    except FileNotFoundError:
        arquivo = open('dadosLivros.txt', 'w+')
        cadastrarLivros()

def listaLivros():
    linha_limpa = {}
    lista_cabeca = False
    list_of_the_values = ''
    with open('dadosLivros.txt', 'r') as arquivo:
        for linha in arquivo:
            linha_limpa = eval(linha)
            #linha_string = eval(linha)
            #print(type(linha_limpa))
            #print(linha_limpa)
            cabeca = ''
            if not lista_cabeca:
                for keys in linha_limpa.keys():
                    cabeca += str(keys) + ';'
            lista_cabeca = True
            print(cabeca)
                
            for values in linha_limpa.values():
                list_of_the_values += str(values) + ';'
            #print(type(list_of_the_values))
            print(list_of_the_values)
    arquivo.close()

def BuscaLivros(titulo):
    linha_limpa = {}
    my_dict = {}
    arq_exist = False

    with open('dadosLivros.txt', 'r') as arquivo:

        for linha in arquivo:
            linha_limpa = eval(linha)
            my_dict = linha_limpa
            #print(type(linha_limpa))
            #print(linha_limpa)
            
            if my_dict['titulo'] == titulo and int(my_dict['qtd_estoque'])>0:
                arq_exist = True
                break
        
        return arq_exist

    arquivo.close()


def cadastrarUsuarios():
    """ Função para o cadastramento de Usuários """
    try:
        arquivo = open('dadosUsuarios.txt','a+')
        arquivo.close()
        dados = {}
        nome = input('Informe o Nome: ')
        telefone = input('Informe o Telefone: ')
        nacionalidade = input('Informe a Nacionalidade: ')
        
        dados = {'nome': nome, 'telefone': telefone, 'nacionalidade': nacionalidade}

        #for i in range(len(dados)):
        with open('dadosUsuarios.txt','a+') as arquivo:
            arquivo.write(str(dados))
            arquivo.write('\n')
            arquivo.close()
        retornarLista = open('dadosUsuarios.txt','r')
        lista2 = retornarLista.readlines()
        retornarLista.close()
        #return lista2
        print(f'{nome} Cadastrado com sucesso')
    
    except FileNotFoundError:
        arquivo = open('dadosUsuarios.txt', 'w+')
        cadastrarUsuarios()


def listaUsuarios():
    linha_limpa = {}
    lista_cabeca = False
    list_of_the_values = ''
    with open('dadosUsuarios.txt', 'r') as arquivo:
        for linha in arquivo:
            linha_limpa = eval(linha)
            cabeca = ''
            if not lista_cabeca:
                for keys in linha_limpa.keys():
                    cabeca += str(keys) + ';'
            lista_cabeca = True
            print(cabeca)
                
            for values in linha_limpa.values():
                list_of_the_values += str(values) + ';'
            print(list_of_the_values)
    arquivo.close()

def BuscaUsuario(nome):
    linha_limpa = {}
    my_dict = {}
    arq_exist = False

    with open('dadosUsuarios.txt', 'r') as arquivo:

        for linha in arquivo:
            linha_limpa = eval(linha)
            my_dict = linha_limpa
           
            if my_dict['nome'] == nome:
                arq_exist = True
        
        return arq_exist
    arquivo.close()


def emprestimo ():
    nomeUsuario = input('Informe o nome do usuario: ')
    tituloLivro = input('Informe o titulo do livro: ')

    try:
        arquivo = open('dadosEmprestimo.txt','a+')
        arquivo.close()
        dados = {}
        while 1:
            if not BuscaEmprestimo(nomeUsuario, tituloLivro):
                usuarioexiste = BuscaUsuario(nomeUsuario)
                Livroexiste = BuscaLivros(tituloLivro)
                if not usuarioexiste:
                    print("Usuário não disponível")
                    break

                if not Livroexiste:
                    print("Livro não disponível")
                    break
                    
                
                agora = datetime.datetime.today()
                agora_str = agora.strftime("%d/%m/%Y")
                datadevolucao = agora + datetime.timedelta(5)
                datadevolucao_str = datadevolucao.strftime("%d/%m/%Y")

                dados = {'nome': nomeUsuario, 'titulo': tituloLivro, 'dataemprestimo': agora_str, 'datadevolucao': datadevolucao_str, 'qtdrenova': 0, 'situacao':'Emprestado'}
            
                with open('dadosEmprestimo.txt','a+') as arquivo:
                    arquivo.write(str(dados))
                    arquivo.write('\n')
                    arquivo.close()
                retornarLista = open('dadosEmprestimo.txt','r')
                lista2 = retornarLista.readlines()
                retornarLista.close()
                #return lista2
                estoquelivro ('E', tituloLivro) #ajusta estoque
                print(f"Livro {tituloLivro} emprestado para {nomeUsuario}. Devolver até: {datadevolucao_str}")
                break
            else:
                renovar = input((f"Deseja Renovar ou Devolver o livro {tituloLivro} de {nomeUsuario}? (R/D)"))
                if renovar.upper() in ('R', 'D'):
                    novoarquivo =[]
                    with open('dadosEmprestimo.txt', 'r') as arquivo:
                        for linha in arquivo:
                            linha_limpa = eval(linha)
                            my_dict = linha_limpa
                                                        
                            if my_dict['nome'] == nomeUsuario and my_dict['titulo'] == tituloLivro:
                                agora = datetime.datetime.today()
                                agora_str = agora.strftime("%d/%m/%Y")
                                if renovar.upper() == 'R':
                                    
                                    qtdrevonar = int(my_dict['qtdrenova'])
                                    
                                    datadevolucao = agora + datetime.timedelta(5)
                                    datadevolucao_str = datadevolucao.strftime("%d/%m/%Y")
                                    if qtdrevonar < 3:
                                        qtdrevonar +=1
                                        my_dict['dataemprestimo'] = agora_str
                                        my_dict['datadevolucao'] = datadevolucao_str
                                        my_dict['qtdrenova'] = qtdrevonar
                                        my_dict['situacao'] = 'Renovado'

                                    else:
                                        print("Você já excedeu o número de renovações")
                                        break
                                elif renovar.upper() == 'D':
                                    datadevolucao_str = agora_str
                                    my_dict['datadevolucao'] = agora_str
                                    my_dict['situacao'] = 'Ok'
                                else:
                                    print("Opção não existe")
                                    break

                            novoarquivo.append(str(my_dict)+'\n')

                    with open('dadosEmprestimo.txt', 'w') as arquivo:
                        arquivo.writelines(novoarquivo)
                        arquivo.close()  
                        if renovar.upper() == 'R':
                            print(f"Livro {tituloLivro} renovado para {nomeUsuario}. Devolver até: {datadevolucao_str}")
                        elif renovar.upper() == 'D':
                            estoquelivro ('I', tituloLivro)
                            print(f"{nomeUsuario} Devolveu o Livro {tituloLivro} em {datadevolucao_str}")
                        break       
                else:
                    break                
    except FileNotFoundError:
        arquivo = open('dadosEmprestimo.txt', 'w+')
        emprestimo()


def BuscaEmprestimo(nome, titulo):
    linha_limpa = {}
    my_dict = {}
    arq_exist = False

    with open('dadosEmprestimo.txt', 'r') as arquivo:

        for linha in arquivo:
            linha_limpa = eval(linha)
            my_dict = linha_limpa
           
            if my_dict['nome'] == nome and my_dict['titulo'] == titulo and my_dict['situacao'].upper() != "OK":
                arq_exist = True
                arquivo.close()
                break
        
        return arq_exist

def devolucao ():
    nomeUsuario = input('Informe o nome do usuario: ')
    tituloLivro = input('Informe o titulo do livro: ')

    try:
        arquivo = open('dadosEmprestimo.txt','a+')
        arquivo.close()
        dados = {}
        while 1:
            if not BuscaEmprestimo(nomeUsuario, tituloLivro):
                print(f'Não há livro {tituloLivro} emprestado para {nomeUsuario}')
                break
            else:
                novoarquivo =[]
                with open('dadosEmprestimo.txt', 'r') as arquivo:
                    for linha in arquivo:
                        linha_limpa = eval(linha)
                        my_dict = linha_limpa
                                                    
                        if my_dict['nome'] == nomeUsuario and my_dict['titulo'] == tituloLivro:
                            agora = datetime.datetime.today()
                            agora_str = agora.strftime("%d/%m/%Y")
                            datadevolucao_str = agora_str
                            my_dict['datadevolucao'] = agora_str
                            my_dict['situacao'] = 'Ok'

                        novoarquivo.append(str(my_dict)+'\n')

                    with open('dadosEmprestimo.txt', 'w') as arquivo:
                        arquivo.writelines(novoarquivo)
                        arquivo.close()  
                        estoquelivro ('I', tituloLivro)
                        print(f"{nomeUsuario} Devolveu o Livro {tituloLivro} em {datadevolucao_str}")
                        break       
                
    except FileNotFoundError:
        arquivo = open('dadosEmprestimo.txt', 'w+')
        emprestimo()

def estoquelivro (operacao, tituloLivro):
    novoarquivo =[]
    with open('dadosLivros.txt', 'r') as arquivo:
        
        for linha in arquivo:
            linha_limpa = eval(linha)
            my_dict = linha_limpa
                                        
            if my_dict['titulo'] == tituloLivro :
                if operacao.upper() == 'I':
                    qtd = int(my_dict['qtd_estoque'])
                    my_dict['qtd_estoque'] = qtd + 1
                    
                elif operacao.upper() == 'E':
                    qtd = int(my_dict['qtd_estoque'])
                    my_dict['qtd_estoque'] = qtd - 1
                else:
                    print("Opção não existe")
                    break

            novoarquivo.append(str(my_dict)+'\n')

    with open('dadosLivros.txt', 'w') as arquivo:
        arquivo.writelines(novoarquivo)
        arquivo.close()
    
    return True
