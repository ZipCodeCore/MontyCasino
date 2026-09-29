"""The contract for all games."""

from abc import ABC, abstractmethod

from montycasino.player import Player


class Game(ABC):
    """Base class for casino games.

    Games that support more than one player get that for free from
    :meth:`add` and :meth:`remove`; subclasses decide how :meth:`run` works.
    """

    def __init__(self) -> None:
        self.players: list[Player] = []

    def add(self, player: Player) -> None:
        """Add a player to the game."""
        self.players.append(player)

    def remove(self, player: Player) -> None:
        """Remove a player from the game."""
        self.players.remove(player)

    @abstractmethod
    def run(self) -> None:
        """Specify how the game will run."""
