"""The casino's games."""

from montycasino.game import Game
from montycasino.games.numberguess import NumberGuessGame, NumberGuessPlayer
from montycasino.games.slots import SlotsGame, SlotsPlayer
from montycasino.player import Player

# Menu name -> (game class, player class). Add new games here.
GAMES: dict[str, tuple[type[Game], type[Player]]] = {
    "SLOTS": (SlotsGame, SlotsPlayer),
    "NUMBERGUESS": (NumberGuessGame, NumberGuessPlayer),
}

__all__ = ["GAMES", "NumberGuessGame", "NumberGuessPlayer", "SlotsGame", "SlotsPlayer"]
