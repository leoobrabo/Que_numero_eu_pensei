import random
# nome do programa print('Que número eu pensei?\n'))


def nivel_de_jogo():
    dificuldade = input('Escolha o nivel de dificuldade')
    if dificuldade == 'facil':
        facil = random.randint(1, 10)
        return facil
    elif dificuldade == 'medio':
        medio = random.randint(1, 100)
        return medio
    elif dificuldade == 'dificil':
        dificil = random.randint(1, 1000)
        return dificil
    else:
        print('opçao invalida ')


def iniciar_programa():
    input('Digite enter para iniciar o programa...')


def gerar_valor_aleatorio():
    numero_aleatorio = random.randint(1, 100)
    # print(numero_aleatorio)
    print('Foi gerado um numero entre 1 e 100')
    return numero_aleatorio


def chute_um_numero():
    numero_aleatorio = int(gerar_valor_aleatorio())
    jogar = True
    while jogar:
        valor_chute = int(input('Chute um numero de 1 a 100: '))
        if valor_chute == numero_aleatorio:
            verde('Parabens!!!\nVocê acertou')
            jogar = False
            # nivel_de_jogo()
            jogar_novamente()
        elif valor_chute > numero_aleatorio:

            azul('Digite um valor menor')
        else:
            amarelo('Digite um valor maior')


def jogar_novamente():
    escolha = input('Deseja jogar novamente: (s/n) ')
    escolha.lower()
    if escolha == 's' or escolha == 'sim':
        chute_um_numero()
    elif escolha == 'n' or escolha == 'nao' or escolha == 'não':
        print('Obrigado por jogar...')


def separar_por_linha():
    print('-'*141)


def vermelho(palavra):
    print(f'\u001b[31m{palavra}\u001b[0m')


def verde(palavra):
    print(f'\u001b[32m{palavra}\u001b[0m')


def amarelo(palavra):
    print(f'\u001b[33m{palavra}\u001b[0m')


def azul(palavra):
    print(f'\u001b[34m{palavra}\u001b[0m')


def apresentar_programa():
    separar_por_linha()
    print('''\u001b[32m  _______                                                                                                                      __     _____ 
 |   _   |.--.--..-----.   .-----..--.--..--------..-----..----..-----.   .-----..--.--.   .-----..-----..-----..-----..-----.|__|   |__   |
 |.  |   ||  |  ||  -__|   |     ||  |  ||        ||  -__||   _||  _  |   |  -__||  |  |   |  _  ||  -__||     ||__ --||  -__||  |   ',  ,- 
 |.  |   ||_____||_____|   |__|__||_____||__|__|__||_____||__|  |_____|   |_____||_____|   |   __||_____||__|__||_____||_____||__|    |--|  
 |:  1   |                                                                                 |__|                                       '--   
 |::..   |                                                                                                                                  
 `----|:.|                                                                                                                                  
      `--'                                                                                                                                  \u001b[0m''')
    print(' '*27 + 'Chute o numero!')
    separar_por_linha()


apresentar_programa()
iniciar_programa()
chute_um_numero()
