"""Casino accounts and the manager that stores them."""


class CasinoAccount:
    """An account registered for each user of the casino.

    The account is used to log in and select a game to play. It outlives any
    single game, so it is the natural owner of the player's balance.
    """


class CasinoAccountManager:
    """Stores, manages and retrieves :class:`CasinoAccount` objects.

    It is advised that every operation in this class is logged.
    """

    def get_account(self, name: str, password: str) -> CasinoAccount | None:
        """Return the account with this name and password, or ``None``."""
        raise NotImplementedError

    def create_account(self, name: str, password: str) -> CasinoAccount:
        """Log and create a new account (without registering it)."""
        raise NotImplementedError

    def register_account(self, account: CasinoAccount) -> None:
        """Log and register an account so :meth:`get_account` can find it."""
        raise NotImplementedError
