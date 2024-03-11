
def game_xo(first_player_score=0, second_player_score=0):
    numbers_for_game = ['0', '1', '2', '3', '4', '5', '6', '7', '8']

    print(f'{numbers_for_game[:3]}\n{numbers_for_game[3:6]}\n{numbers_for_game[6:9]}')

    winning_combinations = [(0, 1, 2), (3, 4, 5), (6, 7, 8),
                            (0, 3, 6), (1, 4, 7), (2, 5, 8),
                            (0, 4, 8), (2, 4, 6)]

    while True:
        first_player_x = int(input('First player: Enter a position for X '))
        if 0 < first_player_x > 8 or numbers_for_game[first_player_x] == 'O' or numbers_for_game[first_player_x] == 'X':
            print('Try again')
        else:
            numbers_for_game[first_player_x] = 'X'
            print(f'{numbers_for_game[:3]}\n{numbers_for_game[3:6]}\n{numbers_for_game[6:9]}')
            for combination in winning_combinations:
                if numbers_for_game[combination[0]] == numbers_for_game[combination[1]]\
                        == numbers_for_game[combination[2]] == 'X':
                    first_player_score += 1
                    if first_player_score == 3:
                        winner = 'Winner is first player'
                        return winner
                    print(f'First player score - {first_player_score}, Second player score - {second_player_score}')
                    return game_xo(first_player_score, second_player_score)
                elif numbers_for_game.count('X') == 5:
                    return 'No winner'
            else:
                while True:
                    second_player_o = int(input('Second Player: Enter a position for O '))
                    if 0 < second_player_o > 8 or numbers_for_game[second_player_o] == 'X' \
                            or numbers_for_game[second_player_o] == 'O':
                        print('Try again')
                    else:
                        numbers_for_game[second_player_o] = 'O'
                        for combination in winning_combinations:
                            if numbers_for_game[combination[0]] == numbers_for_game[combination[1]]\
                                    == numbers_for_game[combination[2]] == 'O':
                                second_player_score += 1
                                if second_player_score == 3:
                                    winner = 'Winner is second player'
                                    return winner
                                print(f'First player score - {first_player_score}, Second player score - {second_player_score}')
                                return game_xo(first_player_score, second_player_score)

                        else:
                            print(f'{numbers_for_game[:3]}\n{numbers_for_game[3:6]}\n{numbers_for_game[6:9]}')
                            break


print(game_xo())
