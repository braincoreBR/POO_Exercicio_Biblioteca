import Biblioteca

while 1:
            print()
            print('Menu do Sistema'.center(40))
            print('Escolha o número referente a opção desejada'.center(40))
            print()
            opcao = input("1 - Cadastro 2 - Movimentações 3 - Finalizar: ")

            if(opcao == '1'):
                print()
                opcaoCad = input('1 - Cadastrar Aluno 2 - Cadastrar Livro 3 - Retornar ao Menu Anterior: ')
                
                if(opcaoCad == '1'):
                    print()
                    print('...::: Cadastro de Alunos :::...')
                    cadMaisUm = 'sim'
                    while(cadMaisUm != 'nao'): #inicia o loop para solicitar ao usuário se deseja cadastrar mais um
                        Biblioteca.cadastrarUsuarios() #executa a função cadastrar usuario
                        cadMaisUm = str.lower(input('Deseja cadastrar mais um usuario ? Sim ou Nao: '))
                    #fim do loop
                elif(opcaoCad == '2'):
                    print()
                    print('...::: Cadastro de Livros :::...')
                    cadMaisUm = 'sim'
                    while(cadMaisUm != 'nao'): #inicia o loop para solicitar ao usuário se deseja cadastrar mais um
                        Biblioteca.cadastrarLivros() #recebe a função cadastrarLivro
                        cadMaisUm = str.lower(input('Deseja cadastrar mais um livro ? Sim ou Nao: '))
                    #fim do loop
                elif(opcaoCad == '3'):
                    continue
            
            elif(opcao == '2'):
                while 1:
                    print()
                    opcaoCad = input('1 - Consultar Acervo 2 - Empréstimo 3 - Devolução 4 - Retornar ao Menu Anterior: ')
                    
                    if(opcaoCad == '1'):
                        print('-' * 40)
                        print('...::: Livros disponíveis :::...')
                        print()
                        Biblioteca.listaLivros()
                        print()
                        print('-' * 40)
                        continue
                    elif(opcaoCad == '2'):
                        print('-' * 40)
                        print('...::: Empréstimo de Livros :::...')
                        print()
                        Biblioteca.emprestimo() 
                        print()
                        print('-' * 40)
                    elif(opcaoCad == '3'):
                        print('-' * 40)
                        print('...::: Devolução de Livros :::...')
                        print()
                        Biblioteca.devolucao() #recebe a função devolução onde irá acessar o arquivo aluno e livro e fazer a transação
                        print()
                        print('-' * 40)
                    elif(opcaoCad == '4'):
                        break

            
            elif(opcao == '3'):
                break