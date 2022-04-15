import os
from random import randint

option = ''
error_message = '\nOpção inválida, tente novamente !'

while option != '4':
  os.system('cls||clear')
  print('>(1) Jogador vs Jogador\n')
  print('>(2) Jogador vs Computador\n')
  print('>(3) Computador vs Computador\n')
  print('Obs: Digite qualquer outra tecla para sair\n')
  option = input('\nEscolha uma opção: ')
  if option == '1' or option == '2' or option == '3':
    exit_selected_mode = False
    player_one_points = 0
    player_two_points = 0
    draws = 0
    matches = 1
    player_won = 0  # could be player one (1) or two (2) or anybody (0)
    continue_playing = 0  # could be YES (1) or NO (0)
    skip_score = 0
    proceed_to_selected_mode = ''
    player_one_option = ''
    player_two_option = ''
    player_one_result_option = ''
    player_two_result_option = ''
    if option == '2':
      os.system('cls||clear')
      print('Você escolheu Jogador vs Computador, deseja continuar ?\n')
      print('>(1) Sim\n')
      print('Obs: Digite qualquer outra tecla para sair\n')
      proceed_to_selected_mode = input('\nEscolha uma opção: ')
      if proceed_to_selected_mode == '1':
        while matches != 4 or not exit_selected_mode:
          os.system('cls||clear')
          print(
              f'Jogador(Venceu {player_one_points}) vs Computador(Venceu {player_two_points})\n')
          print(f'Total de Partidas: {matches - 1}\n\n')
          print('>(1) Pedra\n')
          print('>(2) Papel\n')
          print('>(3) Tesoura\n')
          print('Obs: Digite qualquer outra tecla para sair\n')
          player_one_option = input('\nEscolha uma opção: ')
          if(player_one_option == '1' or player_one_option == '2' or player_one_option == '3'):
            player_two_option = str(randint(1, 3))
            if(player_one_option == '1' and player_two_option == '2'):
              player_won = 2
            elif(player_one_option == '2' and player_two_option == '1'):
              player_won = 1
            elif(player_one_option == '3' and player_two_option == '1'):
              player_won = 2
            elif(player_two_option == '3' and player_one_option == '1'):
              player_won = 1
            elif(player_one_option == '3' and player_two_option == '2'):
              player_won = 1
            elif(player_two_option == '3' and player_one_option == '2'):
              player_won = 2
            elif(player_one_option == player_two_option):
              player_won = 0
            if player_won == 1:
              player_one_points += 1
            elif player_won == 2:
              player_two_points += 1

            if(player_one_option == 1):
              player_one_result_option = 'Pedra'
            elif(player_one_option == 2):
              player_one_result_option = 'Papel'
            else:
              player_one_result_option = 'Tesoura'

            if(player_two_option == 1):
              player_two_result_option = 'Pedra'
            elif(player_two_option == 2):
              player_two_result_option = 'Papel'
            else:
              player_two_result_option = 'Tesoura'
            os.system('cls||clear')
            print('Resumo da partida:\n')
            print(f'Jogador escolheu: {player_one_result_option}\n')
            print(f'Computador escolheu: {player_two_result_option}\n')
            if(player_won == 1):
              print('Jogador venceu !\n')
            elif(player_won == 2):
              print('Computador venceu !\n')
            else:
              draws += 1
              print('Ocorreu um empate !\n')
            print('\nDeseja continuar?\n')
            print('>(1) Sim\n')
            print('Obs: Digite qualquer outra tecla para sair\n')
            continue_playing = int(input('\nEscolha uma opção: '))

            if(continue_playing != 1):
              exit_selected_mode
            matches += 1

            if(matches == 4):
              while(skip_score == 0):
                os.system('cls||clear')
                print(
                    f'Total de partidas jogadas: {matches-1}\n')
                print(
                    f'Partidas vencidas pelo jogador 1: {player_one_points}\n')
                print(
                    f'Partidas vencidas pelo computador: {player_two_points}\n')
                print(
                    f'Número de empates: {draws}\n')
                int(input('\n>Digite qualquer tecla para sair'))
                skip_score = 1
          else:
            exit_selected_mode = True
  elif option == 4:
    print('Até mais !')
  else:
    os.system('cls||clear')
    print(f"{error_message}")
    option = 0
