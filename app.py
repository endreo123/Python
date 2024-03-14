import os
from platform import system

restaurantes = [{
        'nome': 'Sushi',
        'categoria': 'Japonesa',
        'ativo': False
    },
    {
        'nome': 'Pizza Suprema',
        'categoria': 'Italiana',
        'ativo': 'False'
    },
    {
        'nome': 'Cantina',
        'categoria': 'Italiano',
        'ativo': False
    }
];

def limpar_tela():
    ''' Função para limpar o terminal em sistemas Linux, Mac, e Windows'''
    system_os = system()

    if (system_os == 'Linux' or system_os == 'Mac'):
        os.system('clear')
    else:
        os.system('cls')

def exibir_nome_do_programa():
    '''Função que exibe o nome do Programa'''

    print("""
    ░██████╗░█████╗░██████╗░░█████╗░██████╗░  ███████╗██╗░░██╗██████╗░██████╗░███████╗░██████╗░██████╗
    ██╔════╝██╔══██╗██╔══██╗██╔══██╗██╔══██╗  ██╔════╝╚██╗██╔╝██╔══██╗██╔══██╗██╔════╝██╔════╝██╔════╝
    ╚█████╗░███████║██████╦╝██║░░██║██████╔╝  █████╗░░░╚███╔╝░██████╔╝██████╔╝█████╗░░╚█████╗░╚█████╗░
    ░╚═══██╗██╔══██║██╔══██╗██║░░██║██╔══██╗  ██╔══╝░░░██╔██╗░██╔═══╝░██╔══██╗██╔══╝░░░╚═══██╗░╚═══██╗
    ██████╔╝██║░░██║██████╦╝╚█████╔╝██║░░██║  ███████╗██╔╝╚██╗██║░░░░░██║░░██║███████╗██████╔╝██████╔╝
    ╚═════╝░╚═╝░░╚═╝╚═════╝░░╚════╝░╚═╝░░╚═╝  ╚══════╝╚═╝░░╚═╝╚═╝░░░░░╚═╝░░╚═╝╚══════╝╚═════╝░╚═════╝░
        """)

def exibir_opcoes():
    '''Função que exibe as opções disponíveis'''

    print('1 - Cadastrar Restaurante');
    print('2 - Listar Restaurante');
    print('3 - Alternar estado do restaunte');
    print('4 - Sair \n');

def finalizar_app():
    '''Função que finaliza o app'''
    exibir_subtitulo('Saindo do app\n')

def opcao_invalida():
    '''Essa função é utilizada quando o usuário opta por uma opção invalida'''
    print('Opção invalida!!\n');
    voltar_ao_menu_principal();

def exibir_subtitulo(texto):
    '''Função para exibição de subtitulos'''
    limpar_tela();
    linha = '*' * len(texto)
    print(linha)
    print(texto);
    print(linha)

def cadastrar_novo_restaurante():
    '''Essa função é resposavel por cadastrar um novo restaurante

    Inputs:
    - Nome do Restaurante
    - Categoria

    Output:
    - Adiciona um novo restaurante a lista de Restaurantes

    '''
    exibir_subtitulo('Cadastro de novos restaurantes')

    nome_do_restaurantes = input('Digite o nome do restaunte que deseja cadastrar: ')
    categoria = input(f'Digite o nome da categoria do restaurante {nome_do_restaurantes}: ')

    dados_do_restaunte = {
        'nome': nome_do_restaurantes,
        'categoria': categoria,
        'ativo': False
    }

    restaurantes.append(dados_do_restaunte);

    print(f'O restaurante {nome_do_restaurantes} foi incluido com sucesso\n')

    voltar_ao_menu_principal();

def voltar_ao_menu_principal():
    input('\nDigite uma tecla para voltar ao menu principal');
    main();

def listar_restaurentes():
    '''Função que lista os Restaurantes'''
    exibir_subtitulo('Listando os restaurantes:');

    print('')
    for restaurante in restaurantes:
        nome_restaurante = restaurante['nome']
        categoria = restaurante['categoria']
        ativo = 'ativado' if restaurante['ativo'] else 'desativado'
        print(f' - {nome_restaurante.ljust(20)} | {categoria.ljust(20)} | {ativo}')

    voltar_ao_menu_principal();

def alternar_estado_do_restaurante():
    '''Função que ativa/desativa os restaurantes'''
    exibir_subtitulo('Alternando estado do restaurante');

    nome_do_restaurante = input('Digite o nome do restautente: ')

    restaurante_encontrado = False;

    for restaurante in restaurantes:
        if(nome_do_restaurante == restaurante['nome']):
            restaurante_encontrado = True
            restaurante['ativo'] = not restaurante['ativo']
            mensagem = f'O restaurante {nome_do_restaurante} foi ativo com sucesso' if restaurante['ativo'] else f'o restaurante {nome_do_restaurante} foi desativado com sucesso'

            print(mensagem)

    if not (restaurante_encontrado):
        print('O restaunte não foi encontrado')

    voltar_ao_menu_principal();

def escolher_opcao():
    '''Função que captura a opção escolhida e mostra o menu correspondente'''
    try:
        opcao_escolhida = int(input('Esolha uma opção:'))

        if opcao_escolhida == 1:
            cadastrar_novo_restaurante()
        elif opcao_escolhida == 2:
            listar_restaurentes()
        elif opcao_escolhida == 3:
            alternar_estado_do_restaurante()
        elif opcao_escolhida == 4:
            finalizar_app()
        else:
            opcao_invalida()
    except:
        opcao_invalida()

def main():
    '''Função Principal'''
    limpar_tela()
    exibir_nome_do_programa();
    exibir_opcoes();
    escolher_opcao();

if (__name__ == '__main__'):
    main()
