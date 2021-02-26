import pytest

from base import TicTacToe
from enums import Sign


@pytest.fixture()
def create_tic_tac():
    tic_tac_toe = TicTacToe()
    tic_tac_toe.chosen_field = 0
    tic_tac_toe.game_field = tic_tac_toe.make_turn(Sign.computer)
    return tic_tac_toe
