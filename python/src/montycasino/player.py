"""The contract for all players."""

from abc import ABC, abstractmethod
from typing import Any

from montycasino.accounts import CasinoAccount


class Player(ABC):
    """Base class for the player of a game.

    Every player holds a reference to the :class:`CasinoAccount` used to log
    in, and can :meth:`play` its game. The account is *shared*, not owned:
    discarding a player must not discard the account.
    """

    def __init__(self, account: CasinoAccount) -> None:
        self.account = account

    @abstractmethod
    def play(self) -> Any:
        """Define how this kind of player plays its game.

        Return whatever value you would like.
        """
