# Jogo criado por Gabriel Chiarelli - 31/03/2022

from random import randint                                                                          # importa a função 'randint' do módulo 'random'

numeros_possiveis = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]                                                  # números que o Jogador pode escolher
opcoes_possiveis = ['PAR', 'P', 'ÍMPAR', 'IMPAR', 'I']                                              # palavras/letras que o Jogador pode digitar
continuar = 'S'                                                                                     # controla se o Jogador vai continuar jogando ou não
vitorias_jogador = vitorias_cpu = 0                                                                 # contador de vitórias (começa com o placar de 0 para os dois)

while continuar in 'S'[0]:
    computador = randint(0, 10)                                                                     # o Computador sorteia um número de 0 a 10
    #print(f'DEBUG: O COMPUTADOR ESCOLHEU {computador}')                                            # remover a '#' para ver a escolha do Computador e testar o jogo

    jogador = int(input('Digite um número de 0 a 10: '))
    while jogador not in numeros_possiveis:                                                         # roda enquanto o Jogador não digitar um número válido
        jogador = int(input('Valor inválido. Por favor, digite um número de 0 a 10: '))
    soma = (jogador + computador)
    conta = (soma % 2)                                                                              # pega o módulo da divisão da soma

    opcao = str(input('PAR ou ÍMPAR? [P = par|| I = ímpar]: ')).strip().upper()[0]
    while opcao not in opcoes_possiveis:                                                            # roda enquanto o Jogador não digitar uma palavra/letra válida
        opcao = str(input('Valor inválido. Por favor, coloque P para par ou I para ímpar: '))
    if opcao in 'P':                                                                                # se o Jogador optar por PAR
        print('Você escolheu PAR')
        if conta == 0:
            print(f'Você jogou {jogador} e eu joguei {computador}. O total é {soma}, ou seja, o resultado é PAR! \nVOCÊ VENCEU!')
            vitorias_jogador += 1
        else:
            print(f'Você jogou {jogador} e eu joguei {computador}. O total é {soma}, ou seja, o resultado é ÍMPAR! \nVOCÊ PERDEU!')
            vitorias_cpu += 1
    elif opcao in 'I':                                                                              # se o Jogador optar por ÍMPAR
        print('Você escolheu ÍMPAR')
        if conta == 0:
            print(f'Você jogou {jogador} e eu joguei {computador}. O total é {soma}, ou seja, o resultado é PAR! \nVOCÊ PERDEU!')
            vitorias_cpu += 1
        else:
            print(f'Você jogou {jogador} e eu joguei {computador}. O total é {soma}, ou seja, o resultado é ÍMPAR! \nVOCÊ VENCEU!')
            vitorias_jogador += 1

    print('-=' * 19)
    continuar = str(input('Deseja continuar jogando? [S/N] ')).strip().upper()[0]
    print('-=' * 19)
    while continuar not in 'SN':                                                                    # roda enquanto o Jogador não digitar uma opção válida
        continuar = str(input('Opção inválida. Por favor coloque S para SIM ou N para NÃO: ')).strip().upper()[0]

print('FIM DE JOGO')
print('-=' * 19)
print(f'PLACAR FINAL: JOGADOR {vitorias_jogador} x {vitorias_cpu} COMPUTADOR')                      # exibe o placar final
print('-=' * 19)
print('Obrigado por jogar! Volte sempre :)')

# Jogo criado por Gabriel Chiarelli - 31/03/2022