numbers_for_game = ['0', '1', '2', '3', '4', '5', '6', '7', '8']

print(numbers_for_game[:3])
print(numbers_for_game[3:6])
print(numbers_for_game[6:9])

p = 0
while p < 9:
    first_player_X = int(input('First player: Enter a position for X '))
    if 0 < first_player_X > 8 or numbers_for_game[first_player_X] == 'O' or numbers_for_game[first_player_X] == 'X':
        print('Try again')
        p -= 1
    else:
        numbers_for_game[first_player_X] = 'X'
        print(numbers_for_game[:3])
        print(numbers_for_game[3:6])
        print(numbers_for_game[6:9])
        if \
                (numbers_for_game[0]+numbers_for_game[1] + numbers_for_game[2]) == 'XXX' \
                or (numbers_for_game[0]+numbers_for_game[3] + numbers_for_game[6]) == 'XXX' \
                or (numbers_for_game[0]+numbers_for_game[4] + numbers_for_game[8]) == 'XXX'\
                or (numbers_for_game[1]+numbers_for_game[4] + numbers_for_game[7]) == 'XXX'\
                or (numbers_for_game[2]+numbers_for_game[5] + numbers_for_game[8]) == 'XXX'\
                or (numbers_for_game[2]+numbers_for_game[4] + numbers_for_game[6]) == 'XXX'\
                or (numbers_for_game[6]+numbers_for_game[7] + numbers_for_game[8]) == 'XXX'\
                or (numbers_for_game[3]+numbers_for_game[4] + numbers_for_game[5]) == 'XXX':
            print('Winner is first player')
            break
        elif numbers_for_game.count('X') == 5:
            print('No Winner')
            break
        else:
            p += 1
            while True:
                second_player_O = int(input('Second Player: Enter a position for O '))
                if 0 < second_player_O > 8 or numbers_for_game[second_player_O] == 'X' \
                        or numbers_for_game[second_player_O] == 'O':
                    print('Try again')
                else:
                    numbers_for_game[second_player_O] = 'O'
                    if \
                            (numbers_for_game[0] + numbers_for_game[1] + numbers_for_game[2]) == 'OOO' \
                            or (numbers_for_game[0] + numbers_for_game[3] + numbers_for_game[6]) == 'OOO' \
                            or (numbers_for_game[0] + numbers_for_game[4] + numbers_for_game[8]) == 'OOO' \
                            or (numbers_for_game[1] + numbers_for_game[4] + numbers_for_game[7]) == 'OOO' \
                            or (numbers_for_game[2] + numbers_for_game[5] + numbers_for_game[8]) == 'OOO' \
                            or (numbers_for_game[2] + numbers_for_game[4] + numbers_for_game[6]) == 'OOO' \
                            or (numbers_for_game[6] + numbers_for_game[7] + numbers_for_game[8]) == 'OOO' \
                            or (numbers_for_game[3] + numbers_for_game[4] + numbers_for_game[5]) == 'OOO':
                        print('Winner is second player')
                        p = 200
                        break
                    else:
                        print(numbers_for_game[:3])
                        print(numbers_for_game[3:6])
                        print(numbers_for_game[6:9])
                        p += 1
                        break
