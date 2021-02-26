import pytest

from base import TicTacToe, ComputerPlayer, UserPlayer
from enums import Sign


@pytest.mark.parametrize(
    'chosen_field, sign, expected',
    [
        (0, Sign.computer, ['X', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ']),
        (3, Sign.user, [' ', ' ', ' ', 'O', ' ', ' ', ' ', ' ', ' ']),
        (7, Sign.computer, [' ', ' ', ' ', ' ', ' ', ' ', ' ', 'X', ' '])
    ]
)
def test_make_turn(chosen_field, sign, expected):
    tic_tac_toe = TicTacToe()
    tic_tac_toe.chosen_field = chosen_field
    assert tic_tac_toe.make_turn(sign) == expected


def test_find_empty_field(create_tic_tac):
    computer = ComputerPlayer()
    assert computer.find_empty_field(create_tic_tac.game_field) == [_ for _ in range(1, 9)]


def test_is_empty(create_tic_tac):
    user = UserPlayer()
    assert user.is_empty(create_tic_tac.chosen_field, create_tic_tac.game_field) is False
