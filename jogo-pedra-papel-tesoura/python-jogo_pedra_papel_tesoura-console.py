#Jogo criado por Gabriel Chiarelli - 30/03/2022

from random import randint
from time import sleep

opcao = 'S'                                                                         # diz se o jogador quer continuar jogando (começa com 'S' (sim))
vcpu = 0                                                                            # vitórias do computador
vjog = 0                                                                            # vitórias do jogador

print('-=' * 5)
print('JO-KEN-PÔ')
print('-=' * 5)

while opcao in 'S':
    computador = randint(0, 2)
    #print(f'DEBUG: O COMPUTADOR ESCOLHEU: {computador}')                           # remover a '#' para ver a jogada do computador e, assim, testar o jogo
    print('[ 0 ] PEDRA [ 1 ] PAPEL [ 2 ] TESOURA')
    jogador = str(input('Sua jogada: '))

    while jogador not in '012':
        jogador = str(input('Jogada inválida. Tente novamente: '))                  # caso o jogador não digite 0 ou 1 ou 2
        if jogador in '012':
            break

    sleep(0.7)                                                                      # o computador "dorme" por x segundos, dando a ilusão de que ele está pensando

    if computador == 0:                                                             # se o computador jogar PEDRA
        if jogador == '0':
            print('Você escolheu PEDRA e o computador também escolheu PEDRA')
            print('EMPATE')
        elif jogador == '1':
            print('Você escolheu PAPEL e o computador escolheu PEDRA')
            print('JOGADOR VENCEU')
            vjog += 1
        elif jogador == '2':
            print('Você escolheu TESOURA e o computador escolheu PEDRA')
            print('COMPUTADOR VENCEU')
            vcpu += 1
    elif computador == 1:                                                           # se o computador jogar PAPEL
        if jogador == '0':
            print('Você escolheu PEDRA e o computador escolheu PAPEL')
            print('COMPUTADOR VENCEU')
            vcpu += 1
        elif jogador == '1':
            print('Você escolheu PAPEL e o computador também escolheu PAPEL')
            print('EMPATE')
        elif jogador == '2':
            print('Você escolheu TESOURA e o computador escolheu PAPEL')
            print('JOGADOR VENCEU')
            vjog += 1
    elif computador == 2:                                                           # se o computador jogar TESOURA
        if jogador == '0':
            print('Você escolheu PEDRA e o computador escolheu TESOURA')
            print('JOGADOR VENCEU')
            vjog += 1
        if jogador == '1':
            print('Você escolheu PAPEL e o computador escolheu TESOURA')
            print('COMPUTADOR VENCEU')
            vcpu += 1
        if jogador == '2':
            print('Você escolheu TESOURA e o computador também escolheu TESOURA')
            print('EMPATE')
    opcao = str(input('Deseja continuar jogando? [S/N] ')).strip().upper()          # pergunta se o jogador que jogar navamente

print('-=' * 17)
print('FIM DE JOGO')
print(f'PLACAR: JOGADOR {vjog} X {vcpu} COMPUTADOR')                                # mostra o placar final do jogo
print('Obrigado por jogar! Volte sempre :)')

#Jogo criado por Gabriel Chiarelli - 30/03/2022
