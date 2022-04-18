from asyncio.windows_events import NULL
import os
from random import randint

option = ''
while option != '4':
  os.system('cls||clear')
  print('>(1) Jogador vs Jogador\n')
  print('>(2) Jogador vs Computador\n')
  print('>(3) Computador vs Computador\n')
  print('Obs: Digite qualquer outra tecla para sair\n')
  option = input('\nEscolha uma opção: ')
  if option == '1' or option == '2' or option == '3':
    os.system('cls||clear')
    if option == '1':
      print('Você escolheu Jogador vs Jogador, deseja continuar ?\n')
      player_one_name = 'Jogador1'
      player_two_name = 'Jogador2'
      number_of_input_options = 2
    elif option == '2':
      print('Você escolheu Jogador vs Computador, deseja continuar ?\n')
      player_one_name = 'Jogador'
      player_two_name = 'Computador'
      number_of_input_options = 1
    elif option == '3':
      print('Você escolheu Computador vs Computador, deseja continuar ?\n')
      player_one_name = 'Computador1'
      player_two_name = 'Computador2'
    print('>(1) Sim\n')
    print('Obs: Digite qualquer outra tecla para sair\n')
    proceed_to_selected_mode = input('\nEscolha uma opção: ')
    if proceed_to_selected_mode == '1':
      player_one_points = 0
      player_two_points = 0
      draws = 0
      matches = 1
      exit_selected_mode = False
      while not exit_selected_mode:
        player_one_option = NULL
        player_two_option = NULL
        if(option == '1' or option == '2'):
          counter = 0
          while counter < number_of_input_options and not exit_selected_mode:
            os.system('cls||clear')
            print('>(1) Pedra\n')
            print('>(2) Papel\n')
            print('>(3) Tesoura\n')
            print('Obs: Digite qualquer outra tecla para sair\n')
            if(option == '1' and counter == 0):
              player_one_option = input(
                  f'\nEscolha uma opção {player_one_name}: ')
            elif(option == '1' and counter == 1):
              player_two_option = input(
                  f'\nEscolha uma opção {player_two_name}: ')
            elif(option == '2'):
              player_one_option = input('\nEscolha uma opção: ')
              player_two_option = str(randint(1, 3))
            else:
              counter = number_of_input_options
            if(player_one_option != NULL and player_one_option != '1' and player_one_option != '2' and player_one_option != '3' or player_two_option != NULL and player_two_option != '1' and player_two_option != '2' and player_two_option != '3'):
              exit_selected_mode = True
            counter += 1
        else:
          player_one_option = str(randint(1, 3))
          player_two_option = str(randint(1, 3))
        if((player_one_option == '1' or player_one_option == '2' or player_one_option == '3') and (player_two_option == '1' or player_two_option == '2' or player_two_option == '3')):
          if(player_one_option == '1' and player_two_option == '3' or player_one_option == '2' and player_two_option == '1' or player_one_option == '3' and player_two_option == '2'):
            player_won = 1
            player_one_points += 1
            winner_name = player_one_name
          elif(player_two_option == '1' and player_one_option == '3' or player_two_option == '2' and player_one_option == '1' or player_two_option == '3' and player_one_option == '2'):
            player_won = 2
            player_two_points += 1
            winner_name = player_two_name
          elif(player_one_option == player_two_option):
            player_won = 0
            draws += 1
          if(player_one_option == '1'):
            player_one_result_option = 'Pedra'
          elif(player_one_option == '2'):
            player_one_result_option = 'Papel'
          else:
            player_one_result_option = 'Tesoura'
          if(player_two_option == '1'):
            player_two_result_option = 'Pedra'
          elif(player_two_option == '2'):
            player_two_result_option = 'Papel'
          else:
            player_two_result_option = 'Tesoura'
          os.system('cls||clear')
          print('Resumo da partida:\n')
          print(
              f'{player_one_name} ({player_one_points} pontos) vs {player_two_name} ({player_two_points} pontos) \n')
          print(f'{player_one_name} escolheu: {player_one_result_option}\n')
          print(f'{player_two_name} escolheu: {player_two_result_option}\n')
          if(player_won != 0):
            print(f'Resultado: {winner_name} venceu !\n')
          else:
            print('Ocorreu um empate !\n')
          print('\nDeseja continuar?\n')
          print('>(1) Sim\n')
          print('Obs: Digite qualquer outra tecla para sair\n')
          continue_playing = input('\nEscolha uma opção: ')
          if(continue_playing != '1'):
            exit_selected_mode = True
          matches += 1
          if(matches == 4):
            exit_selected_mode = True
            win_percentage_player_one = (player_one_points/3)*100
            win_percentage_player_two = (player_two_points/3)*100
            os.system('cls||clear')
            print(
                f'Total de partidas jogadas: {matches-1}\n')
            print(
                f'Porcentagem de vitória {player_one_name}: {win_percentage_player_one:.2f}%\n')
            print(
                f'Porcentagem de vitória {player_two_name}: {win_percentage_player_two:.2f}%\n')
            print(
                f'Número de empates: {draws}\n')
            input('\n>Digite qualquer tecla para voltar ao menu principal: ')
  else:
    os.system('cls||clear')
    option = '4'
