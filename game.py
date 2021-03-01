import math
from typing import List, Optional, Union

import config
from base import UserPlayer, ComputerPlayer, TicTacToe
from enums import Sign
from utils import (is_row_filled, is_column_filled,
                   is_diag_filled, change_player)


def get_winner(
        current_game_field: List[str],
        sign: Sign,
        chosen_field: Optional[int]
) -> Union[None, Sign, str]:
    if chosen_field is None:
        return None
    rows_count = int(math.sqrt(config.MAX_FIELDS_COUNT))
    handler = {
        'row': is_row_filled,
        'column': is_column_filled,
        'diag': is_diag_filled,
    }
    for key in handler:
        check_winner = handler[key]
        if check_winner(current_game_field, sign, chosen_field, rows_count):
            return sign

    if all([f != ' ' for f in current_game_field]):
        return 'tie'
    return None


def show_result(result: Union[bool, Sign, None]) -> None:
    if result == 'tie':
        print('It is a tie!')
    else:
        print(f'{result.value} is winner!')


def game(game: TicTacToe, user: UserPlayer, computer: ComputerPlayer):
    numbers_game_field = game.get_initial_game_field_with_numbers()
    print(game.prep_game_field_for_print(numbers_game_field))
    is_user_starts = config.IS_USER_STARTS_THE_GAME
    sign = Sign.computer if is_user_starts else Sign.user

    while not get_winner(game.game_field, sign, game.chosen_field):

        sign, is_user_starts = change_player(is_user_starts, sign)

        if is_user_starts:
            game.chosen_field = computer.choose_empty_field(computer.find_empty_fields(game.game_field))
        else:
            while True:
                game.chosen_field = int(input(user.ask_user_for_field_number()))
                if user.is_empty_field(game.chosen_field, game.game_field):
                    break
                print('This field is taken. Try again.')
        game.game_field = game.make_turn(sign)
        print(game.get_info_about_turn(game.chosen_field, sign))
        print(game.prep_game_field_for_print(game.game_field))

    return show_result(get_winner(game.game_field, sign, game.chosen_field))


if __name__ == '__main__':
    user = UserPlayer()
    computer = ComputerPlayer()
    game(TicTacToe(), user, computer)
