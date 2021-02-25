from typing import Tuple, List

from enums import Sign


def change_player(user_starts: bool, sign: Sign) -> Tuple[Sign, bool]:
    if sign == Sign.computer:
        sign = Sign.user
    else:
        sign = Sign.computer
    return sign, not user_starts


def is_row_filled(current_game_field: List[str], sign: Sign, chosen_field: int, rows_count: int) -> bool:
    row_id = chosen_field // rows_count
    row = current_game_field[row_id * rows_count:rows_count * (row_id+1)]
    if all([r == sign.value for r in row]):
        return True


def is_column_filled(current_game_field: List[str], sign: Sign, chosen_field: int, rows_count: int) -> bool:
    column_id = chosen_field % rows_count
    column = current_game_field[column_id::rows_count]
    if all([c == sign.value for c in column]):
        return True


def is_diag_filled(current_game_field: List[str], sign: Sign, chosen_field: int, rows_count: int) -> bool:
    if chosen_field % 2 == 0 or chosen_field == 0:
        diag_left = current_game_field[::rows_count+1]
        diag_right = current_game_field[rows_count-1:-1:rows_count-1]
        if (all([s == sign.value for s in diag_right]) or
                all([s == sign.value for s in diag_left])):
            return True
