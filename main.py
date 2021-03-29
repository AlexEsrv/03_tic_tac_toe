import os

game_field_keys = " 1 | 2 | 3 \n" \
           " 4 | 5 | 6 \n" \
           " 7 | 8 | 9 "


def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')


def process_game_field(p1_marks, p2_marks):
    game_field_marks = [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ']

    for mark in p1_marks:
        game_field_marks[mark-1] = 'X'

    for mark in p2_marks:
        game_field_marks[mark-1] = '0'

    game_field = f" {game_field_marks[0]} | {game_field_marks[1]} | {game_field_marks[2]} \n" \
               f" {game_field_marks[3]} | {game_field_marks[4]} | {game_field_marks[5]} \n" \
               f" {game_field_marks[6]} | {game_field_marks[7]} | {game_field_marks[8]} "

    print(game_field)


def check_victory(player_marks):
    winning_combinations = [[1, 2, 3], [4, 5, 6], [7, 8, 9], [1, 4, 7], [2, 5, 8], [3, 6, 9], [1, 5, 9], [3, 5, 7]]
    check = False
    for comb in winning_combinations:
        check = all(item in player_marks for item in comb)
        if check:
            break
    return check


def process_screen(p1_marks, p2_marks):
    clear_screen()
    print("------------------")
    print(game_field_keys)
    print("------------------")
    process_game_field(p1_marks, p2_marks)
    print("------------------")


player1_marks = []
player2_marks = []

game_over = False
current_move = 'Player 1'
while not game_over:
    process_screen(player1_marks, player2_marks)

    waiting_for_input = True
    player_move = 0
    while waiting_for_input:
        player_move = input(current_move + " move: ").strip()
        if player_move == 'q':
            game_over = True
            break

        if player_move.isdigit():
            player_move = int(player_move)
            if player_move not in (player1_marks + player2_marks) and 0 < player_move < 10:
                waiting_for_input = False
                if current_move == 'Player 1':
                    player1_marks.append(player_move)
                else:
                    player2_marks.append(player_move)

    if game_over:
        continue

    game_over = check_victory(player1_marks) or check_victory(player2_marks)

    if game_over:
        process_screen(player1_marks, player2_marks)
        print(current_move + " won!")
        continue

    if current_move == 'Player 1':
        current_move = 'Player 2'
    else:
        current_move = 'Player 1'
