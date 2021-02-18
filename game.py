import random
from typing import List, Union, Tuple, Optional

from enums import Sign


def initial_game_field() -> List[str]:
    return [' ' for _ in range(9)]


def initial_conditions(sign) -> Tuple[Sign, bool, None]:
    return sign.computer, True, None


def print_game_field(current_game_field: List[str]) -> None:
    for i in range(3):
        row = [_ for _ in current_game_field[i*3:i*3 + 3]]
        print('|' + '|'.join(row) + '|')


def initial_game_field_with_numbers() -> List[str]:
    return [str(_) for _ in range(9)]


def find_empty_field(field: List[str]) -> List[int]:
    empty_fields = [i for i in range(len(field)) if field[i] == ' ']
    return empty_fields


def computer_choose_empty_field(empty_field: List[int]) -> int:
    return random.choice(empty_field)


def ask_user_for_field_number() -> int:
    field_number = int(input("O's turn. Input a number of free field: "))
    return field_number


def is_empty(chosen_field: int, current_game_field: List[str]) -> bool:
    return current_game_field[chosen_field] == ' '


def make_turn(
        current_game_field: List[str],
        chosen_field: int,
        sign: Sign
) -> List[str]:
    update_game_field = current_game_field.copy()
    update_game_field[chosen_field] = sign.value
    return update_game_field


def info_about_turn(chosen_field: int, sign: Sign) -> None:
    print(f'{sign.value} makes turn to field {chosen_field}')


def who_win(
        current_game_field: List[str],
        sign: Sign,
        chosen_field: Optional[int]
) -> Union[None, Sign, bool]:
    if chosen_field is None:
        return None

    row_id = chosen_field // 3
    row = current_game_field[row_id * 3:row_id * 3 + 3]
    if all([r == sign.value for r in row]):
        return sign

    column_id = chosen_field % 3
    column = current_game_field[column_id::3]
    if all([c == sign.value for c in column]):
        return sign

    if chosen_field % 2 == 0 or chosen_field == 0:
        diag_left = current_game_field[::4]
        diag_right = current_game_field[2:-1:2]
        if (all([s == sign.value for s in diag_right]) or
                all([s == sign.value for s in diag_left])):
            return sign
    if all([f != ' ' for f in current_game_field]):
        return True
    return None


def show_result(result: Union[bool, Sign, None]) -> None:
    if result is True:
        print('It is a tie!')
    else:
        print(f'{sign.value} is winner!')


def turn(
        current_game_field: List[str],
        sign: Sign,
        computer: bool
) -> Tuple[List[str], int]:
    if not computer:
        while True:
            chosen_field = ask_user_for_field_number()
            if is_empty(chosen_field, current_game_field):
                break
            print('This field is taken. Try again.')
    if computer:
        empty_field = find_empty_field(current_game_field)
        chosen_field = computer_choose_empty_field(empty_field)
    player_make_turn = make_turn(current_game_field, chosen_field, sign)
    info_about_turn(chosen_field, sign)
    print_game_field(player_make_turn)
    return player_make_turn, chosen_field


def change_player(computer: bool, sign: Sign) -> Tuple[Sign, bool]:
    if sign == Sign.computer:
        sign = Sign.user
    else:
        sign = Sign.computer
    return sign, not computer


current_game_field = initial_game_field()
sign, computer, chosen_field = initial_conditions(Sign)
game_field_with_numbers = initial_game_field_with_numbers()
print_game_field(game_field_with_numbers)

while not who_win(current_game_field, sign, chosen_field):
    sign, computer = change_player(computer, sign)
    current_game_field, chosen_field = turn(current_game_field, sign, computer)
show_result(who_win(current_game_field, sign, chosen_field))
