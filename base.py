import math
import random
from typing import List

import config
from enums import Sign


class TicTacToe:

    def __init__(self):
        self.game_field = self.get_initial_game_field()
        self.chosen_field = None

    @staticmethod
    def get_initial_game_field() -> List[str]:
        return [' ' for _ in range(config.MAX_FIELDS_COUNT)]

    @staticmethod
    def get_initial_game_field_with_numbers() -> List[str]:
        return [str(_) for _ in range(config.MAX_FIELDS_COUNT)]

    def make_move(
            self,
            sign: Sign
    ) -> List[str]:
        update_game_field = self.game_field.copy()
        update_game_field[self.chosen_field] = sign.value
        return update_game_field

    @staticmethod
    def prep_game_field_for_print(game_field) -> str:
        result_field = ''
        rows_count = int(math.sqrt(config.MAX_FIELDS_COUNT))
        for i in range(rows_count):
            row = [_ for _ in game_field[i * rows_count:i * rows_count + rows_count]]
            result_field += '|' + '|'.join(row) + '|\n'
        return result_field

    def get_info_about_turn(self,  chosen_field: int, sign: Sign) -> str:
        return f'{sign.value} makes turn to field {chosen_field}'


class ComputerPlayer:
    def __init__(self):
        self.sign = Sign.computer

    def find_empty_fields(self, field: List[str]) -> List[int]:
        empty_fields = [i for i in range(len(field)) if field[i] == ' ']
        return empty_fields

    def choose_empty_field(self, empty_field: List[int]) -> int:
        return random.choice(empty_field)


class UserPlayer:
    def __init__(self):
        self.sign = Sign.user

    def ask_user_for_field_number(self) -> str:
        return f'{self.sign.value} turn. Input a number of free field: '

    def is_empty_field(self, chosen_field: int, game_field: List[str]) -> bool:
        return game_field[chosen_field] == ' '
